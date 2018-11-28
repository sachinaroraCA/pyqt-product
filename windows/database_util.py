from PyQt5 import QtSql
from PyQt5.QtWidgets import QMessageBox
import pymysql


class DatabaseConnect:
    def __init__(self):
        self.connection = pymysql.connect(host='localhost',
                                          db='fpat_db',
                                          user="root",
                                          charset='utf8mb4',
                                          cursorclass=pymysql.cursors.DictCursor)

    def auth_user(self, un, password):
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

    def get_products(self):
        product_list = []
        productId_list = []

        try:
            with self.connection.cursor() as cursor:
                query = "select id,name from fpat_product;"
                cursor.execute(query)
                result = cursor.fetchall()
                for product_details in result:
                    product_list.append(product_details["name"])
                    productId_list.append(product_details['id'])
                cursor.close()
            return product_list, productId_list
        except Exception as ex:
            print(ex)
            QMessageBox.about(QMessageBox(), "Warning", "Database Error !!!")
            return []

    def save_product_record(self, name, code, categorya, categoryb, info1='', info2='', info3='', info4='',info5='',
                            info6='', info7=''):

        try:
            with self.connection.cursor() as cursor:
                query = "insert into fpat_product(name,code, categorya, categoryb, info1,info2, info3, info4,"\
                        " info5, info6, info7) values('{name}','{code}', '{categorya}', '{categoryb}', '{info1}', " \
                    "'{info2}', '{info3}', '{info4}', '{info5}', '{info6}', '{info7}')".format(name=name,
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

    def update_product_record(self, id, name, code, categorya, categoryb, info1="", info2="", info3="", info4="",
                              info5="", info6="", info7=""):

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

    def get_all_questions(self):
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
        ##TODO: Create Evaluation
        ##TODO: Upadte the Evaluation_Id in Product
        #TODO: Create all Evaluation Answers
        #TODO: Add every answer to the evaluation_evaluation_answer

        try:
            with self.connection.cursor() as cursor:
                evalution_query = "INSERT INTO fpat_db.fpat_evalutions ( attachment_one, attachment_two) VALUES"\
                                  "('{attachment_one}', '{attachment_two}');".format(attachment_one=attachment_one,
                                                                                     attachment_two=attachment_two)

                cursor.execute(evalution_query)
                evalution_id = cursor.lastrowid
                self.connection.commit()

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

    def save_answers(self, answer, question, dimension):
        try:
            with self.connection.cursor() as cursor:
                answer_query = "INSERT INTO fpat_evaluation_answers(answer, dimension, question)"\
                               " VALUES( {answer}, {dimension}, '{question}');".format(answer=answer,
                                                                                       dimension=dimension,
                                                                                       question=question)
                # """INSERT INTO fpat_evaluation_answers ( answer, dimension, question) VALUES(1 , 0, '');"""

                cursor.execute(answer_query)
                self.connection.commit()
                answer_id = cursor.lastrowid
                cursor.close()

                return answer_id
        except Exception as ex:
            print(ex)
            QMessageBox.about(QMessageBox(), "Warning", "Database Error !!!")
            return False

    def map_evaluation_answer(self, evaluation_id, answer_id):
        try:
            with self.connection.cursor() as cursor:
                mapping_query = "INSERT INTO fpat_db.fpat_evalutions_evalution_answers (fpat_evalutions_ID,"\
                               " evalution_answers_ID) VALUES({fpat_evalutions_ID}, {evalution_answers_ID});"\
                                "".format(fpat_evalutions_ID=evaluation_id,
                                          evalution_answers_ID=answer_id)

                cursor.execute(mapping_query)
                self.connection.commit()
                cursor.close()
                return True
        except Exception as ex:
            print(ex)
            QMessageBox.about(QMessageBox(), "Warning", "Database Error !!!")
            return False

    def delete_evaluation(self, product_id):
        try:
            with self.connection.cursor() as cursor:
                # Get Evaluation records of a product
                product_query = "select evalutions_ID from fpat_product where id={id};".format(id=product_id)
                cursor.execute(product_query)
                product_dict = cursor.fetchone()
                evaluation_id = product_dict["evalutions_ID"]

                # Get all answers_ids in selected evaluation
                answer_query = "SELECT evalution_answers_ID FROM fpat_db.fpat_evalutions_evalution_answers"\
                               " WHERE fpat_evalutions_ID={id};".format(id=evaluation_id)

                cursor.execute(answer_query)
                answer_list = cursor.fetchall()

                # Delete answer and evaluation mapping
                answer_map_delete_query = "DELETE FROM fpat_db.fpat_evalutions_evalution_answers"\
                                          " WHERE fpat_evalutions_ID={id};".format(id=evaluation_id)
                cursor.execute(answer_map_delete_query)

                # Delete all selected answers
                answer_delete_query = "DELETE FROM fpat_evaluation_answers "\
                                      "WHERE id in ({id_list})".format(id_list=",".join([str(answer["evalution_answers_ID"]) for answer in answer_list]))
                cursor.execute(answer_delete_query)

                # Update Product record to remove evaluation_id
                product_update_query = "UPDATE fpat_product SET evalutions_ID={evalutions_ID}, evaluated={evaluated}"\
                                       " WHERE id={id};".format(evaluated=0,
                                                                evalutions_ID="NULL",
                                                                id=product_id)
                cursor.execute(product_update_query)
                self.connection.commit()

                # Delete evaluation record
                evaluation_delete_query = "DELETE FROM fpat_db.fpat_evalutions WHERE id={id}".format(id=evaluation_id)
                cursor.execute(evaluation_delete_query)

                cursor.execute(product_update_query)
                self.connection.commit()
                cursor.close()
                return True

        except Exception as ex:
            print(ex)
            QMessageBox.about(QMessageBox(), "Warning", "Database Error !!!")
            return False

    def test_def(self):
        with self.connection.cursor() as cursor:
            evalution_query = "INSERT INTO fpat_db.fpat_evalutions ( attachment_one, attachment_two) VALUES" \
                              "('{attachment_one}', '{attachment_two}');".format(attachment_one="",
                                                                                 attachment_two="")

            cursor.execute(evalution_query)
            evalution_id = cursor.lastrowid
            self.connection.commit()
            print(evalution_id)


if __name__ == '__main__':
    conn = DatabaseConnect()
    conn.delete_evaluation(product_id=3)
    # conn.get_product_details("exercitation ullamco lab")
    # conn.get_all_questions()
    # conn.update_product_record(id=3, name="Aman", code="007",categorya="A", categoryb="B")
