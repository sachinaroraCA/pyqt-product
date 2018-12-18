def get_scores(product_id):
    from utils.database_utils import DatabaseConnect
    db = DatabaseConnect()
    dimension_scores = {}
    answers = db.get_answers_by_evaluation(product_id)
    if answers:
        formatted_answers = format_answer_to_get_score(answers)
        for dimension, answers in formatted_answers.items():
            d_score = get_dimension_score(answers)
            dimension_scores.update({dimension: d_score})
    return dimension_scores


def get_dimension_score(answer_list):
    """
    :param answer_list:
    :return:
    """
    total_marks = 0
    for answer in answer_list:
        total_marks += int(answer)
    total_questions = len(answer_list)
    if total_questions:
        return round(total_marks / total_questions * 25 - 25)
    else:
        return 0


def format_answer_to_get_score(dict_list):
    result_dict = {}

    for item in dict_list:
        if item["dimension"] not in result_dict:
            result_dict.update({item["dimension"]: [item["answer"]]})
        else:
            answer = item["answer"]
            answer_list = result_dict[item["dimension"]]
            answer_list.append(answer)
            result_dict.update({item["dimension"]:answer_list})
    return result_dict


def evaluate_dimensions(dimension_score_dict):

    dimensions_result = {}
    index = 0
    for key, value in dimension_score_dict:
        index += 1
        if key == "S1":
            if dimension_score_dict["S1"] >= 60:
                if (dimension_score_dict["S2"] < 30 and dimension_score_dict["S3"] < 30 and dimension_score_dict["S4"] < 30 and
                    dimension_score_dict["S5"] < 30 and dimension_score_dict["S6"] < 30 and dimension_score_dict["S7"] < 30 and
                        dimension_score_dict["S8"] < 30 and dimension_score_dict["S9"] < 30):
                    result = "Product is of D1 kind"

                elif (dimension_score_dict["S2"] < 40 and dimension_score_dict["S3"] < 40 and dimension_score_dict["S4"] < 40 and
                      dimension_score_dict["S5"] < 40 and dimension_score_dict["S6"] < 40 and dimension_score_dict["S7"] < 40 and
                      dimension_score_dict["S8"] < 40 and dimension_score_dict["S9"] < 40):
                    result = """Product may be of D1 kind"""
                else:
                    result = """Product is not of D1 kind"""
            else:
               result = """Product is not of D1 kind"""
        else:
            if value >= 40:
                result = "Product is of D{} kind".format(index)
            elif value >= 30:
                result = "Product tends to be of D{} kind".format(index)
            else:
                result = "Product is not of D{} kind".format(index)

        dimensions_result.update({key: result})

    return dimensions_result


def analyse_module(source_file, time_series_type):
    import numpy as np
    import pandas as pd

    df = pd.read_excel(source_file, header=None, usecols=[0, 1])

    if time_series_type == 1:
        y = 10
        start_index = 20
    else:
        y = 8
        start_index = 25

    array = np.zeros((12, y))
    i, j, index = 0, 0, 0
    while index < (12 * y):
        if i < 12:
            if j < y:
                array[i][j] = df[1][index + start_index]
                index += 1
                j += 1
            else:
                j = 0
                i += 1
    print(array)
    create_index(array, y)


def create_index(array, y):
    import pandas as pd

    index_dict = {}
    i, j, index, sum = 0, 0, 0, 0

    while index < (12 * y):
        if i < 12:
            if j < y:
                for item in range(y):
                    if not pd.isnull(array[j][item]):
                        sum += array[j][item]
                index_dict["index" + str(i+1) + "-" + str(j+1)] = sum / y
                index += 1
                j += 1
                sum = 0
            else:
                j = 0
                i += 1

    print(index_dict)


analyse_module(source_file="/home/cloudanalogy/Downloads/Demo-data.xls", time_series_type=1)


