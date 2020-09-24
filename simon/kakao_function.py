import requests

apikey = "3bded7c4b06d014ee5ebe60ed301e399"
apikey = "1239093320414f1bbd3640ef81c189ea"
apikey = "1e5f83f57d7b6ba65a213fb725362d5d"
def kakao_keyword(key_word, cent_x, cent_y, radius = 1000, page = 1, size = 2):

    url = "https://dapi.kakao.com/v2/local/search/keyword.json?"
    headers = {"Authorization": f"KakaoAK {apikey}"}
    params = {'query': key_word,
              'x': cent_y,
              'y': cent_x,
              'radius': radius,
              'page': page,
              'size': size,
              'sort': 'distance'}
    json_data = requests.get(url, params=params, headers=headers).json()
    return json_data

def kakao_dong_name(list_cent_pos, user_district):

    url = "https://dapi.kakao.com/v2/local/geo/coord2regioncode.json?"
    headers = {"Authorization": f"KakaoAK {apikey}"}
    # 왜 카카오는 이걸반데로 쓰는지 도무지 이해가 안간다.-__-
    params = {'x': list_cent_pos[1],
              'y': list_cent_pos[0]}
    json_data = requests.get(url, params=params, headers=headers).json()


    dic_data = json_data["documents"][0]
    if dic_data["region_1depth_name"] != "광주광역시" or dic_data[
        "region_2depth_name"] != user_district:
        return None

    return dic_data["region_3depth_name"]



