import requests as requests
import pdfkit
from bs4 import BeautifulSoup
import json
import sqlite3 as sl
import urllib.parse
import time
from datetime import datetime
import os

SESSID = os.getenv('SPONSR_SESSID')
UUIDNA = os.getenv('SPONSR_UUIDNA')
LASTEMAIL = os.getenv('SPONSR_LASTEMAIL')
USERID = os.getenv('SPONSR_USERID')
PROJECTDESC_KEY = os.getenv('SPONSR_PROJECTDESC_KEY')
PROJECTDESC_VALUE = os.getenv('SPONSR_PROJECTDESC_VALUE')
USERAGENT = os.getenv('SPONSR_USERAGENT')
PROJECTID = os.getenv('SPONSR_PROJECTID')

con = sl.connect('sponsrru-collector.db')

options = {
    'cookie': [
        ('last_email', LASTEMAIL),
        (PROJECTDESC_KEY, PROJECTDESC_VALUE),
        ('SESSID', SESSID),
        ('user_id', USERID),
        ('uuid_na', UUIDNA)
    ]
}

iteration = 0
with con:
    # res = con.execute("SELECT * FROM project_name ORDER BY post_id DESC LIMIT 5")
    # res = con.execute("SELECT * FROM project_name WHERE post_id = 24694")
    # res = con.execute("SELECT * FROM project_name WHERE post_id = 22582")
    res = con.execute("SELECT * FROM project_name")
    for row in res:
        time.sleep(5)
        post_id = row[0]
        iteration = iteration + 1
        print('Iteration: ' + str(iteration) + '; current post_id: ' + str(post_id))
        post_date = row[1]
        post_title = row[2]
        post_url = row[14]
        # print(post_id, post_date, post_title, post_url)
        datetime_object = datetime.fromisoformat(post_date[:-1] + '+00:00')
        # print(datetime_object)
        titleDate = str(datetime_object.date()) + ' ' + str(datetime_object.time().hour) + '.' + str(datetime_object.time().minute)
        # print(titleDate)
        pretty_title = "".join(x for x in post_title if x not in ['"', '\\', '/', ':', '*', '?', '<', '>', '|', '\n'])
        # print(post_title)
        # print(pretty_title)
        final_title = titleDate + ' ' + pretty_title
        print(final_title)
        # print('===================================')

        host = 'https://sponsr.ru'
        download_url = host+post_url
        print(download_url)
        pdf = pdfkit.from_url(download_url, final_title+'.pdf', options=options, verbose=True)
        # resp = requests.get(download_url, headers=headers, cookies=cookies)
        # with open(final_title+'.html', 'w', encoding="utf-8") as file:
        #     file.write(resp.text)



