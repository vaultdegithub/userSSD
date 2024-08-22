from ultralytics import YOLO
import supervision as sv
import pickle
import os
import cv2
import pandas as pd
import sys
sys.path.append('../')
from utils import get_center_of_bbox, get_bbox_width, get_foot_position, measure_distance

class Tracker:
    def __init__(self, model_path):
        self.model = YOLO(model_path)
        self.tracker = sv.ByteTrack()

    def add_position_to_tracks(self, tracks):
        for obj, obj_tracks in tracks.items():
            for frame_num, track in enumerate(obj_tracks):
                for track_id, track_info in track.items():
                    bbox = track_info['bbox']
                    if object == 'ball':
                        position = get_center_of_bbox(bbox)
                    else:
                        position = get_foot_position(bbox)
                    tracks[obj][frame_num][track_id]['position'] = position
    
    def interpolate_ball_positions(self, ball_positions):
        ball_positions = [x.get(1,{}).get('bbox,{}') for x in ball_positions]
        df_ball_positions = pd.DataFrame(ball_positions, columns=['x1', 'y1', 'x2', 'y2'])

        # interpolate missing values
        df_ball_positions = df_ball_positions.interpolate()
        df_ball_positions = df_ball_positions.bfill()

        ball_positions = [{1:{'bbox':x}} for x in df_ball_positions.to_numpy().tolist()]

        return ball_positions


    
    def detect_frames(self, frame):
        batch_size = 20
        detections = []

        for i in range(0, len(frame), batch_size):
            detections_batch = self.model.predict(frame[i : i + batch_size],conf=0.1)
            detections.extend(detections_batch)
        return detections
    
    def get_object_tracks(self, frame, read_from_stub=False,stub_path=None):

        if read_from_stub and stub_path is not None and os.path.exists(stub_path):
            with open(stub_path,"rb") as f:
                tracks = pickle.load(f)
            return tracks

        detections = self.detect_frames(frame)
        tracks={
            "players":[],
            "referees":[],
            "ball":[]
        }

        for frame_num, detection in enumerate(detections):
            cls_names = detection.names
            cls_names_inv = {v: k for k, v in cls_names.items()}

            detection_supervision = sv.Detections.from_ultralytics(detection)

            #converting "goalkeeper" to "player"
            for obj_inx, class_id in enumerate(detection_supervision.class_id):
                if cls_names[class_id] == "goalkeeper":
                    detection_supervision.class_id[obj_inx] = cls_names_inv["player"]
            
            detection_with_tracks = self.tracker.update_with_detections(detection_supervision)

            tracks["players"].append({})
            tracks["referees"].append({})
            tracks["ball"].append({})
            
            # @given supervision data.format
            for frame_detection in detection_with_tracks:
                bbox = frame_detection[0].tolist()
                cls_id = frame_detection[3]
                tracks_id = frame_detection[4]

                if cls_id == cls_names_inv["player"]:
                    tracks["players"][frame_num][tracks_id] = {"bbox":bbox}
                
                if cls_id == cls_names_inv["referee"]:
                    tracks["referees"][frame_num][tracks_id] = {"bbox":bbox}
                
            for frame_detection in detection_with_tracks:
                bbox = frame_detection[0].tolist()
                cls_id = frame_detection[3]

                if cls_id == cls_names_inv["ball"]:
                    tracks["ball"][frame_num][1] = {"bbox":bbox}
        
        if stub_path is not None:
            with open(stub_path,"wb") as f:
                pickle.dump(tracks,f)

        return tracks
    
    def draw_annotations(self, video_frames, tracks, ball_tracking=None):
        output_video_frames = []

        for frame_num, frame in enumerate(video_frames):
            frame = frame.copy()

            player_dict = tracks["players"][frame_num]
            referee_dict = tracks["referees"][frame_num]
            ball_dict = tracks["ball"][frame_num]

            player_color = (0, 255, 0)
            referee_color = (255, 0, 0)
            ball_color = (0, 0, 255)

            # draw player
            for track_id, player in player_dict.items():
                frame = self.draw_ellipse(frame, player["bbox"], player_color, track_id)
                
                #TODO: triangulate player with ball
            
            # draw referee
            for _, referee in referee_dict.items():
                frame = self.draw_ellipse(frame, referee["bbox"], referee_color, None)

            # draw ball
            for _, ball in ball_dict.items():
                frame = self.draw_ellipse(frame, ball["bbox"], ball_color, None)

            #TODO: draw team ball control
            
            output_video_frames.append(frame)
        return output_video_frames

    def draw_ellipse(self, frame, bbox, color, track_id=None):
        y2 = int(bbox[3])
        x_center,_ = get_center_of_bbox(bbox)
        width = get_bbox_width(bbox)

        cv2.ellipse(frame, center=(x_center, y2), 
                    axes=(int(width),int(0.35*width)),
                    angle=0.0,
                    startAngle=-45,
                    endAngle=235,
                    color=color,
                    thickness=2,
                    lineType=cv2.LINE_4)
        
        rectangle_height = 40
        rectangle_width = 20
        x1_rect = x_center - rectangle_width//2
        x2_rect = x_center + rectangle_width//2
        y1_rect = (y2 - rectangle_height//2) +15
        y2_rect = (y2 + rectangle_height//2) +15

        if track_id is not None:
            cv2.rectangle(frame,
                         (x1_rect, y1_rect),
                         (x2_rect, y2_rect),
                         color, cv2.FILLED)
                         
        return frame
            
        
    def draw_team_ball_control(self, frame, frame_num, team_ball_control):

        #semi transparent overlay
        overlay = frame.copy()
        cv2.rectangle(overlay, (1350,850), (1900, 970), (255,255,255), -1)
        alpha = 0.4
        cv2.addWeighted(overlay, alpha, frame, 1-alpha, 0, frame)
        
        team_ball_control_till_frame = team_ball_control[:frame_num+1]

        t1_num_frames = team_ball_control_till_frame[team_ball_control_till_frame==1].shape[0]
        t2_num_frames = team_ball_control_till_frame[team_ball_control_till_frame==2].shape[0]
        t1 = t1_num_frames/(t1_num_frames+t2_num_frames)
        t2 = t2_num_frames/(t1_num_frames+t2_num_frames)

        cv2.putText(frame, f"T1: {t1*100:.2f}", (1400, 900), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 1, 3)
        cv2.putText(frame, f"T2: {t2*100:.2f}", (1400, 950), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 1, 3)

        return frame

