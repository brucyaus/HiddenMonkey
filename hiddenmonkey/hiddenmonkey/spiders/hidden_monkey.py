import scrapy
import time
import re
import MySQLdb


class HiddenMonkeySpider(scrapy.Spider):
    db = MySQLdb.connect(host="localhost", user="root", passwd="adaymaycomewhen", db="hidden_monkey")
    db_cur = db.cursor()
    db_cur.execute('SELECT video_url FROM video_list;')
    start_urls = []
    for row in db_cur.fetchall() :
        start_urls.append(row[0])

    name = "YouTube"
    allowed_domains = ["www.youtube.com"]


    def parse(self, response):
        views = response.css('div .watch-view-count::text').extract()
        log_file = open('log', 'a')
        db = MySQLdb.connect(host="localhost", user="root", passwd="adaymaycomewhen", db="hidden_monkey")
        cur = db.cursor()
        cur.execute('INSERT INTO video_stats(video_id,video_url) VALUES;')
        viewsString = str(views)
        thisTime = str(time.time())

        log_file.write(viewsString + thisTime)
        log_file.close()