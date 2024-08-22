def get_center_of_bbox(bbox):
    # @format: x1, y1, x2, y2 = bbox
    return int((bbox[0] + bbox[2]) / 2), int((bbox[1] + bbox[3]) / 2)

def get_bbox_width(bbox):
    # @format: x1, y1, x2, y2 = bbox
    return bbox[2] - bbox[0]

def measure_distance(p1, p2):
    return ((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)**0.5

def measure_xy_distance(p1, p2):
    return abs(p1[0] - p2[0]), abs(p1[1] - p2[1])

def get_foot_position(bbox):
    # @format: x1, y1, x2, y2 = bbox
    return int((bbox[0] + bbox[2]) / 2), int(bbox[3])

