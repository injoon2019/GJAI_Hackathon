import requests
import json

# starbucks = grading("스타벅스", center_point_list[num], three_point=350, two_point=600, one_point=900,
def grading(target, where_am_i, three_point, two_point, one_point, bonus_point):
    apikey = "1239093320414f1bbd3640ef81c189ea"
    import json
    import requests
    if target == "편의점":

        category_group_code = "CS2"
        where_am_i_x = where_am_i[0]
        where_am_i_y = where_am_i[1]

        url_three_point = f"https://dapi.kakao.com/v2/local/search/category.json?category_group_code={category_group_code}&y={where_am_i_y}&x={where_am_i_x}&radius={three_point}"
        url_three_point_result = requests.get(url_three_point,
                                              params={'category_group_code': category_group_code, 'page': 1, 'size': 2},
                                              headers={'Authorization': 'KakaoAK ' + apikey}).json()

        url_two_point = f"https://dapi.kakao.com/v2/local/search/category.json?category_group_code={category_group_code}&y={where_am_i_y}&x={where_am_i_x}&radius={two_point}"
        url_two_point_result = requests.get(url_two_point,
                                            params={'category_group_code': category_group_code, 'page': 1, 'size': 2},
                                            headers={'Authorization': 'KakaoAK ' + apikey}).json()

        url_one_point = f"https://dapi.kakao.com/v2/local/search/category.json?category_group_code={category_group_code}&y={where_am_i_y}&x={where_am_i_x}&radius={one_point}"
        url_one_point_result = requests.get(url_one_point,
                                            params={'category_group_code': category_group_code, 'page': 1, 'size': 2},
                                            headers={'Authorization': 'KakaoAK ' + apikey}).json()

        if len(url_three_point_result['documents']) > 0:
            grade = 3
            is_it_close = f"{three_point}미터 안에 {len(url_three_point_result['documents'])}개 존재"
        elif len(url_two_point_result['documents']) > 0:
            grade = 2
            is_it_close = f"{two_point}미터 안에 {len(url_two_point_result['documents'])}개 존재"
        elif len(url_one_point_result['documents']) > 0:
            grade = 1
            is_it_close = f"{one_point}미터 안에 {len(url_one_point_result['documents'])}개 존재"
        else:
            grade = 0
            is_it_close = f"{one_point}미터 안에 없음"

        if bonus_point != 0:
            if grade != 0:
                grade = grade + bonus_point

        return [grade, is_it_close]

    elif target == "지하철역":

        category_group_code = "SW8"
        where_am_i_x = where_am_i[0]
        where_am_i_y = where_am_i[1]

        url_three_point = f"https://dapi.kakao.com/v2/local/search/category.json?category_group_code={category_group_code}&y={where_am_i_y}&x={where_am_i_x}&radius={three_point}"
        url_three_point_result = requests.get(url_three_point,
                                              params={'category_group_code': category_group_code, 'page': 1, 'size': 3},
                                              headers={'Authorization': 'KakaoAK ' + apikey}).json()

        url_two_point = f"https://dapi.kakao.com/v2/local/search/category.json?category_group_code={category_group_code}&y={where_am_i_y}&x={where_am_i_x}&radius={two_point}"
        url_two_point_result = requests.get(url_two_point,
                                            params={'category_group_code': category_group_code, 'page': 1, 'size': 3},
                                            headers={'Authorization': 'KakaoAK ' + apikey}).json()

        url_one_point = f"https://dapi.kakao.com/v2/local/search/category.json?category_group_code={category_group_code}&y={where_am_i_y}&x={where_am_i_x}&radius={one_point}"
        url_one_point_result = requests.get(url_one_point,
                                            params={'category_group_code': category_group_code, 'page': 1, 'size': 3},
                                            headers={'Authorization': 'KakaoAK ' + apikey}).json()

        if len(url_three_point_result['documents']) > 0:
            grade = 3
            is_it_close = f"{three_point}미터 안에 {len(url_three_point_result['documents'])}개 존재"
        elif len(url_two_point_result['documents']) > 0:
            grade = 2
            is_it_close = f"{two_point}미터 안에 {len(url_two_point_result['documents'])}개 존재"
        elif len(url_one_point_result['documents']) > 0:
            grade = 1
            is_it_close = f"{one_point}미터 안에 {len(url_one_point_result['documents'])}개 존재"
        else:
            grade = 0
            is_it_close = f"{one_point}미터 안에 없음"

        if bonus_point != 0:
            if grade != 0:
                grade = grade + bonus_point

        return [grade, is_it_close]

    else:
        query = target

        where_am_i_x = where_am_i[0]
        where_am_i_y = where_am_i[1]

        url_three_point = f"https://dapi.kakao.com/v2/local/search/keyword.json?query={query}&y={where_am_i_y}&x={where_am_i_x}&radius={three_point}"
        url_three_point_result = requests.get(url_three_point, params={'query': query, 'page': 1, 'size': 2},
                                              headers={'Authorization': 'KakaoAK ' + apikey}).json()

        url_two_point = f"https://dapi.kakao.com/v2/local/search/keyword.json?query={query}&y={where_am_i_y}&x={where_am_i_x}&radius={two_point}"
        url_two_point_result = requests.get(url_two_point, params={'query': query, 'page': 1, 'size': 2},
                                            headers={'Authorization': 'KakaoAK ' + apikey}).json()

        url_one_point = f"https://dapi.kakao.com/v2/local/search/keyword.json?query={query}&y={where_am_i_y}&x={where_am_i_x}&radius={one_point}"
        url_one_point_result = requests.get(url_one_point, params={'query': query, 'page': 1, 'size': 2},
                                            headers={'Authorization': 'KakaoAK ' + apikey}).json()

        if len(url_three_point_result['documents']) > 0:
            grade = 3
            is_it_close = f"{three_point}미터 안에 {len(url_three_point_result['documents'])}개 존재"
        elif len(url_two_point_result['documents']) > 0:
            grade = 2
            is_it_close = f"{two_point}미터 안에 {len(url_two_point_result['documents'])}개 존재"
        elif len(url_one_point_result['documents']) > 0:
            grade = 1
            is_it_close = f"{one_point}미터 안에 {len(url_one_point_result['documents'])}개 존재"
        else:
            grade = 0
            is_it_close = f"{one_point}미터 안에 없음"

        if bonus_point != 0:
            if grade != 0:
                grade = grade + bonus_point

        return [grade, is_it_close]

def final_grading(center_point_list):
    apikey = "1239093320414f1bbd3640ef81c189ea"

    total_grade_list = []
    point_grade_dict_list = []
    dong_name_list = []
    for num in range(len(center_point_list)):
        dong_url = f"https://dapi.kakao.com/v2/local/geo/coord2regioncode.json?x={center_point_list[num][0]}&y={center_point_list[num][1]}"
        dong_url_result = requests.get(dong_url, headers={'Authorization': 'KakaoAK ' + apikey}).json()
        dong_name = dong_url_result['documents'][0]['region_3depth_name']

        point_grade_dict = {}
        starbucks = grading("스타벅스", center_point_list[num], three_point=350, two_point=600, one_point=900,
                            bonus_point=0)
        macdonald = grading("맥도날드", center_point_list[num], three_point=350, two_point=600, one_point=900,
                            bonus_point=0)
        burgerking = grading("버거킹", center_point_list[num], three_point=350, two_point=600, one_point=900,
                             bonus_point=0)
        daiso = grading("다이소", center_point_list[num], three_point=350, two_point=600, one_point=900, bonus_point=1)
        oliveyoung = grading("올리브영", center_point_list[num], three_point=350, two_point=600, one_point=900,
                             bonus_point=0)
        subwaystation = grading("지하철역", center_point_list[num], three_point=350, two_point=600, one_point=900,
                                bonus_point=2)
        cvs = grading("편의점", center_point_list[num], three_point=200, two_point=400, one_point=600, bonus_point=0)

        total_grade_list.append(
            sum([starbucks[0], macdonald[0], burgerking[0], daiso[0], oliveyoung[0], subwaystation[0], cvs[0]]))

        point_grade_dict["스타벅스"] = starbucks[1]
        point_grade_dict["맥도날드"] = macdonald[1]
        point_grade_dict["버거킹"] = burgerking[1]
        point_grade_dict["다이소"] = daiso[1]
        point_grade_dict["올리브영"] = oliveyoung[1]
        point_grade_dict["지하철역"] = subwaystation[1]
        point_grade_dict["편의점"] = cvs[1]

        point_grade_dict_list.append(point_grade_dict)
        dong_name_list.append(dong_name)
    return [total_grade_list, point_grade_dict_list, dong_name_list]