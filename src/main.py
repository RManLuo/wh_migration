#!/usr/bin/python3
# -*-coding:utf-8 -*-
# Reference:**********************************************
# @Time     : 2020/1/31
# @Author   : Raymond Luo
# @File     : main.py
# @User     : luoli
# @Software: vscode
# Reference:**********************************************
import requests
import csv
import os
import json
from datetime import datetime, timedelta


class Spider():
    '''
    爬取武汉迁出信息
    '''

    def __init__(self, outputDir='../data/migration.csv'):
        self.apiUrl = "https://huiyan.baidu.com/migration/cityrank.jsonp?dt=city&id=420100&type=move_out&date={}"  # 百度迁徙数据api
        self.outputDir = outputDir
        # 完善header
        self.header = {'Upgrade-Insecure-Requests': '1',
                       'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
                       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                       'Referer': self.apiUrl,
                       'Accept-Encoding': 'gzip, deflate, sdch',
                       'Accept-Language': 'zh-CN,zh;q=0.8',
                       }

    def download(self, startDate, endDate):
        '''
        下载指定日期的数据
        startDate: yyyy-mm-dd
        ennDate: yyyy-mm-dd
        '''
        date = datetime.strptime(startDate, "%Y%m%d")
        end = datetime.strptime(endDate, "%Y%m%d")
        final_list = []
        while date <= end:
            currentDate = date.strftime('%Y%m%d')
            print(currentDate)
            date = date + timedelta(days=1)
            url = self.apiUrl.format(currentDate)
            # 请求API
            res = requests.get(url, headers=self.header)
            try:
                city_list = json.loads(res.text[3:-1])['data']['list']
                result = [currentDate, '武汉']
                for data in city_list:
                    result.append(data['city_name'])
                    result.append(data['value'])
                final_list.append(result)
            except Exception as e:
                print(e)

        with open(self.outputDir, 'w', encoding='utf-8-sig', newline='') as outFileCsv:
            writer = csv.writer(outFileCsv)
            # 表头
            result = ['date', 'startCity']
            for i in range(1, 51):
                result.append("endCity"+str(i))
                result.append("ratio"+str(i))
            writer.writerow(result)
            writer = csv.writer(outFileCsv)
            # 数据
            writer.writerows(final_list)

if __name__ == "__main__":
    spider = Spider()
    spider.download('20200101', '20200130')
