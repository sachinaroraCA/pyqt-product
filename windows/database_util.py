from PyQt5 import QtSql
from PyQt5.QtWidgets import QMessageBox


class DatabaseConnect:

    def get_users(self):
        user_list = []
        db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName('sports.db')
        if not db.open():
            print("not created")
            return False

        query = QtSql.QSqlQuery()
        query.exec_("select username from user")
        print(query.result())
        while query.next():
            print(query.value(0))
            user_list.append(query.value(0))
        db.close()
        return user_list

    def auth_user(self, un, password):
        db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName('sports.db')
        if not db.open():
            print("not created")
            return False

        query = QtSql.QSqlQuery()
        query.exec_("select username from user where username = '{username}' and password = '{password}'".format(
            username=un,
            password=password))
        if query.next():
            print("logged in")
            db.close()
            # QMessageBox.about(QMessageBox(), "Greetings", "Successfully logged in")
            return True
        else:
            db.close()
            QMessageBox.about(QMessageBox(), "Warning", "Invalid Username or Password !!!")
            return False

    # def get_products(self):
    #     db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
    #     db.setDatabaseName('sports.db')
    #     product_list = []
    #     if not db.open():
    #         print("not created")
    #         return False
    #
    #     query = QtSql.QSqlQuery()
    #     query.exec_("select Name from Product")
    #
    #     while query.next():
    #         print(query.value(0))
    #         product_list.append(query.value(0))
    #     db.close()
    #     return product_list

    def save_product_record(self, name, code, category_a, category_b, info_1='', info_2='', info_3='', info_4='',
                            info_5='', info_6='', info_7=''):
        db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName('sports.db')
        if not db.open():
            print("not created")
            return False

        query = QtSql.QSqlQuery()
        query_str = "insert into Product values('{name}','{code}', '{category_a}', '{category_b}', '{info_1}', " \
                    "'{info_2}', '{info_3}', '{info_4}', '{info_5}', '{info_6}', '{info_7}')".format(name=name,
                                                                                                     code=code,
                                                                                                     category_a=category_a,
                                                                                                     category_b=category_b,
                                                                                                     info_1=info_1,
                                                                                                     info_2=info_2,
                                                                                                     info_3=info_3,
                                                                                                     info_4=info_4,
                                                                                                     info_5=info_5,
                                                                                                     info_6=info_6,
                                                                                                     info_7=info_7
                                                                                                     )
        print("query_str:::::" + query_str)
        query.exec_(query_str)
        db.close()
        return query.isValid()

    def update_product_record(self, name, code, category_a, category_b, info_1='', info_2='', info_3='', info_4='',
                            info_5='', info_6='', info_7=''):
        db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName('sports.db')
        if not db.open():
            print("not created")
            return False

        query = QtSql.QSqlQuery()
        query_str= "UPDATE Product SET Name='{name}', Category_A='{category_a}', Category_B='{category_b}', "\
                   "info_1='{info_1}', info_2='{info_2}', info_3='{info_3}', info_4='{info_4}', info_5='{info_5}', " \
                   "info_6='{info_6}', info_7='{info_7}' WHERE Code='{code}'".format(name=name,
                                                                                     code=code,
                                                                                     category_a=category_a,
                                                                                     category_b=category_b,
                                                                                     info_1=info_1,
                                                                                     info_2=info_2,
                                                                                     info_3=info_3,
                                                                                     info_4=info_4,
                                                                                     info_5=info_5,
                                                                                     info_6=info_6,
                                                                                     info_7=info_7
                                                                                     )
        print("query_str:::::" + query_str)
        query.exec_(query_str)
        db.close()
        return query.isValid()

#     def get_product_details(self, product_name):
#         db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
#         db.setDatabaseName('sports.db')
#         product_string = ""
#
#         if not db.open():
#             print("not created")
#             return False
#
#         query = QtSql.QSqlQuery()
#         query.exec_("select * from Product where Name = '{name}'".format(name=product_name))
#
#         if query.next():
#             size = query.record().count()
#             for index in range(0, size):
#                 # print(query.value(index))
#                 if query.value(index) != "" and query.value(index):
#                     product_string += str(query.value(index)) + "\n"
#             print(product_string)
#
#         db.close()
#
#
# conn = DatabaseConnect()
# conn.get_product_details("Product 5")
#
