#!/usr/bin/env python
# -*- coding:utf-8 -*-
import json
import unittest
import warnings
from ast import literal_eval

from common.common import *
from common.configHttp import ConfigHttp
from common.log import MyLog



logger = MyLog.get_log().logger
configHttp = ConfigHttp()



class AddChildTask(unittest.TestCase):
    """新增子任务"""
    def setUp(self):
        logger.info('*****启动testAddChildTask用例*****')
        warnings.simplefilter('ignore',ResourceWarning)
        #读取该sheet页的所有用例数据
        self.data_list = get_xls("test-data.xlsx","testUserSearch")


    def test_add_child_task(self):

        """新增子任务接口"""
        # 请求参数
        case_data = get_test_data(self.data_list,"testaddChildTask")
        if not case_data:
            logger.info("用例不存在")

        # 接口路径
        url = case_data.get('url')
        data = eval(case_data.get('data'))
        headers = eval(case_data.get('headers'))

        logger.info(data)
        logger.info(url)


        # 调用configHttp的相关方法
        self.url = configHttp.set_url(url)
        print("self.url:"+self.url)
        self.data =configHttp.set_data(data)
        print(type(self.data))
        self.headers =configHttp.set_headers(headers)

        """ print(configHttp.post())"""
        res = configHttp.post()


        logger.info(res.url)
        logger.info(res.text)
        """result_json = json.dumps(result)"""
        logger.info(res)
        print(res.text)
        print(res.status_code)
        # 判断字段是否存在与json中
        if res.status_code == 200 :
            logger.info('新增成功!')
            pass
        else:
            logger.info('新增失败!')


    def tearDown(self):
        print('*****销毁Add用例*****')

