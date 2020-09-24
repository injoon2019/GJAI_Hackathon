
import pickle
import pandas

from kakao_function import kakao_dong_name
from kakao_function import kakao_keyword


def gather_data(keyword, cent_pos, fir_dis, sec_dis, thir_dis, bonus_point):
    if keyword == "독서실":
        cent_x = cent_pos[0]
        cent_y = cent_pos[1]

        # def kakao_keyword(key_word, cent_x, cent_y, radius=1000, page=1, size=2):
        dic_fir_dis = kakao_keyword(keyword, cent_x, cent_y, radius=fir_dis)
        print(dic_fir_dis)
        print(len(dic_fir_dis))
        dic_sec_dis = kakao_keyword(keyword, cent_x, cent_y, radius=sec_dis)
        dic_thir_dis = kakao_keyword(keyword, cent_x, cent_y, radius=thir_dis)



def gather_data_from_cent(list_cent_pos, user_district):


    list_all_grade = []
    list_point_grade_dict = []
    list_dong_name = []
    dic_result = {}

    # api 제한 때문에 피클로 대체함.
    # for idx in range(len(list_cent_pos)):
    #     dong_name = kakao_dong_name(list_cent_pos[idx], user_district)
    #     list_dong_name.append(dong_name)

    # with open("namgu_dong_name.pickle","wb") as file:
    #     pickle.dump(list_dong_name, file)

    with open("namgu_dong_name.pickle", "rb") as file:
        list_dong_name = pickle.load(file)

    for idx in range(len(list_cent_pos)):
        if list_dong_name[idx] == None:
            continue

        study_cafe = gather_data("독서실", list_cent_pos[idx],
                                fir_dis=300, sec_dis=600, thir_dis=900,bonus_point=0)

        break




