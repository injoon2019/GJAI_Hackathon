import folium
import pandas as pd
import json
import requests

from folium.plugins import MarkerCluster

# CUSTOM
import kakao_function
import centroid
from gather_data import gather_data_from_cent

pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)

def get_centorid_data():
    # 구별 위치 정보 든 geo json 불러옴 --------------------------------------
    with open("korea_seperate_gu.json", encoding="utf-8-sig") as file:
        json_geo_data = json.load(file)

    list_dic_geo = []
    for dic_data in json_geo_data["features"]:
        # 전국 데이터에서 광주 구별 데이터만 ID로 가져옴.
        if dic_data["properties"]["SIG_CD"] in ["29170", "29200", "29140", "29155", "29110"]:
            list_dic_geo.append(dic_data)

    dic_all_centroid = {}
    # 각 구별로 계산 --------------------------------------
    for dic_distrcit_data in list_dic_geo:
        name = dic_distrcit_data["properties"]["SIG_KOR_NM"] # 남구 동구...
        # if name != "남구":
        #     continue

        dic_result = centroid.all_centroied_poses_of_district(dic_distrcit_data, div_num=15)
        dic_all_centroid[name] = dic_result

    return dic_all_centroid

def main():
    # DATA public library -------------------------------------
    df_republic_library = pd.read_csv("gwangju_public_library_20190531.csv", encoding="cp949")
    df_republic_lib = df_republic_library[["도서관명", "위도", "경도"]]

    # DATA small library -------------------------------------
    df_korea_all_libraries = pd.read_csv("korea_all_library.csv", encoding="cp949")

    df_gwangju_all_library = df_korea_all_libraries[df_korea_all_libraries["시도명"] == "광주광역시"]
    df_small_library = df_gwangju_all_library[df_gwangju_all_library["도서관유형"] == "작은도서관"]
    df_small_library.reset_index(inplace=True)

    # MARKER - republic library -------------------------------------
    start_x = 35.139737
    start_y = 126.913963
    # map = folium.Map(location=[35.139737, 126.913963], zoom_start=17)
    map = folium.Map(location=[start_x, start_y], zoom_start=17)
    map_cluster_republic_lib = folium.plugins.MarkerCluster()
    map_cluster_small_lib = folium.plugins.MarkerCluster()


    # MARKER - republic library -------------------------------------
    for idx in range(len(df_republic_lib)):
        series = df_republic_lib.loc[idx,:]
        marker = folium.Marker([series["위도"], series["경도"]],
                               popup=series["도서관명"],icon=folium.Icon(icon='book', color='red'))
        map_cluster_republic_lib.add_child(marker)
        map.add_child(map_cluster_republic_lib)

    # MARKER - small library -------------------------------------
    for idx in range(len(df_small_library)):
        series = df_small_library.loc[idx,:]
        marker = folium.Marker([series["위도"], series["경도"]],
                               popup=series["도서관명"],icon=folium.Icon(icon='book', color='green'))
        map_cluster_small_lib.add_child(marker)
        map.add_child(map_cluster_small_lib)

    # CREATE centroid
    dic_all_centroid = get_centorid_data()


    # TEST ----------  centroid
    user_district = "남구"
    for x, y in dic_all_centroid[user_district]["centroids"]:
        folium.CircleMarker([x, y], popup=user_district, icon=folium.Icon(color='blue'),
                            radius=dic_all_centroid[user_district]["x_y_radius_dis"][0] * 0.01).add_to(map)


    result = gather_data_from_cent(dic_all_centroid[user_district]["centroids"], user_district)


    # map.save("map.html")

    print("DONE!!!")



if __name__ == "__main__":
    main()