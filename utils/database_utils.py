from PyQt5.QtWidgets import QMessageBox
import pymysql
from utils.time_utils import get_current_time, unix_time_millis


class DatabaseConnect:
    def __init__(self):
        """
                        Create a connection to the database
        """
        try:
            self.connection = pymysql.connect(host='localhost',
                                              db='fpat_db',
                                              user="root",
                                              charset='utf8mb4',
                                              cursorclass=pymysql.cursors.DictCursor)
        except Exception as ex:
            QMessageBox.about(QMessageBox(), "Warning", str(ex))

    """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
                                USERS FOR LOGIN SYSTEM
    """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    def auth_user(self, un, password):
        """
                                    Authenticate the User to login the system
        :param un: Username
        :param password: Secret key to authenticate the user
        :return: authorised (True/False)
        """
        try:
            with self.connection.cursor() as cursor:
                query = "select username, password from fpat_user where username = '{username}' and password ="\
                        " '{password}';".format(username=un,
                                                password=password)
                cursor.execute(query)
                result = cursor.fetchone()
                cursor.close()
                if result and result["password"] == password:
                    return True
                else:
                    return False
        except Exception:
            return False

    def get_users(self):
        """
                                Return all the users registered to the system

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
            return False
    
    """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
                                PRODUCT MODULE
    """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    def get_products(self, evaluate=None, window=QMessageBox()):
        """
        # Get all the Products
        :return: List of all the products
        """
        product_list = []
        productId_list = []
        is_evaluated_list = []

        try:
            with self.connection.cursor() as cursor:
                query = "select id,name,evaluated,categorya from fpat_product;"
                cursor.execute(query)
                products_dict = cursor.fetchall()
                for product_details in products_dict:
                    product_list.append(product_details["name"])
                    productId_list.append(product_details['id'])
                    is_evaluated_list.append(product_details["evaluated"])
                cursor.close()
            if evaluate:
                return product_list, productId_list, is_evaluated_list, products_dict
            else:
                return product_list, productId_list
        except Exception as ex:
            print(ex)
            QMessageBox.about(window, "Warning", "Database Error !!!")
            if evaluate:
                return product_list, productId_list, is_evaluated_list, {}
            else:
                return product_list, productId_list

    def save_product_record(self, name, code, categorya, categoryb, info1="NULL", info2='NULL', info3='NULL',
                            info4='NULL', info5='NULL', info6='NULL', info7='NULL'):
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
            return False

    def update_product_record(self, id, name, code, categorya, categoryb, info1="NULL", info2="NULL", info3="NULL",
                              info4="NULL", info5="NULL", info6="NULL", info7="NULL"):
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
            return False

    def get_product_details(self, id, window=QMessageBox()):
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
                query = "select id, name, code, categorya, categoryb, info1, info2, info3, info4, info5, info6, info7"\
                        " from fpat_product where id = '{id}'".format(id=id)
                cursor.execute(query)
                result = cursor.fetchall()
                for product_details in result:
                    for key, value in product_details.items():
                        if key not in ['id', 'evaluated', 'created_at', 'evalutions_ID'] and value:
                            product_info += str(key).title() + "\t:  " + str(value) + "\n"
                    product_info_dict.update(product_details)
                cursor.close()
            return product_info, product_info_dict
        except Exception as ex:
            print(ex)
            QMessageBox.about(window, "Warning", "Database Error !!!")
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
            return False
        
    """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
                            EVALUATION MODULE
    """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    def get_all_questions(self, window=QMessageBox()):
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
            QMessageBox.about(window, "Warning", "Database Error !!!")
            return []

    def get_answers_by_evaluation(self, product_id, window=QMessageBox()):
        """
                                        Get all answers of an evaluation of a product

        This function includes following steps:
        1. Get Evaluation records of a product
        2. Get all answers_ids in selected evaluation
        3. Select all answers of the selected evaluation

        :param product_id:
        :return: answers
        """
        answers_ids = []
        answers = []
        try:
            with self.connection.cursor() as cursor:
                # Get Evaluation records of a product
                if product_id:
                    product_query = "select evalutions_ID from fpat_product where id={id};".format(id=product_id)
                    cursor.execute(product_query)
                    product_dict = cursor.fetchone()
                    if "evalutions_ID" in product_dict:
                        evaluation_id = product_dict["evalutions_ID"]
                    else:
                        evaluation_id = None
                else:
                    evaluation_id = None

                # Get all answers_ids in selected evaluation
                if evaluation_id:
                    answer_query = "SELECT evalution_answers_ID FROM fpat_db.fpat_evalutions_evalution_answers" \
                                   " WHERE fpat_evalutions_ID={id};".format(id=evaluation_id)

                    cursor.execute(answer_query)
                    answers_ids.extend(cursor.fetchall())

                # Select all answers of the selected evaluation
                if answers_ids:
                    answers_query = "SELECT dimension, question, answer FROM fpat_evaluation_answers " \
                                    "WHERE id in ({id_list})".format(
                                    id_list=",".join([str(answer["evalution_answers_ID"]) for answer in answers_ids]))
                    cursor.execute(answers_query)
                    answers.extend(cursor.fetchall())

                    self.connection.commit()
                cursor.close()

        except Exception as ex:
            print(ex)
            QMessageBox.about(window, "Warning", "Database Error !!!")
        return answers

    def get_attachments(self, window, product_id ):
        attachments = {}
        try:

            with self.connection.cursor() as cursor:
                # Get Evaluation records of a product
                if product_id:
                    product_query = "select evalutions_ID from fpat_product where id={id};".format(id=product_id)
                    cursor.execute(product_query)
                    product_dict = cursor.fetchone()
                    if "evalutions_ID" in product_dict:
                        evaluation_id = product_dict["evalutions_ID"]
                    else:
                        evaluation_id = None
                else:
                    evaluation_id = None

                if evaluation_id:
                    product_query = "select id, attachment_one, attachment_two from fpat_evalutions where id={id};".format(id=evaluation_id)
                    cursor.execute(product_query)
                    attachments.update(cursor.fetchone())

        except Exception as ex:
            print(ex)
            QMessageBox.about(window, "Warning", "Database Error !!!")
        return attachments


    def create_evaluation(self, product_id, attachment_one, attachment_two, window=QMessageBox()):
        """
                                            Create a new Evaluation of a Product.
        :param product_id:
        :param attachment_one:
        :param attachment_two:
        :return: evalution id

        Steps to create an Evaluation:
        1. Create Evaluation
        2. Update the Evaluation_Id in Product
        3. Create all Evaluation Answers
        4. Add every answer to the evaluation_evaluation_answer
        """

        try:
            with self.connection.cursor() as cursor:

                # Create Evaluation
                evalution_query = "INSERT INTO fpat_evalutions (created_at, attachment_one,"\
                                  " attachment_two) VALUES({created_at}, '{attachment_one}', "\
                                  "'{attachment_two}');".format(created_at=get_current_time(),
                                                                attachment_one=attachment_one,
                                                                attachment_two=attachment_two)
                cursor.execute(evalution_query)
                evalution_id = cursor.lastrowid
                self.connection.commit()

                # Update the Evaluation_Id in Product
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
            QMessageBox.about(window, "Warning", "Database Error !!!")
            return False

    def save_answers(self, answer, question, dimension, evaluation_id, window=QMessageBox()):
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
            QMessageBox.about(window, "Warning", "Database Error !!!")
            return False

    def delete_evaluation(self, product_id, window=QMessageBox()):
        """
                                                Reset the evaluation of a product
        This function include following steps:
        1. Get Evaluation records of a product
        2. Get all answers_ids in selected evaluation
        3. Delete answer and evaluation mapping
        4. Delete all answers of current evaluation
        5. Update Product record to remove evaluation_id
        6. Delete attachments from evaluation and evaluation record
        :param product_id:
        :return:
        """
        try:
            with self.connection.cursor() as cursor:

                answer_list = []
                # Get Evaluation records of a product
                if product_id:
                    product_query = "select evalutions_ID from fpat_product where id={id};".format(id=product_id)
                    cursor.execute(product_query)
                    product_dict = cursor.fetchone()
                    if "evalutions_ID" in product_dict:
                        evaluation_id = product_dict["evalutions_ID"]
                    else:
                        evaluation_id = None
                else:
                    evaluation_id = None

                # Get all answers_ids in selected evaluation
                if evaluation_id:
                    answer_query = "SELECT evalution_answers_ID FROM fpat_db.fpat_evalutions_evalution_answers"\
                                   " WHERE fpat_evalutions_ID={id};".format(id=evaluation_id)

                    cursor.execute(answer_query)
                    answer_list.extend(cursor.fetchall())

                    # Delete answer and evaluation mapping

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

                # Delete attachments from evaluation and evaluation record
                if evaluation_id:
                    # Delete attachments from evaluation
                    evaluation_attachment_query = "SELECT attachment_one, attachment_two FROM fpat_db.fpat_evalutions"\
                                              " WHERE id={id}".format(id=evaluation_id)
                    cursor.execute(evaluation_attachment_query)
                    attachments = cursor.fetchone()
                    if attachments["attachment_one"]:
                        self.remove_file(attachments["attachment_one"])
                    if attachments["attachment_two"]:
                        self.remove_file(attachments["attachment_two"])

                    # Delete Evaluation
                    evaluation_delete_query = "DELETE FROM fpat_db.fpat_evalutions WHERE id={id}".format(id=evaluation_id)
                    cursor.execute(evaluation_delete_query)

                    self.connection.commit()
                cursor.close()
                return True

        except Exception as ex:
            print(ex)
            QMessageBox.about(window, "Warning", "Database Error !!!")
            return False

    def remove_file(self, file):
        """
                                        Delete a file from the file storage using file_path
        :param file:
        :return:
        """
        import os
        if file and os.path.exists(file):
            os.remove(file)
            return True
        else:
            return False

    """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
                                TIME SERIES MODULE
    """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    def save_timeseries(self, analyse_type, description, empty_data, end_time, file_type, name, series_data,
                        start_time, source_file, window=QMessageBox()):
        """
                                Create a time-series record in the database
        :param analyse_type:
        :param description:
        :param empty_data:
        :param end_time:
        :param file_type:
        :param name:
        :param series_data:
        :param start_time:
        :param source_file: File path
        :return:
        """
        try:
            from datetime import datetime
            with self.connection.cursor() as cursor:

                timeseries_query = "INSERT INTO fpat_db.fpat_timeseries (created_at, analyse_type, description,"\
                                   " empty_data, end_time, file_type, name, series_data, start_time, source_file)"\
                                   " VALUES({created_at}, '{analyse_type}', '{description}', '{empty_data}',"\
                                   " {end_time}, '{file_type}', '{name}', {series_data}, {start_time}, '{source_file}'"\
                                   ");".format(created_at=get_current_time(),
                                               analyse_type=analyse_type,
                                               description=description,
                                               empty_data=empty_data,
                                               end_time=end_time,
                                               file_type=file_type,
                                               name=name,
                                               series_data=series_data,
                                               start_time=start_time,
                                               source_file=source_file
                                               )

                cursor.execute(timeseries_query)
                timeseries_id = cursor.lastrowid
                self.connection.commit()
                return timeseries_id

        except Exception as ex:
            print(ex)
            QMessageBox.about(window, "Warning", "Database Error !!!")
            return False

    def get_timeserieses(self, window=QMessageBox()):
        """
                        Get the list of the time-series in the database

        :return: timeseries_list, timeseriesId_list
        """
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

        except Exception as ex:
            print(ex)
            QMessageBox.about(window, "Warning", "Database Error !!!")

        return timeseries_list, timeseriesId_list
    
    def get_timeseries_details(self, timeseries_id, window=QMessageBox()):
        """
                        Get all the field values of a time-series using id
        :param timeseries_id:
        :return: dictionary containing all the fields of a time-series
        """
        timeseries_info_dict = {}
        try:
            with self.connection.cursor() as cursor:
                query = "select * from fpat_timeseries where id = '{id}'".format(id=timeseries_id)
                cursor.execute(query)
                timeseries_info_dict.update(cursor.fetchone())
                cursor.close()
        except Exception as ex:
            print(ex)
            QMessageBox.about(window, "Warning", "Database Error !!!")
        return timeseries_info_dict

    def delete_timeseries(self, id, window=QMessageBox()):
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
            if type(ex) == 'IntegrityError':
                QMessageBox.about(window, "IntegrityError",  "This Time series has a child record")
            else:
                if "fpat_models" in str(ex):
                    warning = "Cannot delete or update because this time-series is used in a Model record"
                    QMessageBox.about(window, "Warning", warning)
                elif "fpat_product" in str(ex):
                    warning = "Cannot delete or update because this time-series is bind with the Product record"
                    QMessageBox.about(window, "Warning", warning)
                else:
                    warning = str(ex)
                    QMessageBox.about(window, "Warning", warning)
            return False

    def update_timeseries_productId(self, timeseries_id, product_id, window=QMessageBox()):
        """
                                                BIND AND UNBIND PRODUCT WITH TIME-SERIES
        :param timeseries_id:
        :param product_id:
        :return:
        """
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
            QMessageBox.about(window, "Warning", "Database Error !!!")
            return False

    def update_timeseries(self, product_id, timeseries_id, analyse_type, description, empty_data, end_time, file_type,
                          name, series_data, start_time, source_file, window=QMessageBox()):
        """
                                                    UPDATE TIME-SERIES
        :param product_id:
        :param timeseries_id:
        :param analyse_type:
        :param description:
        :param empty_data:
        :param end_time:
        :param file_type:
        :param name:
        :param series_data:
        :param start_time:
        :param source_file:
        :return:
        """
        try:
            with self.connection.cursor() as cursor:
                query = "UPDATE fpat_db.fpat_timeseries SET analyse_type='{analyse_type}', description='{description}'"\
                        ", empty_data='{empty_data}', end_time={end_time}, file_type='{file_type}', name='{name}', "\
                        "series_data={series_data}, start_time={start_time},"\
                        " source_file='{source_file}' WHERE id={id};".format(id=timeseries_id,
                                                                             product_id=product_id,
                                                                             analyse_type=analyse_type,
                                                                             description=description,
                                                                             empty_data =empty_data,
                                                                             end_time=end_time,
                                                                             file_type=file_type,
                                                                             name=name,
                                                                             series_data=series_data,
                                                                             start_time=start_time,
                                                                             source_file=source_file)
                cursor.execute(query)
                self.connection.commit()
                cursor.close()
                return True
        except Exception as ex:
            print(ex)
            QMessageBox.about(window, "Warning", "Database Error !!!")
            return False

    """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
                                MODEL MODULE
    """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    def get_models(self, evaluate=None, window=QMessageBox()):
        """
                                        GET LIST OF MODELS FROM DATABASE
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
        except Exception:
            QMessageBox.about(window, "Warning", "Database Error !!!")
        return model_list, modelId_list

    def save_model_record(self, name, me1, me10, me11, me12, me13, me14, me15, me16,me2, me3, me4, me5, me6, me7, me8,
                          me9, description, param1, param2, param3, type, time_series_ID, window=QMessageBox()):
        """
                                    Create a new model
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
            QMessageBox.about(window, "Warning", "Database Error !!!")
            return False

    def update_model_record(self, name, me1, me10, me11, me12, me13, me14, me15, me16,me2, me3, me4, me5, me6, me7, me8,
                            me9, description, param1, param2, param3, type, time_series_ID, model_id, window=QMessageBox()):
        """
                                Update a model record in the database
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
                            ' time_series_ID={time_series_ID} WHERE id={model_id};'.format(me1=me1, me10=me10,
                            me11=me11, me12=me12, me13=me13, me14=me14, me15=me15, me16=me16, me2=me2, me3=me3,
                            me4=me4, me5=me5, me6=me6, me7=me7, me8=me8, me9=me9, description=description, name=name,
                            param1=param1, param2=param2, param3=param3, type=type, time_series_ID=time_series_ID,
                                                                                         model_id=model_id)
                cursor.execute(query_str)
                self.connection.commit()
                cursor.close()
            return True
        except Exception as ex:
            print(ex)
            QMessageBox.about(window, "Warning", "Database Error !!!")
            return False

    def get_model_details(self, id, window=QMessageBox()):
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
                query = "select id, name, param1, param2, param3, type, me1, me2, me3, me4, me5, me6, me7, me8, me9,"\
                        "me10, me11, me12, me13, me14, me15, me16, description, time_series_ID from fpat_models"\
                        " where id = '{id}'".format(id=id)
                cursor.execute(query)
                result = cursor.fetchall()
                for model_details in result:
                    for key, value in model_details.items():
                        if key not in ['id', 'created_at', 'time_series_ID'] and value:
                            model_info += str(key).title() + "\t:  " + str(value) + "\n"
                    model_info_dict.update(model_details)
                cursor.close()
        except Exception:
            QMessageBox.about(window, "Warning", "Database Error !!!")
        return model_info, model_info_dict

    def delete_model(self, id, window=QMessageBox()):
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
                return True, "Deleted successfully !!!"
        except Exception as ex:
            QMessageBox.about(window, "Warning", "Database Error !!!")
            return False

    def get_index_analysis(self, index, analyse_type, window=QMessageBox()):
        """
        Get the standard values of sub-indexes for the time-series of given analyse-type
        :param index: int
        :param analyse_type: str
        :return: analysis_dict
        """
        analysis_dict = {}
        try:
            with self.connection.cursor() as cursor:
                query = "select sub_index, standard_value from fpat_analysis where analyse_type='" + analyse_type +\
                        "' AND `index`=" + str(index)
                cursor.execute(query)
                query_result = cursor.fetchall()
                for item in query_result:
                    analysis_dict[item["sub_index"]] = item["standard_value"]
                cursor.close()
        except Exception as ex:
            print(ex)
            QMessageBox.about(window, "Warning", "Database Error !!!")
        return analysis_dict


if __name__ == '__main__':
    conn = DatabaseConnect()
    dict = conn.get_index_analysis(index=1,
                                   analyse_type="B")
    print(dict)
