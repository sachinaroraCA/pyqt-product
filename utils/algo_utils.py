def get_scores(product_id):
    """
                        Calculate the score of all dimensions
    :param product_id:
    :return: Dictionary containing the dimention as a key and score as a value.
    """
    from utils.database_utils import DatabaseConnect
    db = DatabaseConnect()
    dimension_scores = {}
    answers = db.get_answers_by_evaluation(product_id)  # Get all the answers of an evaluation
    if answers:
        formatted_answers = format_answer_to_get_score(answers)
        for dimension, answers in formatted_answers.items():
            d_score = get_dimension_score(answers)
            dimension_scores.update({dimension: d_score})
    return dimension_scores


def get_dimension_score(answer_list):
    """
                            Calculate the score of a dimension
    :param answer_list:
    :return: dimension_score
    """
    total_marks = 0
    for answer in answer_list:
        total_marks += int(answer)
    total_questions = len(answer_list)
    if total_questions:
        return round(total_marks / total_questions * 25 - 25)
    else:
        return 0


def format_answer_to_get_score(answer_list):
    """
                            Convert the answer_list (list of dictionaries) to a single dictionary
    :param answer_list:
    :return:
    """
    result_dict = {}

    for item in answer_list:
        if item["dimension"] not in result_dict:
            result_dict.update({item["dimension"]: [item["answer"]]})
        else:
            answer = item["answer"]
            answer_list = result_dict[item["dimension"]]
            answer_list.append(answer)
            result_dict.update({item["dimension"]:answer_list})
    return result_dict


def evaluate_dimensions(dimension_score_dict):
    """
                                    Calculate and get the type of the dimension as per their score of sub_indexes
    :param dimension_score_dict:
    :return:
    """

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


def analyse_module(source_file, time_series_type, index):
    """
                                    Algorithm to analysis of indexes
    :param source_file:
    :param time_series_type:
    :param index:
    :return:
    """
    import numpy as np
    import pandas as pd

    if index == 1:
        """
                Algorithm to analysis of index-1
        """
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

        return create_index(array, y)
    else:
        # Todo: Write here algorithms for the analysis of other indexes
        # for now we are returning 0 as a value of every sub-index for index 2-12
        return {k: 0 for k in range(1, 13)}


def create_index(array, y):
    """
                Calculate the scores sub_index value for index 1.
    :param array:
    :param y:
    :return: dictionary of sub_index values for index 1
    """
    import pandas as pd

    index_dict = {}
    i, j, index, sum = 0, 0, 0, 0

    while index < (12 * y):
        if i < 12:
            for j in range(y):
                if not pd.isnull(array[i][j]):
                    sum += array[i][j]
                index += 1
            index_dict[i+1] = sum / y
            i += 1
            sum = 0
        else:
            index += 12 * y

    return index_dict

