import math
from haversine import haversine

# CAL_MAP_GEO_MIN_MAX_POS
def calculate_map_geo_min_max_pos(list_geo_loc_poses):
    # MIN --------------------------------------
    x_min = math.inf
    y_min = math.inf
    for y, x in list_geo_loc_poses:
        if x_min > x:
            x_min = x
        if y_min > y:
            y_min = y
    # MAX --------------------------------------
    x_max = 0
    y_max = 0
    for y, x in list_geo_loc_poses:
        if x_max < x:
            x_max = x
        if y_max < y:
            y_max = y

    return x_min, y_min, x_max, y_max

# CENTROID_ALL_POSES --------------------------------------
def all_centroied_poses_of_district(dic_distrcit_data, div_num):
    if div_num > 20:
        print("더 작은 숫자로. 다시 설정해주세요!!!")
        return None

    dic_data = {}
    list_geo_loc_poses = dic_distrcit_data["geometry"]["coordinates"][0]
    # 구별 최대 최소 위치 값 가져옴.
    x_min, y_min, x_max, y_max = calculate_map_geo_min_max_pos(list_geo_loc_poses)

    # 각 늘어날 타일 (위도 경도) 사이즈 계산
    x_div_size = (x_max - x_min) / div_num
    y_div_size = (y_max - y_min) / div_num
    # 늘어날 크기에 절반 더하고 시작 (중점 마추기 위함.)
    x_min_add_half = x_min + (x_div_size / 2)
    y_min_add_half = y_min + (y_div_size / 2)

    list_x_center_poses = []
    list_y_center_poses = []

    # loop 돌면서 중심점 구해서 list에 넣어줌. x, y --------------------------------------
    for i in range(div_num):
        list_x_center_poses.append(x_min_add_half + x_div_size * i)
        list_y_center_poses.append(y_min_add_half + y_div_size * i)

    # x y 를 각각 합쳐줌 [x, y]로
    all_regions_center_poses = []
    for y_center in list_y_center_poses:
        for x_center in list_x_center_poses:
            all_regions_center_poses.append([x_center, y_center])
    dic_data["centroids"] = all_regions_center_poses

    # 나눈 거리가 실제로 얼마의 거리를 가지는지 x y 에 대해서 계산함. 나중에 보여주기위함. ----------
    x_radius_meter = haversine((x_min , y_min),  (x_min_add_half, y_min), unit = 'm')
    y_radius_meter = haversine((x_min , y_min_add_half),  (x_min, y_min), unit = 'm')
    dic_data["x_y_radius_dis"] = (x_radius_meter, y_radius_meter)

    return dic_data
