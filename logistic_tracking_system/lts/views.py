import os
import time
# import wmi,json
# import pythoncom


from django.shortcuts import render
from django.http import HttpResponse
from django.urls.conf import re_path
from django.views import View
import json
import logging
import datetime
from utils.import_common import test11
from utils.test import opt
# from utils import *


from django.contrib.auth.hashers import make_password, check_password

from common.db import DB
from page.Page import Page
from pathlib import Path
logger = logging.getLogger(__name__)
# logger.setLevel(logging.INFO)

# Create your views here.


class test2222(View):
    def get(self, request):
        try:
            db = DB()
            conn = db.get_connection("db_common")
            sql = """
                 show tables like "product_%" 
                """
            drs = db.execute_sql(conn, sql)

            print(drs)

            for dr in drs:
                print(dr)

            data = {"code": 0, "message": "创建人员成功"}

            data = json.dumps(data)

            return HttpResponse(data)

        except Exception as e:
            data = {"code": 1, "message": "创建人员失败%s" % e}
            logger.error("创建人员失败", e)
            data = json.dumps(data)
            print(e)
            return HttpResponse(data)


class LogisticLogin(View):
    """
    登录系统，  校验通过就进入系统
    """
    def get(self, request):
        try:
            print("---->>>ksishi")
            # pwd = "admin123"
            # auth_user = "admin"
            db = DB()
            conn = db.get_connection_nodb()
            db_list = []
            sql = """
            show databases
            """
            drs = db.execute_sql(conn, sql)
            for dr in drs:
                db_list.append(dr[0])

            auth_user = request.GET.get("user")
            pwd = request.GET.get("password")
            product_id = request.GET.get("product_id")
            work_id = request.GET.get("work_id")
            # work_type = request.GET.get("work_type")
            print("----->", work_id)
            request.session.set_expiry(0)
            if auth_user == "admin":
                if product_id:
                    if product_id in db_list:
                        conn = db.get_connection(product_id)
                        print("-------------=============>", product_id)

                        sql = """
                                    select * from person_manage where user_name = '{0}' and  user_password = '{1}'
                              """
                        sql_main = sql.format(auth_user, pwd)
                        drs = db.execute_sql(db.get_connection("db_common"), sql_main)
                        if drs:
                            sql_type = """
                                    select work_type from work_station where work_id = '{0}'
                                    """
                            sql_type = sql_type.format(work_id)
                            print("================================>", sql_type)
                            drs_type = db.execute_sql(conn, sql_type)
                            print("----------------------------------------->>>>>>>>>>>>>",drs_type)

                            if drs_type:
                                work_type = drs_type[0][0]
                            else:
                                work_type = "没有工站类型"
                            # project_id = auth_user[auth_user.index('@') + 1:].lower()
                            current_person_id = drs[0][0]
                            request.session['session_projectId'] = product_id
                            request.session['session_currentId'] = current_person_id
                            request.session['session_workId'] = work_id
                            request.session['session_workType'] = work_type

                            print("登录成功")
                            print("----->>>>>>>>>", request.session['session_projectId'])
                            print("----->>>>", request.session)
                            data = {"code": 0, "message": "success"}
                            data = json.dumps(data)
                            return HttpResponse(data)
                    else:
                        data = {"code": 1, "message": "无此项目"}
                        data = json.dumps(data)
                        return HttpResponse(data)
                    # request.session['session_projectId'] = product_id
                    #
                    # print(request.session.get("session_projectId"))
                    # print("start_person--------admin")
                else:
                    request.session['session_projectId'] = "db_common"

                    print("end---", request.session.get("session_projectId"))
                conn = db.get_connection("db_common")
                sql_type = """
                            select work_type from work_station where work_id = '{0}'
                            """
                sql_type = sql_type.format(work_id)
                print(sql_type)
                drs_type = db.execute_sql(conn, sql_type)
                print(drs_type)

                if drs_type:
                    work_type = drs_type[0][0]
                else:
                    work_type = "没有加工站"

                sql = """
                      select * from person_manage where user_name = '{0}' and  user_password = '{1}'
                      """
                sql_main = sql.format(auth_user, pwd)
                drs = db.execute_sql(conn, sql_main)
                current_person_id = drs[0][0]
                request.session['session_currentId'] = current_person_id
                request.session['session_workId'] = work_id
                request.session['session_workType'] = work_type

                data = {"code": 0, "message": "success"}
                data = json.dumps(data)
                return HttpResponse(data)

            else:
                if product_id in db_list:
                    conn = db.get_connection(product_id)
                    request.session.set_expiry(0)
                    sql_type = """
                                select work_type from work_station where work_id = '{0}'
                                """
                    sql_type = sql_type.format(work_id)
                    print(sql_type)
                    drs_type = db.execute_sql(conn, sql_type)
                    print(drs_type)

                    if drs_type:
                        work_type = drs_type[0][0]
                    else:
                        work_type = "没有加工站"
                    sql = """
                                select * from person where user_name = '{0}' and  user_password = '{1}'
                          """
                    sql_main = sql.format(auth_user, pwd)
                    drs = db.execute_sql(conn, sql_main)

                    if drs:
                        work_ids = drs[0][4]
                        work_ids_list = str(work_ids).split(",")
                        # print("===>>>", work_ids_list)
                        # sql = """
                        # SELECT work_code FROM work_station where work_id = '{0}';
                        # """
                        # sql = sql.format(work_id)
                        # conn_in = db.get_connection(product_id)
                        # dfs = db.execute_sql(conn_in, sql)
                        # work_id_one = dfs[0][0]
                        print("-->>>", work_id)
                        if work_id in work_ids_list:
                            current_person_id = drs[0][0]
                            request.session['session_projectId'] = product_id
                            request.session['session_currentId'] = current_person_id
                            request.session['session_workId'] = work_id
                            request.session['session_workType'] = work_type

                            print("登录成功")
                            print("----->>>>>>>>>", request.session['session_projectId'])
                            print("----->>>>>>>>>", request.session['session_workType'])
                            # print("----->>>>>>>>>", request.session['current_person_id'])
                            print("----->>>>", request.session)

                            data = {"code": 0, "message": "登录成功"}
                            logger.info("登录成功")
                        else:
                            data = {"code": 1, "message": "用户没有进入此工站的权限"}
                            logging.error("用户没有进入此工站的权限")
                    else:
                        print("用户名或者密码错误")
                        data = {"code": 1, "message": "用户名或者密码错误"}
                        logger.error(auth_user, "用户名或者密码错误")
                    data = json.dumps(data)

                    return HttpResponse(data)
                else:
                    data = {"code": 1, "message": "没有此项目"}
                    data = json.dumps(data)

                    return HttpResponse(data)
        except Exception as e:

            data = {"code": 1, "message": "登录失败"}
            data = json.dumps(data)
            logger.error("用户登录失败----", e)
            print(e)
            return HttpResponse(data)


class ManageLogisticLogin(View):
    def get(self, request):
        try:
            # request.session.set_expiry(1800 ** 200)
            db = DB()
            auth_user = request.GET.get("user")
            pwd = request.GET.get("password")
            product_id = request.GET.get("product_id")

            print(auth_user, pwd, product_id)
            # auth_user = "test"
            # pwd = "test"
            # product_id = "winter"

            if auth_user == "admin":
                if product_id:
                    request.session['session_projectId'] = product_id
                else:
                    request.session['session_projectId'] = "db_common"

                conn = db.get_connection("db_common")
                sql = """
                      select * from person_manage where user_name = '{0}' and  user_password = '{1}'
                      """
                sql_main = sql.format(auth_user, pwd)
                drs = db.execute_sql(conn, sql_main)
                current_person_id = drs[0][0]
                if drs:
                    request.session.set_expiry(0)
                    # request.session['session_projectId'] = "db_common"
                    request.session['session_currentId'] = current_person_id

                    data = {"code": 0, "message": "登录成功"}
                    data = json.dumps(data)
                    logger.info("登录成功")

                    return HttpResponse(data)
                else:
                    data = {"code": 1, "message": "用户名或者密码不正确"}
                    data = json.dumps(data)

                    return HttpResponse(data)
            else:
                if product_id:
                    product_id_list = []

                    db = DB()
                    conn = db.get_connection("db_common")
                    sql_product = """
                                    select product_id from productlist
                                    """
                    dfs = db.execute_sql(conn, sql_product)
                    for df in dfs:
                        product_id_list.append(df[0])
                    if product_id in product_id_list:

                        conn = db.get_connection(product_id)
                        sql = """
                                select * from person where user_name = '{0}' and  user_password = '{1}'
                              """
                        sql_main = sql.format(auth_user, pwd)
                        drs = db.execute_sql(conn, sql_main)
                        current_person_id = drs[0][0]
                        if drs:
                            request.session.set_expiry(0)
                            request.session['session_projectId'] = product_id
                            request.session['session_currentId'] = current_person_id
                            data = {"code": 0, "message": "登录成功"}
                            logger.info("登录成功")
                            data = json.dumps(data)

                            return HttpResponse(data)
                        else:
                            data = {"code": 1, "message": "用户名或者密码错误"}
                            data = json.dumps(data)

                            return HttpResponse(data)

                else:
                    data = {"code": 1, "message": "项目名称不能为空或者项目名称不在项目内"}
                    data = json.dumps(data)

                    return HttpResponse(data)
            pwd = request.GET.get("password")
            product_id = request.GET.get("product_id")
            conn = db.get_connection("db_common")
            sql = """
                select * from person_manage where user_name = '{0}' and  user_password = '{1}'
                """
            sql_main = sql.format(auth_user, pwd)
            drs = db.execute_sql(conn, sql_main)
            if drs:
                if product_id:
                    request.session.set_expiry(0)
                    request.session['session_projectId'] = product_id
                    data = {"code": 0, "message": "登录成功"}
                    logger.info("登录成功")
                else:
                    data = {"code": 0, "message": "登录成功"}
                    logger.info("登录成功")
            else:
                print("用户名或者密码错误")
                data = {"code": 1, "message": "用户名或者密码错误"}
                logger.error(auth_user, "用户名或者密码错误")
            data = json.dumps(data)

            return HttpResponse(data)
        except Exception as e:
            print(e)
            data = {"code": 1, "message": "用户名或者密码错误"}
            data = json.dumps(data)

            return HttpResponse(data)


class ModifyPassword(View):
    def get(self, request):
        try:
            db = DB()
            product_id = request.session.get("session_projectId")
            conn = db.get_connection(product_id)
            current_person_id = request.session['session_currentId']
            old_password = request.GET.get("old_password")
            new_password = request.GET.get("new_password")
            sql = """
            select user_password from person where user_code = '{0}'
            """
            sql = sql.format(current_person_id)
            drs = db.execute_sql(conn, sql)

            if old_password == drs[0][0]:
                sql_update = """
                     update person set 
                     user_password='{0}'
                     where user_code = '{1}'    
                """
                sql_update = sql_update.format(new_password, current_person_id)
                db.execute_sql(conn, sql_update)
                data = {"code": 0, "message": "操作成功"}
                data = json.dumps(data)
                return HttpResponse(data)
            else:
                data = {"code": 1, "message": "输入的旧密码有误"}
                data = json.dumps(data)
                return HttpResponse(data)

        except Exception as e:
            print(e)
            data = {"code": 1, "message": "操作失败"}
            data = json.dumps(data)
            return HttpResponse(data)


class ShowDatabase(View):
    def get(self, request):
        try:
            data_list = []
            db = DB()
            conn = db.get_connection("db_common")
            sql = """
            show tables
            """
            drs = db.execute_sql(conn, sql)
            for dr in drs:
                data_list.append(dr[0])
            data = {"code": 0, "message": "操作成功", "data": data_list}
            data = json.dumps(data)
            logger.info("查询数据库成功", data)
            return HttpResponse(data)

        except Exception as e:
            data = {"code": 1, "message": "操作失败", "data": ""}
            data = json.dumps(data)
            print(e)
            logger.error("查询数据库失败", e)
            return HttpResponse(data)


class NewDatabase(View):
    """
    新建数据库表 和新建数据库接口
    """
    def get(self, request):
        try:
            database_list = []
            db_base = "db_common"
            # db_base = request.GET.get("")
            db = DB()
            conn = db.get_connection_mysql()
            sql = """
            show databases
            """
            drs = db.execute_sql(conn, sql)

            for dr in drs:
                database_list.append(dr[0])
            if db_base in database_list:
                data = {"code": 1, "message": "数据库已经存在"}
                logger.info("数据库已经存在")
            else:
                sql = """
                CREATE DATABASE {0} DEFAULT CHARACTER SET utf8
                """
                sql_main = sql.format(db_base)
                drs = db.execute_sql(conn, sql_main)
                data = {"code": 0, "message": "数据库已经建好"}
                logger.info("数据库已经建好")

            # data = {"code": 1, "message": "操作成功"}
            data = json.dumps(data)
            return HttpResponse(data)

        except Exception as e:
            print(e)
            data = {"code": 1, "message": "新建数据库失败"}
            logger.error("新建数据库失败")
            data = json.dumps(data)
            return HttpResponse(data)


class PersonDeal(View):

    def get(self, request):

        try:
            product_id = request.session.get("session_projectId")
            user_id = request.GET.get("user_id")
            user_name = request.GET.get("user_name")
            status = request.GET.get("status")
            page = int(request.GET.get("page"))
            page_size = int(request.GET.get("page_size"))
            # user_id = "001"
            # user_name = "admin"
            # status = ""
            # page = 1
            # page_size = 10

            if len(user_id) == 0 and len(user_name) == 0 and len(status) == 0:
                data_add_int = {}
                data = []
                data_list = []
                db = DB()
                conn = db.get_connection(product_id)
                sql = """
                select * from person
                """
                drs = db.execute_sql(conn, sql)

                for dr in drs:
                    dict_data = {}

                    dict_data["user_code"] = dr[0]
                    dict_data["user_id"] = dr[1]
                    dict_data["user_name"] = dr[2]
                    dict_data["user_password"] = dr[3]
                    dict_data["user_authority"] = dr[4]
                    dict_data["status"] = dr[5]
                    data_list.append(dict_data)
                    # data_list.append(dict_data)

                page_result = Page(page, page_size, data_list)
                data = page_result.get_str_json()

                sql_num = """
                select count(*) from person
                """
                dfs = db.execute_sql(conn, sql_num)
                sql_num_int = dfs[0][0]

                data_add_int["data"] = data
                data_add_int["total"] = sql_num_int

                # data_add_int["code"] = 0
                # data_add_int["message"] = "调取成功"

                result = {"code": 0, "message": "调取成功", "data": data_add_int}

                result = json.dumps(result)

                return HttpResponse(result)

            elif len(user_id) != 0 and len(user_name) != 0 and len(status) != 0:
                data_add_int = {}
                data = []
                db = DB()
                conn = db.get_connection(product_id)
                sql = """
                     select * from person where user_id = '{0}' and user_name = '{1}' and status = '{2}'
                     """
                sql_main = sql.format(user_id, user_name, status)
                drs = db.execute_sql(conn, sql_main)

                for dr in drs:
                    dict_data = {}
                    dict_data["user_code"] = dr[0]
                    dict_data["user_id"] = dr[1]
                    dict_data["user_name"] = dr[2]
                    dict_data["user_password"] = dr[3]
                    dict_data["user_authority"] = dr[4]
                    dict_data["status"] = dr[5]
                    data.append(dict_data)
                sql_num = """               
                select count(*) from person where user_id = '{0}' and user_name = '{1}' and status = '{2}'
                """
                sql_format = sql_num.format(user_id, user_name, status)
                dfs = db.execute_sql(conn, sql_format)
                df = dfs[0][0]

                data_add_int["data"] = data
                data_add_int["total"] = df

                result = {"code": 0, "message": "调取成功", "data": data_add_int}
                result = json.dumps(result)

                return HttpResponse(result)

            elif len(user_id) == 0 and len(user_name) != 0 and len(status) != 0:
                data_add_int = {}
                data = []
                db = DB()
                conn = db.get_connection(product_id)
                sql = """
                     select * from person where user_name = '{0}' and status = '{1}'
                     """
                sql_main = sql.format(user_name, status)
                drs = db.execute_sql(conn, sql_main)
                for dr in drs:
                    dict_data = {}
                    dict_data["user_code"] = dr[0]
                    dict_data["user_id"] = dr[1]
                    dict_data["user_name"] = dr[2]
                    dict_data["user_password"] = dr[3]
                    dict_data["user_authority"] = dr[4]
                    dict_data["status"] = dr[5]
                    data.append(dict_data)
                sql_num = """               
                select count(*) from person where user_name = '{0}' and status = '{1}'
                """
                sql_format = sql_num.format(user_name, status)
                dfs = db.execute_sql(conn, sql_format)
                df = dfs[0][0]

                data_add_int["data"] = data
                data_add_int["total"] = df

                result = {"code": 0, "message": "调取成功", "data": data_add_int}
                result = json.dumps(result)

                return HttpResponse(result)

            elif len(user_id) != 0 and len(user_name) != 0 and len(status) == 0:
                data_add_int = {}
                data = []
                db = DB()
                conn = db.get_connection(product_id)
                sql = """
                     select * from person where user_name = '{0}' and user_id = '{1}'
                     """
                sql_main = sql.format(user_name, user_id)
                drs = db.execute_sql(conn, sql_main)
                for dr in drs:
                    dict_data = {}
                    dict_data["user_code"] = dr[0]
                    dict_data["user_id"] = dr[1]
                    dict_data["user_name"] = dr[2]
                    dict_data["user_password"] = dr[3]
                    dict_data["user_authority"] = dr[4]
                    dict_data["status"] = dr[5]
                    data.append(dict_data)
                sql_num = """               
                select count(*) from person where user_name = '{0}' and user_id = '{1}'
                """
                sql_format = sql_num.format(user_name, user_id)
                dfs = db.execute_sql(conn, sql_format)
                df = dfs[0][0]

                data_add_int["data"] = data
                data_add_int["total"] = df

                result = {"code": 0, "message": "调取成功", "data": data_add_int}
                result = json.dumps(result)

                return HttpResponse(result)

            elif len(user_id) != 0 and len(user_name) == 0 and len(status) != 0:
                data_add_int = {}
                data = []
                db = DB()
                conn = db.get_connection(product_id)
                sql = """
                     select * from person where user_id = '{0}' and status = '{1}'
                     """
                sql_main = sql.format(user_id, status)
                drs = db.execute_sql(conn, sql_main)
                for dr in drs:
                    dict_data = {}
                    dict_data["user_code"] = dr[0]
                    dict_data["user_id"] = dr[1]
                    dict_data["user_name"] = dr[2]
                    dict_data["user_password"] = dr[3]
                    dict_data["user_authority"] = dr[4]
                    dict_data["status"] = dr[5]
                    data.append(dict_data)
                sql_num = """               
                select count(*) from person where user_id = '{0}' and status = '{1}'
                """
                sql_format = sql_num.format(user_id, status)
                dfs = db.execute_sql(conn, sql_format)
                df = dfs[0][0]

                data_add_int["data"] = data
                data_add_int["total"] = df

                result = {"code": 0, "message": "调取成功", "data": data_add_int}
                result = json.dumps(result)

                return HttpResponse(result)

            elif len(user_id) == 0 and len(user_name) == 0 and len(status) != 0:
                data_add_int = {}
                data = []
                db = DB()
                conn = db.get_connection(product_id)
                sql = """
                     select * from person where status = '{0}'
                     """
                sql_main = sql.format(status)
                drs = db.execute_sql(conn, sql_main)
                for dr in drs:
                    dict_data = {}
                    dict_data["user_code"] = dr[0]
                    dict_data["user_id"] = dr[1]
                    dict_data["user_name"] = dr[2]
                    dict_data["user_password"] = dr[3]
                    dict_data["user_authority"] = dr[4]
                    dict_data["status"] = dr[5]
                    data.append(dict_data)

                sql_num = """               
                select count(*) from person where status = '{0}'
                """
                sql_format = sql_num.format(status)
                dfs = db.execute_sql(conn, sql_format)
                df = dfs[0][0]

                data_add_int["data"] = data
                data_add_int["total"] = df

                result = {"code": 0, "message": "调取成功", "data": data_add_int}
                result = json.dumps(result)

                return HttpResponse(result)

            elif len(user_id) == 0 and len(user_name) != 0 and len(status) == 0:
                data_add_int = {}
                data = []
                db = DB()
                conn = db.get_connection(product_id)
                sql = """
                     select * from person where user_name = '{0}'
                     """
                sql_main = sql.format(user_name)
                drs = db.execute_sql(conn, sql_main)
                for dr in drs:
                    dict_data = {}
                    dict_data["user_code"] = dr[0]
                    dict_data["user_id"] = dr[1]
                    dict_data["user_name"] = dr[2]
                    dict_data["user_password"] = dr[3]
                    dict_data["user_authority"] = dr[4]
                    dict_data["status"] = dr[5]
                    data.append(dict_data)
                sql_num = """               
                select count(*) from person where user_name = '{0}'
                """
                sql_format = sql_num.format(user_name)
                dfs = db.execute_sql(conn, sql_format)
                df = dfs[0][0]

                data_add_int["data"] = data
                data_add_int["total"] = df

                result = {"code": 0, "message": "调取成功", "data": data_add_int}
                result = json.dumps(result)

                return HttpResponse(result)

            elif len(user_id) != 0 and len(user_name) == 0 and len(status) == 0:
                data_add_int = {}
                data = []
                db = DB()
                conn = db.get_connection(product_id)
                sql = """
                     select * from person where user_id = '{0}'
                     """
                sql_main = sql.format(user_id)
                drs = db.execute_sql(conn, sql_main)
                for dr in drs:
                    dict_data = {}
                    dict_data["user_code"] = dr[0]
                    dict_data["user_id"] = dr[1]
                    dict_data["user_name"] = dr[2]
                    dict_data["user_password"] = dr[3]
                    dict_data["user_authority"] = dr[4]
                    dict_data["status"] = dr[5]
                    data.append(dict_data)
                sql_num = """               
                select count(*) from person where user_id = '{0}'
                """
                sql_format = sql_num.format(user_id)
                dfs = db.execute_sql(conn, sql_format)
                df = dfs[0][0]

                data_add_int["data"] = data
                data_add_int["total"] = df

                result = {"code": 0, "message": "调取成功", "data": data_add_int}
                result = json.dumps(result)

                return HttpResponse(result)

        except Exception as e:
            logger.error("调取person数据库有错误", e)
            result = {"code": 1, "message": "调取失败", "data": ""}
            result = json.dumps(result)
            print(e)
            return HttpResponse(result)

    def post(self, request):
        try:
            product_id = request.session.get("session_projectId")
            db = DB()
            conn = db.get_connection(product_id)
            sql = """
                 select max(order_number) from person
                """
            id_num = db.execute_sql(conn, sql)

            if id_num[0][0] == None:
                id_num = 1
            else:
                id_num = id_num[0][0] + 1
            user_code = str("Im_User_" + str(id_num))

            json_data = request.body
            str_data = json.loads(json_data)

            user_id = str_data.get("user_id")
            user_name = str_data.get("user_name")
            user_password = str_data.get("user_password")
            user_authority = str_data.get("user_authority")
            status = str_data.get("status")

            print("==>", user_authority)

            # user_id = "0206"
            # user_name = "keny"
            # user_password = "imotion"
            # user_authority = "001,002"
            # status = "在职"

            sql_insert = """
                insert into person(user_code, user_id, user_name, user_password, user_authority, status, order_number)
                values('{0}', '{1}', '{2}', '{3}', '{4}', '{5}', '{6}')
                """

            sql_insert_format = sql_insert.format(user_code, user_id, user_name,
                                                  user_password, user_authority, status, id_num)

            drs = db.execute_sql(conn, sql_insert_format)
            data = {"code": 0, "message": "创建人员成功"}

            data = json.dumps(data)

            return HttpResponse(data)

        except Exception as e:
            data = {"code": 1, "message": "创建人员失败%s" % e}
            logger.error("创建人员失败", e)
            data = json.dumps(data)
            print(e)
            return HttpResponse(data)


class PutPerson(View):

    def get(self, request):
        try:
            product_id = request.session.get("session_projectId")
            db = DB()
            conn = db.get_connection(product_id)

            user_code = request.GET.get("user_code")
            user_id = request.GET.get("user_id")
            user_name = request.GET.get("user_name")
            user_password = request.GET.get("user_password")
            user_authority = request.GET.get("user_authority")
            status = request.GET.get("status")

            print("===>", user_authority)
            sql = """
                      update person set user_id='{0}',
                      user_name='{1}',user_password='{2}',user_authority='{3}',status='{4}' where user_code = '{5}'
                      """
            sql_format = sql.format(user_id, user_name, user_password, user_authority, status, user_code)
            db.execute_sql(conn, sql_format)

            data = {"code": 0, "message": "修改人员成功"}

            data = json.dumps(data)

            return HttpResponse(data)

        except Exception as e:
            print(e)
            data = {"code": 1, "message": "修改人员失败,---%s" % e}
            data = json.dumps(data)
            return HttpResponse(data)


class DeletePerson(View):

    def get(self, request):
        try:
            product_id = request.session.get("session_projectId")
            db = DB()
            conn = db.get_connection(product_id)
            user_code = request.GET.get("user_code")
            # user_code = "Im_User_3"
            sql = """
            delete FROM person where user_code = '{0}'       
            """
            sql_format = sql.format(user_code)
            db.execute_sql(conn, sql_format)

            sql_check = """
             SELECT * FROM person where user_code = "{0}"              
            """
            sql_check_format = sql_check.format(user_code)
            drs = db.execute_sql(conn, sql_check_format)
            if len(drs) == 0:
                data = {"code": 0, "message": "删除成功"}
                data = json.dumps(data)
                return HttpResponse(data)
            else:
                data = {"code": 1, "message": "删除失败"}
                data = json.dumps(data)

                return HttpResponse(data)

        except Exception as e:
            data = {"code":1, "message": "删除失败"}
            data = json.dumps(data)
            print(e)
            return HttpResponse(data)


class PersonTable(View):
    """
    新增个人详情表  在公共库里面加一张表格 加人员
    """
    def get(self, request):
        try:
            table_list = []
            db = DB()
            conn = db.get_connection("db_common")
            sql = """
            create table person(user_code varchar(64) primary key not null,
            user_id varchar(64), user_name varchar(32),
            user_password varchar(64), user_authority varchar(255), status varchar(10), order_number int);
            """
            dr = db.execute_sql(conn, sql)
            sql_main = """
            show tables
            """
            drs = db.execute_sql(conn, sql_main)
            for pe in drs:
                table_list.append(pe[0])
            if "person" in table_list:
                data = {"code": 0, "message": "操作成功"}
            else:
                data = {"code": 1, "message": "操作失败"}
            data = json.dumps(data)
            return HttpResponse(data)

        except Exception as e:
            print(e)


class CreatePersonMatter(View):

    def get(self, request):
        try:
            table_list = []
            db = DB()
            conn = db.get_connection("db_common")
            sql = """
            create table Person_Matter(matter_code varchar(64) primary key not null,
            matter_id varchar(64),
            matter_name varchar(64), matter_category varchar(64), rule varchar(64),
            matter_count int, product_time datetime, status varchar(128), order_number int);
            """
            dr = db.execute_sql(conn, sql)
            sql_main = """
            show tables
            """
            drs = db.execute_sql(conn, sql_main)
            for pe in drs:
                table_list.append(pe[0])
            if "person" in table_list:
                data = {"code": 0, "message": "操作成功"}
                logger.info("创建物料详情结构表成功！")
            else:
                data = {"code": 1, "message": "操作失败"}
                logger.info("创建物料详情结构表失败！")
            data = json.dumps(data)
            return HttpResponse(data)

        except Exception as e:
            data = {"code": 0, "message": "操作失败"}
            data = json.dumps(data)
            print(e)
            logger.error("----创建物料详情结构表失败", e)
            return HttpResponse(data)


class PersonMatter(View):

    def get(self, request):
        try:
            product_id = request.session.get("session_projectId")
            data_list = []
            data_add_int = {}
            matter_id = request.GET.get("matter_id")
            matter_name = request.GET.get("matter_name")
            matter_category = request.GET.get("matter_category")
            # status = request.GET.get("status")

            page = int(request.GET.get("page"))
            page_size = int(request.GET.get("page_size"))
            #
            # matter_id = ""
            # matter_name = ""
            # matter_category = ""
            # status = "已使用"
            #
            # page = 1
            # page_size = 10

            db = DB()
            conn = db.get_connection(product_id)

            if matter_id:
                matter_id_sql = " and matter_id =" + "'" + matter_id + "'"
            else:
                matter_id_sql = ""
            if matter_name:
                matter_name_sql = " and matter_name = " + "'" + matter_name + "'"
            else:
                matter_name_sql = ""
            if matter_category:
                matter_category_sql = " and matter_category = " + "'" + matter_category+"'"
            else:
                matter_category_sql = ""

            sql = """
             select pm.matter_code, ml.matter_name, ml.rule, ml.matter_category, pm.matter_count,
              pm.product_time from person_matter as pm left join matter_list as ml on pm.matter_code = ml.bom_matter_code
              where 2 > 1 {0} {1} {2}
            """

            sql_main = sql.format(matter_id_sql, matter_name_sql, matter_category_sql)

            drs = db.execute_sql(conn, sql_main)
            for dr in drs:
                dict_data = {}
                dict_data["matter_code"] = dr[0]
                dict_data["matter_name"] = dr[1]
                dict_data["rule"] = dr[2]
                dict_data["matter_category"] = dr[3]
                dict_data["matter_count"] = dr[4]
                s = dr[5]
                if s:
                    s1 = s.strftime("%Y-%m-%d %H:%M:%S ")
                else:
                    s1 = ""
                dict_data["product_time"] = s1
                data_list.append(dict_data)

            page_result = Page(page, page_size, data_list)
            data = page_result.get_str_json()
            sql_num = """
            select count(*) from person_matter where 2 > 1 {0} {1} {2}
            """
            sql_num_format = sql_num.format(matter_id_sql, matter_name_sql, matter_category_sql)
            dfs = db.execute_sql(conn, sql_num_format)
            sql_num_int = dfs[0][0]

            data_add_int["data"] = data
            data_add_int["total"] = sql_num_int

            result = {"code": 0, "message": "调取成功", "data": data_add_int}
            result = json.dumps(result)
            return HttpResponse(result)

        except Exception as e:
            logger.error("调取personmatter数据库有错误", e)
            result = {"code": 1, "message": "调取失败", "data": ""}
            result = json.dumps(result)
            print(e)
            return HttpResponse(result)

    def post(self, request):
        """
        物料清单表
        :param request:
        :return:
        """

        try:
            db = DB()

            product_id = request.session.get("session_projectId")
            conn = db.get_connection(product_id)
            sql = """
             SELECT max(order_number) FROM person_matter;
            """
            matter_type = db.execute_sql(conn, sql)
            if matter_type[0][0] == None:
                id_num = 1
            else:
                id_num = matter_type[0][0] + 1
            json_data = request.body
            str_data = json.loads(json_data)

            matter_code = str_data.get("matter_code")

            matter_count = str_data.get("matter_count")
            product_time = str_data.get("product_time")
            # status = str_data.get("status")

            # matter_id = "2"
            # matter_name = "3434"
            # matter_category = "B类"
            # rule = "1"
            # matter_count = 5
            # product_time = "2021-07-06"
            # status = "正常"

            order_number = id_num

            # if len(matter_id.split(",")) == 1:

            sql_insert = """
                       insert into Person_Matter(matter_code, matter_count, product_time, order_number)
                       values('{0}', '{1}', '{2}', '{3}')
                       """
            sql_insert_format = sql_insert.format(matter_code, matter_count, product_time, order_number)
            drs = db.execute_sql(conn, sql_insert_format)

            data = {"code": 0, "message": "创建物料详情表成功"}
            logger.info("创建物料详情表成功")
            # else:
            #     data = {"code": 1, "message": "创建物料详情表失败"}
            #     logger.error("创建物料详情表失败")
            data = json.dumps(data)

            return HttpResponse(data)

        except Exception as e:

            data = {"code": 1, "message": "创建物料详情表失败%s" % e}
            logger.error("创建物料详情表失败", e)
            data = json.dumps(data)
            print(e)

            return HttpResponse(data)


class PutPersonMatter(View):

    def get(self, request):
        try:
            product_id = request.session.get("session_projectId")

            db = DB()
            conn = db.get_connection(product_id)
            matter_code = request.GET.get("matter_code")
            # matter_id = request.GET.get("matter_id")
            # matter_name = request.GET.get("matter_name")
            # matter_category = request.GET.get("matter_category")
            # rule = request.GET.get("rule")
            matter_count = request.GET.get("matter_count")
            product_time = request.GET.get("product_time")

            # status = request.GET.get("status")

            # matter_code = 'Im_Matter_1'
            # matter_id = 'A00011'
            # matter_name = '钢笔'
            # matter_category = '11'
            # rule = '10,23,22'
            # matter_count = 1
            # product_time = '2021-07-06'
            # status = '不启用'
            sql = """
             update person_matter set 
             matter_count ='{0}', product_time='{1}'
             where matter_code = '{2}'          
            """
            sql_main = sql.format(matter_count, product_time, matter_code)
            drs = db.execute_sql(conn, sql_main)
            db.close_connection(conn)

            data = {"code": 0, "message": "修改成功"}
            data = json.dumps(data)

            return HttpResponse(data)

        except Exception as e:
            print(e)
            data = {"code": 1, "message":"修改失败"}
            logger.error("修改失败---->%s",e)
            data = json.dumps(data)
            return HttpResponse(data)


class DeletePersonMatter(View):

    def get(self, request):
        try:
            product_id = request.session.get("session_projectId")
            db = DB()
            conn = db.get_connection(product_id)

            matter_code = request.GET.get("matter_code")
            # matter_code = 'Im_Matter_5'
            sql = """
            delete from person_matter where matter_code = '{0}'
            """
            sql_main = sql.format(matter_code)
            des = db.execute_sql(conn, sql_main)

            data = {"code": 0, "message": "删除成功"}

            # else:
            #     data = {"code": 1, "message": "删除失败"}

            data = json.dumps(data)

            return HttpResponse(data)

        except Exception as e:
            print(e)
            data = {"code": 1, "message":"删除失败"}
            data = json.dumps(data)
            return HttpResponse(data)


class CreateBOMProductList(View):
    """
    创建产品列表结构表
    """

    def get(self, request):
        try:
            table_list = []
            db = DB()
            conn = db.get_connection("db_common")
            sql = """
            create table ProductList(prodect_code varchar(255) primary key not null,
            product_name varchar(255), product_id varchar(255), rule varchar(255),
            product_status varchar(255), description varchar(255), order_number int);          
            """
            dr = db.execute_sql(conn, sql)
            sql_main = """
                        show tables                 
                      """
            drs = db.execute_sql(conn, sql_main)
            for pe in drs:
                table_list.append(pe[0])

            if "productlist" in table_list:
                data = {"code": 0, "message": "操作成功"}
                logger.info("创建产品列表结构表成功")
            else:
                data = {"code": 1, "message": "操作失败"}
                logger.info("创建的表格已经存在")
            data = json.dumps(data)
            return HttpResponse(data)

        except Exception as e:
            print(e)
            data = {"code": 0, "message": "操作失败-%s"%e}
            data = json.dumps(data)
            logger.error("创建表格失败！！", e)

            return HttpResponse(data)


class CreateBOMMatterList(View):
    """
    创建物料结构表
    """
    def get(self, request):
        try:
            table_list = []
            db = DB()
            conn = db.get_connection("db_common")
            sql = """
                       create table matter_list(bom_matter_code varchar(64) primary key not null,
                    prodect_code varchar(64) not null,
                       matter_name varchar(64), rule varchar(64),matter_category varchar(64),
                       matter_usage int, order_number int)         
                       """
            dr = db.execute_sql(conn, sql)
            sql_main = """
                        show tables                 
                        """
            drs = db.execute_sql(conn, sql_main)
            for pe in drs:
                table_list.append(pe[0])

            if "matter_list" in table_list:
                data = {"code": 0, "message": "操作成功"}
                logger.info("创建产品物料列表结构表成功")
            else:
                data = {"code": 1, "message": "操作失败"}
                logger.info("创建产品物料已经存在")
            data = json.dumps(data)
            return HttpResponse(data)

        except Exception as e:
            print(e)
            data = {"code": 0, "message": "操作失败-%s" % e}
            data = json.dumps(data)
            logger.error("创建产品物料列表结构表失败！！", e)

            return HttpResponse(data)


class BOMProductList(View):
    """
    GET  查询产品列表
    post  插入产品名称 状态 型号等  新增产品列表
    """

    def get(self, request):
        try:
            data_list = []
            matter_list = []
            data_add_int = {}
            db = DB()
            product_id = request.session.get("session_projectId")
            # conn = db.get_connection("db_common")
            conn = db.get_connection(product_id)

            page = int(request.GET.get("page"))
            page_size = int(request.GET.get("page_size"))

            product_name = request.GET.get("product_name")
            rule = request.GET.get("rule")
            product_status = request.GET.get("product_status")


            # product_name = ""
            # rule = ""
            # product_status = "正常"
            # page = 1
            # page_size = 10
            if product_id == "db_common":
                s = ""
            else:
                s = "and product_id =" + "'" + product_id + "'"

            if product_name:
                product_name_sql = "and product_name = " + "'" + product_name + "'"
            else:
                product_name_sql = ""
            if rule:
                rule_sql = "and rule = " + "'" + rule + "'"
            else:
                rule_sql = ""
            if product_status:
                product_status_sql = "and product_status = " + "'" + product_status + "'"
            else:
                product_status_sql = ""
            sql = """
             select * from productlist where 2 > 1 {0} {1} {2} {3}
            """

            sql_main = sql.format(s, product_name_sql, rule_sql, product_status_sql)

            drs = db.execute_sql(db.get_connection("db_common"), sql_main)

            if drs:
                for dr in drs:
                    dict_data = {}
                    dict_data["prodect_code"] = dr[0]
                    dict_data["product_name"] = dr[1]
                    dict_data["product_id"] = dr[2]
                    dict_data["rule"] = dr[3]
                    dict_data["product_status"] = dr[4]
                    dict_data["description"] = dr[5]

                    sql_matter = """
                    select * from matter_list where prodect_code = '{0}'
                    """
                    sql_matter_format = sql_matter.format(dr[0])
                    matter_dfs = db.execute_sql(conn, sql_matter_format)
                    if matter_dfs:
                        respose_list = []
                        for matter_df in matter_dfs:
                            response_data = {}
                            response_data["bom_matter_code"] = matter_df[0]
                            response_data["prodect_code"] = matter_df[1]
                            response_data["matter_name"] = matter_df[2]
                            response_data["rule"] = matter_df[3]
                            response_data["matter_category"] = matter_df[4]
                            response_data["matter_usage"] = matter_df[5]
                            respose_list.append(response_data)
                        dict_data["response_datas"] = respose_list
                        data_list.append(dict_data)
                    else:
                        dict_data["response_datas"] = []
                        data_list.append(dict_data)

                page_result = Page(page, page_size, data_list)
                data = page_result.get_str_json()
                sql_num = """
                select count(*) from productlist where 2 > 1 {0} {1} {2} {3}
                """
                sql_num_main = sql_num.format(s, product_name_sql, rule_sql, product_status_sql)

                dfs = db.execute_sql(db.get_connection("db_common"), sql_num_main)
                sql_num_int = dfs[0][0]

                data_add_int["data"] = data
                data_add_int["total"] = sql_num_int

                result = {"code": 0, "message": "操作成功", "data": data_add_int}
                result = json.dumps(result)

                return HttpResponse(result)

            else:
                result = {"code": 0, "message": "操作失败", "data": []}
                result = json.dumps(result)

                return HttpResponse(result)

        except Exception as e:
            print(e)
            data = {"code": 1, "message": "调取BOM产品列表失败"}
            data = json.dumps(data)
            logger.error("查询产品列表失败")

            return HttpResponse(data)

    def post(self, request):
        try:

            json_data = request.body
            str_data = json.loads(json_data)

            product_db = str_data.get("product_id")
            db = DB()
            db.create_database(product_db)
            conn = db.get_connection(product_db)
            sql_person = """
                        create table person(user_code varchar(64) primary key not null,
                        user_id varchar(64), user_name varchar(32),
                        user_password varchar(64), user_authority varchar(255), status varchar(10), order_number int);
                        """
            dr = db.execute_sql(conn, sql_person)

            sql_matter = """           
                       create table Matter_List(bom_matter_code varchar(64) primary key not null,
                    prodect_code varchar(64) not null,
                       matter_name varchar(64), rule varchar(64),matter_category varchar(64),
                       matter_usage int, order_number int)                                    
                     """
            dr = db.execute_sql(conn, sql_matter)

            sql_work = """
                            create table Work_Station(work_code varchar(64) primary key not null,
                            work_id varchar(64) not null,
                            work_name varchar(64), work_type varchar(128), order_number int)         
                            """
            dr = db.execute_sql(conn, sql_work)

            sql_process = """
                                          create table Process_Deal(production_code varchar(128) primary key not null,
                                          production_id varchar(128) not null,
                                          production_name varchar(128), work_id varchar(128),
                                          leader_work_id varchar(128),
                                          description varchar(128), order_number int)         
                                          """
            dr = db.execute_sql(conn, sql_process)

            sql_check = """
                            create table Check_ProductDeal(check_code varchar(128) primary key not null,
                            prodect_code varchar(128),
                            work_code varchar(128) not null,
                            production_code varchar(128), check_method varchar(128), order_number int)         
                            """
            dr = db.execute_sql(conn, sql_check)

            sql_product_plan = """
                            create table Product_PlanDeal(prodect_code varchar(128) not null,
                            product_plan_code varchar(128) primary key not null,
                            plan_name varchar(128), plan_count int, plan_start_day datetime, plan_end_day datetime, 
                            description varchar(128), order_number int)         
                            """
            dr = db.execute_sql(conn, sql_product_plan)

            sql_pick_matter = """
                                   create table Product_PickMatter(
                                   materials_production_code varchar(128) primary key not null,
                                   materials_person varchar(128) not null,
                                   product_plan_code varchar(128), material_time datetime, description varchar(128),
                                    order_number int)         
                                   """
            dr = db.execute_sql(conn, sql_pick_matter)

            sql_transit = """
                            create table ProductTransitInfo(product_transit_code varchar(128) primary key not null,
                                                 matter_code varchar(128), user_code varchar(128),
                                                 work_code varchar(128),
                                                 test_result varchar(128), 
                                                 description varchar(255), 
                                                 enter_time datetime,
                                                 out_time datetime,
                                                 product_plan_code varchar(128),
                                                 end_product_code varchar(128),
                                                 product_code varchar(128),                                     
                                                 order_number int)         
                                                 """
            dr = db.execute_sql(conn, sql_transit)

            sql_martial = """
                       create table Person_Matter(matter_code varchar(128) primary key not null,
                       matter_count int, product_time datetime, order_number int);
                       """
            dr = db.execute_sql(conn, sql_martial)

            sql_product_parameter = """
                                                 create table Product_Parameter(test_code varchar(128) primary key not null,
                                                 check_code varchar(128), test_parameter varchar(128),
                                                 test_parameter_count varchar(128),
                                                 test_status varchar(128), order_number int)         
                                                 """
            dr = db.execute_sql(conn, sql_product_parameter)

            sql_matters = """
                        create table Pick_Matter(materials_code varchar(128) primary key not null, 
                        materials_production_code varchar(128) not null,
                        matter_code varchar(128), matter_count int, order_number int)
                        """
            df = db.execute_sql(conn, sql_matters)

            sql_pick = """
                        create table Pick_box(pick_code varchar(255) primary key not null,
                        work_id varchar(255), 
                        pick_number int,
                        description varchar(255), order_number int)
                        """
            df = db.execute_sql(conn, sql_pick)

            sql_back = """
                        create table product_back_matter(materials_back_code varchar(255) primary key not null,
                        back_person varchar(255), 
                        product_plan_code varchar(255),
                        back_time datetime,
                        description varchar(255), order_number int)
                      """
            df = db.execute_sql(conn, sql_back)

            sql_deal_back = """
                        create table back_matter(deal_back_code varchar(255) primary key not null,
                        materials_back_code varchar(255), 
                        matter_code varchar(255),
                        matter_count int,
                        order_number int)
                      """
            df = db.execute_sql(conn, sql_deal_back)

            sql_enter_status = """           
            create table enter_storage_status(pack_id varchar(255) primary key not null,
                              product_id varchar(255),product_name varchar(255),
                              enter_user varchar(255), enter_time datetime, 
                              status varchar(255),order_number int)
            """
            db.execute_sql(conn, sql_enter_status)

            sql_enter = """
            create table enter_storage(enter_storage_code varchar(255) primary key not null, 
                              pack_id varchar(255),
                              finished_product_code varchar(255),
                              order_number int)
            """
            db.execute_sql(conn, sql_enter)

            sql_operate = """
            create table operate(ID int primary key not null, 
                     Package_Qty int,
                     Rv varchar(255),
                     Itemcode_C_Shipping varchar(255),
                     Supplier varchar(255),
                     No_Ship int,
                     CS_type varchar(255),
                     Shipping_SN_length int,
                     order_number int);
            """
            db.execute_sql(conn, sql_operate)

            sql_function = """
                        create table function_list(function_list_code int AUTO_INCREMENT primary key not null, 
                                 function_name varchar(255));
                        """
            db.execute_sql(conn, sql_function)






            sql_matter = """
            SELECT max(order_number) FROM matter_list;
            """
            matter_type = db.execute_sql(conn, sql_matter)
            if matter_type[0][0] == None:
                matter_num = 0
            else:
                matter_num = matter_type[0][0]

            conn_product = db.get_connection("db_common")

            sql = """
                         SELECT max(order_number) FROM productlist;
                """
            product_type = db.execute_sql(conn_product, sql)
            if product_type[0][0] == None:
                id_num = 1
            else:
                id_num = product_type[0][0] + 1
            prodect_code = str("Im_Product_" + str(id_num))
            product_name = str_data.get("product_name")
            rule = str_data.get("rule")
            product_status = str_data.get("product_status")
            description = str_data.get("description")
            response_datas = str_data.get("response_datas")

            order_number = id_num

            # response_datas = [{"matter_name": "袋子", "rule": "方形", "matter_category": "A", "matter_usage": 1},
            #                   {"matter_name": "布", "rule": "圆形","matter_category": "B", "matter_usage": 1}]


            # product_name = "桌子"
            # rule = "木头"
            # product_status = "正常"
            # description = "学习用品"
            # order_number = id_num
            sql_insert = """
                        insert into productlist(prodect_code, product_name, product_id, rule,
                        product_status, description, order_number)
                        values('{0}', '{1}', '{2}', '{3}', '{4}', '{5}', '{6}')
                        """
            sql_insert_format = sql_insert.format(prodect_code, product_name, product_db, rule, product_status,
                                                  description, order_number)

            drs = db.execute_sql(conn_product, sql_insert_format)

            for response_data in response_datas:
                # db = DB()
                # conn = db.get_connection("db_common")
                matter_name = response_data.get("matter_name")
                rule = response_data.get("rule")
                matter_category = response_data.get("matter_category")
                matter_usage = response_data.get("matter_usage")
                matter_num = matter_num+1
                bom_matter_code = str("Im_BOM_Matter_" + str(matter_num))
                sql_response = """
                        insert into matter_list(bom_matter_code,prodect_code, matter_name, rule,
                        matter_category, matter_usage, order_number)
                        values('{0}', '{1}', '{2}', '{3}', '{4}','{5}', '{6}')
                """
                sql_response_format = sql_response.format(bom_matter_code, prodect_code, matter_name,
                                                          rule, matter_category, matter_usage, matter_num)
                matter_drs = db.execute_sql(conn, sql_response_format)

            data = {"code": 0, "message": "创建产品详情表成功"}
            logger.info("创建产品详情表成功")

            data = json.dumps(data)

            return HttpResponse(data)
        except Exception as e:
            print(e)
            data = {"code": 1, "message": "创建产品详情表失败"}
            logger.error("创建产品详情表失败")
            data = json.dumps(data)
            return HttpResponse(data)


class PutBOMProductList(View):

    """
    修改产品列表

    """
    def get(self, request):
        try:
            db = DB()
            conn = db.get_connection("db_common")
            prodect_code = request.GET.get("prodect_code")
            product_name = request.GET.get("product_name")
            rule = request.GET.get("rule")
            product_status = request.GET.get("product_status")
            description = request.GET.get("description")

            response_datas = request.GET.get("response_datas")
            product_id = request.session['session_projectId']
            # current_person_id = request.session['session_currentId']
            # work_id = request.session['session_workId']

            if response_datas:
                response_datas = eval(response_datas)
            else:
                response_datas = response_datas

            # prodect_code = 'Im_Product_7'
            # product_name = '空调'
            # rule = '电力'
            # product_status = '正常'
            # description = '常用品'
            #
            # response_datas = [{"bom_matter_code": "Im_BOM_Matter_2","prodect_code":"Im_Product_7",
            #                    "matter_name": "风扇", "rule": "圆形", "matter_usage": 2}]

            # new_check_list = [prodect_code, product_name, rule, product_status, description]

            sql = """
                update productlist set 
                   product_name='{0}',rule='{1}',product_status='{2}', description ='{3}'
                   where prodect_code = '{4}'
                   """
            sql_main = sql.format(product_name, rule, product_status, description, prodect_code)
            drs = db.execute_sql(conn, sql_main)

            for response_data in response_datas:
                bom_matter_code = response_data.get("bom_matter_code")
                if bom_matter_code:
                    sql_delete = """
                     delete FROM matter_list where bom_matter_code = '{0}'
                    """
                    sql_delete_format = sql_delete.format(bom_matter_code)
                    conn = db.get_connection(product_id)
                    db.execute_sql(conn, sql_delete_format)

            conn = db.get_connection(product_id)
            sql_after = """
                        SELECT max(order_number) FROM matter_list
                        """
            num = db.execute_sql(conn, sql_after)
            if num[0][0]:
                sql_num = num[0][0]
            else:
                sql_num = 0

            for response_data in response_datas:
                # db = DB()
                # conn = db.get_connection("db_common")
                matter_name = response_data.get("matter_name")
                rule = response_data.get("rule")
                matter_category = response_data.get("matter_category")
                matter_usage = response_data.get("matter_usage")
                sql_num = sql_num + 1
                bom_matter_code = str("Im_BOM_Matter_" + str(sql_num))
                sql_response = """
                                    insert into matter_list(bom_matter_code,prodect_code, matter_name, rule,
                                    matter_category, matter_usage, order_number)
                                    values('{0}', '{1}', '{2}', '{3}', '{4}','{5}', '{6}')
                            """
                sql_response_format = sql_response.format(bom_matter_code, prodect_code, matter_name,
                                                          rule, matter_category, matter_usage, sql_num)
                matter_drs = db.execute_sql(conn, sql_response_format)
            data = {"code": 0, "message": "修改成功"}

            data = json.dumps(data)

            db.close_connection(conn)

            return HttpResponse(data)

        except Exception as e:
            print(e)
            data = {"code": 1, "message": "修改失败"}
            logger.error("修改失败---->%s", e)
            data = json.dumps(data)
            return HttpResponse(data)


class DeleteBOMProductList(View):
    """
    删除产品列表的一行

    """
    def get(self, request):
        try:
            db = DB()
            db_base = request.GET.get("product_id")
            product_id = request.session.get("product_id")
            # product_id = request.session.get("product_id")
            conn = db.get_connection("db_common")

            prodect_code = request.GET.get("prodect_code")

            # prodect_code = "Im_Product_2"
            response_datas = request.GET.get("response_datas")
            # response_datas = eval(response_datas)
            response_datas = eval(response_datas)

            # response_datas = ""
            # response_datas = [{"bom_matter_code": "Im_BOM_Matter_5"}, {"bom_matter_code": "Im_BOM_Matter_6"}]
            if len(response_datas) != 0:

                for response_data in response_datas:
                    bom_matter_code = dict(response_data).get("bom_matter_code")
                    sql = """
                    delete from matter_list where bom_matter_code = '{0}'
                    """
                    sql_format = sql.format(bom_matter_code)
                    db.execute_sql(conn, sql_format)
            else:
                sql_drop_db = """
                drop 
                """


                sql_matter = """
                               SELECT * FROM matter_list where prodect_code = '{0}'
                               """
                sql_matter_format = sql_matter.format(prodect_code)
                matter_dfs = db.execute_sql(conn, sql_matter_format)
                for matter_df in matter_dfs:
                    bom_matter_code = matter_df[0]
                    sql_delete = """
                    delete FROM matter_list where bom_matter_code = '{0}'
                    """
                    sql_delete_format = sql_delete.format(bom_matter_code)
                    db.execute_sql(conn, sql_delete_format)
                sql = """
                    delete from productlist where prodect_code = '{0}'
                    """
                sql_main = sql.format(prodect_code)
                des = db.execute_sql(conn, sql_main)

            data = {"code": 0, "message": "删除成功"}
            logger.info("修改产品列表或者物料表成功")

            data = json.dumps(data)

            return HttpResponse(data)

        except Exception as e:
            print(e)
            data = {"code": 1, "message": "删除失败"}
            data = json.dumps(data)
            logger.error("修改产品列表失败,%s"% e)
            return HttpResponse(data)


class BOMMatterList(View):

    def get(self, request):
        try:
            data_list = []
            data_add_int = {}
            db = DB()
            conn = db.get_connection("db_common")
            page = int(request.GET.get("page"))
            page_size = int(request.GET.get("page_size"))

            matter_name = request.Get.get("matter_name")
            rule = request.Get.get("rule")
            # matter_name = ""
            # rule = ""
            # page = 1
            # page_size = 10
            if len(rule) == 0 and len(matter_name) == 0:
                sql = """
                    select * from matter_list
                    """
                drs = db.execute_sql(conn, sql)
                if drs:
                    for dr in drs:
                        dict_data = {}
                        dict_data["prodect_code"] = dr[0]
                        dict_data["matter_name"] = dr[1]
                        dict_data["rule"] = dr[2]
                        dict_data["matter_usage"] = dr[3]
                        dict_data["order_number"] = dr[4]
                        data_list.append(dict_data)

                    page_result = Page(page, page_size, data_list)
                    data = page_result.get_str_json()
                    sql_num = """
                                    select count(*) from matter_list
                                    """
                    dfs = db.execute_sql(conn, sql_num)
                    sql_num_int = dfs[0][0]

                    data_add_int["data"] = data
                    data_add_int["total"] = sql_num_int
                else:
                    pass

            else:
                sql = """
                select * from matter_list where matter_name = '{0}' and rule = '{1}'               
                """
                sql_main = sql.format(matter_name, rule)
                drs = db.execute_sql(conn, sql_main)
                if drs:
                    for dr in drs:
                        dict_data = {}
                        dict_data["prodect_code"] = dr[0]
                        dict_data["matter_name"] = dr[1]
                        dict_data["rule"] = dr[2]
                        dict_data["matter_usage"] = dr[3]
                        dict_data["order_number"] = dr[4]
                        data_list.append(dict_data)

                    page_result = Page(page, page_size, data_list)
                    data = page_result.get_str_json()
                    sql_num = """
                        select count(*) from matter_list 
                        where matter_name = '{0}' and rule = '{1}'
                          """
                    sql_format = sql_num.format(matter_name, rule)
                    dfs = db.execute_sql(conn, sql_format)
                    sql_num_int = dfs[0][0]

                    data_add_int["data"] = data
                    data_add_int["total"] = sql_num_int

                else:
                    pass
            data = {"code": 0, "message": "操作成功", "data": data_add_int}
            data = json.dumps(data)
            logger.info("查询产品列表成功")

            return HttpResponse(data)
        except Exception as e:
            print(e)
            data = {"code": 1, "message": "调取BOM产品列表失败"}
            data = json.dumps(data)
            logger.error("新增产品列表成功")

            return HttpResponse(data)

    def post(self, request):
        try:
            db = DB()
            conn = db.get_connection("db_common")

            sql = """
                         SELECT max(order_number) FROM matter_list;
                        """
            matter_type = db.execute_sql(conn, sql)
            if matter_type[0][0] == None:
                id_num = 1
            else:
                id_num = matter_type[0][0] + 1

            prodect_code = request.POST.get("prodect_code")
            matter_name = request.POST.get("matter_name")
            rule = request.POST.get("rule")
            matter_usage = request.POST.get("matter_usage")
            order_number = id_num

            # prodect_code = "Im_Product_3"
            # matter_name = "键格"
            # rule = "发光"
            # matter_usage = 26
            # order_number = id_num

            # product_name = "键盘"
            # rule = "10,23,22"
            # product_status = "正常"
            # description = "办公用品"
            # order_number = id_num
            sql_insert = """
                        insert into matter_list(prodect_code, matter_name, rule,
                        matter_usage, order_number)
                        values('{0}', '{1}', '{2}', '{3}', '{4}')
                        """
            sql_insert_format = sql_insert.format(prodect_code, matter_name, rule, matter_usage,
                                                  order_number)

            drs = db.execute_sql(conn, sql_insert_format)
            sql_after = """
                        SELECT max(order_number) FROM matter_list
                        """
            num = db.execute_sql(conn, sql_after)
            if num[0][0] == order_number:
                data = {"code": 0, "message": "创建物料详情表成功"}
                logger.info("创建物料详情表成功")
            else:
                data = {"code": 1, "message": "创建物料详情表失败"}
                logger.error("创建物料详情表失败")
            data = json.dumps(data)

            return HttpResponse(data)
        except Exception as e:
            print(e)
            data = {"code": 1, "message": "创建物料详情表失败"}
            logger.error("创建物料详情表失败")
            data = json.dumps(data)


class CreateWorkStation(View):
    def get(self, request):
        try:
            db = DB()
            conn = db.get_connection("db_common")
            sql = """
                create table Work_Station(work_code varchar(64) primary key not null,
                work_id varchar(64) not null,
                work_name varchar(64), work_type varchar(128), order_number int)         
                """
            dr = db.execute_sql(conn, sql)

            data = {"code": 0, "message": "操作成功"}
        except Exception as e:
            print(e)
            data = {"code": 1, "message": "操作失败"}

        data = json.dumps(data)

        return HttpResponse(data)


class WorkStation(View):

    def get(self, request):
        try:
            # table_list = []
            data_list = []
            matter_list = []
            data_add_int = {}
            product_id = request.session.get("session_projectId")
            db = DB()
            conn = db.get_connection(product_id)

            page = int(request.GET.get("page"))
            page_size = int(request.GET.get("page_size"))

            work_id = request.GET.get("work_id")
            work_name = request.GET.get("work_name")
            # page = 1
            # page_size = 10
            # work_id = "001"
            # work_name = ""

            if work_id:
                work_id = str("work_e_") + str(work_id)
                work_id_sql = " and work_id =" + "'" + work_id + "'"
            else:
                work_id_sql = ""
            if work_name:
                work_name_sql = " and work_name =" + "'" + work_name + "'"
            else:
                work_name_sql = ""

            sql = """
                select * from  work_station where 2>1 {0} {1}
                """
            sql_main = sql.format(work_id_sql, work_name_sql)
            drs = db.execute_sql(conn, sql_main)

            if drs:
                for dr in drs:
                    dict_data = {}
                    dict_data["work_code"] = dr[0]
                    dict_data["work_id"] = dr[1]
                    dict_data["work_name"] = dr[2]
                    dict_data["work_type"] = dr[3]
                    data_list.append(dict_data)
                page_result = Page(page, page_size, data_list)
                data = page_result.get_str_json()
                sql_num = """
                          select count(*) from work_station
                           """
                dfs = db.execute_sql(conn, sql_num)
                sql_num_int = dfs[0][0]

                data_add_int["data"] = data
                data_add_int["total"] = sql_num_int

            else:
                data_add_int["data"] = []
                data_add_int["total"] = 0

            result = {"code": 0, "message": "调取成功", "data": data_add_int}
            result = json.dumps(result)
            return HttpResponse(result)
        except Exception as e:
            print(e)
            result = {"code": 0, "message": "调取失败", "data": e}
            result = json.dumps(result)
            return HttpResponse(result)

    def post(self, request):
        try:
            respose_data_json = request.body
            respose_data_dict = json.loads(respose_data_json)
            work_id_str = respose_data_dict.get("work_id")

            work_id = str("product_transit_") + str(work_id_str)
            work_name = respose_data_dict.get("work_name")
            work_type = respose_data_dict.get("work_type")

            db = DB()
            product_id = request.session.get("session_projectId")
            conn = db.get_connection(product_id)


            sql = """
             SELECT max(order_number) FROM work_station;
            """
            works = db.execute_sql(conn, sql)
            if works[0][0] == None:
                id_num = 1
            else:
                id_num = works[0][0] + 1
            work_code = str("Im_WorkStation_" + str(id_num))

            # work_id = "003"
            # work_name = "003站"
            # work_type = "3站"

            sql_insert = """
                               insert into work_station(work_code, work_id, work_name,
                               work_type, order_number)
                               values('{0}', '{1}', '{2}', '{3}', '{4}')   
                        """
            sql_insert_format = sql_insert.format(work_code, work_id_str, work_name, work_type, id_num)
            drs = db.execute_sql(conn, sql_insert_format)

            sql_create_table = """
                create table {0}(product_transit_code varchar(128) primary key not null,
                                     matter_code varchar(128), 
                                     matter_id varchar(128),
                                     finished_product_code varchar(128),
                                     user_code varchar(128),
                                     work_code varchar(128),
                                     test_result varchar(128), 
                                     description varchar(255), 
                                     enter_time datetime,
                                     out_time datetime,
                                     product_plan_code varchar(128),
                                     end_product_code varchar(128),
                                     product_code varchar(128),                                     
                                     order_number int) 
            
            """
            sql_create_table_main = sql_create_table.format(work_id)
            dr = db.execute_sql(conn, sql_create_table_main)

            sql_un_table = str("unqualified_product_") + str(work_id_str)
            sql_create_un_table = """
            CREATE TABLE IF NOT EXISTS {0}(unqualified_product_code varchar(255) primary key not null, 
                                                      product_plan_code varchar(255),
                                                      finished_product_code varchar(255),
                                                      matter_code varchar(255),
                                                      matter_id varchar(255),
                                                      description varchar(255),
                                                      leader_work_id varchar(255),
                                                      later_work_id varchar(255),
                                                      solve_method varchar(255),
                                                      solve_result varchar(255),                             
                                                      order_number int)           
            """
            sql_create_un_table = sql_create_un_table.format(sql_un_table)
            db.execute_sql(conn, sql_create_un_table)
            data = {"code":0, "message":"创建工站信息表和产品过站表成功"}

            data = json.dumps(data)

            return HttpResponse(data)
        except Exception as e:
            print(e)

            data = {"code":1, "message":"创建工站信息表失败"}
            data = json.dumps(data)

            return HttpResponse(data)


class PutWorkStation(View):

    def get(self, request):
        try:
            db = DB()
            product_id = request.session.get("session_projectId")
            conn = db.get_connection(product_id)

            work_code = request.GET.get("work_code")
            work_id = request.GET.get("work_id")
            work_name = request.GET.get("work_name")
            work_type = request.GET.get("work_type")

            # work_code = "Im_WorkStation_3"
            # work_id = "003"
            # work_name = "003站"
            # work_type = "测试站"
            sql = """
                    update work_station set 
                    work_id='{0}',work_name='{1}', work_type ='{2}'
                    where work_code = '{3}'
                    """
            sql_main = sql.format(work_id, work_name, work_type, work_code)
            drs = db.execute_sql(conn, sql_main)

            data = {"code": 0, "message": "修改成功", "data": ""}
            data = json.dumps(data)

            return HttpResponse(data)

        except Exception as e:
            print(e)
            data = {"code": 0, "message": "操作失败", "data": e}
            data = json.dumps(data)

            return HttpResponse(data)


class DeleteWorkStation(View):

    def get(self, request):
        try:
            db = DB()
            product_id = request.session.get("session_projectId")
            conn = db.get_connection(product_id)
            # work_code = request.GET.get("work_code")
            work_id = request.GET.get("work_id")
            sql = """
            delete FROM work_station where work_id = "{0}"           
            """
            sql_num = sql.format(work_id)

            drs = db.execute_sql(conn, sql_num)

            work_id_tansit = str("product_transit_") + str(work_id)

            sql_product_tansit = """
            drop table {0}
            """
            sql_product_tansit_main = sql_product_tansit.format(work_id_tansit)
            dfs = db.execute_sql(conn, sql_product_tansit_main)

            data = {"code":0, "message": "删除成功", "data":""}

            data = json.dumps(data)

            return HttpResponse(data)

        except Exception as e:
            print(e)
            data = {"code":1, "message": "删除失败", "data":e}
            data = json.dumps(data)

            return HttpResponse(data)


class CreateProductPlanDeal(View):

    def get(self, request):
        try:
            db = DB()
            conn = db.get_connection("db_common")
            sql = """
                create table Product_PlanDeal(prodect_code varchar(128) not null,
                product_plan_code varchar(128) primary key not null,
                plan_name varchar(128), plan_count int, plan_start_day datetime, plan_end_day datetime, 
                description varchar(128), order_number int)         
                """
            dr = db.execute_sql(conn, sql)

            data = {"code": 0, "message":"操作成功"}
            # data = json.dumps(data)
        except Exception as e:
            print(e)
            data = {"code":1, "message":"操作失败"}

        data = json.dumps(data)

        return HttpResponse(data)


class ProductPlanDeal(View):

    def get(self, request):
        try:
            data_list = []
            data_add_int = {}
            product_id = request.session.get("session_projectId")
            db = DB()
            conn = db.get_connection(product_id)
            page = int(request.GET.get("page"))
            page_size = int(request.GET.get("page_size"))
            prodect_code = request.GET.get("prodect_code")
            plan_name = request.GET.get("plan_name")

            # page = 1
            # page_size = 10
            # prodect_code = "Im_Product_10"
            # plan_name = ""

            if len(prodect_code) == 0 and len(plan_name) == 0:
                sql = """
                    select * from product_plandeal
                    """
                drs = db.execute_sql(conn, sql)
                if drs:
                    for dr in drs:
                        dict_data = {}
                        dict_data["prodect_code"] = dr[0]
                        dict_data["product_plan_code"] = dr[1]
                        dict_data["plan_name"] = dr[2]
                        dict_data["plan_count"] = dr[3]
                        s = dr[4]
                        s1 = s.strftime("%Y-%m-%d %H:%M:%S ")
                        dict_data["plan_start_day"] = s1
                        d = dr[5]
                        s2 = d.strftime("%Y-%m-%d %H:%M:%S ")
                        dict_data["plan_end_day"] = s2
                        dict_data["description"] = dr[6]
                        data_list.append(dict_data)

                    page_result = Page(page, page_size, data_list)
                    data = page_result.get_str_json()
                    sql_num = """
                                    select count(*) from product_plandeal
                                    """
                    dfs = db.execute_sql(conn, sql_num)
                    sql_num_int = dfs[0][0]

                    data_add_int["data"] = data
                    data_add_int["total"] = sql_num_int
                else:
                    data_add_int["data"] = ""

            elif len(prodect_code) != 0 and len(plan_name) != 0:
                sql = """
                select * from product_plandeal where prodect_code = '{0}' and plan_name = '{1}'
                """
                sql_main = sql.format(prodect_code, plan_name)
                drs = db.execute_sql(conn, sql_main)
                if drs:
                    for dr in drs:
                        dict_data = {}
                        dict_data["prodect_code"] = dr[0]
                        dict_data["product_plan_code"] = dr[1]
                        dict_data["plan_name"] = dr[2]
                        dict_data["plan_count"] = dr[3]
                        s = dr[4]
                        s1 = s.strftime("%Y-%m-%d %H:%M:%S ")
                        dict_data["plan_start_day"] = s1
                        d = dr[5]
                        s2 = d.strftime("%Y-%m-%d %H:%M:%S ")
                        dict_data["plan_end_day"] = s2
                        dict_data["description"] = dr[6]
                        data_list.append(dict_data)

                    page_result = Page(page, page_size, data_list)
                    data = page_result.get_str_json()
                    sql_num = """
                            select count(*) from product_plandeal where prodect_code = '{0}' and plan_name = '{1}'
                              """
                    sql_num_format = sql_num.format(prodect_code, plan_name)
                    dfs = db.execute_sql(conn, sql_num_format)
                    sql_num_int = dfs[0][0]

                    data_add_int["data"] = data
                    data_add_int["total"] = sql_num_int
                else:
                    data_add_int["data"] = ""

            elif len(prodect_code) == 0 and len(plan_name) != 0:
                sql = """
                select * from product_plandeal where plan_name = '{0}'
                """
                sql_main = sql.format(plan_name)
                drs = db.execute_sql(conn, sql_main)
                if drs:
                    for dr in drs:
                        dict_data = {}
                        dict_data["prodect_code"] = dr[0]
                        dict_data["product_plan_code"] = dr[1]
                        dict_data["plan_name"] = dr[2]
                        dict_data["plan_count"] = dr[3]
                        s = dr[4]
                        s1 = s.strftime("%Y-%m-%d %H:%M:%S ")
                        dict_data["plan_start_day"] = s1
                        d = dr[5]
                        s2 = d.strftime("%Y-%m-%d %H:%M:%S ")
                        dict_data["plan_end_day"] = s2
                        dict_data["description"] = dr[6]
                        data_list.append(dict_data)

                    page_result = Page(page, page_size, data_list)
                    data = page_result.get_str_json()
                    sql_num = """
                            select count(*) from product_plandeal where plan_name = '{0}'
                              """
                    sql_num_format = sql_num.format(plan_name)
                    dfs = db.execute_sql(conn, sql_num_format)
                    sql_num_int = dfs[0][0]

                    data_add_int["data"] = data
                    data_add_int["total"] = sql_num_int
                else:
                    data_add_int["data"] = ""

            elif len(prodect_code) != 0 and len(plan_name) == 0:
                sql = """
                select * from product_plandeal where prodect_code = '{0}'
                """
                sql_main = sql.format(prodect_code)
                drs = db.execute_sql(conn, sql_main)
                if drs:
                    for dr in drs:
                        dict_data = {}
                        dict_data["prodect_code"] = dr[0]
                        dict_data["product_plan_code"] = dr[1]
                        dict_data["plan_name"] = dr[2]
                        dict_data["plan_count"] = dr[3]
                        s = dr[4]
                        s1 = s.strftime("%Y-%m-%d %H:%M:%S ")
                        dict_data["plan_start_day"] = s1
                        d = dr[5]
                        s2 = d.strftime("%Y-%m-%d %H:%M:%S ")
                        dict_data["plan_end_day"] = s2
                        dict_data["description"] = dr[6]
                        data_list.append(dict_data)

                    page_result = Page(page, page_size, data_list)
                    data = page_result.get_str_json()
                    sql_num = """
                            select count(*) from product_plandeal where prodect_code = '{0}'
                              """
                    sql_num_format = sql_num.format(prodect_code)
                    dfs = db.execute_sql(conn, sql_num_format)
                    sql_num_int = dfs[0][0]

                    data_add_int["data"] = data
                    data_add_int["total"] = sql_num_int
                else:
                    data_add_int["data"] = ""

            result = {"code": 0, "message": "操作成功", "data": data_add_int}
            result = json.dumps(result)

            return HttpResponse(result)

        except Exception as e:
            print(e)
            data = {"code": 1, "message": "查询失败"}
            data = json.dumps(data)

            return HttpResponse(data)

    def post(self, request):
        try:
            db = DB()
            product_id = request.session.get("session_projectId")
            conn = db.get_connection(product_id)

            sql = """
             SELECT max(order_number) FROM product_plandeal;
            """
            works = db.execute_sql(conn, sql)
            if works[0][0] == None:
                id_num = 1
            else:
                id_num = works[0][0] + 1

            order_number = id_num

            response_data_json = request.body
            response_data = json.loads(response_data_json)
            product_plan_code = str("Im_ProductPlan_" + str(id_num))

            prodect_code = response_data.get("prodect_code")
            plan_name = response_data.get("plan_name")
            plan_count = response_data.get("plan_count")
            plan_start_day = response_data.get("plan_start_day")
            plan_end_day = response_data.get("plan_end_day")
            description = response_data.get("description")
            # prodect_code = "Im_Product_10"
            # plan_name = "桌子计划"
            # plan_count = 100
            # plan_start_day = "2021-07-06"
            # plan_end_day = "2021-07-22"
            # description = ""
            sql_insert = """
                               insert into product_plandeal(prodect_code, product_plan_code,
                               plan_name, plan_count, plan_start_day, plan_end_day, description, order_number)
                               values('{0}', '{1}', '{2}', '{3}', '{4}','{5}', '{6}', '{7}')   
                        """
            sql_insert_format = sql_insert.format(prodect_code, product_plan_code, plan_name, plan_count,
                                                  plan_start_day, plan_end_day, description, order_number)
            drs = db.execute_sql(conn, sql_insert_format)

            data = {"code": 0, "message": "创建工站信息表成功"}

            data = json.dumps(data)

            return HttpResponse(data)

        except Exception as e:
            print(e)

            data = {"code": 1, "message": "创建工站信息表失败"}
            data = json.dumps(data)

            return HttpResponse(data)


class PutProductPlanDeal(View):

    def get(self, request):
        try:
            db = DB()
            product_id = request.session.get("session_projectId")
            conn = db.get_connection(product_id)
            prodect_code = request.GET.get("prodect_code")
            product_plan_code = request.GET.get("product_plan_code")
            plan_name = request.GET.get("plan_name")
            plan_count = request.GET.get("plan_count")
            plan_start_day = request.GET.get("plan_start_day")
            plan_end_day = request.GET.get("plan_end_day")
            description = request.GET.get("description")

            # prodect_code = "Im_Product_10"
            # product_plan_code = "Im_ProductPlan_2"
            # plan_name = "火箭计划"
            # plan_count = 50
            # plan_start_day = "2021-07-06"
            # plan_end_day = "2021-07-26"
            # description = "sjjsh"


            sql = """
            update product_plandeal set prodect_code='{0}',plan_name='{1}', plan_count ='{2}', 
            plan_start_day='{3}',plan_end_day = '{4}', description = '{5}' where product_plan_code = '{6}'
                    """

            sql_main = sql.format(prodect_code, plan_name, plan_count,
                                  plan_start_day, plan_end_day, description, product_plan_code)
            drs = db.execute_sql(conn, sql_main)

            data = {"code": 0, "message": "修改成功", "data":""}
            data = json.dumps(data)

            return HttpResponse(data)

        except Exception as e:
            print(e)
            data = {"code": 0, "message": "操作失败", "data": e}
            data = json.dumps(data)

            return HttpResponse(data)


class DeleteProductPlanDeal(View):

    def get(self, request):
        try:
            db = DB()
            product_id = request.session.get("session_projectId")
            conn = db.get_connection(product_id)
            product_plan_code = request.GET.get("product_plan_code")

            print("----->>>>>", product_plan_code)
            # product_plan_code = "Im_ProductPlan_2"
            sql = """
            delete FROM product_plandeal where product_plan_code = "{0}"           
            """
            sql_num = sql.format(product_plan_code)
            drs = db.execute_sql(conn, sql_num)

            data = {"code":0, "message": "删除成功", "data":""}

            data = json.dumps(data)

            return HttpResponse(data)

        except Exception as e:
            print(e)
            data = {"code":1, "message": "删除失败", "data":e}
            data = json.dumps(data)

            return HttpResponse(data)


class ProductCodeName(View):
    def get(self, request):
        try:
            data_list = []
            db = DB()
            # product_id = request.session.get("session_projectId")
            # conn = db.get_connection(product_id)
            product_id = "db_common"
            conn = db.get_connection(product_id)
            sql = """
            select prodect_code,product_name from productlist
            """
            drs = db.execute_sql(conn, sql)
            for dr in drs:
                data_dict = {}
                data_dict["product_code"] = dr[0]
                data_dict["product_name"] = dr[1]
                data_list.append(data_dict)
            data = {"code": 0, "message": "操作成功", "data": data_list}
            data = json.dumps(data)

            return HttpResponse(data)

        except Exception as e:
            print(e)
            data = {"code": 1, "message": "操作失败", "data": e}
            data = json.dumps(data)

            return HttpResponse(data)


class CreateProductPickMatter(View):
    def get(self, request):
        try:
            db = DB()
            product_id = request.session.get("session_projectId")
            conn = db.get_connection(product_id)
            sql = """
                       create table Product_PickMatter(materials_production_code varchar(128) primary key not null,
                       materials_person varchar(128) not null,
                       product_plan_code varchar(128), material_time datetime, description varchar(128), order_number int)         
                       """
            dr = db.execute_sql(conn, sql)

            sql_matter = """
            create table Pick_Matter(materials_code varchar(128) primary key not null, 
            materials_production_code varchar(128) not null,
            matter_code varchar(128), matter_count int, order_number int)
            """
            df = db.execute_sql(conn, sql_matter)

            data = {"code": 0, "message": "操作成功"}
            # data = json.dumps(data)
        except Exception as e:
            print(e)
            data = {"code": 1, "message": "操作失败"}

        data = json.dumps(data)

        return HttpResponse(data)


class ProductPickMatter(View):

    def get(self, request):
        try:
            data_list = []
            matter_list = []
            data_add_int = {}
            db = DB()
            product_id = request.session.get("session_projectId")
            conn = db.get_connection(product_id)

            page = int(request.GET.get("page"))
            page_size = int(request.GET.get("page_size"))

            materials_person = request.GET.get("materials_person")
            product_plan_code = request.GET.get("product_plan_code")

            # page = 1
            # page_size = 10
            # materials_person = "小小笑"
            # product_plan_code = ""
            if len(materials_person) == 0 and len(product_plan_code) == 0:
                sql = """
                    select * from product_pickmatter
                    """
                drs = db.execute_sql(conn, sql)
                if drs:
                    for dr in drs:
                        dict_data = {}
                        dict_data["materials_production_code"] = dr[0]
                        dict_data["materials_person"] = dr[1]
                        dict_data["product_plan_code"] = dr[2]
                        s = dr[3]
                        s1 = s.strftime("%Y-%m-%d %H:%M:%S ")
                        dict_data["material_time"] = s1

                        dict_data["description"] = dr[4]
                        sql_matter = """
                        select * from pick_matter where materials_production_code = '{0}'
                        """
                        sql_matter_format = sql_matter.format(dr[0])
                        matter_dfs = db.execute_sql(conn, sql_matter_format)
                        if matter_dfs:
                            respose_list = []
                            for matter_df in matter_dfs:
                                response_data = {}
                                response_data["materials_code"] = matter_df[0]
                                response_data["materials_production_code"] = matter_df[1]
                                response_data["matter_code"] = matter_df[2]
                                response_data["matter_count"] = matter_df[3]
                                respose_list.append(response_data)
                            dict_data["response_datas"] = respose_list
                            data_list.append(dict_data)
                        else:
                            dict_data["response_datas"] = []
                            data_list.append(dict_data)
                    page_result = Page(page, page_size, data_list)
                    data = page_result.get_str_json()

                    sql_num = """
                                    select count(*) from product_pickmatter
                                    """
                    dfs = db.execute_sql(conn, sql_num)
                    sql_num_int = dfs[0][0]

                    data_add_int["data"] = data
                    data_add_int["total"] = sql_num_int

                    result = {"code": 0, "message":"操作成功", "data": data_add_int}
                    result = json.dumps(result)

                    return HttpResponse(result)

                else:
                    result = {"code": 0, "message": "操作失败", "data": ""}
                    result = json.dumps(result)

                    return HttpResponse(result)

            elif len(materials_person) != 0 and len(product_plan_code) == 0:
                sql = """
                    select * from product_pickmatter where materials_person = '{0}'
                    """
                sql_main = sql.format(materials_person)
                drs = db.execute_sql(conn, sql_main)
                if drs:
                    for dr in drs:
                        dict_data = {}
                        dict_data["materials_production_code"] = dr[0]
                        dict_data["materials_person"] = dr[1]
                        dict_data["product_plan_code"] = dr[2]
                        s = dr[3]
                        s1 = s.strftime("%Y-%m-%d %H:%M:%S ")
                        dict_data["material_time"] = s1

                        dict_data["description"] = dr[4]
                        sql_matter = """
                        select * from pick_matter where materials_production_code = '{0}'
                        """
                        sql_matter_format = sql_matter.format(dr[0])
                        matter_dfs = db.execute_sql(conn, sql_matter_format)
                        if matter_dfs:
                            respose_list = []
                            for matter_df in matter_dfs:
                                response_data = {}
                                response_data["materials_code"] = matter_df[0]
                                response_data["materials_production_code"] = matter_df[1]
                                response_data["matter_code"] = matter_df[2]
                                response_data["matter_count"] = matter_df[3]
                                respose_list.append(response_data)
                            dict_data["response_datas"] = respose_list
                            data_list.append(dict_data)
                        else:
                            dict_data["response_datas"] = []
                            data_list.append(dict_data)
                    page_result = Page(page, page_size, data_list)
                    data = page_result.get_str_json()

                    sql_num = """
                            select count(*) from product_pickmatter where materials_person = '{0}'
                            """
                    sql_num_format = sql_num.format(materials_person)

                    dfs = db.execute_sql(conn, sql_num_format)
                    sql_num_int = dfs[0][0]

                    data_add_int["data"] = data
                    data_add_int["total"] = sql_num_int

                    result = {"code": 0, "message":"操作成功", "data": data_add_int}
                    result = json.dumps(result)

                    return HttpResponse(result)

                else:
                    result = {"code": 0, "message": "操作失败", "data": ""}
                    result = json.dumps(result)

                    return HttpResponse(result)

            elif len(materials_person) == 0 and len(product_plan_code) != 0:
                sql = """
                    select * from product_pickmatter where product_plan_code = '{0}'
                    """
                sql_main = sql.format(product_plan_code)
                drs = db.execute_sql(conn, sql_main)
                if drs:
                    for dr in drs:
                        dict_data = {}
                        dict_data["materials_production_code"] = dr[0]
                        dict_data["materials_person"] = dr[1]
                        dict_data["product_plan_code"] = dr[2]
                        s = dr[3]
                        s1 = s.strftime("%Y-%m-%d %H:%M:%S ")
                        dict_data["material_time"] = s1

                        dict_data["description"] = dr[4]
                        sql_matter = """
                        select * from pick_matter where materials_production_code = '{0}'
                        """
                        sql_matter_format = sql_matter.format(dr[0])
                        matter_dfs = db.execute_sql(conn, sql_matter_format)
                        if matter_dfs:
                            respose_list = []
                            for matter_df in matter_dfs:
                                response_data = {}
                                response_data["materials_code"] = matter_df[0]
                                response_data["materials_production_code"] = matter_df[1]
                                response_data["matter_code"] = matter_df[2]
                                response_data["matter_count"] = matter_df[3]
                                respose_list.append(response_data)
                            dict_data["response_datas"] = respose_list
                            data_list.append(dict_data)
                        else:
                            dict_data["response_datas"] = []
                            data_list.append(dict_data)
                    page_result = Page(page, page_size, data_list)
                    data = page_result.get_str_json()

                    sql_num = """
                            select count(*) from product_pickmatter where product_plan_code = '{0}'
                            """
                    sql_num_format = sql_num.format(product_plan_code)

                    dfs = db.execute_sql(conn, sql_num_format)
                    sql_num_int = dfs[0][0]

                    data_add_int["data"] = data
                    data_add_int["total"] = sql_num_int

                    result = {"code": 0, "message":"操作成功", "data": data_add_int}
                    result = json.dumps(result)

                    return HttpResponse(result)

                else:
                    result = {"code": 0, "message": "操作失败", "data": ""}
                    result = json.dumps(result)

                    return HttpResponse(result)

            elif len(materials_person) != 0 and len(product_plan_code) != 0:
                sql = """
                    select * from product_pickmatter where materials_person = '{0}' and product_plan_code = '{1}'
                    """
                sql_main = sql.format(materials_person, product_plan_code)
                drs = db.execute_sql(conn, sql_main)
                if drs:
                    for dr in drs:
                        dict_data = {}
                        dict_data["materials_production_code"] = dr[0]
                        dict_data["materials_person"] = dr[1]
                        dict_data["product_plan_code"] = dr[2]
                        s = dr[3]
                        s1 = s.strftime("%Y-%m-%d %H:%M:%S ")
                        dict_data["material_time"] = s1
                        dict_data["description"] = dr[4]
                        sql_matter = """
                        select * from pick_matter where materials_production_code = '{0}'
                        """
                        sql_matter_format = sql_matter.format(dr[0])
                        matter_dfs = db.execute_sql(conn, sql_matter_format)
                        if matter_dfs:
                            respose_list = []
                            for matter_df in matter_dfs:
                                response_data = {}
                                response_data["materials_code"] = matter_df[0]
                                response_data["materials_production_code"] = matter_df[1]
                                response_data["matter_code"] = matter_df[2]
                                response_data["matter_count"] = matter_df[3]
                                respose_list.append(response_data)
                            dict_data["response_datas"] = respose_list
                            data_list.append(dict_data)
                        else:
                            dict_data["response_datas"] = []
                            data_list.append(dict_data)
                    page_result = Page(page, page_size, data_list)
                    data = page_result.get_str_json()

                    sql_num = """
                            select count(*) from product_pickmatter 
                            where materials_person = '{0}' and product_plan_code = '{1}'
                            """
                    sql_num_format = sql_num.format(materials_person, product_plan_code)

                    dfs = db.execute_sql(conn, sql_num_format)
                    sql_num_int = dfs[0][0]

                    data_add_int["data"] = data
                    data_add_int["total"] = sql_num_int

                    result = {"code": 0, "message": "操作成功", "data": data_add_int}
                    result = json.dumps(result)

                    return HttpResponse(result)

                else:
                    result = {"code": 0, "message": "操作失败", "data": ""}
                    result = json.dumps(result)

                    return HttpResponse(result)

        except Exception as e:

            print(e)
            result = {"code": 1, "message": "操作失败", "data": e}
            result = json.dumps(result)

            return HttpResponse(result)

    def post(self, request):
        try:

            json_data = request.body
            str_data = json.loads(json_data)

            db = DB()
            product_id = request.session.get("session_projectId")
            conn = db.get_connection(product_id)

            sql_matter = """
                   SELECT max(order_number) FROM pick_matter;
                   """
            matter_type = db.execute_sql(conn, sql_matter)
            if matter_type[0][0] == None:
                matter_num = 0
            else:
                matter_num = matter_type[0][0]

            sql = """
                  SELECT max(order_number) FROM product_pickmatter;
                  """
            product_type = db.execute_sql(conn, sql)
            if product_type[0][0] == None:
                id_num = 1
            else:
                id_num = product_type[0][0] + 1

            materials_production_code = str("Im_Product_Pick_Matter_" + str(id_num))
            materials_person = str_data.get("materials_person")
            product_plan_code = str_data.get("product_plan_code")
            material_time = str_data.get("material_time")
            description = str_data.get("description")
            response_datas = str_data.get("response_datas")
            # materials_person = "小小笑"
            # product_plan_code = "Im_ProductPlan_1"
            # material_time = "2021-07-06"
            # description = "无"
            # response_datas = [{"matter_code": "Im_Matter_10", "matter_count": "10"},
            #                   {"matter_code": "Im_Matter_11", "matter_count": "20"}]

            order_number = id_num

            sql_insert = """
                               insert into product_pickmatter(materials_production_code, materials_person, 
                               product_plan_code,
                               material_time, description, order_number)
                               values('{0}', '{1}', '{2}', '{3}', '{4}', '{5}')
                               """
            sql_insert_format = sql_insert.format(materials_production_code, materials_person,
                                                  product_plan_code, material_time,
                                                  description, order_number)
            drs = db.execute_sql(conn, sql_insert_format)
            for response_data in response_datas:
                # db = DB()
                # conn = db.get_connection("db_common")
                matter_code = response_data.get("matter_code")
                matter_count = response_data.get("matter_count")
                matter_num = matter_num + 1
                materials_code = str("Im_Materials_Pick_" + str(matter_num))
                sql_response = """
                               insert into pick_matter(materials_code, materials_production_code,matter_code, matter_count,
                               order_number)
                               values('{0}', '{1}', '{2}', '{3}', '{4}')
                       """
                sql_response_format = sql_response.format(materials_code, materials_production_code,
                                                          matter_code, matter_count,
                                                          matter_num)
                matter_drs = db.execute_sql(conn, sql_response_format)
            data = {"code": 0, "message": "创建产品详情表成功"}
            logger.info("创建产品详情表成功")
            data = json.dumps(data)

            return HttpResponse(data)
        except Exception as e:
            print(e)
            data = {"code": 1, "message": "创建产品详情表失败"}
            logger.error("创建产品详情表失败")
            data = json.dumps(data)
            return HttpResponse(data)


class PutProductPickMatter(View):

    def get(self, request):
        try:
            db = DB()
            product_id = request.session.get("session_projectId")
            conn = db.get_connection(product_id)
            materials_production_code = request.GET.get("materials_production_code")
            materials_person = request.GET.get("materials_person")
            product_plan_code = request.GET.get("product_plan_code")
            material_time = request.GET.get("material_time")
            description = request.GET.get("description")

            response_datas = request.GET.get("response_datas")
            if response_datas:
                response_datas = eval(response_datas)
            else:
                response_datas = response_datas

            # materials_production_code = 'Im_Product_Pick_Matter_1'
            # materials_person = 'keny'
            # product_plan_code = 'Im_ProductPlan_1'
            # material_time = '2021-07-07'
            # description = '常用品'
            # #
            # response_datas = [{"materials_production_code": "Im_Product_Pick_Matter_1", "matter_code": "Im_Matter_10",
            #                    "matter_count": "33"}]

            # new_check_list = [prodect_code, product_name, rule, product_status, description]
            sql = """
                      update product_pickmatter set 
                      materials_person='{0}',product_plan_code='{1}', material_time ='{2}',
                      description= '{3}' where materials_production_code = '{4}'
                      """
            sql_main = sql.format(materials_person, product_plan_code, material_time, description,
                                  materials_production_code)
            drs = db.execute_sql(conn, sql_main)


            sql_matter_num = """
             SELECT max(order_number) FROM pick_matter
            """
            dras = db.execute_sql(conn, sql_matter_num)

            if dras[0][0] != None:
                sql_num = dras[0][0]
            else:
                sql_num = 0

            for response_data in response_datas:
                # materials_production_code = response_data.get("materials_production_code")
                materials_code = response_data.get("materials_code")
                # materials_production_code = response_data.get("materials_production_code")
                matter_code = response_data.get("matter_code")
                matter_count = response_data.get("matter_count")
                if materials_code:
                    sql = """
                       update pick_matter set materials_production_code = '{0}', 
                       matter_code = '{1}', matter_count ='{2}' where materials_code = '{3}'
                    """
                    sql = sql.format(materials_production_code, matter_code, matter_count, materials_code)
                    db.execute_sql(conn, sql)
                else:
                    sql_num = sql_num + 1

                    materials_code = str("Im_Materials_Pick_" + str(sql_num))

                    sql_response = """
                                          insert into pick_matter(materials_code,materials_production_code, 
                                          matter_code, matter_count, order_number) values('{0}',
                                           '{1}', '{2}', '{3}', '{4}')
                                  """
                    sql_response_format = sql_response.format(materials_code, materials_production_code,
                                                              matter_code, matter_count, sql_num)
                    db.execute_sql(conn, sql_response_format)

                # sql_matter = """
                #    update person_matter set status='已使用' where matter_code = '{0}'
                #  """
                # sql_matter_format = sql_matter.format(matter_code)
                # matters = db.execute_sql(conn, sql_matter_format)
            # sql_matter

            data = {"code": 0, "message": "修改成功"}

            data = json.dumps(data)

            db.close_connection(conn)

            return HttpResponse(data)

        except Exception as e:
            print(e)
            data = {"code": 1, "message": "修改失败"}
            logger.error("修改失败---->%s", e)
            data = json.dumps(data)
            return HttpResponse(data)


class DeleteProductPickMatter(View):

    def get(self, request):
        try:
            db = DB()
            product_id = request.session.get("session_projectId")
            conn = db.get_connection(product_id)

            materials_production_code = request.GET.get("materials_production_code")
            response_datas = request.GET.get("response_datas")
            response_datas = eval(response_datas)
            # materials_production_code = "Im_Product_Pick_Matter_1"
            # response_datas = [{"materials_code": "Im_Materials_Pick_1"}]
            if len(response_datas) != 0:

                for response_data in response_datas:
                    materials_code = dict(response_data).get("materials_code")
                    sql = """
                       delete from pick_matter where materials_code = '{0}'
                       """
                    sql_format = sql.format(materials_code)
                    db.execute_sql(conn, sql_format)
            else:
                sql_matter = """
                                  SELECT * FROM product_pickmatter where materials_production_code = '{0}'
                                  """
                sql_matter_format = sql_matter.format(materials_production_code)
                matter_dfs = db.execute_sql(conn, sql_matter_format)
                for matter_df in matter_dfs:
                    materials_code = matter_df[0]
                    sql_delete = """
                       delete FROM pick_matter where materials_code = '{0}'
                       """
                    sql_delete_format = sql_delete.format(materials_code)
                    db.execute_sql(conn, sql_delete_format)
                sql = """
                       delete from product_pickmatter where materials_production_code = '{0}'
                       """
                sql_main = sql.format(materials_production_code)
                des = db.execute_sql(conn, sql_main)

            data = {"code": 0, "message": "删除成功"}
            logger.info("删除产品列表或者物料表成功")

            data = json.dumps(data)

            return HttpResponse(data)

        except Exception as e:
            print(e)
            data = {"code": 1, "message": "删除失败"}
            data = json.dumps(data)
            logger.error("删除产品列表失败,%s" % e)
            return HttpResponse(data)


class NoPagePersonMatter(View):
    def get(self, request):
        try:
            data_list = []
            data_add_int = {}
            db = DB()
            # conn = db.get_connection("db_common")
            product_id = request.session.get("session_projectId")
            conn = db.get_connection(product_id)
            sql = """
            select pm.matter_code, ml.matter_name, ml.rule, ml.matter_category, 
            pm.matter_count,pm.product_time from person_matter as pm
            left join matter_list as ml on pm.matter_code = ml.bom_matter_code
            """
            drs = db.execute_sql(conn, sql)
            for dr in drs:
                dict_data = {}
                dict_data["matter_code"] = dr[0]
                # dict_data["matter_id"] = dr[1]
                dict_data["matter_name"] = dr[1]
                dict_data["rule"] = dr[2]
                dict_data["matter_category"] = dr[3]
                dict_data["matter_count"] = dr[4]
                s = dr[5]
                if s:
                    s1 = s.strftime("%Y-%m-%d %H:%M:%S ")
                else:
                    s1 = ""
                dict_data["product_time"] = s1
                data_list.append(dict_data)
            sql_num = """
            select count(*) from person_matter
            """
            dfs = db.execute_sql(conn, sql_num)
            sql_num_int = dfs[0][0]

            data_add_int["data"] = data_list
            data_add_int["total"] = sql_num_int

            result = {"code": 0, "message": "调取成功", "data": data_add_int}
            result = json.dumps(result)
            return HttpResponse(result)

        except Exception as e:
            print(e)
            result = {"code": 1, "message": "操作失败", "data": e}
            result = json.dumps(result)
            return HttpResponse(result)


class CreateProcessDeal(View):
    def get(self, request):
        try:
            db = DB()
            product_id = request.session.get("session_projectId")
            conn = db.get_connection(product_id)
            sql = """
                              create table Process_Deal(production_code varchar(128) primary key not null,
                              production_id varchar(128) not null,
                              production_name varchar(128), prodect_code varchar(128), work_id varchar(128),
                              leader_work_id varchar(128), description varchar(128), order_number int)         
                              """
            dr = db.execute_sql(conn, sql)
            data = {"code": 0, "message": "操作成功"}
            # data = json.dumps(data)
        except Exception as e:
            print(e)
            data = {"code": 1, "message": "操作失败"}
        data = json.dumps(data)

        return HttpResponse(data)


class ProcessDeal(View):
    def get(self, request):
        try:
            data_list = []
            data_add_int = {}
            db = DB()
            product_id = request.session.get("session_projectId")
            current_person_id = request.session['session_currentId']
            # work_id = request.session['session_workId']
            conn = db.get_connection(product_id)
            page = int(request.GET.get("page"))
            page_size = int(request.GET.get("page_size"))

            production_name = request.GET.get("production_name")
            # prodect_code = request.GET.get("prodect_code")
            work_id = request.GET.get("work_id")
            # #
            # page = 1
            # page_size = 10
            # production_name = ""
            # prodect_code = ""
            # work_code = ""

            # page = 1
            # page_size = 10
            # prodect_code = "Im_Product_10"
            # plan_name = ""

            if production_name:
                production_name_sql = "and production_name =" + "'"+ production_name+"'"
            else:
                production_name_sql = ""

            if work_id:
                work_id_sql = "and work_id = " + "'" + work_id + "'"
            else:
                work_id_sql = ""

            sql = """
                       select * from  process_deal where 2>1 {0} {1}
                       """
            sql_main = sql.format(production_name_sql, work_id_sql)
            drs = db.execute_sql(conn, sql_main)

            if drs:
                for dr in drs:
                    dict_data = {}
                    dict_data["production_code"] = dr[0]
                    dict_data["production_id"] = dr[1]
                    dict_data["production_name"] = dr[2]
                    dict_data["work_id"] = dr[3]
                    dict_data["leader_work_id"] = dr[4]
                    dict_data["description"] = dr[5]
                    sql_matter = """
                            select * from process_matter_deal where work_id = '{0}'
                             """
                    sql_matter_format = sql_matter.format(dr[3])
                    matter_dfs = db.execute_sql(conn, sql_matter_format)
                    if matter_dfs:
                        respose_list = []
                        for matter_df in matter_dfs:
                            response_data = {}
                            response_data["process_matter_deal_code"] = matter_df[0]
                            response_data["work_id"] = matter_df[1]
                            response_data["matter_code"] = matter_df[2]
                            response_data["install_number"] = matter_df[3]
                            respose_list.append(response_data)
                        dict_data["response_datas"] = respose_list
                        data_list.append(dict_data)
                    else:
                        dict_data["response_datas"] = []
                        data_list.append(dict_data)
                    # data_list.append(dict_data)
                page_result = Page(page, page_size, data_list)
                data = page_result.get_str_json()
                sql_num = """
                        select count(*) from process_deal
                        """
                dfs = db.execute_sql(conn, sql_num)
                sql_num_int = dfs[0][0]
                data_add_int["data"] = data
                data_add_int["total"] = sql_num_int
            else:
                data_add_int["data"] = []
                data_add_int["data"] = 0
            data = {"code":0, "message":"操作成功", "data": data_add_int}

            data = json.dumps(data)

            return HttpResponse(data)


        except Exception as e:
            print(e)
            data = {"code": 1, "message": "操作失败", "data": e}
            data = json.dumps(data)
            return HttpResponse(data)

    def post(self, request):
        try:
            table_list = []
            db = DB()
            product_id = request.session.get("session_projectId")
            current_person_id = request.session['session_currentId']
            # work_id = request.session['session_workId']
            conn = db.get_connection(product_id)
            sql = """
                    SELECT max(order_number) FROM process_deal;
                   """
            works = db.execute_sql(conn, sql)
            if works[0][0] == None:
                id_num = 1
            else:
                id_num = works[0][0] + 1

            production_code = str("Im_Process_" + str(id_num))
            respose_data_json = request.body
            respose_data_dict = json.loads(respose_data_json)

            production_id = respose_data_dict.get("production_id")
            production_name = respose_data_dict.get("production_name")
            # prodect_code = respose_data_dict.get("prodect_code")
            work_id = respose_data_dict.get("work_id")
            leader_work_id = respose_data_dict.get("leader_work_id")
            # code_count = respose_data_dict.get("code_count")
            description = respose_data_dict.get("description")
            response_datas = respose_data_dict.get("response_datas")

            # production_id = "003"
            # production_name = "CO2项目"
            # prodect_code = "Im_Product_9"
            # work_code = "Im_WorkStation_3"
            # leader_production_code = "Im_WorkStation_2"
            # description = "sss"

            sql_insert = """          
                                     insert into process_deal(production_code, production_id, production_name,
                                      work_id, leader_work_id, description, order_number)
                                      values('{0}', '{1}', '{2}', '{3}', '{4}', '{5}', {6})   
                               """
            sql_insert_format = sql_insert.format(production_code, production_id, production_name,
                                                  work_id, leader_work_id, description, id_num)
            drs = db.execute_sql(conn, sql_insert_format)
            sql_table = """
            show tables
            """
            drs = db.execute_sql(conn, sql_table)
            for dr in drs:
                table_list.append(dr[0])
            if "process_matter_deal" not in table_list:
                sql_create_table = """
                create table process_matter_deal(process_matter_deal_code varchar(255) primary key not null,
                              work_id varchar(255) not null,
                              matter_code varchar(255),
                               install_number int, order_number int)        
                """
                db.execute_sql(conn, sql_create_table)
            else:
                pass
            if response_datas:

                for response_data in response_datas:
                    process_matter_deal_code = response_data.get("process_matter_deal_code")
                    matter_code = response_data.get("matter_code")
                    install_number = response_data.get("matter_usage")
                    if process_matter_deal_code:
                        sql_update = """
                        update process_matter_deal set matter_code = '{0}', 
                        install_number = '{1}',
                        work_id = '{2}',
                        where process_matter_deal_code = '{3}'
                        """
                        sql_update = sql_update.format(matter_code, install_number, work_id,
                                                       process_matter_deal_code)
                        drs = db.execute_sql(conn, sql_update)
                    else:

                        sql_matter_num = """
                                        SELECT max(order_number) FROM process_matter_deal
                                       """
                        dras = db.execute_sql(conn, sql_matter_num)
                        if dras[0][0] == None:
                            id_num = 1
                        else:
                            id_num = dras[0][0] + 1
                        process_matter_deal_code = str("Im_process_matter_deal_" + str(id_num))
                        sql_insert = """
                        insert into process_matter_deal(process_matter_deal_code, work_id, matter_code,
                                          install_number, order_number)
                                          values('{0}', '{1}', '{2}', '{3}', '{4}')   
                        """
                        sql_insert = sql_insert.format(process_matter_deal_code, work_id,
                                                       matter_code, install_number, id_num)
                        drs = db.execute_sql(conn, sql_insert)
            else:
                pass

            data = {"code": 0, "message": "创建工序信息表成功"}

            data = json.dumps(data)

            return HttpResponse(data)
        except Exception as e:
            print(e)

            data = {"code": 1, "message": "创建工序信息表失败"}
            data = json.dumps(data)

            return HttpResponse(data)


class PutProcessDeal(View):
    def get(self, request):
        try:
            db = DB()
            product_id = request.session.get("session_projectId")
            conn = db.get_connection(product_id)

            production_code = request.GET.get("production_code")
            production_id = request.GET.get("production_id")
            production_name = request.GET.get("production_name")
            prodect_code = request.GET.get("prodect_code")
            work_id = request.GET.get("work_id")
            leader_work_id = request.GET.get("leader_work_id")
            # code_count = request.GET.get("code_count")
            description = request.GET.get("description")

            response_datas = request.GET.get("response_datas")
            if response_datas:
                response_datas = eval(response_datas)
            for response_data in response_datas:
                # response_data = dict(response_data)
                process_matter_deal_code = response_data.get("process_matter_deal_code")
                install_number = response_data.get("install_number")
                sql = """
                update process_matter_deal set install_number = '{0}' where process_matter_deal_code = '{1}'
                """
                sql = sql.format(install_number, process_matter_deal_code)
                db.execute_sql(conn, sql)

            # production_code = "Im_Process_1"
            # production_id = "001"
            # production_name = "jjj"
            # prodect_code = "Im_Product_9"
            # work_code = "Im_WorkStation_2"
            # leader_production_code = "Im_WorkStation_1"
            # description = "不测试"

            sql = """
                            update process_deal set 
                            production_id='{0}', production_name ='{1}',
                            work_id = '{2}', leader_work_id = '{3}', description = '{4}' 
                            where production_code = '{5}'
                            """
            sql_main = sql.format(production_id, production_name, work_id,
                                  leader_work_id, description, production_code)
            drs = db.execute_sql(conn, sql_main)
            data = {"code": 0, "message": "操作成功", "data": ""}
            data = json.dumps(data)

            return HttpResponse(data)

        except Exception as e:
            print(e)
            data = {"code": 0, "message": "操作失败", "data":e}
            data = json.dumps(data)
            return HttpResponse(data)


class DeleteProcessDeal(View):

    def get(self, request):
        try:
            db = DB()
            product_id = request.session.get("session_projectId")
            work_id = request.session.get("session_workId")
            conn = db.get_connection(product_id)

            # production_code = request.GET.get("production_code")

            response_datas = request.GET.get("response_datas")

            if len(response_datas) != 0:

                for response_data in response_datas:
                    bom_matter_code = dict(response_data).get("bom_matter_code")
                    sql = """
                       delete from matter_list where bom_matter_code = '{0}'
                       """
                    sql_format = sql.format(bom_matter_code)
                    db.execute_sql(conn, sql_format)

            else:
                process_list = []
                sql_matter = """
                              SELECT process_matter_deal_code FROM process_matter_deal where work_id = '{0}'
                              """
                sql_matter_format = sql_matter.format(work_id)
                matter_dfs = db.execute_sql(conn, sql_matter_format)
                for matter_df in matter_dfs:
                    process_list.append(matter_df[0])
                for process_lis in process_list:
                    sql_delete = """
                    
                    """



            # sql = """
            #           delete from process_deal where production_code = '{0}'
            #           """
            # sql_main = sql.format(production_code)
            # des = db.execute_sql(conn, sql_main)

            data = {"code": 0, "message": "操作成功", "data": ""}
            data = json.dumps(data)

            return HttpResponse(data)

        except Exception as e:
            print(e)
            data = {"code":1, "message":"操作失败", "data":e}
            data = json.dumps(data)

            return HttpResponse(data)


class ProductPlanCodeName(View):
    def get(self, request):
        try:
            data_list = []
            db = DB()
            product_id = request.session.get("session_projectId")
            conn = db.get_connection(product_id)
            sql = """
            SELECT product_plan_code, plan_name FROM product_plandeal
            """
            drs = db.execute_sql(conn, sql)
            for dr in drs:
                data_dict = {}
                data_dict["product_plan_code"] = dr[0]
                data_dict["product_plan_name"] = dr[1]
                data_list.append(data_dict)
            data = {"code":0, "message":"操作成功", "data": data_list}
            data = json.dumps(data)

            return HttpResponse(data)
        except Exception as e:
            print(e)
            data = {"code": 1, "message":"操作失败", "data": e}
            data = json.dumps(data)

            return HttpResponse(data)


class PersonCodeName(View):
    def get(self, request):
        try:
            data_list = []
            db = DB()
            product_id = request.session.get("session_projectId")
            conn = db.get_connection(product_id)
            sql = """
                       SELECT user_code, user_name FROM person
                       """
            drs = db.execute_sql(conn, sql)
            for dr in drs:
                data_dict = {}
                data_dict["user_code"] = dr[0]
                data_dict["user_name"] = dr[1]
                data_list.append(data_dict)
            data = {"code": 0, "message": "操作成功", "data": data_list}
            data = json.dumps(data)

            return HttpResponse(data)

        except Exception as e:
            print(e)
            data = {"code":1, "message":"操作失败", "data":e}
            data = json.dumps(data)

            return HttpResponse(data)


class WorkCodeName(View):
    def get(self, request):
        try:
            data_list = []
            db = DB()
            # project_id = request.GET.get("project_id")
            product_id = request.session.get("session_projectId")
            conn = db.get_connection(product_id)
            # conn = db.get_connection(project_id)
            sql = """
                       SELECT work_code, work_id, work_name FROM work_station
                       """
            drs = db.execute_sql(conn, sql)
            for dr in drs:
                data_dict = {}
                data_dict["work_code"] = dr[0]
                data_dict["work_id"] = dr[1]
                data_dict["work_name"] = dr[2]
                data_list.append(data_dict)
            data = {"code": 0, "message": "操作成功", "data": data_list}
            data = json.dumps(data)

            return HttpResponse(data)

        except Exception as e:
            print(e)
            data = {"code": 1, "message": "操作失败", "data":e}
            data = json.dumps(data)

            return HttpResponse(data)


class CreateCheckProductDeal(View):
    def get(self, request):
        try:
            db = DB()
            conn = db.get_connection("db_common")
            sql = """
                                     create table Check_ProductDeal(check_code varchar(128) primary key not null,
                                     prodect_code varchar(128),
                                     work_code varchar(128) not null,
                                     production_code varchar(128), check_method varchar(128), order_number int)         
                                     """
            dr = db.execute_sql(conn, sql)
            data = {"code": 0, "message": "操作成功"}

        except Exception as e:
            print(e)
            data = {"code": 1, "message": "操作失败"}
        data = json.dumps(data)

        return HttpResponse(data)


class CreateProductParameter(View):
    def get(self, request):
        try:
            db = DB()
            conn = db.get_connection("db_common")
            sql = """
                                     create table Product_Parameter(test_code varchar(128) primary key not null,
                                     check_code varchar(128), test_parameter varchar(128),
                                     test_parameter_count varchar(128),
                                     test_status varchar(128), order_number int)         
                                     """
            dr = db.execute_sql(conn, sql)
            data = {"code": 0, "message": "操作成功"}

        except Exception as e:
            print(e)
            data = {"code": 1, "message": "操作失败"}
        data = json.dumps(data)

        return HttpResponse(data)


class CheckProductDeal(View):
    def get(self, request):
        try:
            data_list = []
            data_add_int = {}
            prodect_code = request.GET.get("prodect_code")
            work_code = request.GET.get("work_code")
            production_code = request.GET.get("production_code")
            check_method = request.GET.get("check_method")

            page = int(request.GET.get("page"))
            page_size = int(request.GET.get("page_size"))

            # prodect_code = "Im_Product_10"
            # work_code = ""
            # production_code = ""
            # check_method = ""
            #
            # page = 1
            # page_size = 10

            db = DB()
            product_id = request.session.get("session_projectId")
            conn = db.get_connection(product_id)

            if prodect_code:
                prodect_code_sql = " and prodect_code =" + "'" + prodect_code + "'"
            else:
                prodect_code_sql = ""
            if work_code:
                work_code_sql = " and work_code = " + "'" + work_code + "'"
            else:
                work_code_sql = ""
            if production_code:
                production_code_sql = " and production_code = " + "'" + production_code+"'"
            else:
                production_code_sql = ""
            if check_method:
                check_method_sql = " and check_method = " + "'"+check_method+"'"
            else:
                check_method_sql = ""

            sql = """
             select * from check_productdeal where 2 > 1 {0} {1} {2} {3}
            """
            sql_main = sql.format(prodect_code_sql, work_code_sql, production_code, check_method_sql)

            # sql_main = sql.format(matter_id_sql, matter_name_sql, matter_category_sql, status_sql)
            # print(sql_main)
            drs = db.execute_sql(conn, sql_main)
            for dr in drs:
                dict_data = {}
                dict_data["check_code"] = dr[0]
                dict_data["prodect_code"] = dr[1]
                dict_data["work_code"] = dr[2]
                dict_data["production_code"] = dr[3]
                dict_data["check_method"] = dr[4]
                # data_list.append(dict_data)

                sql_matter = """
                            select * from product_parameter where check_code = '{0}'
                            """
                sql_matter_format = sql_matter.format(dr[0])
                matter_dfs = db.execute_sql(conn, sql_matter_format)
                if matter_dfs:
                    respose_list = []
                    for matter_df in matter_dfs:
                        response_data = {}
                        response_data["test_code"] = matter_df[0]
                        response_data["check_code"] = matter_df[1]
                        response_data["test_parameter"] = matter_df[2]
                        response_data["test_parameter_count"] = matter_df[3]
                        response_data["test_status"] = matter_df[4]
                        respose_list.append(response_data)
                    dict_data["response_datas"] = respose_list
                    data_list.append(dict_data)
                else:
                    dict_data["response_datas"] = []
                    data_list.append(dict_data)

            page_result = Page(page, page_size, data_list)
            data = page_result.get_str_json()

            sql_num = """
                                        select count(*) from check_productdeal 
                                        where 2 > 1 {0} {1} {2} {3}
                                          """
            sql_format = sql_num.format(prodect_code_sql, work_code_sql, production_code, check_method_sql)
            dfs = db.execute_sql(conn, sql_format)
            sql_num_int = dfs[0][0]

            data_add_int["data"] = data
            data_add_int["total"] = sql_num_int

            result = {"code": 0, "message": "操作成功", "data": data_add_int}
            result = json.dumps(result)

            # print(type(data))

            return HttpResponse(result)

        except Exception as e:
            logger.error("调取check_productdeal数据库有错误", e)
            result = {"code": 1, "message": "调取失败", "data": ""}
            result = json.dumps(result)
            print(e)
            return HttpResponse(result)

    def post(self, request):
        db = DB()
        product_id = request.session.get("session_projectId")
        conn = db.get_connection(product_id)
        # print("---->", product_id)
        try:
            json_data = request.body
            str_data = json.loads(json_data)
            sql_matter = """
                          SELECT max(order_number) FROM check_productdeal;
                          """
            checkproduct = db.execute_sql(conn, sql_matter)
            # print("--->>>", checkproduct)
            if checkproduct[0][0] == None:
                matter_num = 1
            else:
                matter_num = checkproduct[0][0] + 1
            sql = """
                 SELECT max(order_number) FROM product_parameter;
                 """
            product_parameter = db.execute_sql(conn, sql)
            if product_parameter[0][0] == None:
                id_num = 0
            else:
                id_num = product_parameter[0][0]

            check_code = str("Im_Check_Product_" + str(matter_num))
            prodect_code = str_data.get("prodect_code")
            work_code = str_data.get("work_code")
            production_code = str_data.get("production_code")
            check_method = str_data.get("check_method")
            response_datas = str_data.get("response_datas")
            # check_code = str("Im_Check_Product_" + str(matter_num))
            # prodect_code = "Im_Product_9"
            # work_code = "Im_WorkStation_3"
            # production_code = "Im_Process_2"
            # check_method = "人工"
            # response_datas = [{"test_parameter": "yuan", "test_parameter_count": "chao", "test_status": "正常"},
            #                   {"test_parameter": "方形", "test_parameter_count": "正", "test_status": "正常"}]

            sql_insert = """
                                      insert into check_productdeal(check_code, prodect_code, 
                                      work_code,
                                      production_code, check_method, order_number)
                                      values('{0}', '{1}', '{2}', '{3}', '{4}', '{5}')
                                      """
            sql_insert_format = sql_insert.format(check_code, prodect_code,
                                                  work_code, production_code,
                                                  check_method, matter_num)
            drs = db.execute_sql(conn, sql_insert_format)
            for response_data in response_datas:
                # db = DB()
                # conn = db.get_connection("db_common")
                test_parameter = response_data.get("test_parameter")
                test_parameter_count = response_data.get("test_parameter_count")
                test_status = response_data.get("test_status")
                id_num = id_num + 1
                test_code = str("Im_Test_" + str(id_num))
                sql_response = """
                                      insert into product_parameter(test_code, check_code, 
                                      test_parameter,test_parameter_count, test_status,
                                      order_number)
                                      values('{0}', '{1}', '{2}', '{3}', '{4}', '{5}')
                              """
                sql_response_format = sql_response.format(test_code, check_code, test_parameter,
                                                          test_parameter_count, test_status,
                                                          id_num)
                matter_drs = db.execute_sql(conn, sql_response_format)

            data = {"code": 0, "message": "创建检验详情表成功"}
            logger.info("创建检验详情表成功")
            data = json.dumps(data)

            return HttpResponse(data)
        except Exception as e:
            print(e)
            data = {"code": 1, "message": "创建检验详情表失败"}
            logger.error("创建检验详情表失败")
            data = json.dumps(data)
            return HttpResponse(data)


class PutCheckProductDeal(View):
    def get(self, request):
        try:
            db = DB()
            product_id = request.session.get("session_projectId")
            conn = db.get_connection(product_id)
            check_code = request.GET.get("check_code")
            prodect_code = request.GET.get("prodect_code")
            work_code = request.GET.get("work_code")
            production_code = request.GET.get("production_code")
            check_method = request.GET.get("check_method")

            response_datas = request.GET.get("response_datas")

            # check_code = "Im_Check_Product_1"
            # prodect_code = "Im_Product_10"
            # work_code = "Im_WorkStation_2"
            # production_code = "Im_Process_1"
            # check_method = "机器"
            #
            # response_datas = [{"test_code": "Im_Test_1", "test_parameter":"buyuan",
            #                    "test_parameter_count": "hhhh", "test_status": "正常"},
            #                   {"test_parameter": "cankaozhi",
            #                    "test_parameter_count": "sss", "test_status": "暂定"}]
            #
            if response_datas:
                response_datas = eval(response_datas)
            else:
                response_datas = response_datas

            sql = """
                   update check_productdeal set 
                   prodect_code='{0}',work_code='{1}', production_code ='{2}'
                   ,check_method = '{3}' where check_code = '{4}'
                   """
            sql_main = sql.format(prodect_code, work_code, production_code, check_method, check_code)
            drs = db.execute_sql(conn, sql_main)

            for response_data in response_datas:
                test_code = response_data.get("test_code")
                if test_code:
                    sql_delete = """
                     delete FROM product_parameter where test_code = '{0}'
                    """
                    sql_delete_format = sql_delete.format(test_code)
                    db.execute_sql(conn, sql_delete_format)

            sql_after = """
                        SELECT max(order_number) FROM product_parameter
                        """
            num = db.execute_sql(conn, sql_after)
            if num[0][0]:
                sql_num = num[0][0]
            else:
                sql_num = 0

            for response_data in response_datas:
                # db = DB()
                # conn = db.get_connection("db_common")
                # check_code = response_data.get("check_code")
                test_parameter = response_data.get("test_parameter")
                test_parameter_count = response_data.get("test_parameter_count")
                test_status = response_data.get("test_status")
                sql_num = sql_num + 1
                test_code = str("Im_Test_" + str(sql_num))
                sql_response = """
                                    insert into product_parameter(test_code,check_code, test_parameter, test_parameter_count,
                                    test_status,order_number)
                                    values('{0}', '{1}', '{2}', '{3}', '{4}', '{5}')
                            """
                sql_response_format = sql_response.format(test_code, check_code, test_parameter, test_parameter_count,
                                                          test_status, sql_num)
                matter_drs = db.execute_sql(conn, sql_response_format)
            data = {"code": 0, "message": "修改成功"}

            data = json.dumps(data)

            db.close_connection(conn)

            return HttpResponse(data)

        except Exception as e:
            print(e)
            data = {"code": 1, "message": "修改失败"}
            logger.error("修改失败---->%s", e)
            data = json.dumps(data)
            return HttpResponse(data)


class DeleteCheckProductDeal(View):

    def get(self, request):
        try:
            db = DB()
            product_id = request.session.get("session_projectId")
            conn = db.get_connection(product_id)

            check_code = request.GET.get("check_code")
            response_datas = request.GET.get("response_datas")
            response_datas = eval(response_datas)
            # materials_production_code = "Im_Product_Pick_Matter_1"
            # response_datas = [{"materials_code": "Im_Materials_Pick_1"}]
            if len(response_datas) != 0:

                for response_data in response_datas:
                    test_code = dict(response_data).get("test_code")
                    sql = """
                              delete from product_parameter where test_code = '{0}'
                              """
                    sql_format = sql.format(test_code)
                    db.execute_sql(conn, sql_format)
            else:
                sql_matter = """
                                         SELECT * FROM check_productdeal where check_code = '{0}'
                                         """
                sql_matter_format = sql_matter.format(check_code)
                matter_dfs = db.execute_sql(conn, sql_matter_format)
                for matter_df in matter_dfs:
                    test_code = matter_df[0]
                    sql_delete = """
                              delete FROM product_parameter where test_code = '{0}'
                              """
                    sql_delete_format = sql_delete.format(test_code)
                    db.execute_sql(conn, sql_delete_format)
                sql = """
                              delete from check_productdeal where check_code = '{0}'
                              """
                sql_main = sql.format(check_code)
                des = db.execute_sql(conn, sql_main)

            data = {"code": 0, "message": "删除成功"}
            logger.info("删除产品列表或者物料表成功")

            data = json.dumps(data)

            return HttpResponse(data)

        except Exception as e:
            print(e)
            data = {"code": 1, "message": "删除失败"}
            data = json.dumps(data)
            logger.error("删除产品列表失败,%s" % e)
            return HttpResponse(data)


class CreateProductTransitInfo(View):

    def get(self, request):
        try:
            db = DB()
            conn = db.get_connection("db_common")
            sql = """
                                     create table ProductTransitInfo(product_transit_code varchar(128) primary key not null,
                                     matter_code varchar(128), user_code varchar(128),
                                     work_code varchar(128),
                                     test_result varchar(128), 
                                     enter_time datetime,
                                     out_time datetime,
                                     product_plan_code varchar(128),
                                     end_product_code varchar(128),
                                     product_code varchar(128),                                     
                                     order_number int)         
                                     """
            dr = db.execute_sql(conn, sql)
            data = {"code": 0, "message": "操作成功"}

        except Exception as e:
            print(e)
            data = {"code": 1, "message": "操作失败"}
        data = json.dumps(data)

        return HttpResponse(data)


class ProductTransitInfo(View):
    def get(self, request):
        try:
            data_list = []
            data_add_int = {}
            db = DB()
            product_id = request.session.get("session_projectId")
            session_work_id = request.session.get("session_workId")
            conn = db.get_connection(product_id)
            sql_work_code = """
                       SELECT work_code FROM work_station where work_id = '{0}'
                       """
            sql_work_code_main = sql_work_code.format(session_work_id)
            drss = db.execute_sql(conn, sql_work_code_main)
            work_code = drss[0][0]

            page = int(request.GET.get("page"))
            page_size = int(request.GET.get("page_size"))

            matter_code = request.GET.get("matter_code")
            finished_product_code = request.GET.get("finished_product_code")
            matter_id = request.GET.get("matter_id")
            user_code = request.GET.get("user_code")
            description = request.GET.get("description")
            # work_code = request.GET.get("work_code")
            test_result = request.GET.get("test_result")
            enter_time = request.GET.get("enter_time")
            out_time = request.GET.get("out_time")
            product_plan_code = request.GET.get("product_plan_code")
            product_code = request.GET.get("product_code")

            # page = 1
            # page_size = 10
            #
            # matter_code = "Im_Matter_2"
            # user_code = ""
            # work_code = ""
            # test_result = ""
            # enter_time = ""
            # out_time = ""
            # product_plan_code = ""
            # product_code = ""

            if matter_code:
                matter_code_sql = " and matter_code =" + "'" + matter_code + "'"
            else:
                matter_code_sql = ""
            if user_code:
                user_code_sql = " and user_code = " + "'" + user_code + "'"
            else:
                user_code_sql = ""
            if work_code:
                work_code_sql = " and work_code = " + "'" + work_code+"'"
            else:
                work_code_sql = ""
            if test_result:
                test_result_sql = " and test_result = " + "'"+test_result+"'"
            else:
                test_result_sql = ""
            # if enter_time:
            #     enter_time_sql = " and enter_time = " + "'"+enter_time+"'"
            # else:
            #     enter_time_sql = ""
            if out_time:
                out_time_sql = " and out_time = " + "'"+out_time+"'"
            else:
                out_time_sql = ""
            if product_plan_code:
                product_plan_code_sql = " and product_plan_code = " + "'"+product_plan_code+"'"
            else:
                product_plan_code_sql = ""
            if product_code:
                product_code_sql = " and product_code = " + "'" + product_code + "'"
            else:
                product_code_sql = ""

            if finished_product_code:
                finished_product_code_sql = " and finished_product_code = " + "'" + finished_product_code + "'"
            else:
                finished_product_code_sql = ""
            select_table = str("product_transit_") + str(session_work_id)

            sql = """
             select * from {0} where 2 > 1 {1} {2} {3} {4} {5} {6} {7} {8} 
            """

            sql_main = sql.format(select_table, matter_code_sql, finished_product_code_sql, user_code_sql,
                                  work_code_sql, test_result_sql,
                                  out_time_sql,
                                  product_plan_code_sql, product_code_sql)
            drs = db.execute_sql(conn, sql_main)

            if drs:
                for dr in drs:
                    dict_data = {}
                    dict_data["product_transit_code"] = dr[0]
                    dict_data["matter_code"] = dr[1]
                    dict_data["matter_id"] = dr[2]
                    dict_data["finished_product_code"] = dr[3]
                    dict_data["user_code"] = dr[4]
                    dict_data["work_code"] = dr[5]
                    dict_data["test_result"] = dr[6]
                    dict_data["description"] = dr[7]
                    if dr[8]:
                        dp = dr[8]
                        dp = dp.strftime("%Y-%m-%d %H:%M:%S ")
                        dict_data["enter_time"] = dp
                    else:
                        dict_data["enter_time"] = ""
                    ds = dr[9]
                    sq = ds.strftime("%Y-%m-%d %H:%M:%S ")
                    dict_data["out_time"] = sq
                    dict_data["product_plan_code"] = dr[10]
                    dict_data["end_product_code"] = dr[11]
                    dict_data["product_code"] = dr[12]
                    data_list.append(dict_data)

                page_result = Page(page, page_size, data_list)
                data = page_result.get_str_json()
                sql_num = """
                           select count(*) from {0} where 2 > 1 {1} {2} {3} {4} {5} {6} {7} 
                           """
                sql_num_format = sql_num.format(select_table, matter_code_sql, user_code_sql, work_code_sql,
                                                test_result_sql,
                                                 out_time_sql, product_plan_code_sql,
                                                product_code_sql)
                dfs = db.execute_sql(conn, sql_num_format)

                sql_num_int = dfs[0][0]

                data_add_int["data"] = data
                data_add_int["total"] = sql_num_int

                result = {"code": 0, "message": "调取成功", "data": data_add_int}
                result = json.dumps(result)
                return HttpResponse(result)
            else:
                data_add_int["data"] = []
                data_add_int["total"] = 0
                result = {"code": 0, "message": "无数据", "data": data_add_int}
                result = json.dumps(result)
                return HttpResponse(result)
        except Exception as e:
            print(e)
            data = {"code": 1, "message": "操作失败", "data": e}
            data = json.dumps(data)

            return HttpResponse(data)

    def post(self, request):

        try:
            db = DB()
            product_id = request.session.get("session_projectId")
            str_data = request.body
            json_data = json.loads(str_data)
            session_work_id = request.session.get("session_workId")
            user_code = request.session.get("session_currentId")

            conn = db.get_connection(product_id)
            response_datas = json_data.get("response_datas")
            matter_code_list = []
            matter_id_list = []
            for response_data in response_datas:
                matter_code_list.append(dict(response_data).get("matter_code"))
                matter_id_list.append(dict(response_data).get("matter_id"))
            matter_code = matter_code_list
            matter_id = matter_id_list
            finished_product_code = json_data.get("finished_product_code")
            test_result = json_data.get("test_result")
            description = json_data.get("description")

            out_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S ")
            print("--------------------------------->", out_time)
            product_plan_code = json_data.get("product_plan_code")
            product_code = json_data.get("product_code")

            if test_result == "不合格":
                tables_list = []

                un_pro_table = str("unqualified_product_") + str(session_work_id)

                sql_select_db = """
                show tables
                """
                drs = db.execute_sql(conn, sql_select_db)
                for dr in drs:
                    tables_list.append(dr[0])
                if un_pro_table not in tables_list:
                    sql_create_unqualified = """
                             create table {0}(unqualified_product_code varchar(255) primary key not null,
                              product_plan_code varchar(255), finished_product_code varchar(255), 
                              matter_code varchar(255), matter_id varchar(255),description varchar(255),
                              leader_work_id varchar(255), later_work_id varchar(255), solve_method varchar(255),
                              solve_result varchar(255), order_number int)
                                    """
                    sql_create_unqualified = sql_create_unqualified.format(un_pro_table)
                    db.execute_sql(conn, sql_create_unqualified)
                else:
                    pass
                sql_unqualified_product = """
                                         SELECT max(order_number) FROM {0};
                                         """
                sql_unqualified_product = sql_unqualified_product.format(un_pro_table)
                unqualified_product_nums = db.execute_sql(conn, sql_unqualified_product)
                if unqualified_product_nums[0][0]:
                    matter_num = unqualified_product_nums[0][0]
                else:
                    matter_num = 0

                s = 0

                for matter_code_one in matter_code:
                    matter_num = matter_num + 1
                    matter_id_one = matter_id_list[s]
                    unqualified_product_code = str("Im_Unqualified_Product_" + str(matter_num))
                    sql_insert = """
                        insert into {0}(unqualified_product_code, product_plan_code, matter_code, matter_id, 
                        finished_product_code,
                        description, order_number)
                                        values('{1}', '{2}', '{3}', '{4}', '{5}', '{6}', '{7}')
                    """
                    sql_insert_main = sql_insert.format(un_pro_table, unqualified_product_code,
                                                        product_plan_code, matter_code_one, matter_id_one,
                                                        finished_product_code, description, matter_num)
                    db.execute_sql(conn, sql_insert_main)
                    s += 1

            # matter_code = "test"
            # finished_product_code = "asd"
            # test_result = "合格"
            # out_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S ")
            # product_plan_code = "Im_ProductPlan_1"
            # product_code = ""

            sql_work_code = """
            SELECT work_code FROM work_station where work_id = '{0}'
            """
            sql_work_code_main = sql_work_code.format(session_work_id)
            drss = db.execute_sql(conn, sql_work_code_main)
            work_code = drss[0][0]

            select_table = str("product_transit_") + str(session_work_id)

            dater = datetime.datetime.now().strftime("%Y%m%d")
            sql_producttransit = """
                                      SELECT max(order_number) FROM {0};
                                      """
            sql_producttransit_main = sql_producttransit.format(select_table)
            producttransit = db.execute_sql(conn, sql_producttransit_main)
            if producttransit[0][0] == None:
                matter_num = 0
            else:
                matter_num = producttransit[0][0]
            # end_product_code = product_id + "_" + dater + "_" + str(matter_num + 1)
            s = 0
            for matter_code_one in matter_code:
                matter_num = matter_num + 1
                matter_id_one = matter_id_list[s]
                product_transit_code = str("Im_Product_Transit_" + str(matter_num))
                sql_insert = """
                                            insert into {0}(product_transit_code, matter_code, matter_id,
                                             finished_product_code, user_code,
                                              work_code, test_result, description, out_time, product_plan_code, 
                                              end_product_code, product_code,
                                              order_number)
                                              values('{1}', '{2}', '{3}', '{4}', '{5}', '{6}','{7}', 
                                              '{8}', '{9}', '{10}', '{11}', '{12}','{13}')
                                            """
                sql_insert_main = sql_insert.format(select_table, product_transit_code, matter_code_one, matter_id_one,
                                                    finished_product_code, user_code, work_code,
                                                    test_result, description, out_time,
                                                    product_plan_code, matter_id_one, product_code, matter_num)
                drs = db.execute_sql(conn, sql_insert_main)
                s+=1

            data = {"code": 0, "message": "操作成功", "data": []}
            data = json.dumps(data)

            return HttpResponse(data)

        except Exception as e:
            print(e)
            data = {"code": 1, "message": "操作失败", "data": e}
            data = json.dumps(data)
            return HttpResponse(data)


class MatterNameCode(View):
    def get(self, request):
        try:
            data_list = []

            db = DB()
            product_id = request.session.get("session_projectId")
            conn = db.get_connection(product_id)
            sql = """
             SELECT pm.matter_code, ml.matter_name FROM person_matter as pm left join matter_list as ml
              on pm.matter_code = ml.bom_matter_code
            """
            drs = db.execute_sql(conn, sql)
            for dr in drs:
                data_dict = {}
                data_dict["matter_code"] = dr[0]
                data_dict["matter_name"] = dr[1]
                data_list.append(data_dict)

            data = {"code": 0, "message": "操作成功", "data": data_list}
            data = json.dumps(data)

            return HttpResponse(data)
        except Exception as e:
            print(e)
            data = {"code": 1, "message": "操作失败", "data": e}
            data = json.dumps(data)

            return HttpResponse(data)


class ProcessNameCode(View):
    def get(self, request):
        try:
            data_list = []
            db = DB()
            product_id = request.session.get("session_projectId")
            conn = db.get_connection(product_id)
            sql = """
             SELECT production_code, production_name FROM process_deal
            """
            drs = db.execute_sql(conn, sql)
            for dr in drs:
                data_dict = {}
                data_dict["production_code"] = dr[0]
                data_dict["production_name"] = dr[1]
                data_list.append(data_dict)

            data = {"code": 0, "message": "操作成功", "data": data_list}
            data = json.dumps(data)

            return HttpResponse(data)
        except Exception as e:
            print(e)
            data = {"code": 1, "message": "操作失败", "data": e}
            data = json.dumps(data)

            return HttpResponse(data)


class CurrentUserInfo(View):
    def get(self, request):
        try:
            dict_data = {}
            product_id = request.session.get("session_projectId")
            work_id = request.session.get("session_workId")
            user_code = request.session.get("session_currentId")
            work_type = request.session.get("session_workType")
            # current_user_code = "Im_User_5"
            db = DB()

            conn_num = db.get_connection(product_id)

            print(product_id, work_id, user_code, work_type)


            sql_num = """
             SELECT pick_number FROM pick_box where work_id = '{0}'
            """

            sql_num = sql_num.format(work_id)
            drs = db.execute_sql(conn_num, sql_num)

            if drs:
                pick_number = drs[0][0]
            else:
                pick_number = 0
            print("-->",pick_number)
            if user_code == "Im_user_1":
                conn = db.get_connection("db_common")
                sql = """
                        select * from person_manage where user_code = '{0}'
                     """
            else:
                conn = db.get_connection(product_id)
                sql = """
                   select * from person where user_code = '{0}'
                   """
            sql_main = sql.format(user_code)
            drs = db.execute_sql(conn, sql_main)
            print("------>>>", drs)

            for dr in drs:
                dict_data["user_code"] = dr[0]
                dict_data["user_id"] = dr[1]
                dict_data["user_name"] = dr[2]
                dict_data["user_password"] = dr[3]
                dict_data["user_authority"] = dr[4]
                dict_data["status"] = dr[5]
                dict_data["product_id"] = product_id
                dict_data["work_type"] = work_type
                dict_data["pick_number"] = pick_number
                dict_data["work_id"] = work_id
            data = {"code": 0, "message": "success", "data": dict_data}
            data = json.dumps(data)
            print(data)
            return HttpResponse(data)
        except Exception as e:
            print(e)
            data = {"code": 1, "message": "操作失败", "data":e}
            data = json.dumps(data)

            return HttpResponse(data)


class ProjectSearchWorkcode(View):
    def get(self, request):
        try:
            data_list = []
            product_id = request.GET.get("product_id")
            db = DB()
            conn = db.get_connection(product_id)
            sql = """
            select work_id, work_name from work_station
            """
            drs = db.execute_sql(conn, sql)
            for dr in drs:
                data_dict = {}
                data_dict["work_id"] = dr[0]
                data_dict["work_name"] = dr[1]
                data_list.append(data_dict)
            data = {"code": 0, "message": "操作成功", "data": data_list}
            data = json.dumps(data)

            return HttpResponse(data)

        except Exception as e:
            data = {"code": 1, "message": "操作失败", "data": e}
            data = json.dumps(data)
            return HttpResponse(data)


class GetProductId(View):
    def get(self, request):
        try:
            product_id_list = []

            db = DB()
            conn = db.get_connection("db_common")
            sql_product = """
                       select product_id, product_name from productlist
                       """
            dfs = db.execute_sql(conn, sql_product)
            for df in dfs:
                product_id_dict = {}
                product_id_dict["product_id"] = df[0]
                product_id_dict["product_name"] = df[1]
                product_id_list.append(product_id_dict)

            data = {"code": 0, "message": "操作成功", "data": product_id_list}
            data = json.dumps(data)

            return HttpResponse(data)
        except Exception as e:
            print(e)
            data = {"code": 1, "message": "操作失败", "data": e}
            data = json.dumps(data)

            return HttpResponse(data)


class UnqualifiedProduct(View):
    def get(self, request):
        try:
            data_list = []
            data_add_int = {}
            db = DB()
            page = int(request.GET.get("page"))
            page_size = int(request.GET.get("page_size"))

            product_id = request.session.get("session_projectId")
            session_work_id = request.session.get("session_workId")
            user_code = request.session.get("session_currentId")
            conn = db.get_connection(product_id)
            product_plan_code = request.GET.get("product_plan_code")
            matter_code = request.GET.get("matter_code")
            solve_method = request.GET.get("solve_method")
            matter_id = request.GET.get("matter_id")
            finished_product_code = request.GET.get("finished_product_code")

            un_pro_table = str("unqualified_product_") + str(session_work_id)
            # unqualified_product_code = request.GET.get("unqualified_product_code")
            # solve_result = request.GET.get("solve_result")
            # leader_work_id = request.GET.get("leader_work_id")
            # later_work_id = request.GET.get("later_work_id")
            # description = request.GET.get("description")
            if finished_product_code:
                finished_product_code_sql = " and finished_product_code = " + "'" + finished_product_code + "'"
            else:
                finished_product_code_sql = ""
            if product_plan_code:
                product_plan_code_sql = " and product_plan_code = " + "'" + product_plan_code + "'"
            else:
                product_plan_code_sql = ""
            if matter_code:
                matter_code_sql = " and matter_code = " + "'" + matter_code + "'"
            else:
                matter_code_sql = ""
            if solve_method:
                solve_method_sql = " and solve_method = " + "'" + solve_method + "'"
            else:
                solve_method_sql = ""
            sql = """
                select * from {0} where 2 > 1 {1} {2} {3} {4} group by finished_product_code
               """
            sql_main = sql.format(un_pro_table, product_plan_code_sql, matter_code_sql,
                                  solve_method_sql, finished_product_code_sql)
            drs = db.execute_sql(conn, sql_main)

            if drs:
                for dr in drs:
                    dict_data = {}
                    dict_data["unqualified_product_code"] = dr[0]
                    dict_data["product_plan_code"] = dr[1]
                    dict_data["finished_product_code"] = dr[2]
                    dict_data["matter_code"] = []
                    dict_data["matter_id"] = []
                    dict_data["description"] = dr[5]
                    dict_data["leader_work_id"] = dr[6]
                    dict_data["later_work_id"] = dr[7]
                    dict_data["solve_method"] = dr[8]
                    dict_data["solve_result"] = dr[9]
                    data_list.append(dict_data)

                page_result = Page(page, page_size, data_list)
                data = page_result.get_str_json()
                sql_num = """
                        select count(*) from {0} where 2 > 1 {1} {2} {3} {4} group by finished_product_code
                        """
                sql_num_format = sql_num.format(un_pro_table, product_plan_code_sql, matter_code_sql,
                                                solve_method_sql, finished_product_code_sql)
                dfs = db.execute_sql(conn, sql_num_format)
                sql_num_int = dfs[0][0]

                data_add_int["data"] = data
                data_add_int["total"] = sql_num_int

                result = {"code": 0, "message": "调取成功", "data": data_add_int}
                result = json.dumps(result)

                return HttpResponse(result)
            else:
                data_add_int["data"] = []
                data_add_int["total"] = 0
                result = {"code": 0, "message": "无数据", "data": data_add_int}
                result = json.dumps(result)
                return HttpResponse(result)

        except Exception as e:
            print(e)
            data = {"code": 1, "message": "查询错误", "data": e}
            data = json.dumps(data)

            return HttpResponse(data)


class PutUnqualifiedProduct(View):
    def get(self, request):
        try:
            db = DB()
            product_id = request.session.get("session_projectId")
            session_work_id = request.session.get("session_workId")
            user_code = request.session.get("session_currentId")
            conn = db.get_connection(product_id)
            unqualified_product_code = request.GET.get("unqualified_product_code")
            product_plan_code = request.GET.get("product_plan_code")
            matter_code = request.GET.get("matter_code")
            solve_method = request.GET.get("solve_method")
            leader_work_id = request.GET.get("leader_work_id")
            later_work_id = request.GET.get("later_work_id")
            solve_result = request.GET.get("solve_result")
            matter_id = request.GET.get("matter_id")
            description = request.GET.get("description")
            un_pro_table = str("unqualified_product_") + str(session_work_id)
            sql_update_unqualified = """
            update {0} set product_plan_code = '{1}',
                       matter_code='{2}',matter_id= '{3}',description='{4}',solve_method='{5}', leader_work_id ='{6}'
                       ,later_work_id = '{7}', solve_result = '{8}' where unqualified_product_code = '{9}'
            """
            sql_update_unqualified_main = sql_update_unqualified.format(un_pro_table, product_plan_code, matter_code,
                                                                        matter_id, description, solve_method,
                                                                        leader_work_id, later_work_id,
                                                                        solve_result, unqualified_product_code)
            drs = db.execute_sql(conn, sql_update_unqualified_main)
            data = {"code": 0, "message": "修改成功", "data": []}
            data = json.dumps(data)

            return HttpResponse(data)

        except Exception as e:
            print(e)
            data = {"code": 1, "message": "修改错误", "data": e}
            data = json.dumps(data)

            return HttpResponse(data)


class DeleteUnqualifiedProduct(View):
    def get(self, request):

        try:
            db = DB()
            product_id = request.session.get("session_projectId")
            session_work_id = request.session.get("session_workId")
            user_code = request.session.get("session_currentId")
            conn = db.get_connection(product_id)
            un_pro_table = str("unqualified_product_") + str(session_work_id)
            unqualified_product_code = request.GET.get("unqualified_product_code")

            sql = """
                      delete from {0} where unqualified_product_code = '{1}'
                      """
            sql_main = sql.format(un_pro_table, unqualified_product_code)
            des = db.execute_sql(conn, sql_main)

            data = {"code": 0, "message": "操作成功", "data": ""}
            data = json.dumps(data)

            return HttpResponse(data)

        except Exception as e:
            print(e)
            data = {"code": 1, "message": "操作失败", "data": e}
            data = json.dumps(data)

            return HttpResponse(data)


class QualifiedMatterCode(View):
    def get(self, request):
        try:
            db = DB()
            table_list = []
            product_id = request.session.get("session_projectId")
            session_work_id = request.session.get("session_workId")
            user_code = request.session.get("session_currentId")
            finished_product_code = request.GET.get("finished_product_code")

            print("---->>", session_work_id)

            # matter_code = request.GET.get("matter_code")
            # product_id = "personai"
            # session_work_id = "fix"
            # user_code = ""
            # matter_code = "king"
            conn = db.get_connection(product_id)
            sql_table = "unqualified_product_" + str(session_work_id)

            sql = """
            show tables
            """
            drs = db.execute_sql(conn, sql)
            for dr in drs:
                table_list.append(dr[0])
            if sql_table in table_list:
                sql_check = """
                SELECT * FROM {0} where finished_product_code = '{1}' and leader_work_id = '{2}'
                """
                sql_check = sql_check.format(sql_table, finished_product_code, session_work_id)
                dfs = db.execute_sql(conn, sql_check)
                if dfs:
                    test_result = "合格"
                    data = {"code": 0, "message": "操作成功", "data": test_result}

                    data = json.dumps(data)
                    return HttpResponse(data)
                else:
                    sql_work_id = """
                    SELECT leader_work_id FROM process_deal where work_id = "{0}";
                    """
                    sql_work_id = sql_work_id.format(session_work_id)
                    drs = db.execute_sql(conn, sql_work_id)
                    if drs[0][0]:
                        leader_work_id = drs[0][0]
                        select_work_table = str("product_transit_") + str(leader_work_id)
                        sql_table = """
                          SELECT test_result FROM {0} where finished_product_code = '{1}' group by finished_product_code             
                        """
                        sql_table = sql_table.format(select_work_table, finished_product_code)
                        dfs = db.execute_sql(conn, sql_table)
                        if dfs:
                            test_result = dfs[0][0]
                            print("---------->", test_result)
                            if test_result == "合格":
                                print("===>", "kkkk")
                                data = {"code": 0, "message": "成功", "data": test_result}
                            else:
                                print("===>", "ooooo")
                                data = {"code": 1, "message": "该产品上一工站不合格", "data": test_result}
                        else:
                            test_result = "找不到此成品码"
                            data = {"code": 1, "message": "找不到此成品码", "data": test_result}

                        data = json.dumps(data)
                        return HttpResponse(data)
                    else:
                        data = {"code": 0, "message": "此工站是第一工站", "data": ""}
                        data = json.dumps(data)
                        # print("------------->", data)

                        return HttpResponse(data)
            else:
                sql_work_id = """
                                   SELECT leader_work_id FROM process_deal where work_id = "{0}";
                                   """
                sql_work_id = sql_work_id.format(session_work_id)
                drs = db.execute_sql(conn, sql_work_id)
                if drs[0][0]:
                    leader_work_id = drs[0][0]
                    select_work_table = str("product_transit_") + str(leader_work_id)
                    sql_table = """
                             SELECT test_result FROM {0} where finished_product_code = '{1}' 
                             group by finished_product_code             
                           """
                    sql_table = sql_table.format(select_work_table, finished_product_code)
                    dfs = db.execute_sql(conn, sql_table)
                    if dfs:
                        test_result = dfs[0][0]
                        # data = {"code": 0, "message": "成功", "data": test_result}
                        if test_result == "合格":
                            print("===>", "kkkkss")
                            data = {"code": 0, "message": "成功", "data": test_result}
                        else:
                            print("===>", "oooooss")
                            data = {"code": 1, "message": "该产品上一工站不合格", "data": test_result}
                    else:
                        test_result = "找不到此成品码"
                        data = {"code": 1, "message": "找不到此成品码", "data": test_result}

                    data = json.dumps(data)

                    return HttpResponse(data)
                else:
                    data = {"code": 0, "message": "此工站是第一站,前面没有工站, 找不到数据", "data": ""}
                    data = json.dumps(data)

                    return HttpResponse(data)

        except Exception as e:
            print(e)
            data = {"code": 0, "message": "查到前一工站里面的物料报错", "data": e}
            data = json.dumps(data)
            return HttpResponse(data)


class BomMatterCodeName(View):
    def get(self, request):
        try:
            data_list = []
            db = DB()
            product_id = request.session.get("session_projectId")
            session_work_id = request.session.get("session_workId")
            conn = db.get_connection(product_id)

            sql = """
                SELECT bom_matter_code, matter_name, rule FROM matter_list;
                """
            sql = sql.format(session_work_id)
            drs = db.execute_sql(conn, sql)
            if drs:
                for df in drs:
                    matter_code_dict = {}
                    matter_code_dict["matter_code"] = df[0]
                    matter_code_dict["matter_name"] = df[1]
                    matter_code_dict["rule"] = df[2]
                    data_list.append(matter_code_dict)

                data = {"code": 0, "message": "操作成功", "data": data_list}
                data = json.dumps(data)
            else:
                data = {"code": 0, "message": "没有找到数据", "data": []}
                data = json.dumps(data)
            return HttpResponse(data)

        except Exception as e:
            print(e)
            data = {"code": 1, "message": "调取matter_list数据库失败", "data": e}
            data = json.dumps(data)
            return HttpResponse(data)


class WorkStationGetData(View):
    def get(self, request):
        try:
            data_list = []
            data_add_int = {}
            dict_data = {}
            db = DB()
            product_id = request.session.get("session_projectId")
            work_id = request.session.get("session_workId")
            current_person_id = request.session['session_currentId']
            # work_id = request.session['session_workId']
            conn = db.get_connection(product_id)
            # page = int(request.GET.get("page"))
            # page_size = int(request.GET.get("page_size"))
            sql_matter = """
                        select * from process_matter_deal where work_id = '{0}'
                         """
            sql_matter_format = sql_matter.format(work_id)
            matter_dfs = db.execute_sql(conn, sql_matter_format)
            if matter_dfs:
                respose_list = []
                for matter_df in matter_dfs:
                    response_data = {}
                    response_data["process_matter_deal_code"] = matter_df[0]
                    response_data["work_id"] = matter_df[1]
                    response_data["matter_code"] = matter_df[2]
                    response_data["install_number"] = matter_df[3]
                    respose_list.append(response_data)
                dict_data["response_datas"] = respose_list
                data_list.append(dict_data)

            else:
                dict_data["response_datas"] = []
                data_list.append(dict_data)

            data = {"code": 0, "message": "操作成功", "data": data_list}

            data = json.dumps(data)

            return HttpResponse(data)

        except Exception as e:
            print(e)
            data = {"code": 1, "message": "操作失败", "data": e}
            data = json.dumps(data)

            return HttpResponse(data)


class FinishedCodeGetMatterCodeID(View):
    def get(self, request):
        try:
            db = DB()
            product_id = request.session.get("session_projectId")

            finished_product_code = request.GET.get("finished_product_code")
            conn = db.get_connection(product_id)

            if finished_product_code:
                finished_product_code_sql = "and finished_product_code = " + "'" + finished_product_code + "'"
                current_person_id = request.session['session_currentId']
                # work_id = request.session['session_workId']
                sql_tabale = """
                            show tables like "product_transit_%" 
                            """
                table_list = db.execute_sql(conn, sql_tabale)

                respose_list = []
                for table_type in table_list:
                    table_one = table_type[0]

                    sql_matter = """
                                           select finished_product_code, matter_code, matter_id, 
                                           product_transit_code from {0} where 2 > 1 {1}
                                            """
                    sql_matter_format = sql_matter.format(table_one, finished_product_code_sql)
                    matter_dfs = db.execute_sql(conn, sql_matter_format)
                    if matter_dfs:
                        for matter_df in matter_dfs:
                            response_data = {}
                            response_data["finished_product_code"] = matter_df[0]
                            response_data["matter_code"] = matter_df[1]
                            response_data["matter_id"] = matter_df[2]
                            response_data["work_id"] = table_one[16:]
                            response_data["product_transit_code"] = matter_df[3]
                            respose_list.append(response_data)
                    else:
                        pass
            else:
                respose_list = []
            data = {"code": 0, "message": "操作成功", "data": respose_list}

            data = json.dumps(data)
            return HttpResponse(data)

        except Exception as e:
            print(e)
            data = {"code": 1, "message": "操作失败", "data": e}
            data = json.dumps(data)

            return HttpResponse(data)


class PutFinishedCodeGetMatterCodeID(View):
    def get(self, request):
        try:
            db = DB()
            product_id = request.session.get("session_projectId")
            response_datas = request.GET.get("response_datas")

            if response_datas:
                response_datas = eval(response_datas)
            finished_product_code = request.GET.get("finished_product_code")
            return_work_id = request.GET.get("return_work_id")
            conn = db.get_connection(product_id)
            sql_tabale = """
                      show tables like "product_transit_%" 
                      """
            table_list = db.execute_sql(conn, sql_tabale)
            for table_type in table_list:
                for response_data in response_datas:

                    product_transit_code = response_data.get("product_transit_code")
                    matter_id = response_data.get("matter_id")
                    table_one = table_type[0]
                    sql_matter = """
                                      update {0} set matter_id = '{1}' 
                                      where product_transit_code = '{2}'
                                       """
                    sql_matter_format = sql_matter.format(table_one, matter_id, product_transit_code)
                    matter_dfs = db.execute_sql(conn, sql_matter_format)

            sql_select_table = "unqualified_product_" + str(return_work_id)
            sql_is_create_table = """
               CREATE TABLE IF NOT EXISTS {0}(unqualified_product_code varchar(255) primary key not null,
                              product_plan_code varchar(255), finished_product_code varchar(255), 
                              matter_code varchar(255), matter_id varchar(255),description varchar(255),
                              leader_work_id varchar(255), later_work_id varchar(255), solve_method varchar(255),
                              solve_result varchar(255), order_number int) 
            """
            sql_is_create_table = sql_is_create_table.format(sql_select_table)
            drs = db.execute_sql(conn, sql_is_create_table)

            sql_unqualified_product = """
                                     SELECT max(order_number) FROM {0};
                                     """
            sql_unqualified_product = sql_unqualified_product.format(sql_select_table)
            unqualified_product_nums = db.execute_sql(conn, sql_unqualified_product)
            if unqualified_product_nums[0][0]:
                matter_num = unqualified_product_nums[0][0] + 1
            else:
                matter_num = 1

            unqualified_product_code = "Im_Unqualified_Product_" + str(matter_num)

            sql_disqualification = """
            insert into {0}(unqualified_product_code, finished_product_code, leader_work_id)
                                              values('{1}', '{2}', '{3}')
            """
            sql_disqualification = sql_disqualification.format(sql_select_table, unqualified_product_code,
                                                               finished_product_code, return_work_id)
            db.execute_sql(conn, sql_disqualification)

            data = {"code": 0, "message": "修改成功"}
            data = json.dumps(data)
            return HttpResponse(data)

        except Exception as e:
            print(e)
            data = {"code": 0, "message": e }

            data = json.dumps(data)
            return HttpResponse(data)


class DeleteFinishedCodeGetMatterCodeID(View):
    def get(self, request):
        try:
            db = DB()
            product_id = request.session.get("session_projectId")
            finished_product_code = request.GET.get("finished_product_code")
            return_work_id = request.GET.get("work_id")
            conn = db.get_connection(product_id)
            finished_product_code_sql = "and finished_product_code = " + "'" + finished_product_code + "'"
            sql_tabale = """
                       show tables like "product_transit_%" 
                       """
            table_list = db.execute_sql(conn, sql_tabale)
            for table_type in table_list:
                table_one = table_type[0]
                sql_matter = """
                           delete from {0} where 2 > 1 {1}
                            """
                sql_matter_format = sql_matter.format(table_one, finished_product_code_sql)
                matter_dfs = db.execute_sql(conn, sql_matter_format)

            data = {"code": 0, "message": "重置成功"}

            data = json.dumps(data)
            return HttpResponse(data)

        except Exception as e:
            print(e)
            data = {"code": 0, "message": e}

            data = json.dumps(data)
            return HttpResponse(data)


class Pick(View):
    def get(self, request):
        try:
            data_list = []
            data_add_int = {}
            db = DB()
            product_id = request.session.get("session_projectId")
            conn = db.get_connection(product_id)
            work_id = request.GET.get("work_id")

            page = int(request.GET.get("page"))
            page_size = int(request.GET.get("page_size"))

            if work_id:
                work_id_sql = "and work_id = " + "'" + work_id + "'"
            else:
                work_id_sql = ""

            sql = """
                        select * from pick_box where 2 > 1 {0}
                       """

            sql_main = sql.format(work_id_sql)

            drs = db.execute_sql(conn, sql_main)

            if drs:
                for dr in drs:
                    dict_data = {}
                    dict_data["pick_code"] = dr[0]
                    dict_data["work_id"] = dr[1]
                    dict_data["pick_number"] = dr[2]
                    dict_data["description"] = dr[3]
                    data_list.append(dict_data)
                    # dict_data["product_status"] = dr[4]
                    # dict_data["description"] = dr[5]

                    page_result = Page(page, page_size, data_list)
                    data = page_result.get_str_json()

                    sql_num = """
                                select count(*) from pick_box where 2 > 1 {0}
                                """
                    sql_num_main = sql_num.format(work_id_sql)

                    dfs = db.execute_sql(conn, sql_num_main)
                    if dfs:
                        sql_num_int = dfs[0][0]
                    else:
                        sql_num_int = 0
                    data_add_int["data"] = data
                    data_add_int["total"] = sql_num_int
            else:
                data_add_int["data"] = []
                data_add_int["total"] = 0

            result = {"code": 0, "message": "操作成功", "data": data_add_int}
            result = json.dumps(result)
            return HttpResponse(result)

        except Exception as e:
            print(e)
            result = {"code": 1, "message": "操作失败", "data": e}
            result = json.dumps(result)
            return HttpResponse(result)

    def post(self, request):
        try:
            db = DB()
            product_id = request.session.get("session_projectId")
            conn = db.get_connection(product_id)
            json_data = request.body
            str_data = json.loads(json_data)
            work_id = str_data.get("work_id")
            pick_number = str_data.get("pick_number")
            description = str_data.get("description")

            # product_id = "pen"
            # conn = db.get_connection(product_id)
            # work_id = "dsf_hf"
            # pick_number = 12
            # description = ""
            sql = """
                 select max(order_number) from pick_box
                """
            id_num = db.execute_sql(conn, sql)
            if id_num[0][0] == None:
                id_num = 1
            else:
                id_num = id_num[0][0] + 1

            pick_code = str(product_id) + "pickbox" + str(id_num)

            sql_insert = """
                        insert into pick_box(pick_code, work_id, pick_number, description,order_number)
                        values('{0}', '{1}', '{2}', '{3}', '{4}')
                        """

            sql_insert_format = sql_insert.format(pick_code, work_id, pick_number,
                                                  description, id_num)

            drs = db.execute_sql(conn, sql_insert_format)
            data = {"code": 0, "message": "创建包装箱成功"}

            data = json.dumps(data)

            return HttpResponse(data)
        except Exception as e:
            print(e)
            data = {"code": 1, "message": "创建包装箱失败"}

            data = json.dumps(data)

            return HttpResponse(data)


class PutPick(View):
    def get(self, request):
        try:
            db = DB()
            product_id = request.session.get("session_projectId")
            conn = db.get_connection(product_id)
            pick_code = request.GET.get("pick_code")
            work_id = request.GET.get("work_id")
            pick_number = request.GET.get("pick_number")
            description = request.GET.get("description")

            sql_update = """
                       update pick_box set work_id='{0}',
                        pick_number='{1}',description='{2}' where pick_code = '{3}'
                       """

            sql_insert_format = sql_update.format(work_id, pick_number, description,
                                                  pick_code)

            drs = db.execute_sql(conn, sql_insert_format)
            data = {"code": 0, "message": "修改成功"}

            data = json.dumps(data)

            return HttpResponse(data)
        except Exception as e:
            print(e)
            data = {"code": 1, "message": "修改失败"}

            data = json.dumps(data)

            return HttpResponse(data)


class DeletePick(View):
    def get(self, request):
        try:
            db = DB()
            product_id = request.session.get("session_projectId")
            conn = db.get_connection(product_id)
            pick_code = request.GET.get("pick_code")
            sql_delete = """
                       delete from pick_box where pick_code = '{0}'
                       """
            sql_insert_format = sql_delete.format(pick_code)

            drs = db.execute_sql(conn, sql_insert_format)
            data = {"code": 0, "message": "删除成功"}

            data = json.dumps(data)

            return HttpResponse(data)
        except Exception as e:
            print(e)
            data = {"code": 1, "message": "删除失败"}

            data = json.dumps(data)

            return HttpResponse(data)


class FinishedProductStorage(View):
    def get(self, request):
        try:
            data_list = []
            data_add_int = {}
            db = DB()
            product_id = request.session.get("session_projectId")
            enter_time = request.GET.get("enter_time")
            enter_user = request.GET.get("enter_user")

            page = int(request.GET.get("page"))
            page_size = int(request.GET.get("page_size"))

            # product_id = "pen"
            # enter_time = ""
            # enter_user = ""
            #
            # page = 1
            # page_size = 10
            conn = db.get_connection(product_id)

            if enter_time:
                enter_time_sql = "and enter_time = " + "'" + enter_time + "'"
            else:
                enter_time_sql = ""
            if enter_user:
                enter_user_sql = "and enter_user = " + "'" + enter_user + "'"
            else:
                enter_user_sql = ""

            sql = """
                    select * from enter_storage_status
                   """
            drs = db.execute_sql(conn, sql)

            if drs:

                for dr in drs:
                    dict_data = {}
                    pick_id = dr[0]
                    print(pick_id)
                    dict_data["pack_id"] = dr[0]
                    dict_data["product_id"] = dr[1]
                    dict_data["product_name"] = dr[2]
                    dict_data["enter_user"] = dr[3]
                    s = dr[4]
                    s = s.strftime("%Y-%m-%d %H:%M:%S ")
                    dict_data["enter_time"] = s
                    dict_data["status"] = dr[5]

                    sql_status = """
                    select * from enter_storage where pack_id = '{0}'
                    """
                    sql_status = sql_status.format(pick_id)
                    dfs = db.execute_sql(conn, sql_status)

                    response_datas = []

                    for df in dfs:
                        datas_dict = {}
                        datas_dict["enter_storage_code"] = df[0]
                        datas_dict["pack_id"] = df[1]
                        datas_dict["finished_product_code"] = df[2]
                        response_datas.append(datas_dict)
                        dict_data["response_datas"] = response_datas
                    data_list.append(dict_data)

                    page_result = Page(page, page_size, data_list)
                    data = page_result.get_str_json()

                    sql_num = """
                                select count(*) from enter_storage_status
                                """
                    dfs = db.execute_sql(conn, sql_num)
                    if dfs:
                        sql_num_int = dfs[0][0]
                    else:
                        sql_num_int = 0
                    data_add_int["data"] = data
                    data_add_int["total"] = sql_num_int
            else:
                data_add_int["data"] = []
                data_add_int["total"] = 0

            result = {"code": 0, "message": "操作成功", "data": data_add_int}

            result = json.dumps(result)
            return HttpResponse(result)

        except Exception as e:
            print(e)
            result = {"code": 1, "message": "操作失败", "data": e}
            result = json.dumps(result)
            return HttpResponse(result)

    def post(self, request):
        try:
            db = DB()
            product_id = request.session.get("session_projectId")
            work_id = request.session.get("session_workId")
            enter_user = request.session.get("session_currentId")


            json_data = request.body
            str_data = json.loads(json_data)
            pack_id = str_data.get("pack_id")
            # product_name = str_data.get("product_name")
            status = "已包装"
            response_datas = str_data.get("response_datas")
            conn_product_name = db.get_connection("db_common")
            sql_product_name = """
            SELECT product_name FROM productlist where product_id = '{0}'
            """
            sql_product_name = sql_product_name.format(product_id)
            drs = db.execute_sql(conn_product_name, sql_product_name)
            if drs:
                product_name = drs[0][0]
            else:
                product_name = ""
            # product_id = "pen"
            # # work_id = request.session.get("session_workId")
            # # json_data = request.body
            # # str_data = json.loads(json_data)
            # pack_id = "pen_20210803_2"
            # product_name = "笔"
            # status = "入库"
            # enter_user = "test"
            # response_datas = [{"pack_id": "pen_20210803_2", "finished_product_code": "kokoko",
            #                    "product_name": "笔", "enter_user": "test"},
            #                   {"pack_id": "pen_20210803_2", "finished_product_code": "opopop",
            #                    "product_name": "笔", "enter_user": "test"}]
            conn = db.get_connection(product_id)
            sql1 = """
            CREATE TABLE IF NOT EXISTS enter_storage(enter_storage_code varchar(255) primary key not null, 
                              pack_id varchar(255),
                              finished_product_code varchar(255),
                              order_number int) 
            """
            sql2 = """
            CREATE TABLE IF NOT EXISTS enter_storage_status(pack_id varchar(255) primary key not null,
                              product_id varchar(255),product_name varchar(255),
                              enter_user varchar(255), enter_time datetime, 
                              status varchar(255),order_number int)           
            """
            drs = db.execute_sql(conn, sql1)
            dfs = db.execute_sql(conn, sql2)

            sql_num1 = """
                             select max(order_number) from enter_storage
                            """
            id_num = db.execute_sql(conn, sql_num1)
            if id_num[0][0] == None:
                id_num = 0
            else:
                id_num = id_num[0][0]

            sql_num2 = """
                         select max(order_number) from enter_storage_status
                        """
            id_num2 = db.execute_sql(conn, sql_num2)
            if id_num2[0][0] == None:
                id_num2 = 1
            else:
                id_num2 = id_num2[0][0] + 1
            for response_data in response_datas:
                id_num += 1
                enter_storage_code = str("Im_enter_storage_") + str(id_num)
                pack_id = response_data.get("pack_id")
                finished_product_code = response_data.get("finished_product_code")
                # product_name = response_data.get("product_name")
                # enter_user = response_data.get("enter_user")

                sql_insert = """
                insert into enter_storage(enter_storage_code, pack_id, finished_product_code, order_number)
                values('{0}', '{1}','{2}','{3}')
                """
                sql_insert = sql_insert.format(enter_storage_code, pack_id, finished_product_code,
                                               id_num)

                drs = db.execute_sql(conn, sql_insert)
            enter_time = datetime.datetime.now().strftime("%Y%m%d")

            insert_sql = """
            insert into enter_storage_status(pack_id, product_id, product_name, enter_user, enter_time, status, order_number) 
            values('{0}', '{1}','{2}', '{3}', '{4}', '{5}', '{6}')
            """
            insert_sql = insert_sql.format(pack_id, product_id, product_name, enter_user, enter_time, status, id_num2)
            dfs = db.execute_sql(conn, insert_sql)

            data = {"code": 0, "message": "装包成功"}

            data = json.dumps(data)

            return HttpResponse(data)
        except Exception as e:
            print(e)
            data = {"code": 1, "message": "装包失败"}

            data = json.dumps(data)

            return HttpResponse(data)


class PutFinishedProductStorage(View):
    def get(self, request):
        try:
            db = DB()
            product_id = request.session.get("session_projectId")
            work_id = request.session.get("session_workId")
            enter_user = request.session.get("session_currentId")

            pack_id = request.GET.get("pack_id")
            # product_id = request.GET.get("product_id")
            product_name = request.GET.get("product_name")
            enter_user = request.GET.get("enter_user")
            enter_time = request.GET.get("enter_time")
            status = request.GET.get("status")
            response_datas = request.GET.get("response_datas")
            if response_datas:
                response_datas = eval(response_datas)
            # pack_id = "pen_20210803_1"
            # product_id = "pen"
            # product_name = "笔"
            # enter_user = "Im_User_1"
            # enter_time = "2021-08-03"
            # status = "已包装"
            # response_datas = [{"enter_storage_code":"Im_enter_storage_1",
            #                    "pack_id":"pen_20210803_1", "finished_product_code": "kkkkk"},
            #                   {"enter_storage_code": "Im_enter_storage_2",
            #                    "pack_id": "pen_20210803_1", "finished_product_code": "gggggg"}
            #                   ]
            conn = db.get_connection(product_id)
            for response_data in response_datas:
                enter_storage_code = response_data.get("enter_storage_code")
                pack_id = response_data.get("pack_id")
                finished_product_code = response_data.get("finished_product_code")
                sql_update = """
                 update enter_storage set pack_id='{0}',
                        finished_product_code='{1}' where enter_storage_code = '{2}' 
                """
                sql_update = sql_update.format(pack_id, finished_product_code, enter_storage_code)
                db.execute_sql(conn, sql_update)
            sql_update_status = """
            update enter_storage_status set 
                        product_id='{0}', product_name = '{1}', enter_user = '{2}',enter_time = '{3}',status = '{4}'  
                        where pack_id = '{5}' 
            """
            sql_update_status = sql_update_status.format(product_id, product_name,
                                                         enter_user, enter_time, status, pack_id)
            db.execute_sql(conn, sql_update_status)

            data = {"code": 0, "message": "修改成功"}

            data = json.dumps(data)

            return HttpResponse(data)
        except Exception as e:
            print(e)
            data = {"code": 1, "message": "修改失败"}

            data = json.dumps(data)

            return HttpResponse(data)


class DeleteFinishedProductStorage(View):
    def get(self, request):
        try:
            db = DB()
            product_id = request.session.get("session_projectId")
            work_id = request.session.get("session_workId")
            enter_user = request.session.get("session_currentId")
            pack_id = request.GET.get("pack_id")
            # response_datas = request.GET.get("response_datas")
            response_datas = request.GET.get("response_datas")
            if response_datas:
                response_datas = eval(response_datas)
            else:
                response_datas = response_datas
            # product_id = "pen"
            # pack_id = "pen_20210803_1"
            # response_datas = []
            conn = db.get_connection(product_id)
            if response_datas:
                for response_data in response_datas:
                    storage_id = response_data.get("enter_storage_code")
                    sql_delete = """
                    delete FROM enter_storage where enter_storage_code = "{0}"
                    """
                    sql_delete = sql_delete.format(storage_id)
                    db.execute_sql(conn, sql_delete)
            else:
                sql_delete_status = """
                delete FROM enter_storage_status where pack_id = "{0}"
                """
                sql_delete_status = sql_delete_status.format(pack_id)
                db.execute_sql(conn, sql_delete_status)
                sql_storage = """
                SELECT enter_storage_code FROM enter_storage where pack_id = "{0}";
                """
                sql_storage = sql_storage.format(pack_id)
                drs = db.execute_sql(conn, sql_storage)
                for dr in drs:
                    # enter_list.append(dr[0])
                    enter_id = dr[0]
                    sql_delete = """
                    delete FROM enter_storage where enter_storage_code = "{0}"
                    """
                    sql_delete = sql_delete.format(enter_id)
                    db.execute_sql(conn, sql_delete)

            data = {"code": 0, "message": "删除成功"}

            data = json.dumps(data)

            return HttpResponse(data)
        except Exception as e:
            print(e)
            data = {"code": 1, "message": "删除失败"}

            data = json.dumps(data)

            return HttpResponse(data)


class stockInStockOut(View):
    def get(self, request):
        try:
            db = DB()
            product_id = request.session.get("session_projectId")
            work_id = request.session.get("session_workId")
            enter_user = request.session.get("session_currentId")
            enter_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S ")

            # product_id = "pen"
            # status = "入库"
            # response_datas = [{"pack_id":"pen_20210803_5"}, {"pack_id":"pen_20210803_6"}]
            conn = db.get_connection(product_id)
            status = request.GET.get("status")
            response_datas = request.GET.get("response_datas")

            if response_datas:
                response_datas = eval(response_datas)
                for response_data in response_datas:
                    pack_id = response_data.get("pack_id")
                    sql_update = """
                    update enter_storage_status set 
                        status ='{0}', enter_time = '{1}' 
                        where pack_id = '{2}' 
                    """
                    sql_update = sql_update.format(status, enter_time, pack_id)
                    db.execute_sql(conn, sql_update)
                    data = {"code": 0, "message": "操作成功"}
                    data = json.dumps(data)
                    return HttpResponse(data)
            else:
                data = {"code": 1, "message": "response_datas里面没有数据"}
                data = json.dumps(data)
                return HttpResponse(data)

        except Exception as e:
            print(e)
            data = {"code": 1, "message": "操作失败"}

            data = json.dumps(data)

            return HttpResponse(data)


class BackMatter(View):

    def get(self, request):
        try:
            data_list = []
            matter_list = []
            data_add_int = {}
            db = DB()
            product_id = request.session.get("session_projectId")
            conn = db.get_connection(product_id)

            page = int(request.GET.get("page"))
            page_size = int(request.GET.get("page_size"))

            back_person = request.GET.get("back_person")
            product_plan_code = request.GET.get("product_plan_code")
            if back_person:
                back_person_sql = "and back_person = " + "'" + back_person + "'"
            else:
                back_person_sql = ""
            if product_plan_code:
                product_plan_code_sql = "and product_plan_code = " + "'" + product_plan_code + "'"
            else:
                product_plan_code_sql = ""

            sql = """
            select * from product_back_matter where 2 > 1 {0} {1} 
            """
            sql = sql.format(back_person_sql, product_plan_code_sql)
            drs = db.execute_sql(conn, sql)
            if drs:
                for dr in drs:
                    dict_data = {}
                    dict_data["materials_back_code"] = dr[0]
                    dict_data["back_person"] = dr[1]
                    dict_data["product_plan_code"] = dr[2]
                    s = dr[3]
                    if s:
                        s = s.strftime("%Y-%m-%d %H:%M:%S ")
                    else:
                        s = ""
                    dict_data["back_time"] = s
                    dict_data["description"] = dr[4]
                    sql_back = """
                    select * from back_matter where materials_back_code = '{0}'
                    """
                    sql_back = sql_back.format(dr[0])
                    back_dfs = db.execute_sql(conn, sql_back)
                    if back_dfs:
                        respose_list = []
                        for matter_df in back_dfs:
                            response_data = {}
                            response_data["deal_back_code"] = matter_df[0]
                            response_data["materials_back_code"] = matter_df[1]
                            response_data["matter_code"] = matter_df[2]
                            response_data["matter_count"] = matter_df[3]
                            respose_list.append(response_data)
                        dict_data["response_datas"] = respose_list
                        data_list.append(dict_data)
                    else:
                        dict_data["response_datas"] = []
                        data_list.append(dict_data)
                page_result = Page(page, page_size, data_list)
                data = page_result.get_str_json()
                sql_num = """
                                select count(*) from product_back_matter
                                """
                dfs = db.execute_sql(conn, sql_num)
                if dfs:
                    sql_num_int = dfs[0][0]
                else:
                    sql_num_int = 0
                data_add_int["data"] = data
                data_add_int["total"] = sql_num_int
                result = {"code": 0, "message":"操作成功", "data": data_add_int}
                result = json.dumps(result)
                return HttpResponse(result)
            else:
                result = {"code": 0, "message": "操作失败", "data": ""}
                result = json.dumps(result)

                return HttpResponse(result)
        except Exception as e:

            print(e)
            result = {"code": 1, "message": "操作失败", "data": e}
            result = json.dumps(result)

            return HttpResponse(result)

    def post(self, request):
        try:

            json_data = request.body
            str_data = json.loads(json_data)

            db = DB()
            product_id = request.session.get("session_projectId")
            conn = db.get_connection(product_id)

            sql_matter = """
                   SELECT max(order_number) FROM back_matter;
                   """
            matter_type = db.execute_sql(conn, sql_matter)
            if matter_type[0][0] == None:
                matter_num = 0
            else:
                matter_num = matter_type[0][0]

            sql = """
                  SELECT max(order_number) FROM product_back_matter;
                  """
            product_type = db.execute_sql(conn, sql)
            if product_type[0][0] == None:
                id_num = 1
            else:
                id_num = product_type[0][0] + 1

            materials_back_code = str("Im_Back_Matter_" + str(id_num))
            back_person = str_data.get("back_person")
            product_plan_code = str_data.get("product_plan_code")
            back_time = str_data.get("back_time")
            description = str_data.get("description")
            response_datas = str_data.get("response_datas")

            order_number = id_num
            sql_insert = """
                               insert into product_back_matter(materials_back_code, back_person,
                               product_plan_code,
                               back_time, description, order_number)
                               values('{0}', '{1}', '{2}', '{3}', '{4}', '{5}')
                               """

            sql_insert_format = sql_insert.format(materials_back_code, back_person,
                                                  product_plan_code, back_time,
                                                  description, order_number)

            drs = db.execute_sql(conn, sql_insert_format)
            for response_data in response_datas:
                # db = DB()
                # conn = db.get_connection("db_common")
                matter_code = response_data.get("matter_code")
                matter_count = response_data.get("matter_count")
                matter_num = matter_num + 1
                deal_back_code = str("Im_Deal_Back_" + str(matter_num))
                sql_response = """
                               insert into back_matter(deal_back_code, materials_back_code,matter_code, matter_count,
                               order_number)
                               values('{0}', '{1}', '{2}', '{3}', '{4}')
                       """
                sql_response_format = sql_response.format(deal_back_code, materials_back_code,
                                                          matter_code, matter_count,
                                                          matter_num)
                matter_drs = db.execute_sql(conn, sql_response_format)

            data = {"code": 0, "message": "操作成功"}
            logger.info("BackMatter接口操作成功")
            data = json.dumps(data)

            return HttpResponse(data)
        except Exception as e:
            print(e)
            data = {"code": 1, "message": "操作失败"}
            logger.error("BackMatter接口操作失败")
            data = json.dumps(data)
            return HttpResponse(data)


class PutBackMatter(View):
    def get(self, request):
        try:
            db = DB()
            product_id = request.session.get("session_projectId")
            conn = db.get_connection(product_id)

            materials_back_code = request.GET.get("materials_back_code")
            back_person = request.GET.get("back_person")
            product_plan_code = request.GET.get("product_plan_code")
            back_time = request.GET.get("back_time")
            description = request.GET.get("description")

            response_datas = request.GET.get("response_datas")
            if response_datas:
                response_datas = eval(response_datas)
            else:
                response_datas = response_datas

            # materials_production_code = 'Im_Product_Pick_Matter_1'
            # materials_person = 'keny'
            # product_plan_code = 'Im_ProductPlan_1'
            # material_time = '2021-07-07'
            # description = '常用品'
            # #
            # response_datas = [{"materials_production_code": "Im_Product_Pick_Matter_1", "matter_code": "Im_Matter_10",
            #                    "matter_count": "33"}]

            # new_check_list = [prodect_code, product_name, rule, product_status, description]
            sql = """
                      update product_back_matter set 
                      back_person='{0}',product_plan_code='{1}', back_time ='{2}',
                      description= '{3}' where materials_back_code = '{4}'
                      """
            sql_main = sql.format(back_person, product_plan_code, back_time, description,
                                  materials_back_code)
            drs = db.execute_sql(conn, sql_main)

            sql_matter_num = """
             SELECT max(order_number) FROM back_matter
            """
            dras = db.execute_sql(conn, sql_matter_num)

            if dras:
                sql_num = dras[0][0]
            else:
                sql_num = 0

            for response_data in response_datas:
                # materials_production_code = response_data.get("materials_production_code")
                deal_back_code = response_data.get("deal_back_code")
                # materials_production_code = response_data.get("materials_production_code")
                matter_code = response_data.get("matter_code")
                matter_count = response_data.get("matter_count")
                if deal_back_code:
                    sql = """
                       update back_matter set materials_back_code = '{0}', 
                       matter_code = '{1}', matter_count ='{2}' where deal_back_code = '{3}'
                    """
                    sql = sql.format(materials_back_code, matter_code, matter_count, deal_back_code)
                    db.execute_sql(conn, sql)
                else:
                    sql_num = sql_num + 1

                    deal_back_code = str("Im_Deal_Back_" + str(sql_num))

                    sql_response = """
                                      insert into back_matter(deal_back_code,materials_back_code, 
                                      matter_code, matter_count, order_number) values('{0}',
                                       '{1}', '{2}', '{3}', '{4}')
                                  """
                    sql_response_format = sql_response.format(deal_back_code, materials_back_code,
                                                              matter_code, matter_count, sql_num)
                    db.execute_sql(conn, sql_response_format)

            data = {"code": 0, "message": "修改成功"}

            data = json.dumps(data)

            db.close_connection(conn)

            return HttpResponse(data)

        except Exception as e:
            print(e)
            data = {"code": 1, "message": "修改失败"}
            logger.error("修改失败---->%s", e)
            data = json.dumps(data)
            return HttpResponse(data)


class DeleteBackMatter(View):
    def get(self, request):
        try:
            db = DB()
            product_id = request.session.get("session_projectId")
            conn = db.get_connection(product_id)

            materials_back_code = request.GET.get("materials_back_code")

            response_datas = request.GET.get("response_datas")
            response_datas = eval(response_datas)
            # materials_production_code = "Im_Product_Pick_Matter_1"
            # response_datas = [{"materials_code": "Im_Materials_Pick_1"}]
            if len(response_datas) != 0:

                for response_data in response_datas:
                    deal_back_code = dict(response_data).get("deal_back_code")
                    sql = """
                       delete from back_matter where deal_back_code = '{0}'
                       """
                    sql_format = sql.format(deal_back_code)
                    db.execute_sql(conn, sql_format)
            else:
                sql_matter = """
                              SELECT * FROM back_matter where materials_back_code = '{0}'
                              """
                sql_matter_format = sql_matter.format(materials_back_code)
                matter_dfs = db.execute_sql(conn, sql_matter_format)
                for matter_df in matter_dfs:
                    deal_back_code = matter_df[0]
                    sql_delete = """
                       delete FROM back_matter where deal_back_code = '{0}'
                       """
                    sql_delete_format = sql_delete.format(deal_back_code)
                    db.execute_sql(conn, sql_delete_format)
                sql = """
                       delete from product_back_matter where materials_back_code = '{0}'
                       """
                sql_main = sql.format(materials_back_code)
                des = db.execute_sql(conn, sql_main)
            data = {"code": 0, "message": "删除成功"}
            logger.info("删除生产退料表成功")
            data = json.dumps(data)
            return HttpResponse(data)

        except Exception as e:
            print(e)
            data = {"code": 1, "message": "删除失败"}
            data = json.dumps(data)
            logger.error("删除产品列表失败,%s" % e)
            return HttpResponse(data)


class ModifyFinishProductStatus(View):
    def get(self, request):
        try:
            db = DB()
            product_id = request.session.get("session_projectId")

            response_datas = request.GET.get("response_datas")
            if response_datas:
                response_datas = eval(response_datas)

            # product_id = "pen"
            # response_datas = [{"finished_product_code": "20210708-12", "status": "不合格"},
            # {"finished_product_code": "p21900", "status": "合格"}]

            # current_person_id = request.session['session_currentId']
            # work_id = request.session['session_workId']

            conn = db.get_connection(product_id)
            sql_tabale = """
                        show tables like "product_transit_%" 
                        """
            table_list = db.execute_sql(conn, sql_tabale)
            for table_type in table_list:
                table_one = table_type[0]

                for response_data in response_datas:
                    finished_product_code = response_data.get("finished_product_code")
                    status = response_data.get("status")
                    finished_product_code_sql = "and finished_product_code = " + "'" + finished_product_code + "'"

                    sql_matter = """
                                  select product_transit_code, finished_product_code, test_result from {0} where 2 > 1 {1}
                                   """
                    sql_matter_format = sql_matter.format(table_one, finished_product_code_sql)
                    matter_dfs = db.execute_sql(conn, sql_matter_format)
                    if matter_dfs:
                        transit_list = []
                        for matter_df in matter_dfs:
                            sql_update = """
                                       update {0} set test_result='{1}' where product_transit_code = '{2}'
                                       """
                            sql_update = sql_update.format(table_one, status, matter_df[0])
                            db.execute_sql(conn, sql_update)
                        if status == "不合格":
                            sql_un_table = str("unqualified_product_") + str(table_one[16:])
                            sql = """
                            CREATE TABLE IF NOT EXISTS {0}(unqualified_product_code varchar(255) primary key not null, 
                                          product_plan_code varchar(255),
                                          finished_product_code varchar(255),
                                          matter_code varchar(255),
                                          matter_id varchar(255),
                                          description varchar(255),
                                          leader_work_id varchar(255),
                                          later_work_id varchar(255),
                                          solve_method varchar(255),
                                          solve_result varchar(255),                             
                                          order_number int) 
                            """
                            sql = sql.format(sql_un_table)
                            db.execute_sql(conn, sql)

                            sql_unqualified_product = """
                                                     SELECT max(order_number) FROM {0};
                                                     """
                            sql_unqualified_product = sql_unqualified_product.format(sql_un_table)
                            unqualified_product_nums = db.execute_sql(conn, sql_unqualified_product)
                            if unqualified_product_nums[0][0]:
                                matter_num = unqualified_product_nums[0][0] + 1
                            else:
                                matter_num = 1

                            unqualified_product_code = "Im_Unqualified_Product_" + str(matter_num)

                            sql_insert = """
                            insert into {0}(unqualified_product_code, finished_product_code, description, order_number)
                            values('{1}', '{2}', '{3}', '{4}')
                            """

                            sql_insert = sql_insert.format(sql_un_table,
                                                           unqualified_product_code,
                                                           finished_product_code, "状态改变", matter_num)
                            db.execute_sql(conn, sql_insert)
                        else:
                            sql_un_status = "unqualified_product_" + str(table_one[16:])
                            sql_code = """
                            SELECT unqualified_product_code FROM {0} where finished_product_code = '{1}'
                            """
                            sql_code = sql_code.format(sql_un_status, finished_product_code)
                            drs = db.execute_sql(conn, sql_code)
                            for dr in drs:
                                sql_delete = """
                                delete from {0} where unqualified_product_code='{1}'
                                """
                                sql_delete = sql_delete.format(sql_un_status, dr[0])
                                db.execute_sql(conn, sql_delete)

                    else:
                        pass

            data = {"code": 0, "message": "操作成功"}

            data = json.dumps(data)
            return HttpResponse(data)

        except Exception as e:
            print(e)
            data = {"code": 1, "message": "操作失败"}
            data = json.dumps(data)
            logger.error("修改成品状态失败,%s" % e)
            return HttpResponse(data)


class MatterSearch(View):
    def get(self, request):
        try:
            data_add_int = {}
            db = DB()

            # product_id = "pen"
            # finished_product_code = ""
            # matter_id = ""
            # page = 1
            # page_size = 100

            product_id = request.session.get("session_projectId")
            conn = db.get_connection(product_id)
            finished_product_code = request.GET.get("finished_product_code")
            matter_id = request.GET.get("matter_id")
            work_id = request.GET.get("work_id")
            user_code = request.GET.get("user_code")
            out_start_time = request.GET.get("out_start_time")
            out_end_time = request.GET.get("out_end_time")

            print(out_start_time, out_end_time)

            sql_table = """
                        show tables like "product_transit_%" 
                        """
            table_list = db.execute_sql(conn, sql_table)
            page = int(request.GET.get("page"))
            page_size = int(request.GET.get("page_size"))

            if finished_product_code:
                finished_product_code_sql = "and finished_product_code = " + "'" + finished_product_code + "'"
            else:
                finished_product_code_sql = ""
            if matter_id:
                matter_id_sql = "and matter_id = " + "'" + matter_id + "'"
            else:
                matter_id_sql = ""
            if work_id:
                work_id_sql = "and work_id = " + "'" + work_id + "'"
            else:
                work_id_sql = ""
            if user_code:
                user_code_sql = "and user_code = " + "'" + user_code + "'"
            else:
                user_code_sql = ""
            if out_start_time:
                out_start_time_sql = "and out_time >= " + "'" + out_start_time + "'"
            else:
                out_start_time_sql = ""
            if out_end_time:
                out_end_time_sql = "and out_time <=" + "'" + out_end_time + "'"
            else:
                out_end_time_sql = ""
            data_list = []
            for table_type in table_list:
                table_one = table_type[0]
                sql = """
                SELECT b.matter_name,a.matter_id,b.rule,
                b.matter_category,c.product_time,
                d.work_name,a.user_code,a.out_time,
                a.finished_product_code FROM {0} as a left join 
                matter_list as b on a.matter_code = b.bom_matter_code 
                left join person_matter as c on c.matter_code = a.matter_code 
                left join work_station as d on d.work_code = a.work_code where 2 > 1 {1} {2} {3} {4} {5} {6}
                order by a.out_time desc;
                """
                sql = sql.format(table_one, finished_product_code_sql, matter_id_sql,
                                 work_id_sql, user_code_sql, out_start_time_sql, out_end_time_sql)

                print("-------------------->", sql)
                drs = db.execute_sql(conn, sql)
                for dr in drs:
                    dict_data = {}
                    dict_data["matter_name"] = dr[0]
                    dict_data["matter_id"] = dr[1]
                    dict_data["rule"] = dr[2]
                    dict_data["matter_category"] = dr[3]
                    s2 = dr[4]
                    if s2:
                        s2 = s2.strftime("%Y-%m-%d %H:%M:%S ")
                    dict_data["product_time"] = s2
                    dict_data["work_name"] = dr[5]
                    dict_data["user_code"] = dr[6]
                    s = dr[7]
                    if s:
                        s = s.strftime("%Y-%m-%d %H:%M:%S ")
                    dict_data["out_time"] = s
                    dict_data["finished_product_code"] = dr[8]
                    data_list.append(dict_data)
            data_list.sort(key=lambda x: (x['out_time']), reverse=True)
            # print("==>", data_list)
            #
            # print("=====>", page, page_size)
            # if finished_product_code or matter_id:
            #     page = 1
            page_result = Page(page, page_size, data_list)
            data = page_result.get_str_json()

            sql_num = int(len(data_list))
            data_add_int["data"] = data
            data_add_int["total"] = sql_num
            result = {"code": 0, "message": "操作成功", "data": data_add_int}
            result = json.dumps(result)
            return HttpResponse(result)
        except Exception as e:
            print(e)
            data = {"code": 1, "message": "操作失败"}
            data = json.dumps(data)
            logger.error("查询物料信息失败,%s" % e)
            return HttpResponse(data)


class ProductInfoSearch(View):
    def get(self, request):
        try:
            data_add_int = {}
            db = DB()
            data_list = []
            page = int(request.GET.get("page"))
            page_size = int(request.GET.get("page_size"))
            product_id = request.session.get("session_projectId")
            finished_product_code = request.GET.get("finished_product_code")
            matter_id = request.GET.get("matter_id")

            print("=======>", finished_product_code)

            #
            # page = 1
            # page_size = 100
            # product_id = "pen"
            # finished_product_code = ""
            # matter_id = "volk3e-21dfsds"
            conn = db.get_connection(product_id)
            if finished_product_code:
                finished_product_code_sql = "and finished_product_code = " + "'" + finished_product_code + "'"
            else:
                finished_product_code_sql = ""
            if matter_id:
                matter_get_product_code = ""
                sql_table = """
                            show tables like "product_transit_%" 
                            """
                table_list = db.execute_sql(conn, sql_table)
                for table_type in table_list:
                    table_one = table_type[0]
                    sql = """
                    select finished_product_code from {0} where matter_id = '{1}'
                    """
                    sql = sql.format(table_one, matter_id)
                    finisheds = db.execute_sql(conn, sql)
                    if finisheds:
                        matter_get_product_code = finisheds[0][0]
                    else:
                        pass
                matter_id_sql = "and finished_product_code = " + "'" + matter_get_product_code + "'"

            else:
                matter_id_sql = ""

            conn_db = db.get_connection("db_common")

            sql_table1 = """
            select rule from productlist where product_id = '{0}'
            """
            sql_table1 = sql_table1.format(product_id)
            drs = db.execute_sql(conn_db, sql_table1)
            rule = drs[0][0]
            sql_enter_storage = """
            SELECT a.product_name, b.finished_product_code,a.status,a.pack_id,a.enter_time
            FROM enter_storage_status as a left join enter_storage as b on a.pack_id = b.pack_id
            where 2>1 {0} {1} order by a.enter_time desc;
            """
            sql_enter_storage = sql_enter_storage.format(finished_product_code_sql, matter_id_sql)
            print("-=-=-=>", sql_enter_storage)
            dfs = db.execute_sql(conn, sql_enter_storage)
            for df in dfs:
                data_dict = {}
                data_dict["product_name"] = df[0]
                data_dict["finished_product_code"] = df[1]
                data_dict["rule"] = rule
                data_dict["status"] = df[2]
                data_dict["pack_id"] = df[3]
                s = df[4]
                if s:
                    s = s.strftime("%Y-%m-%d %H:%M:%S ")
                else:
                    s = ""
                data_dict["enter_time"] = s
                sql_table = """
                            show tables like "product_transit_%" 
                            """
                table_list = db.execute_sql(conn, sql_table)

                finish_matter_list = []
                for table_type in table_list:
                    table_one = table_type[0]
                    sql = """
                    select matter_id from {0} where finished_product_code = '{1}'
                    """
                    sql = sql.format(table_one, df[1])
                    matters = db.execute_sql(conn, sql)
                    if matters:
                        for matter in matters:
                            finish_matter_list.append(matter[0])
                    else:
                        pass
                data_dict["response_datas"] = finish_matter_list

                data_list.append(data_dict)
            data_list.sort(key=lambda x: (x['enter_time']), reverse=True)

            page_result = Page(page, page_size, data_list)
            data = page_result.get_str_json()
            sql_num = int(len(data_list))
            data_add_int["data"] = data
            data_add_int["total"] = sql_num
            result = {"code": 0, "message": "操作成功", "data": data_add_int}
            result = json.dumps(result)
            return HttpResponse(result)
        except Exception as e:
            print(e)
            data = {"code": 1, "message": "操作失败"}
            data = json.dumps(data)
            logger.error("查询物产品信息失败,%s" % e)
            return HttpResponse(data)


class NoPageMatterSearch(View):
    def get(self, request):
        try:
            data_add_int = {}
            db = DB()

            # product_id = "pen"
            # finished_product_code = ""
            # matter_id = ""
            # page = 1
            # page_size = 100

            product_id = request.session.get("session_projectId")
            conn = db.get_connection(product_id)
            finished_product_code = request.GET.get("finished_product_code")
            matter_id = request.GET.get("matter_id")

            sql_table = """
                        show tables like "product_transit_%" 
                        """
            table_list = db.execute_sql(conn, sql_table)

            if finished_product_code:
                finished_product_code_sql = "and finished_product_code = " + "'" + finished_product_code + "'"
            else:
                finished_product_code_sql = ""
            if matter_id:
                matter_id_sql = "and matter_id = " + "'" + matter_id + "'"
            else:
                matter_id_sql = ""
            data_list = []
            for table_type in table_list:
                table_one = table_type[0]
                sql = """
                SELECT b.matter_name,a.matter_id,b.rule,
                b.matter_category,c.product_time,
                d.work_name,a.user_code,a.out_time,
                a.finished_product_code FROM {0} as a left join 
                matter_list as b on a.matter_code = b.bom_matter_code 
                left join person_matter as c on c.matter_code = a.matter_code 
                left join work_station as d on d.work_code = a.work_code where 2 > 1 {1} {2}
                """
                sql = sql.format(table_one, finished_product_code_sql, matter_id_sql)
                drs = db.execute_sql(conn, sql)
                for dr in drs:
                    dict_data = {}
                    dict_data["matter_name"] = dr[0]
                    dict_data["matter_id"] = dr[1]
                    dict_data["rule"] = dr[2]
                    dict_data["matter_category"] = dr[3]
                    s2 = dr[4]
                    if s2:
                        s2 = s2.strftime("%Y-%m-%d %H:%M:%S ")
                    dict_data["product_time"] = s2
                    dict_data["work_name"] = dr[5]
                    dict_data["user_code"] = dr[6]
                    s = dr[7]
                    if s:
                        s = s.strftime("%Y-%m-%d %H:%M:%S ")
                    dict_data["out_time"] = s
                    dict_data["finished_product_code"] = dr[8]
                    data_list.append(dict_data)
            data = data_list
            sql_num = int(len(data_list))
            data_add_int["data"] = data
            data_add_int["total"] = sql_num
            result = {"code": 0, "message": "操作成功", "data": data_add_int}
            result = json.dumps(result)
            return HttpResponse(result)
        except Exception as e:
            print(e)
            data = {"code": 1, "message": "操作失败"}
            data = json.dumps(data)
            logger.error("查询物料信息失败,%s" % e)
            return HttpResponse(data)


class NoPageProductInfoSearch(View):
    def get(self, request):
        try:
            data_add_int = {}
            db = DB()
            data_list = []
            product_id = request.session.get("session_projectId")
            finished_product_code = request.GET.get("finished_product_code")
            matter_id = request.GET.get("matter_id")
            #
            # page = 1
            # page_size = 100
            # product_id = "pen"
            # finished_product_code = ""
            # matter_id = "volk3e-21dfsds"
            conn = db.get_connection(product_id)
            if finished_product_code:
                finished_product_code_sql = "and finished_product_code = " + "'" + finished_product_code + "'"
            else:
                finished_product_code_sql = ""
            if matter_id:
                matter_get_product_code = ""
                sql_table = """
                            show tables like "product_transit_%" 
                            """
                table_list = db.execute_sql(conn, sql_table)
                for table_type in table_list:
                    table_one = table_type[0]
                    sql = """
                    select finished_product_code from {0} where matter_id = '{1}'
                    """
                    sql = sql.format(table_one, matter_id)
                    finisheds = db.execute_sql(conn, sql)
                    if finisheds:
                        matter_get_product_code = finisheds[0][0]
                    else:
                        pass
                matter_id_sql = "and finished_product_code = " + "'" + matter_get_product_code + "'"
            else:
                matter_id_sql = ""

            conn_db = db.get_connection("db_common")

            sql_table1 = """
            select rule from productlist where product_id = '{0}'
            """
            sql_table1 = sql_table1.format(product_id)
            drs = db.execute_sql(conn_db, sql_table1)
            rule = drs[0][0]
            sql_enter_storage = """
            SELECT a.product_name, b.finished_product_code,a.status,a.pack_id, a.enter_time
            FROM enter_storage_status as a left join enter_storage as b on a.pack_id = b.pack_id
            where 2>1 {0} {1};
            """
            sql_enter_storage = sql_enter_storage.format(finished_product_code_sql, matter_id_sql)
            dfs = db.execute_sql(conn, sql_enter_storage)
            for df in dfs:
                data_dict = {}
                data_dict["product_name"] = df[0]
                data_dict["finished_product_code"] = df[1]
                data_dict["rule"] = rule
                data_dict["status"] = df[2]
                data_dict["pack_id"] = df[3]
                s = df[4]
                if s:
                    s = s.strftime("%Y-%m-%d %H:%M:%S ")
                else:
                    s = ""
                data_dict["enter_time"] = s
                sql_table = """
                            show tables like "product_transit_%" 
                            """
                table_list = db.execute_sql(conn, sql_table)

                finish_matter_list = []
                for table_type in table_list:
                    table_one = table_type[0]
                    sql = """
                    select matter_id from {0} where finished_product_code = '{1}'
                    """
                    sql = sql.format(table_one, df[1])
                    matters = db.execute_sql(conn, sql)
                    if matters:
                        for matter in matters:
                            finish_matter_list.append(matter[0])
                    else:
                        pass
                data_dict["response_datas"] = finish_matter_list

                data_list.append(data_dict)
            data = data_list
            sql_num = int(len(data_list))
            data_add_int["data"] = data
            data_add_int["total"] = sql_num
            result = {"code": 0, "message": "操作成功", "data": data_add_int}
            result = json.dumps(result)
            return HttpResponse(result)
        except Exception as e:
            print(e)
            data = {"code": 1, "message": "操作失败"}
            data = json.dumps(data)
            logger.error("查询物产品信息失败,%s" % e)
            return HttpResponse(data)


class OperationSystem(View):
    def get(self, request):
        try:
            data_list = []
            data_add_int = {}
            db = DB()
            product_id = request.session.get("session_projectId")
            conn = db.get_connection(product_id)
            # work_id = request.GET.get("work_id")

            page = int(request.GET.get("page"))
            page_size = int(request.GET.get("page_size"))

            # if work_id:
            #     work_id_sql = "and work_id = " + "'" + work_id + "'"
            # else:
            #     work_id_sql = ""

            sql = """
                    select * from operate where 2 > 1
                   """

            # sql_main = sql.format(work_id_sql)

            drs = db.execute_sql(conn, sql)

            if drs:
                for dr in drs:
                    dict_data = {}
                    dict_data["ID"] = dr[0]
                    dict_data["Package_Qty"] = dr[1]
                    dict_data["Rv"] = dr[2]
                    dict_data["Itemcode_C_Shipping"] = dr[3]
                    dict_data["Supplier"] = dr[4]
                    dict_data["No_Ship"] = dr[5]
                    dict_data["CS_type"] = dr[6]
                    dict_data["Shipping_SN_length"] = dr[7]
                    data_list.append(dict_data)
                    # dict_data["product_status"] = dr[4]
                    # dict_data["description"] = dr[5]

                page_result = Page(page, page_size, data_list)
                data = page_result.get_str_json()
                sql_num = """
                            select count(*) from operate where 2 > 1
                            """
                # sql_num_main = sql_num.format(work_id_sql)

                dfs = db.execute_sql(conn, sql_num)
                if dfs:
                    sql_num_int = dfs[0][0]
                else:
                    sql_num_int = 0
                data_add_int["data"] = data
                data_add_int["total"] = sql_num_int
            else:
                data_add_int["data"] = []
                data_add_int["total"] = 0

            result = {"code": 0, "message": "操作成功", "data": data_add_int}
            result = json.dumps(result)
            return HttpResponse(result)

        except Exception as e:
            print(e)
            result = {"code": 1, "message": "操作失败", "data": e}
            result = json.dumps(result)
            return HttpResponse(result)

    def post(self, request):
        try:
            json_data = request.body
            str_data = json.loads(json_data)

            db = DB()
            product_id = request.session.get("session_projectId")
            conn = db.get_connection(product_id)

            sql_matter = """
                   SELECT max(order_number) FROM operate;
                   """
            matter_type = db.execute_sql(conn, sql_matter)
            if matter_type[0][0] == None:
                matter_num = 1
            else:
                matter_num = matter_type[0][0] + 1
            # id = str_data.get("ID")
            Package_Qty = str_data.get("Package_Qty")
            Rv = str_data.get("Rv")
            Itemcode_C_Shipping = str_data.get("Itemcode_C_Shipping")
            Supplier = str_data.get("Supplier")
            No_Ship = str_data.get("No_Ship")
            CS_type = str_data.get("CS_type")
            Shipping_SN_length = str_data.get("Shipping_SN_length")

            print("========================>", matter_num, Package_Qty, Rv, Itemcode_C_Shipping, Supplier, No_Ship,CS_type, Shipping_SN_length)

            sql_insert = """
                               insert into operate(ID, Package_Qty,
                               Rv,
                               Itemcode_C_Shipping, Supplier, No_Ship, CS_type, Shipping_SN_length, order_number)
                               values('{0}', '{1}', '{2}', '{3}', '{4}', '{5}', '{6}', '{7}', '{8}')
                               """
            sql_insert_format = sql_insert.format(matter_num, Package_Qty,
                                                  Rv, Itemcode_C_Shipping,
                                                  Supplier, No_Ship, CS_type, Shipping_SN_length, matter_num)
            drs = db.execute_sql(conn, sql_insert_format)

            data = {"code": 0, "message": "操作成功"}
            logger.info("OperationSystem接口操作成功")
            data = json.dumps(data)

            return HttpResponse(data)
        except Exception as e:
            print(e)
            data = {"code": 1, "message": "操作失败"}
            logger.error("OperationSystem接口操作失败")
            data = json.dumps(data)
            return HttpResponse(data)


class PutOperationSystem(View):
    def get(self, request):
        try:
            db = DB()
            product_id = request.session.get("session_projectId")
            conn = db.get_connection(product_id)
            ID = request.GET.get("ID")
            Package_Qty = request.GET.get("Package_Qty")
            Rv = request.GET.get("Rv")
            Itemcode_C_Shipping = request.GET.get("Itemcode_C_Shipping")
            Supplier = request.GET.get("Supplier")
            No_Ship = request.GET.get("No_Ship")
            CS_type = request.GET.get("CS_type")
            Shipping_SN_length = request.GET.get("Shipping_SN_length")
            sql = """
                   update operate set
                  Package_Qty='{0}',Rv='{1}',Itemcode_C_Shipping='{2}',Supplier='{3}',
                  No_Ship='{4}',CS_type='{5}', Shipping_SN_length='{6}' where ID = '{7}'
                   """
            sql = sql.format(Package_Qty, Rv, Itemcode_C_Shipping, Supplier, No_Ship, CS_type, Shipping_SN_length, ID)
            drs = db.execute_sql(conn, sql)
            result = {"code": 0, "message": "操作成功"}
            result = json.dumps(result)
            return HttpResponse(result)

        except Exception as e:
            print(e)
            result = {"code": 1, "message": "操作失败", "data": e}
            result = json.dumps(result)
            return HttpResponse(result)


class DeleteOperationSystem(View):
    def get(self, request):
        try:
            db = DB()
            product_id = request.session.get("session_projectId")
            conn = db.get_connection(product_id)
            ID = request.GET.get("ID")
            sql = """
                   delete from operate where ID = '{0}'
                   """
            sql = sql.format(ID)
            drs = db.execute_sql(conn, sql)
            result = {"code": 0, "message": "操作成功"}
            result = json.dumps(result)
            return HttpResponse(result)

        except Exception as e:
            print(e)
            result = {"code": 1, "message": "操作失败", "data": e}
            result = json.dumps(result)
            return HttpResponse(result)


class AddModel(View):
    def post(self, request):
        try:
            db = DB()
            product_id = request.session.get("session_projectId")
            conn = db.get_connection(product_id)
            print(product_id)
            type_name = request.POST.get("fileType")
            f = request.FILES.get("file")  # 接收前端的文件
            print("==========>>>>>>>>>>>>>>>>>", f)
            print("----------------->>>>>>>>>>>>>>>>>>",type_name)
            BASE_DIR = Path(__file__).resolve().parent.parent
            path_workstation = os.path.join(BASE_DIR, "media")
            print(path_workstation)
            excit_psth = os.path.join(path_workstation, product_id)
            print(excit_psth)
            if product_id:
                if "txt" in str(f).split("."):
                    sql_create = """
                    CREATE TABLE IF NOT EXISTS project_model(id int AUTO_INCREMENT primary key not null, 
                                              product_id varchar(255),
                                              model_name varchar(255),
                                              type_name varchar(255))
                    """
                    db.execute_sql(conn, sql_create)

                    sql_check = """
                    select * from project_model where product_id = "{0}" and type_name = "{1}"
                    """
                    sql_check = sql_check.format(product_id, type_name)
                    drs = db.execute_sql(conn, sql_check)

                    if drs:
                        result = {"code": 1, "message": "上传的txt文件已经存在，请先删除再添加"}
                        result = json.dumps(result)

                    else:
                        sql_insert = """
                        insert into project_model(product_id, model_name,
                                       type_name)
                                       values('{0}', '{1}', '{2}')
                        """
                        print(product_id)
                        print(f.name)
                        print(type_name)

                        sql_insert = sql_insert.format(product_id, f.name, type_name)
                        print("----------->", sql_insert)

                        db.execute_sql(conn, sql_insert)
                        if os.path.exists(excit_psth):  # 如果存在文件夹的话就将文件放入文件夹下
                            with open(os.path.join(excit_psth, f.name), "wb+") as k:
                                for chunk in f.chunks():
                                    k.write(chunk)
                            print("okkkkkk")
                        else:
                            os.makedirs(excit_psth)   # 如果不存在文件夹的话就创建文件夹再将文件放到下面

                            with open(os.path.join(excit_psth, f.name), "wb+") as k:
                                for chunk in f.chunks():
                                    k.write(chunk)
                            print(excit_psth, "已经创建,已经成功加入")
                        #
                        # path_file = os.path.join(BASE_DIR, r"utils\import_common.py")
                        #
                        # with open(os.path.join(excit_psth, f.name), "r", encoding="utf-8") as w:
                        #     datas = w.readlines()
                        # with open(path_file, "a+", encoding="utf-8") as file:
                        #     for data in datas:
                        #         file.write(data)
                        # print("start-----------")
                        # print("end--------------")

                        result = {"code": 0, "message": "操作成功"}
                        result = json.dumps(result)

                else:
                    if os.path.exists(excit_psth):  # 如果存在文件夹的话就将文件放入文件夹下
                        with open(os.path.join(excit_psth, f.name), "wb+") as k:
                            for chunk in f.chunks():
                                k.write(chunk)
                        print("okkkkkk")
                    else:
                        os.makedirs(excit_psth)  # 如果不存在文件夹的话就创建文件夹再将文件放到下面

                        with open(os.path.join(excit_psth, f.name), "wb+") as k:
                            for chunk in f.chunks():
                                k.write(chunk)
                        print(excit_psth, "已经创建,已经成功加入")
                    result = {"code": 0, "message": "操作成功"}
                    result = json.dumps(result)


            else:
                result = {"code": 1, "message": "session过期，没有项目，请重新登录"}
                result = json.dumps(result)

            return HttpResponse(result)

        except Exception as e:
            print(e)
            result = {"code": 1, "message": "操作失败", "data": e}
            result = json.dumps(result)
            return HttpResponse(result)


class test(View):
    def get(self, request):
        try:
            BASE_DIR = Path(__file__).resolve().parent.parent
            path_file = os.path.join(BASE_DIR, r"utils\import_common.py")

            result = {"code": 0, "message": "操作成功"}
            result = json.dumps(result)
            return HttpResponse(result)

        except Exception as e:
            print(e)
            result = {"code": 1, "message": "操作失败", "data": e}
            result = json.dumps(result)
            return HttpResponse(result)


class PrintApai(View):
    def get(self, request):
        try:
            db = DB()
            product_id = request.session.get("session_projectId")


            # product_id = "kbvnt"
            # work_id = "jibg_o"

            conn = db.get_connection(product_id)
            type_name = request.GET.get("fileType")

            work_id = request.session.get('session_workId')
            BASE_DIR = Path(__file__).resolve().parent.parent
            path_workstation = os.path.join(BASE_DIR, "media")
            store_work = str(product_id) + "_" + str(work_id)
            print_path = os.path.join(path_workstation, store_work)
            # stem1 = request.GET.get("stem1")
            # stem2 = request.GET.get("stem2")
            # stem3 = request.GET.get("stem3")
            # stem4 = request.GET.get("stem4")
            # stem5 = request.GET.get("stem5")
            # stem6 = request.GET.get("stem6")

            print(print_path)

            print("==>", type_name)
            # print("==>", stem1)
            # print("==>", stem2)
            # print("==>", stem3)
            # print("==>", stem4)
            # print("==>", stem5)
            # print("==>", stem6)

            if os.path.exists(print_path):
                pass
            else:
                os.makedirs(print_path)

            if type_name == "box_code":
                stem1 = request.GET.get("stem1")
                sql = """
                            select model_name from project_model where product_id = "{0}" and type_name = "{1}"        
                            """
                sql = sql.format(product_id, type_name)

                print("==>", sql)
                drs = db.execute_sql(conn, sql)
                print(drs)
                if drs[0][0]:
                    print("------", drs[0][0])
                    model_name = drs[0][0]
                    print(path_workstation)
                    file_path1 = os.path.join(path_workstation, product_id)
                    file_path = os.path.join(file_path1, model_name)
                    print("--->>>", file_path)
                    with open(file_path, "r", encoding="utf-8") as f:
                        str1 = f.read()
                        str2 = str1.replace("{0}", stem1)
                    print_file_path = os.path.join(print_path, model_name)
                    print("==========>>>>>>>>>>>>>>>>>>>>>>>", print_file_path)
                    with open(print_file_path, "w+", encoding="utf-8") as k:
                        k.write(str2)
                    data = "print_file_path"
                    result = {"code": 0, "message": "操作成功", "data": data}
                    result = json.dumps(result)
                    return HttpResponse(result)
                else:
                    result = {"code": 1, "message": "请先上传txt模板文件"}
                    result = json.dumps(result)
                    return HttpResponse(result)

            elif type_name == "matter_code":
                print("===============>", "matter_code")
                stem1 = request.GET.get("stem1")
                stem2 = request.GET.get("stem2")
                stem3 = request.GET.get("stem3")
                stem4 = request.GET.get("stem4")
                stem5 = request.GET.get("stem5")
                stem6 = request.GET.get("stem6")
                sql = """
                    select model_name from project_model where product_id = "{0}" and type_name = "{1}"        
                    """
                sql = sql.format(product_id, type_name)

                print("==>", sql)
                drs = db.execute_sql(conn, sql)
                print(drs)
                if drs[0][0]:
                    print("------", drs[0][0])
                    model_name = drs[0][0]
                    print(path_workstation)
                    file_path1 = os.path.join(path_workstation, product_id)
                    file_path = os.path.join(file_path1, model_name)
                    print("--->>>", file_path)
                    with open(file_path, "r", encoding="utf-8") as f:
                        str1 = f.read()
                        str2 = str1.replace("{0}", stem1)
                        str2 = str2.replace("{1}", stem2)
                        str2 = str2.replace("{2}", stem3)
                        str2 = str2.replace("{3}", stem4)
                        str2 = str2.replace("{4}", stem5)
                        str2 = str2.replace("{5}", stem6)
                    print_file_path = os.path.join(print_path, model_name)
                    print("==========>>>>>>>>>>>>>>>>>>>>>>>", print_file_path)
                    with open(print_file_path, "w+", encoding="utf-8") as k:
                        k.write(str2)
                    data = "print_file_path"

                    print("start---->")

                    # os.system("\\10.0.20.107 d:\print.bat")
                    # ip = "10.0.20.107"
                    # username = "Weber.Zhang"
                    # password = "Zhangxy123!@#"
                    # pythoncom.CoInitialize()
                    # conn = wmi.WMI(computer=ip, user=username, password=password)
                    # file_name = r"d:\print.bat"
                    # cmd_callbat = r"cmd /c call %s" % file_name
                    # conn.Win32_Process.Create(CommandLine=cmd_callbat)
                    print("执行成功!")


                    print("end---->")

                    result = {"code": 0, "message": "操作成功", "data": data}
                    result = json.dumps(result)
                    return HttpResponse(result)
                else:
                    result = {"code": 1, "message": "请先上传txt模板文件"}
                    result = json.dumps(result)
                    return HttpResponse(result)

            elif type_name == "deliver_goods_code":
                stem1 = request.GET.get("stem1")
                stem2 = request.GET.get("stem2")
                stem3 = request.GET.get("stem3")
                stem4 = request.GET.get("stem4")
                stem5 = request.GET.get("stem5")
                stem6 = request.GET.get("stem6")
                sql = """
                    select model_name from project_model where product_id = "{0}" and type_name = "{1}"        
                    """
                sql = sql.format(product_id, type_name)

                print("==>", sql)
                drs = db.execute_sql(conn, sql)
                print(drs)
                if drs[0][0]:
                    print("------", drs[0][0])
                    model_name = drs[0][0]
                    print(path_workstation)
                    file_path1 = os.path.join(path_workstation, product_id)
                    file_path = os.path.join(file_path1, model_name)
                    print("--->>>", file_path)
                    with open(file_path, "r", encoding="utf-8") as f:
                        str1 = f.read()
                        str2 = str1.replace("{0}", stem1)
                        str2 = str2.replace("{1}", stem2)
                        str2 = str2.replace("{2}", stem3)
                        str2 = str2.replace("{3}", stem4)
                        str2 = str2.replace("{4}", stem5)
                        str2 = str2.replace("{5}", stem6)
                    print_file_path = os.path.join(print_path, model_name)
                    print("==========>>>>>>>>>>>>>>>>>>>>>>>", print_file_path)
                    with open(print_file_path, "w+", encoding="utf-8") as k:
                        k.write(str2)
                    data = "print_file_path"
                    result = {"code": 0, "message": "操作成功", "data": data}
                    result = json.dumps(result)
                    return HttpResponse(result)
                else:
                    result = {"code": 1, "message": "请先上传txt模板文件"}
                    result = json.dumps(result)
                    return HttpResponse(result)
                #
                # result = {"code": 0, "message": "操作成功"}
                # result = json.dumps(result)
                # return HttpResponse(result)




        except Exception as e:
            print(e)
            result = {"code": 1, "message": "操作失败"}
            result = json.dumps(result)
            return HttpResponse(result)




















































































































