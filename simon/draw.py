import numpy as np
import plotly.graph_objects as go
from chart_studio.plotly import plot, iplot

import matplotlib
import matplotlib.pyplot as plt  # 파이플롯 사용
from IPython.display import set_matplotlib_formats
import seaborn as sns
sns.set_style('whitegrid')


set_matplotlib_formats('retina')  # 한글코드를 더 선명하게 해주는 조치, 레티나 설정
matplotlib.rc('font', family='AppleGothic') # 폰트 설정
matplotlib.rc('axes', unicode_minus=False) #

import chart_studio
chart_studio.tools.set_credentials_file(username="didtlahs", api_key="32K3mAOdfE2DboHNbGmK")

# def draw_map(list_dic_geo ,list_centroid, user_district, size, dic_result_gather):
#     # # 구 코드 정리
#     # gu_code_dict = {}
#     # for num in range(25):
#     #     gu_code_dict[geo_json['features'][num]['properties']['name']] = num
#     #
#     # gu_code = gu_code_dict[gu_name]
#     # # 경도 (좌 - 우)
#     # left_lon = sorted(np.array(geo_json['features'][gu_code]['geometry']['coordinates'][0])[:, 0].tolist())[
#     #     0]  # 가장 작은 경도값 - 제일 왼쪽
#     # right_lon = sorted(np.array(geo_json['features'][gu_code]['geometry']['coordinates'][0])[:, 0].tolist())[
#     #     -1]  # 가장 큰 경도값 - 제일 오른쪽
#     # gap_lon = ((right_lon - left_lon) / size)
#     #
#     # lon_list = []
#     # for num in range(size + 1):
#     #     lon_list.append(left_lon + gap_lon * num)
#     #
#     # lon_center_list = []  # 중점의 세로 좌표
#     # for num in range(size):
#     #     lon_center_list.append(np.mean([lon_list[num], lon_list[num + 1]]))
#     #
#     # # 위도 (상 - 하)
#     # top_lat = sorted(np.array(geo_json['features'][gu_code]['geometry']['coordinates'][0])[:, 1].tolist())[
#     #     -1]  # 가장 높은 위도값 - 제일 위쪽
#     # bottom_lat = sorted(np.array(geo_json['features'][gu_code]['geometry']['coordinates'][0])[:, 1].tolist())[
#     #     0]  # 가장 낮은 위도값 - 제일 위쪽
#     # gap_lat = ((top_lat - bottom_lat) / size)
#     #
#     # lat_list = []
#     # for num in range(size + 1):
#     #     lat_list.append(bottom_lat + gap_lat * num)
#     #
#     # lat_center_list = []  # 중점의 가로 좌표
#     # for num in range(size):
#     #     lat_center_list.append(np.mean([lat_list[num], lat_list[num + 1]]))
#     #
#     # # 중점 좌표 모으기
#     # center_point_list = []
#     # for lat in lat_center_list:
#     #     for lon in lon_center_list:
#     #         center_point_list.append([lon, lat])
#
#
#
#     fig = go.Figure()
#
#     # 세로선 긋기
#     for idx in range(size):
#         fig.add_trace(go.Scattermapbox(
#             showlegend=False,
#             mode="lines",
#             lon=[list_centroid[idx][1], list_centroid[idx][1]],
#             lat=[list_centroid[0][0], list_centroid[size - 1][0]],
#             line={'width': 1, 'color': 'gray'}))
#
#     # 가로선 긋기
#     for num in range(size + 1):
#         fig.add_trace(go.Scattermapbox(
#             showlegend=False,
#             mode="lines",
#             lon=[list_centroid[0][1], list_centroid[size - 1][1]],
#             lat=[list_centroid[idx][0], list_centroid[idx][0]],
#             line={'width': 1, 'color': 'gray'}))
#
#     # 점 추가하기
#     # grading_list 말고 다른 정보까지 리스트로 가져와야한다
#
#     # dic_all_result["list_dong_name"] = list_dong_name
#     # dic_all_result["list_sum_all_grade"] = list_sum_all_grade
#     # dic_all_result["list_dic_text_info"] = list_dic_text_info
#
#     #return [total_grade_list, point_grade_dict_list, dong_name_list]
#
#     for index, point in enumerate(list_centroid):
#         fig.add_trace(go.Scattermapbox(
#             showlegend=False,
#             mode="markers",
#             lon=[point[0]],
#             lat=[point[1]],
#             marker_color='blue',
#             marker_opacity=0.5,
#             marker_size=dic_result_gather["list_sum_all_grade"][index],
#             # hover text 지정하기
#             hoverlabel=dict(bgcolor='white'),
#             hovertemplate=f"{dic_result_gather['list_dong_name'][index]} 인근 자취점수 : {dic_result_gather['list_sum_all_grade'][index]}점<br>========<br>독서실 : {dic_result_gather['list_dic_text_info'][index]['독서실']}"
#                           # f"<br>버거킹 : {fianl_grading[1][index]['버거킹']}"
#                           # f"<br>스타벅스 : {fianl_grading[1][index]['스타벅스']}"
#                           # f"<br>지하철역 : {fianl_grading[1][index]['지하철역']}"
#                           # f"<br>다이소 : {fianl_grading[1][index]['다이소']}"
#                           # f"<br>올리브영 : {fianl_grading[1][index]['올리브영']}"
#                           # f"<br>편의점 : {fianl_grading[1][index]['편의점']}"
#         ))
#
#
#     for dic_distrcit_data in list_dic_geo:
#         name = dic_distrcit_data["properties"]["SIG_KOR_NM"]
#         if name == user_district:
#             geo_json = dic_distrcit_data
#
#     fig.update_layout(
#         mapbox={
#             'style': "stamen-terrain",
#             'center': {'lon': np.mean(np.array(list_centroid)[:, 0]),
#                        'lat': np.mean(np.array(list_centroid)[:, 1])},
#             'zoom': 12,
#             'layers': [{'source': 77,
#                         'type': "fill",
#                         'below': "traces",
#                         'color': "royalblue",
#                         'opacity': 0.3}]},
#         margin={'l': 0, 'r': 0, 'b': 0, 't': 0})
#
#
#     # 다 만들고 그래프를 fig 와 같은 변수에 담음
#
#     plot(fig, filename=f"{user_district} - {size}")
#     fig.show()


def draw_map(geo_json, gu_name, size, fianl_grading):
    # 구 코드 정리
    gu_code_dict = {}
    for num in range(25):
        gu_code_dict[geo_json['features'][num]['properties']['name']] = num

    gu_code = gu_code_dict[gu_name]
    # 경도 (좌 - 우)
    left_lon = sorted(np.array(geo_json['features'][gu_code]['geometry']['coordinates'][0])[:, 0].tolist())[
        0]  # 가장 작은 경도값 - 제일 왼쪽
    right_lon = sorted(np.array(geo_json['features'][gu_code]['geometry']['coordinates'][0])[:, 0].tolist())[
        -1]  # 가장 큰 경도값 - 제일 오른쪽
    gap_lon = ((right_lon - left_lon) / size)

    lon_list = []
    for num in range(size + 1):
        lon_list.append(left_lon + gap_lon * num)

    lon_center_list = []  # 중점의 세로 좌표
    for num in range(size):
        lon_center_list.append(np.mean([lon_list[num], lon_list[num + 1]]))

    # 위도 (상 - 하)
    top_lat = sorted(np.array(geo_json['features'][gu_code]['geometry']['coordinates'][0])[:, 1].tolist())[
        -1]  # 가장 높은 위도값 - 제일 위쪽
    bottom_lat = sorted(np.array(geo_json['features'][gu_code]['geometry']['coordinates'][0])[:, 1].tolist())[
        0]  # 가장 낮은 위도값 - 제일 위쪽
    gap_lat = ((top_lat - bottom_lat) / size)

    lat_list = []
    for num in range(size + 1):
        lat_list.append(bottom_lat + gap_lat * num)

    lat_center_list = []  # 중점의 가로 좌표
    for num in range(size):
        lat_center_list.append(np.mean([lat_list[num], lat_list[num + 1]]))

    # 중점 좌표 모으기
    center_point_list = []
    for lat in lat_center_list:
        for lon in lon_center_list:
            center_point_list.append([lon, lat])

    import plotly.graph_objects as go

    fig = go.Figure()

    # 세로선 긋기

    for num in range(size + 1):
        fig.add_trace(go.Scattermapbox(
            showlegend=False,
            mode="lines",
            lon=[lon_list[num], lon_list[num]],
            lat=[lat_list[0], lat_list[size]],
            line={'width': 1, 'color': 'gray'}))

    # 가로선 긋기

    for num in range(size + 1):
        fig.add_trace(go.Scattermapbox(
            showlegend=False,
            mode="lines",
            lon=[lon_list[0], lon_list[size]],
            lat=[lat_list[num], lat_list[num]],
            line={'width': 1, 'color': 'gray'}))

    # 점 추가하기
    # grading_list 말고 다른 정보까지 리스트로 가져와야한다

    for index, point in enumerate(center_point_list):
        fig.add_trace(go.Scattermapbox(
            showlegend=False,
            mode="markers",
            lon=[point[0]],
            lat=[point[1]],
            marker_color='blue',
            marker_opacity=0.5,
            marker_size=fianl_grading[0][index],
            # hover text 지정하기
            hoverlabel=dict(bgcolor='white'),
            hovertemplate=f"{fianl_grading[2][index]} 인근 자취점수 : {fianl_grading[0][index]}점<br>========<br>맥도날드 : {fianl_grading[1][index]['맥도날드']}<br>버거킹 : {fianl_grading[1][index]['버거킹']}<br>스타벅스 : {fianl_grading[1][index]['스타벅스']}<br>지하철역 : {fianl_grading[1][index]['지하철역']}<br>다이소 : {fianl_grading[1][index]['다이소']}<br>올리브영 : {fianl_grading[1][index]['올리브영']}<br>편의점 : {fianl_grading[1][index]['편의점']}"
        ))

    fig.update_layout(
        mapbox={
            'style': "stamen-terrain",
            'center': {'lon': np.mean(np.array(center_point_list)[:, 0]),
                       'lat': np.mean(np.array(center_point_list)[:, 1])},
            'zoom': 12,
            'layers': [{'source': np.array(geo_json['features'][gu_code]),
                        'type': "fill",
                        'below': "traces",
                        'color': "royalblue",
                        'opacity': 0.3}]},
        margin={'l': 0, 'r': 0, 'b': 0, 't': 0})

    from chart_studio.plotly import plot, iplot

    # 다 만들고 그래프를 fig 와 같은 변수에 담음

    plot(fig, filename=f"{gu_name} - {size}")
    # fig.show()