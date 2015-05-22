#!/usr/bin/python
import MySQLdb
import pandas as pd
import plotly.plotly as py
import time
from plotly.graph_objs import *


def format_rows(rows_in):
    out_rows = []
    for video in rows_in:
        this_row = (video[0], int(float(video[1]) * 100))
        out_rows.append(this_row)
    return out_rows


def create_graph():
    py.sign_in("mon0051", "gz29ruk9zp")
    db = MySQLdb.connect(host="localhost", user="root", passwd="adaymaycomewhen", db="hidden_monkey")
    cursor = db.cursor()
    sql = """ SELECT video_views,time_collected
                FROM video_stats WHERE video_id ="""
    sql_end = """ORDER BY time_collected ASC; """
    full_sql = ""
    for i in range(1, 19):
        full_sql = sql + str(i) + sql_end
        cursor.execute(full_sql)
        rows = cursor.fetchall()
        data_frame = pd.DataFrame(columns={'views', 'time_collected'}, data=format_rows(rows))
        trace1 = Scatter(x=data_frame['views'], y=data_frame['time_collected'])
        # layout = Layout(title="YouTube Views over time", xaxis=XAxis(title="Time"), yaxis=YAxis(title="Views"))
        data = Data([trace1])
        #fig = Figure(data=data, layout=layout)
        py.plot(data, filename="Video_id" + i + str(time.time()))


create_graph()