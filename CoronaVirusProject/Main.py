import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#map bubble chart ///////////////////////////////

data = pd.read_csv('novel-corona-virus-2019-dataset/COVID19_open_line_list.csv')
df = pd.DataFrame(data)
print(df.tail(10))
#df['text'] = df['country'] + '<br>numbers ' + (df['country'].value_counts()/1e6).astype(str)+' case'
limits = [(0,100),(101,200),(201,300),(301,400),(401,500),(501,600),(601,700),(701,800),(801,10500)]
colors = ["royalblue","crimson","lightseagreen","orange","lightgrey","blue","lightblue","purple","red"]
cities = []
scale = 5000
fig = go.Figure()
print(df.columns)
for i in range(len(limits)):
    lim = limits[i]
    df_sub = df[lim[0]:lim[1]]
    fig.add_trace(go.Scattergeo(
        lon = df_sub['longitude'],
        lat = df_sub['latitude'],
        text =df_sub['city'],
        marker = dict(
            #size = df_sub['country'].value_counts(),
            color = colors[i],
            line_color='rgb(40,40,40)',
            line_width=0.5,
            sizemode = 'area'
        ),
        name = '{0} - {1} '.format(lim[0],lim[1])))

fig.update_layout(
        title_text = 'Corona Virus Spreading analysis<br>',
        showlegend = True,
        geo = dict(
            landcolor = 'rgb(217, 217, 217)',
        )
    )

fig.show()