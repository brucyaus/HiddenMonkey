import scrapy
import time
import re
import MySQLdb


class HiddenMonkeySpider(scrapy.Spider):
    db = MySQLdb.connect(host="localhost", user="root", passwd="adaymaycomewhen", db="hidden_monkey")
    db_cur = db.cursor()
    db_cur.execute('SELECT video_url,video_id FROM video_list;')
    start_urls = []
    video_list = db_cur.fetchall()
    for row in video_list:
        start_urls.append(row[0])
    db.close()
    name = "YouTube"
    allowed_domains = ["www.youtube.com"]


    def parse(self, response):
        insert_sql = "INSERT INTO video_stats(video_id , video_views , time_collected) "
        db = MySQLdb.connect(host="localhost", user="root", passwd="adaymaycomewhen", db="hidden_monkey")
        db_cur = db.cursor()

        views = response.css('div .watch-view-count::text').extract()
        view_string = str(views)
        view_count = ""
        for i in re.findall(r'\b\d+\b', view_string):
            print(i)
            view_count = view_count + str(i)
        print("*****---->>> views ="+view_count)
        this_time = str(time.time())

        sub_query_for_id = "(SELECT video_id FROM video_list WHERE video_url='"+response.url+"')"
        print(insert_sql+"VALUE( "+sub_query_for_id+" , " +view_count + " , '" + this_time + "')")
        db_cur.execute(insert_sql+"VALUE( "+sub_query_for_id+" , " +view_count + " , '" + this_time + "')")
        print("******----->>>"+view_count+"\n")
        print("******----->>>"+this_time)
        db.commit()
        db.close()

