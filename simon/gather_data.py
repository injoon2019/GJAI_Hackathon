
import pickle
import pandas

from kakao_function import kakao_dong_name
from kakao_function import kakao_keyword


def gather_data(keyword, cent_pos, fir_dis, sec_dis, thir_dis, bonus_point):

    cent_x = cent_pos[0]
    cent_y = cent_pos[1]

    # def kakao_keyword(key_word, cent_x, cent_y, radius=1000, page=1, size=2):

    dic_sec_dis = None
    dic_thir_dis = None
    grade = 0
    text_dis_info = ""
    fir_num, sec_num, thir_num = 0, 0, 0

    #가장 가까운것 검색
    dic_fir_dis = kakao_keyword(keyword, cent_x, cent_y, radius=fir_dis)
    fir_num = len(dic_fir_dis["documents"])

    # 가장 가까운것 없으면 두번쨰 가까운것
    if fir_num <= 0:
        dic_sec_dis = kakao_keyword(keyword, cent_x, cent_y, radius=sec_dis)
        sec_num = len(dic_sec_dis["documents"])
        # 세번째
        if sec_num <= 0:
            dic_thir_dis = kakao_keyword(keyword, cent_x, cent_y, radius=thir_dis)
            thir_num = len(dic_thir_dis["documents"])

    if fir_num > 0:
        grade = 3 * fir_num
        text_dis_info = f"{fir_dis}미터 안에 {fir_num}개 존재"
    elif sec_num > 0:
        grade = 2 * sec_num
        text_dis_info = f"{sec_dis}미터 안에 {sec_num}개 존재"
    elif thir_num > 0:
        grade = 1 * thir_num
        text_dis_info = f"{thir_dis}미터 안에 {thir_num}개 존재"
    else:
        grade = 0
        text_dis_info = f"{thir_dis}미터 안에 없음"

    if bonus_point != 0:
        if grade != 0:
            grade += bonus_point
    dic_result = {'grade':grade, "text_dis_info": text_dis_info}
    return dic_result


def gather_data_from_cent(list_cent_pos, user_district, is_use_pickle=False):

    if is_use_pickle == False:
        list_sum_all_grade = []
        list_dic_text_info = []
        list_dong_name = []

        #api 제한 때문에 피클로 대체함.
        for idx in range(len(list_cent_pos)):
            dong_name = kakao_dong_name(list_cent_pos[idx], user_district)
            list_dong_name.append(dong_name)

        # with open("namgu_dong_name.pickle","wb") as file:
        #     pickle.dump(list_dong_name, file)


        with open("namgu_dong_name.pickle", "rb") as file:
            list_dong_name = pickle.load(file)

        list_search_keyword = ["독서실", "도서관", "학원"]

        for idx in range(len(list_cent_pos)):
            if list_dong_name[idx] == None:
                list_sum_all_grade.append(None)
                list_dic_text_info.append(None)
                continue

            sum_grade = 0
            dic_text_info = {}
            # 키워드 입력한데로 loop 돔
            for keyword in list_search_keyword:
                if keyword == "독서실":
                    dic_result = gather_data(keyword, list_cent_pos[idx],
                                        fir_dis=300, sec_dis=600, thir_dis=900,bonus_point=0)
                elif keyword == "학원":
                    dic_result = gather_data(keyword, list_cent_pos[idx],
                                        fir_dis=300, sec_dis=600, thir_dis=900,bonus_point=0)
                elif keyword == "도서관":
                    dic_result = gather_data(keyword, list_cent_pos[idx],
                                             fir_dis=300, sec_dis=600, thir_dis=900, bonus_point=3)


                sum_grade += dic_result["grade"]
                dic_text_info[keyword] = dic_result["text_dis_info"]

            list_sum_all_grade.append(sum_grade)
            list_dic_text_info.append(dic_text_info)

        dic_all_result = {}
        dic_all_result["list_dong_name"] = list_dong_name
        dic_all_result["list_sum_all_grade"] = list_sum_all_grade
        dic_all_result["list_dic_text_info"] = list_dic_text_info


        #api 제한 때문에 피클로 대체함.

        with open(f"{user_district}_dic_all_result.pickle","wb") as file:
            pickle.dump(dic_all_result, file)

    with open(f"{user_district}_dic_all_result.pickle", "rb") as file:
        dic_all_result = pickle.load(file)

    return dic_all_result






