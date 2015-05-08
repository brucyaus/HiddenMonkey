#!/usr/bin/python
import MySQLdb
import pandas as pd
import plotly.plotly as py
from plotly.graph_objs import *
py.sign_in("mon0051","gz29ruk9zp")

db = MySQLdb.connect(host="localhost",user="root",passwd="adaymaycomewhen",db="hidden_monkey")
cursor = db.cursor()
cursor.execute("SELECT video_id, video_views,time_collected FROM video_stats WHERE video_id =4 ORDER BY time_collected ASC;")
rows = cursor.fetchall()

data_frame = pd.DataFrame([[ij for ij in i] for i in rows])
data_frame.rename(columns={0:"video_id",1:"video_views",2:"time_collected"})
video_ids = data_frame[0]
trace1 = Scatter(x=data_frame["time_collected"],y=data_frame["video_views"],text=data_frame,mode="markers")
layout = Layout(title="YouTube Views over time", xaxis=XAxis(title="Time"),yaxis=YAxis(title="Views"))
data = Data([trace1])
fig=Figure(data=data,layout=layout)
py.iplot(fig,filename="Video_id 1")