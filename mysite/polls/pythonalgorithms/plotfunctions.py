import pandas as pd
import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from termcolor import colored

colors = {'b':'blue','r':'red','n':'grey'}


def plot_side_to_side_dice(xatt,y1,y2,y3,title = "Graph",blue = "Blue Player",red = "Red Player" ):
    
    fig = make_subplots(rows=1, cols=1)

    fig.add_trace(
        go.Bar(
        name = blue,
        x = xatt,
        y = y1,
        marker_color=colors["b"],
        opacity=0.8
       ),
        row=1, col=1
    )
    fig.add_trace(
        go.Bar(
        name = 'Neutre',
        x = xatt,
        y = y2,
        marker_color=colors["n"],
        opacity=0.8
       ),
        row=1, col=1
    )
    fig.add_trace(
        go.Bar(
        name = red,
        x = xatt,
        y = y3,
        marker_color=colors["r"],
        opacity=0.8
       ),
        row=1, col=1)

    fig.update_layout(title_text=title ,xaxis=dict(showgrid=False),yaxis=dict(showgrid=False))
    fig.write_image("././polls/static/graphs/{}{}.jpeg".format(title), scale=2, width=1100, height=700)        

    return fig

#Plot For ALL Dice player versus player

def subplot_all_dice(xatt,xdef,BlueListSize,RedListSize,attRedList,attBlackList,attWhiteList,defRedList,defWhiteList,title = "Graph",blue = "Blue Player",red = "Red Player" ):
    
    attRed1=attRedList[0]
    attRed2=attRedList[1]
    attRed3=attRedList[2]
    
    attBlack1=attBlackList[0]
    attBlack2=attBlackList[1]
    attBlack3=attBlackList[2]
    
    attWhite1=attWhiteList[0]
    attWhite2=attWhiteList[1]
    attWhite3=attWhiteList[2]
    
    defRed1=defRedList[0]
    defRed2=defRedList[1]
    defRed3=defRedList[2]
    
    defWhite1=defWhiteList[0]
    defWhite2=defWhiteList[1]
    defWhite3=defWhiteList[2]
    
    
    fig = make_subplots(rows=2, cols=3,subplot_titles=("Red Attack", "Black Attack", "White Attack", "Red Def", "", "White Def"))


    fig.add_trace(go.Bar(name = blue,x = xatt,y = attRed1,marker_color=colors["b"],opacity=BlueListSize[0],showlegend = True),row=1, col=1)
    fig.add_trace(go.Bar(name = 'Neutre',x = xatt,y = attRed2,marker_color=colors["n"],opacity=0.8,showlegend = True),row=1, col=1)
    fig.add_trace(go.Bar(name = red,x = xatt, y = attRed3,marker_color=colors["r"],opacity=RedListSize[0],showlegend = True),row=1, col=1)
    
    fig.add_trace(go.Bar(name = blue,x = xatt,y = attBlack1,marker_color=colors["b"],opacity=BlueListSize[1],showlegend = False),row=1, col=2)
    fig.add_trace(go.Bar(name = 'Neutre',x = xatt,y = attBlack2,marker_color=colors["n"],opacity=0.8,showlegend = False),row=1, col=2)
    fig.add_trace(go.Bar(name = red,x = xatt, y = attBlack3,marker_color=colors["r"],opacity=RedListSize[1],showlegend = False),row=1, col=2)
  
    fig.add_trace(go.Bar(name = blue,x = xatt,y = attWhite1,marker_color=colors["b"],opacity=BlueListSize[2],showlegend = False),row=1, col=3)
    fig.add_trace(go.Bar(name = 'Neutre',x = xatt,y = attWhite2,marker_color=colors["n"],opacity=0.8,showlegend = False),row=1, col=3)
    fig.add_trace(go.Bar(name = red,x = xatt, y = attWhite3,marker_color=colors["r"],opacity=RedListSize[2],showlegend = False),row=1, col=3)
  
    fig.add_trace(go.Bar(name = blue,x = xdef,y = defRed1,marker_color=colors["b"],opacity=BlueListSize[3],showlegend = False),row=2, col=1)
    fig.add_trace(go.Bar(name = 'Neutre',x = xdef,y = defRed2,marker_color=colors["n"],opacity=0.8,showlegend = False),row=2, col=1)
    fig.add_trace(go.Bar(name = red,x = xdef, y = defRed3,marker_color=colors["r"],opacity=RedListSize[3],showlegend = False),row=2, col=1)
    
    fig.add_trace(go.Bar(name = blue,x = xdef,y = defWhite1,marker_color=colors["b"],opacity=BlueListSize[4],showlegend = False),row=2, col=3)
    fig.add_trace(go.Bar(name = 'Neutre',x = xdef,y = defWhite2,marker_color=colors["n"],opacity=0.8,showlegend = False),row=2, col=3)
    fig.add_trace(go.Bar(name = red,x = xdef, y = defWhite3,marker_color=colors["r"],opacity=RedListSize[4],showlegend = False),row=2, col=3)
    
    fig.update_layout(title_text=title ,autosize=False,width=1000,height=600)
 
            
    fig.update_xaxes(tickangle = 45)
    fig.update_yaxes(tickangle = 45,showgrid=False,range=list([0,1]))
    
    fig.write_image("././polls/static/graphs/{}.jpeg".format(title), scale=2, width=1100, height=700)  

    return fig

def pie_chart(labelsFirtPie,labelsSecondPie,valueFirstPie,valueSecondPie,colorFirstPie,colorSecondPie, title = "graph",colorFirstPieText="black",colorSecondPieText="black",textFirstPie = 'BluePlayer',textSecondPie = 'RedPlayer',xTextFirstPie= 0.18,xTextSecondPie= 0.84):

    fig = make_subplots(rows=1, cols=2, specs=[[{'type':'domain'}, {'type':'domain'}]])

    fig.add_trace(go.Pie(labels=labelsFirtPie, 
                         values=valueFirstPie,
                         name="Dice Used",marker_colors=colorFirstPie),1, 1)
    
    fig.add_trace(go.Pie(labels=labelsSecondPie, 
                         values=valueSecondPie, 
                         name="Dice Used",marker_colors=colorSecondPie),1, 2)

    
    fig.update_traces(hole=.4, hoverinfo="label+name+value")

    fig.update_layout(
        title_text= title,
        annotations=[dict(text= textFirstPie, x=xTextFirstPie, y=0.5, font=dict(color=colorFirstPieText,size=14), showarrow=False),
                     dict(text= textSecondPie , x=xTextSecondPie, y=0.5, font=dict(color=colorSecondPieText,size=14), showarrow=False)])

    fig.write_image("././polls/static/graphs/{}.jpeg".format(title), scale=2, width=1100, height=700)  

    return fig



def heat_map(color , rounds,listUnits,mainUnitsListRoundTir,mainUnitsListRoundDef):

    # Create subplots: use 'domain' type for Pie subplot
    fig = make_subplots(rows=2, cols=1,subplot_titles=("Attack Activity", "Defence Activity"))

    fig.add_trace(go.Heatmap(x = rounds,y = listUnits,z = mainUnitsListRoundTir,type = 'heatmap',colorscale = 'plasma',colorbar=dict(title='Att'),colorbar_x=1.05)
                  ,1, 1)
    
    fig.add_trace(go.Heatmap(x = rounds,y = listUnits,z = mainUnitsListRoundDef,type = 'heatmap',colorscale = 'plasma',colorbar=dict(title='Def') ,colorbar_x=1.20 )
                  ,2, 1)



    fig.update_layout(title_text=str(color +" Tir and Defence throught rounds") ,autosize=False,width=800,height=800)
    fig.write_image("././polls/static/graphs/heatMap{}.jpeg".format(rounds), scale=2, width=1100, height=700)  
    
    return fig

def plot_for_luck_thorw(plotTitle,idx,fireGroupList,indexRound):
    fig = go.Figure()
    
    fig.add_trace(go.Scatter(x = idx,y = fireGroupList, mode = 'markers',showlegend=False,
                            marker = dict(color=list(map(SetColor, fireGroupList)))))

    fig.update_layout(plot_bgcolor='rgba(189, 207, 219,0.8)',title_text=plotTitle ,autosize=False,width=1000,height=500,xaxis=dict(visible = True,showgrid=False),yaxis=dict(showgrid=False))
    fig.update_xaxes(showticklabels=False,title_text="-------------------->     TIME LINE      -------------------->")
    fig.update_traces(marker={'size': 15})
    
    for i,number in enumerate(indexRound):
        roundNumber = str("Rnd "+str(i+1))
        fig.add_vline(x=number-0.5, line_width=3, line_color="blue", line_dash="dash",annotation_text=roundNumber, annotation_position="top",
              annotation=dict(font_size=20, font_family="Times New Roman"))

    fig.write_image("././polls/static/graphs/{}.jpeg".format(plotTitle), scale=2, width=1100, height=700)  
    return fig


def SetColor(x):
    if(x > 0.54):
        return "green"
    elif( x < 0.46 ):
        return "red"
    else:
        return "yellow"
