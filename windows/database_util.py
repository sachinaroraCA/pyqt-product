from PyQt5 import QtSql
from PyQt5.QtWidgets import QMessageBox
import pymysql
from utils.time_utils import get_current_time, unix_time_millis


class DatabaseConnect:
    def __init__(self):
        """
        # Create a connection to the database
        """
        self.connection = pymysql.connect(host='localhost',
                                          db='fpat_db',
                                          user="root",
                                          charset='utf8mb4',
                                          cursorclass=pymysql.cursors.DictCursor)
    
    """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
                                USERS FOR LOGIN SYSTEM
    """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    def auth_user(self, un, password):
        """
        # Authenticate the User to login the system
        :param un: Username
        :param password: Secret key to authenticate the user
        :return:
        """
        try:
            with self.connection.cursor() as cursor:
                query = "select username from fpat_user where username = '{username}' and password = '{password}';".format(
                        username=un,
                        password=password)
                cursor.execute(query)
                result = cursor.fetchall()
                cursor.close()
                if result:
                    return True
                else:
                    QMessageBox.about(QMessageBox(), "Warning", "Invalid Secret code !!!")
                    return False
        except Exception:
            print(Exception)
            QMessageBox.about(QMessageBox(), "Warning", "Database Error !!!")
            return False

    def get_users(self):
        """
        # Return all the users registered to the system
        :return: List of all the users
        """
        user_list = []

        try:
            with self.connection.cursor() as cursor:
                query = "select username from fpat_user;"
                cursor.execute(query)
                result = cursor.fetchall()
                for user_details in result:
                    user_list.append(user_details["username"])
                cursor.close()
            return user_list
        except Exception as ex:
            print(ex)
            QMessageBox.about(QMessageBox(), "Warning", "Database Error !!!")
            return []
    
    """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
                                PRODUCT MODULE
    """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    def get_products(self, evaluate=None):
        """
        # Return all the Products
        :return: List of all the products
        """
        product_list = []
        productId_list = []
        is_evaluated_list = []

        try:
            with self.connection.cursor() as cursor:
                query = "select id,name,evaluated from fpat_product;"
                cursor.execute(query)
                result = cursor.fetchall()
                for product_details in result:
                    product_list.append(product_details["name"])
                    productId_list.append(product_details['id'])
                    is_evaluated_list.append(product_details["evaluated"])
                cursor.close()
            if evaluate:
                return product_list, productId_list, is_evaluated_list
            else:
                return product_list, productId_list
        except Exception as ex:
            print(ex)
            QMessageBox.about(QMessageBox(), "Warning", "Database Error !!!")
            return []

    def save_product_record(self, name, code, categorya, categoryb, info1="NULL", info2='NULL', info3='NULL', info4='NULL', info5='NULL',
                            info6='NULL', info7='NULL'):
        """
        # Create a record in product table
        :param name:
        :param code:
        :param categorya:
        :param categoryb:
        :param info1:
        :param info2:
        :param info3:
        :param info4:
        :param info5:
        :param info6:
        :param info7:
        :return:
        """
        try:
            with self.connection.cursor() as cursor:
                query = "insert into fpat_product(created_at, name,code, categorya, categoryb, info1,info2, info3, "\
                        "info4, info5, info6, info7) values({created_at}, '{name}', '{code}', '{categorya}', "\
                        "'{categoryb}', '{info1}', '{info2}', '{info3}', '{info4}', '{info5}', '{info6}'"\
                         ", '{info7}')".format(created_at=get_current_time(),
                                               name=name,
                                               code=code,
                                               categorya=categorya,
                                               categoryb=categoryb,
                                               info1=info1,
                                               info2=info2,
                                               info3=info3,
                                               info4=info4,
                                               info5=info5,
                                               info6=info6,
                                               info7=info7
                                               )
                cursor.execute(query)
                self.connection.commit()
                cursor.close()
            return True
        except Exception as ex:
            print(ex)
            QMessageBox.about(QMessageBox(), "Warning", "Database Error !!!")
            return False

    def update_product_record(self, id, name, code, categorya, categoryb, info1="NULL", info2="NULL", info3="NULL", info4="NULL",
                              info5="NULL", info6="NULL", info7="NULL"):
        """
        Update a product in Product(fpat_product) table
        :param id:
        :param name:
        :param code:
        :param categorya:
        :param categoryb:
        :param info1:
        :param info2:
        :param info3:
        :param info4:
        :param info5:
        :param info6:
        :param info7:
        :return:
        """
        try:
            with self.connection.cursor() as cursor:
                query_str = "UPDATE fpat_product SET  categorya='{categorya}', categoryb='{categoryb}', code='{code}',"\
                            "info1='{info1}', info2='{info2}', info3='{info3}', info4='{info4}', info5='{info5}', "\
                            "info6='{info6}',info7='{info7}',name='{name}' WHERE id={id};".format(name=name,
                                                                                                  code=code,
                                                                                                  categorya=categorya,
                                                                                                  categoryb=categoryb,
                                                                                                  info1=info1,
                                                                                                  info2=info2,
                                                                                                  info3=info3,
                                                                                                  info4=info4,
                                                                                                  info5=info5,
                                                                                                  info6=info6,
                                                                                                  info7=info7,
                                                                                                  id=id
                                                                                                  )
                cursor.execute(query_str)
                cursor.fetchone()
                self.connection.commit()
                cursor.close()
            return True
        except Exception as ex:
            print(ex)
            QMessageBox.about(QMessageBox(), "Warning", "Database Error !!!")
            return False

    def get_product_details(self, id):
        """
        # Get all the field values on the basis of "id" of a Product
        :param id:
        :return: product_info - information about a product as a string
                 product_info_dict - a dictionary containing fields of a product
        """
        product_info = ""
        product_info_dict = {}

        try:
            with self.connection.cursor() as cursor:
                query = "select * from fpat_product where id = '{id}'".format(id=id)
                cursor.execute(query)
                result = cursor.fetchall()
                for product_details in result:
                    for key, value in product_details.items():
                        if key not in ['id', 'evaluated', 'created_at', 'evalutions_ID'] and value:
                            product_info += str(key) + "\t:" + str(value) + "\n"
                    product_info_dict.update(product_details)
                cursor.close()
            return product_info, product_info_dict
        except Exception as ex:
            print(ex)
            QMessageBox.about(QMessageBox(), "Warning", "Database Error !!!")
            return []

    def delete_product(self, id):
        """
        # Delete a product from product table on the basis of id.
        :param id:
        :return: IsDeleted - boolean return the state of the product as deleted or not
        """

        try:
            with self.connection.cursor() as cursor:
                query ="DELETE FROM fpat_product WHERE id='{id}'".format(id=id)
                cursor.execute(query)
                self.connection.commit()
                cursor.close()
                return True
        except Exception as ex:
            print(ex)
            QMessageBox.about(QMessageBox(), "Warning", "Database Error !!!")
            return False
        
    """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
                            EVALUATION MODULE
    """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    def get_all_questions(self):
        """
        # Get all the questions mapped with dimensions in tabs
        :return: List of questions
        """
        try:
            with self.connection.cursor() as cursor:
                query = "SELECT id, dimension, question FROM fpat_question order by dimension;"
                cursor.execute(query)
                question_list = cursor.fetchall()
                print(question_list)
            return question_list
        except Exception as ex:
            print(ex)
            QMessageBox.about(QMessageBox(), "Warning", "Database Error !!!")
            return []

    def create_evaluation(self, product_id, attachment_one, attachment_two):
        """
        # Create a new Evaluation of a Product.
        :param product_id:
        :param attachment_one:
        :param attachment_two:
        :return: evalution id
        """
        ##TODO: Create Evaluation
        ##TODO: Upadte the Evaluation_Id in Product
        #TODO: Create all Evaluation Answers
        #TODO: Add every answer to the evaluation_evaluation_answer

        try:
            with self.connection.cursor() as cursor:

                # Create Evaluation
                evalution_query = "INSERT INTO fpat_db.fpat_evalutions (created_at, attachment_one,"\
                                  " attachment_two) VALUES({created_at}, '{attachment_one}', "\
                                  "'{attachment_two}');".format(created_at=get_current_time(),
                                                                attachment_one=attachment_one,
                                                                attachment_two=attachment_two)
                cursor.execute(evalution_query)
                evalution_id = cursor.lastrowid
                self.connection.commit()

                # Upadte the Evaluation_Id in Product
                product_query = "UPDATE fpat_product SET evalutions_ID='{evalutions_ID}', "\
                                "evaluated={evaluated} WHERE id={id};".format(evaluated=1,
                                                                              evalutions_ID=evalution_id,
                                                                              id=product_id)
                cursor.execute(product_query)
                self.connection.commit()
                cursor.close()
            return evalution_id
        except Exception as ex:
            print(ex)
            QMessageBox.about(QMessageBox(), "Warning", "Database Error !!!")
            return False

    def save_answers(self, answer, question, dimension, evaluation_id):
        """
        # Save the answer of the evaluation questions into the database
        :param answer:
        :param question:
        :param dimension:
        :param evaluation_id:
        :return:
        """
        try:
            with self.connection.cursor() as cursor:
                answer_query = "INSERT INTO fpat_evaluation_answers( created_at, answer, dimension, question)"\
                               " VALUES({created_at}, {answer}, {dimension}, '{question}');".format(created_at=get_current_time(),
                                                                                                      answer=answer,
                                                                                                      dimension=dimension,
                                                                                                      question=question)
                cursor.execute(answer_query)
                self.connection.commit()
                answer_id = cursor.lastrowid

                mapping_query = "INSERT INTO fpat_db.fpat_evalutions_evalution_answers (fpat_evalutions_ID," \
                                " evalution_answers_ID) VALUES({fpat_evalutions_ID}, {evalution_answers_ID});" \
                                "".format(fpat_evalutions_ID=evaluation_id,
                                          evalution_answers_ID=answer_id)
                cursor.execute(mapping_query)
                self.connection.commit()
                return True

        except Exception as ex:
            print(ex)
            QMessageBox.about(QMessageBox(), "Warning", "Database Error !!!")
            return False

    def delete_evaluation(self, product_id):
        """
        # Reset the evaluation of a product
        :param product_id:
        :return: Boolean as whether the
        """
        try:
            with self.connection.cursor() as cursor:

                evaluation_id = ""
                answer_list = []
                # Get Evaluation records of a product
                if product_id:
                    product_query = "select evalutions_ID from fpat_product where id={id};".format(id=product_id)
                    cursor.execute(product_query)
                    product_dict = cursor.fetchone()
                    if product_dict["evalutions_ID"]:
                        evaluation_id.replace("", product_dict["evalutions_ID"])

                # Get all answers_ids in selected evaluation
                if evaluation_id:
                    answer_query = "SELECT evalution_answers_ID FROM fpat_db.fpat_evalutions_evalution_answers"\
                                   " WHERE fpat_evalutions_ID={id};".format(id=evaluation_id)

                    cursor.execute(answer_query)
                    answer_list.extend(cursor.fetchall())

                # Delete answer and evaluation mapping
                if evaluation_id:
                    answer_map_delete_query = "DELETE FROM fpat_db.fpat_evalutions_evalution_answers"\
                                              " WHERE fpat_evalutions_ID={id};".format(id=evaluation_id)
                    cursor.execute(answer_map_delete_query)

                # Delete all selected answers
                if answer_list:
                    answer_delete_query = "DELETE FROM fpat_evaluation_answers "\
                                          "WHERE id in ({id_list})".format(id_list=",".join([str(answer["evalution_answers_ID"]) for answer in answer_list]))
                    cursor.execute(answer_delete_query)

                # Update Product record to remove evaluation_id
                if product_id:
                    product_update_query = "UPDATE fpat_product SET evalutions_ID={evalutions_ID}, evaluated={evaluated}"\
                                           " WHERE id={id};".format(evaluated="NULL",
                                                                    evalutions_ID="NULL",
                                                                    id=product_id)
                    cursor.execute(product_update_query)
                self.connection.commit()

                # Delete evaluation record
                if evaluation_id:
                    evaluation_delete_query = "DELETE FROM fpat_db.fpat_evalutions WHERE id={id}".format(id=evaluation_id)
                    cursor.execute(evaluation_delete_query)

                self.connection.commit()
                cursor.close()
                return True

        except Exception as ex:
            print(ex)
            QMessageBox.about(QMessageBox(), "Warning", "Database Error !!!")
            return False
    
    """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
                                TIME SERIES MODULE
    """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    def save_timeseries(self, analyse_type, description, empty_data, end_time, file_type, name, series_data,
                        start_time):
        try:
            from datetime import datetime
            with self.connection.cursor() as cursor:
                # if empty_data:
                #     empty_data = int(empty_data)
                # else:
                #     empty_data = "NULL"
                # if end_time:
                #     end_time = unix_time_millis(datetime.time(end_time))
                # else:
                #     end_time = "NULL"
                # if series_data:
                #     series_data = int(series_data)
                # else:
                #     series_data = "NULL"
                # if start_time:
                #     start_time = unix_time_millis(datetime(start_time))
                # else:
                #     start_time = "NULL"

                timeseries_query = "INSERT INTO fpat_db.fpat_timeseries (created_at, analyse_type, description,"\
                                   " empty_data, end_time, file_type, name, series_data, start_time)"\
                                   " VALUES({created_at}, '{analyse_type}', '{description}', '{empty_data}',"\
                                   " {end_time}, '{file_type}', '{name}', {series_data}, {start_time}"\
                                   ");".format(created_at=get_current_time(),
                                               analyse_type=analyse_type,
                                               description=description,
                                               empty_data=empty_data,
                                               end_time=end_time,
                                               file_type=file_type,
                                               name=name,
                                               series_data=series_data,
                                               start_time=start_time,
                                               )


                cursor.execute(timeseries_query)
                timeseries_id = cursor.lastrowid
                self.connection.commit()
                return timeseries_id

        except Exception as ex:
            print(ex)
            QMessageBox.about(QMessageBox(), "Warning", "Database Error !!!")
            return False

    def get_timeserieses(self):
        timeseries_list = []
        timeseriesId_list = []

        try:
            with self.connection.cursor() as cursor:
                query = "select id,name from fpat_timeseries;"
                cursor.execute(query)
                result = cursor.fetchall()
                for product_details in result:
                    timeseries_list.append(product_details["name"])
                    timeseriesId_list.append(product_details['id'])
                cursor.close()

            return timeseries_list, timeseriesId_list
        except Exception as ex:
            print(ex)
            QMessageBox.about(QMessageBox(), "Warning", "Database Error !!!")
            return []
    
    def get_timeseries_details(self, timeseries_id):
        timeseries_info_dict = {}
        try:
            with self.connection.cursor() as cursor:
                query = "select * from fpat_timeseries where id = '{id}'".format(id=timeseries_id)
                cursor.execute(query)
                timeseries_info_dict.update(cursor.fetchone())
                cursor.close()
            return timeseries_info_dict
        except Exception as ex:
            print(ex)
            QMessageBox.about(QMessageBox(), "Warning", "Database Error !!!")
            return {}

    def delete_timeseries(self, id):
        """
        # Delete a time series from time series table on the basis of id.
        :param id:
        :return: IsDeleted - boolean return the state of the time series as deleted or not
        """

        try:
            with self.connection.cursor() as cursor:
                query = "DELETE FROM fpat_timeseries WHERE id='{id}'".format(id=id)
                cursor.execute(query)
                self.connection.commit()
                cursor.close()
                return True
        except Exception as ex:
            print(ex)
            QMessageBox.about(QMessageBox(), "Warning", "Database Error !!!")
            return False

    def update_timeseries_productId(self, timeseries_id, product_id):
        try:
            with self.connection.cursor() as cursor:
                query = "UPDATE fpat_timeseries SET product_ID={product_id} WHERE id='{id}'".format(id=timeseries_id,
                                                                                                    product_id=product_id)
                cursor.execute(query)
                self.connection.commit()
                cursor.close()
                return True
        except Exception as ex:
            print(ex)
            QMessageBox.about(QMessageBox(), "Warning", "Database Error !!!")
            return False

    def update_timeseries(self, product_id, timeseries_id, analyse_type, description, empty_data, end_time, file_type,
                          name, series_data, start_time):
        try:
            with self.connection.cursor() as cursor:
                query = "UPDATE fpat_db.fpat_timeseries SET analyse_type='{analyse_type}', description='{description}'"\
                        ", empty_data='{empty_data}', end_time={end_time}, file_type='{file_type}', name='{name}', "\
                        "series_data={series_data}, start_time={start_time} WHERE id={id};".format(id=timeseries_id,
                                                                                                   product_id=product_id,
                                                                                                   analyse_type=analyse_type,
                                                                                                   description=description,
                                                                                                   empty_data =empty_data,
                                                                                                   end_time=end_time,
                                                                                                   file_type=file_type,
                                                                                                   name=name,
                                                                                                   series_data=series_data,
                                                                                                   start_time=start_time
                                                                                                   )
                cursor.execute(query)
                self.connection.commit()
                cursor.close()
                return True
        except Exception as ex:
            print(ex)
            QMessageBox.about(QMessageBox(), "Warning", "Database Error !!!")
            return False

    """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
                                MODEL MODULE
    """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    def get_models(self, evaluate=None):
        """
        # Return all the models
        :return: List of all the models
        """
        model_list = []
        modelId_list = []

        try:
            with self.connection.cursor() as cursor:
                query = "select id,name from fpat_models;"
                cursor.execute(query)
                result = cursor.fetchall()
                for model_details in result:
                    model_list.append(model_details["name"])
                    modelId_list.append(model_details['id'])
                cursor.close()
            if evaluate:
                return model_list, modelId_list
            else:
                return model_list, modelId_list
        except Exception as ex:
            print(ex)
            QMessageBox.about(QMessageBox(), "Warning", "Database Error !!!")
            return []

    def save_model_record(self, name, me1, me10, me11, me12, me13, me14, me15, me16,me2, me3, me4, me5, me6, me7, me8,
                          me9, description, param1, param2, param3, type, time_series_ID):
        """
        :param name:
        :param me1:
        :param me10:
        :param me11:
        :param me12:
        :param me13:
        :param me14:
        :param me15:
        :param me16:
        :param me2:
        :param me3:
        :param me4:
        :param me5:
        :param me6:
        :param me7:
        :param me8:
        :param me9:
        :param description:
        :param param1:
        :param param2:
        :param param3:
        :param type:
        :param time_series_ID:
        :return:
        """
        try:
            with self.connection.cursor() as cursor:
                query = "INSERT INTO fpat_db.fpat_models (created_at, me1, me10, me11, me12, me13, me14, me15, me16,"\
                        " me2, me3, me4, me5, me6, me7, me8, me9, description, name, param1, param2, param3, type,"\
                        " time_series_ID) VALUES({created_at}, {me1}, {me10}, {me11}, {me12}, {me13}, {me14}, {me15},"\
                        " {me16}, {me2}, {me3}, {me4}, {me5}, {me6}, {me7}, {me8}, {me9},"\
                        "'{description}', '{name}', '{param1}', '{param2}',"\
                        " '{param3}', '{type}', {time_series_ID});".format(created_at=get_current_time(),
                                                                           me1=me1,
                                                                           me10=me10,
                                                                           me11=me11,
                                                                           me12=me12,
                                                                           me13=me13,
                                                                           me14=me14,
                                                                           me15=me15,
                                                                           me16=me16,
                                                                           me2=me2,
                                                                           me3=me3,
                                                                           me4=me4,
                                                                           me5=me5,
                                                                           me6=me6,
                                                                           me7=me7,
                                                                           me8=me8,
                                                                           me9=me9,
                                                                           description=description,
                                                                           name=name,
                                                                           param1=param1,
                                                                           param2=param2,
                                                                           param3=param3,
                                                                           type=type,
                                                                           time_series_ID=time_series_ID
                                                                           )

                cursor.execute(query)
                self.connection.commit()
                cursor.close()
            return True
        except Exception as ex:
            print(ex)
            QMessageBox.about(QMessageBox(), "Warning", "Database Error !!!")
            return False

    def update_model_record(self, name, me1, me10, me11, me12, me13, me14, me15, me16,me2, me3, me4, me5, me6, me7, me8,
                            me9, description, param1, param2, param3, type, time_series_ID, model_id):
        """
        :param name:
        :param me1:
        :param me10:
        :param me11:
        :param me12:
        :param me13:
        :param me14:
        :param me15:
        :param me16:
        :param me2:
        :param me3:
        :param me4:
        :param me5:
        :param me6:
        :param me7:
        :param me8:
        :param me9:
        :param description:
        :param param1:
        :param param2:
        :param param3:
        :param type:
        :param time_series_ID:
        :param model_id:
        :return:
        """
        try:
            with self.connection.cursor() as cursor:
                query_str = 'UPDATE fpat_models SET me1={me1}, me10={me10}, me11={me11}, me12={me12}, me13={me13},'\
                            ' me14={me14}, me15={me15}, me16={me16}, me2={me2}, me3={me3}, me4={me4}, me5={me5},'\
                            'me6={me6}, me7={me7}, me8={me8}, me9={me9}, description="{description}", name="{name}",'\
                            ' param1="{param1}", param2="{param2}", param3="{param3}", type="{type}",'\
                            ' time_series_ID=time_series_ID WHERE id={model_id};'.format(me1=me1, me10=me10,
                            me11=me11, me12=me12, me13=me13, me14=me14, me15=me15, me16=me16, me2=me2, me3=me3,
                            me4=me4, me5=me5, me6=me6, me7=me7, me8=me8, me9=me9, description=description, name=name,
                            param1=param1, param2=param2, param3=param3, type=type, time_series_ID=time_series_ID,
                                                                                         model_id=model_id)
                cursor.execute(query_str)
                cursor.fetchone()
                self.connection.commit()
                cursor.close()
            return True
        except Exception as ex:
            print(ex)
            QMessageBox.about(QMessageBox(), "Warning", "Database Error !!!")
            return False

    def get_model_details(self, id):
        """
        # Get all the field values on the basis of "id" of a model
        :param id:
        :return: model_info - information about a model as a string
                 model_info_dict - a dictionary containing fields of a model
        """
        model_info = ""
        model_info_dict = {}

        try:
            with self.connection.cursor() as cursor:
                query = "select * from fpat_models where id = '{id}'".format(id=id)
                cursor.execute(query)
                result = cursor.fetchall()
                for model_details in result:
                    for key, value in model_details.items():
                        if key not in ['id', 'created_at', 'time_series_ID'] and value:
                            model_info += str(key) + "\t:" + str(value) + "\n"
                    model_info_dict.update(model_details)
                cursor.close()
            return model_info, model_info_dict
        except Exception as ex:
            print(ex)
            QMessageBox.about(QMessageBox(), "Warning", "Database Error !!!")
            return []

    def delete_model(self, id):
        """
        # Delete a model from model table on the basis of id.
        :param id:
        :return: IsDeleted - boolean return the state of the model as deleted or not
        """

        try:
            with self.connection.cursor() as cursor:
                query = "DELETE FROM fpat_models WHERE id='{id}'".format(id=id)
                cursor.execute(query)
                self.connection.commit()
                cursor.close()
                return True
        except Exception as ex:
            print(ex)
            QMessageBox.about(QMessageBox(), "Warning", "Database Error !!!")
            return False

    def test_def(self, id=1):
        timeseries_info_dict = {}
        try:
            with self.connection.cursor() as cursor:
                query = "select * from fpat_timeseries where id = '{id}'".format(id=id)
                cursor.execute(query)
                timeseries_info_dict.update(cursor.fetchone())
                cursor.close()
            return timeseries_info_dict
        except Exception as ex:
            print(ex)
            QMessageBox.about(QMessageBox(), "Warning", "Database Error !!!")
            return {}


if __name__ == '__main__':
    conn = DatabaseConnect()
    # dict = conn.get_timeserieses()
    # print(dict)
    # conn.get_product_details("exercitation ullamco lab")
    # conn.get_all_questions()
    # conn.update_product_record(id=3, name="Aman", code="007",categorya="A", categoryb="B")
    # print(get_current_time())
