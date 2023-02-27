#!/usr/bin/python
# -*- coding: utf-8 -*-


import requests as requests
import pdfkit
from bs4 import BeautifulSoup
import json
import sqlite3 as sl
import urllib.parse
import time
import os

SESSID = os.getenv('SPONSR_SESSID')
UUIDNA = os.getenv('SPONSR_UUIDNA')
LASTEMAIL = os.getenv('SPONSR_LASTEMAIL')
USERID = os.getenv('SPONSR_USERID')
PROJECTDESC_KEY = os.getenv('SPONSR_PROJECTDESC_KEY')
PROJECTDESC_VALUE = os.getenv('SPONSR_PROJECTDESC_VALUE')
USERAGENT = os.getenv('SPONSR_USERAGENT')
PROJECTID = os.getenv('SPONSR_PROJECTID')

if __name__ == '__main__':
    con = sl.connect('sponsrru-collector.db')
    insert_query = """
        INSERT OR REPLACE INTO project_name 
        (post_id, post_date, post_title, post_status, post_views, 
        post_access_type, post_access_value, access_type, access_value,
        level_price, level_name, 
        post_duration_podcast, post_duration_text, post_duration_video,
        post_url) 
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"""

    host = 'https://sponsr.ru'
    # response rows only 20 (09.12.2022 max posts count is 345)
    maxOffset = 340

    # +1 for maxOffset will be inclusive
    for currentOffset in range(0, maxOffset+1, 20):
        time.sleep(10)
        requestUrl = host + '/project/'+PROJECTID+'/more-posts/?offset='+str(currentOffset)
        headers = {
            'Cookie': 'SESSID='+SESSID+'; uuid_na='+UUIDNA+'; last_email='+LASTEMAIL+'; user_id='+USERID+'; '+PROJECTDESC_KEY+'='+PROJECTDESC_VALUE,
            'User-Agent': USERAGENT,
        }
        response = requests.get(requestUrl, headers=headers)
        print('Response status: ' + str(response))
        print('Response body: ' + str(response.text))
        data = json.loads(response.text)
        print('Data: ' + str(data))

        dbdata = []
        for row in data['response']['rows']:
            dbdata.append((
                row['post_id'],
                row['post_date'],
                row['post_title'],
                row['post_status'],
                row['post_views'],
                row['post_access_type'],
                row['post_access_value'],
                row['access_type'],
                row['access_value'],
                row['level_price'],
                row['level_name'],
                row['post_duration_podcast'],
                row['post_duration_text'],
                row['post_duration_video'],
                row['post_url'],
            ))

        with con:
            con.executemany(insert_query, dbdata)

    # article_url = host + str(data['response']['rows'][15]['post_url'])
    # print(article_url)
    # print('Article id: ' + str(data['response']['rows'][15]['post_id']))
    # response = requests.get(article_url, headers=headers)
    # with open('Input.html', 'w', encoding="utf-8") as file:
    #     file.write(response.text)
    # finish = pdfkit.from_url('Input.html', 'Output.pdf')
    # print(finish)
    # data['response']['rows'][15]
    # 'post_url'
    # 'post_id'
    # 'level_id'
    # {'post_id': 00000, 'project_id': 000, 'level_id': 000, 'post_date': '2022-01-01T00:00:00.000Z', 'post_title': 'Post Title', 'post_teaser': None, 'post_name_type': None, 'post_image': '/images/projects/000/000/aa/aa/aa//000000.jpg', 'post_status': 'active', 'post_views': 000000, 'post_cnt_comments': 0, 'post_cnt_likes': 0, 'post_extended_view': 0, 'post_access_type': None, 'post_access_value': 0, 'access_type': 'active', 'access_value': 000, 'post_poll': None, 'level_price': 0000, 'level_name': 'Level name', 'project_url': 'customprojectname', 'project_comment_disable': 1, 'project_like_disable': 1, 'project_views_disable': 1, 'project_logo': {'1x': '/images/projects/000/000/logo.webp', '2x': '/images/projects/000/000/logo@2x.webp'}, 'project_title': 'Custom Project Title', 'tag_ids': [], 'files': None, 'post_duration_podcast': 0, 'post_duration_text': 1000, 'post_duration_video': 0, '_user_is_smart_date': False, '_like': False, 'post_url': '/customprojectname/00000/ArticleTitle', '_editable': False, 'level_limit': None, 'user_place': False, 'level_subscribers': 0000, '_available_after_sub': False, '_available': False, 'post_lock_photo': '/images/projects/000/000/aa/aa/aa//000000000.jpg', 'post_small_text': 'small article text annotation', 'tags': []}
    # host +

