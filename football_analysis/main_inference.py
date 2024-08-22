from utils import read_video, save_video
from trackers import Tracker
import cv2
import numpy as np
from team_assigner import TeamAssigner
from player_ball_assigner import PlayerBallAssigner
from camera_movement_estimator import CameraMovementEstimator
from view_transformer import ViewTransformer
from speed_and_distance_estimator import SpeedAndDistance_Estimator

def main():
    name = 'input.mp4'
    video_frames = read_video('input_videos/' + name)
    tracker = Tracker('models/best.pt')
    tracks = tracker.get_object_tracks(video_frames,
                                       read_from_stub=True,
                                       stub_path='stubs/'+name+'_'+'track_stubs.pkl')
    tracker.add_position_to_tracks(tracks)
    camera_movement_estimator = CameraMovementEstimator(video_frames[0])
    camera_movement_per_frame = camera_movement_estimator.get_camera_movement(video_frames,
                                                                                read_from_stub=True,
                                                                                stub_path='stubs/'+name+'_'+'camera_movement_stub.pkl')
    camera_movement_estimator.add_adjust_positions_to_tracks(tracks,camera_movement_per_frame)
    view_transformer = ViewTransformer()
    view_transformer.add_transformed_position_to_tracks(tracks)
    tracks["ball"] = tracker.interpolate_ball_positions(tracks["ball"])
    speed_and_distance_estimator = SpeedAndDistance_Estimator()
    speed_and_distance_estimator.add_speed_and_distance_to_tracks(tracks)
    player_assigner =PlayerBallAssigner()
    team_ball_control= []
    # for frame_num, player_track in enumerate(tracks['players']):
    #     ball_bbox = tracks['ball'][frame_num][1]['bbox']
    #     assigned_player = player_assigner.assign_ball_to_player(player_track, ball_bbox)

    #     if assigned_player != -1:
    #         tracks['players'][frame_num][assigned_player]['has_ball'] = True
    #         team_ball_control.append(tracks['players'][frame_num][assigned_player]['team'])
    #     else:
    #         # @error control
    #         if team_ball_control:
    #             # @error index out of bounds
    #             team_ball_control.append(team_ball_control[-1])
    #         else:
    #             print("out of index error")
            # team_ball_control.append(team_ball_control[-1])
    # team_ball_control= np.array(team_ball_control)
    output_video_frames = tracker.draw_annotations(video_frames, tracks, team_ball_control=None)
    output_video_frames = camera_movement_estimator.draw_camera_movement(output_video_frames, camera_movement_per_frame)
    speed_and_distance_estimator.draw_speed_and_distance(output_video_frames, tracks)
    save_video(output_video_frames, "output_videos/output_video.avi")
    pass

if __name__ == "__main__":
    main()