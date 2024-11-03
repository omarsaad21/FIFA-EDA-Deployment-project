import numpy as np 
import pandas as pd 
import plotly.express as px

df = pd.read_csv('Sources/fifa_cleaned.csv')

def best_10_players(col):
    '''
    
    '''
    df_top_10 = df.sort_values(by= col, ascending= False).head(10)
    fig = px.bar(df_top_10, x= 'name', y= col, color= col, color_continuous_scale= 'purp', \
                hover_data= ['club', 'nationality', 'preferred_foot', 'position'])
    fig.update_layout(title= {'text': f'Best 10 {col}', 'x': 0.5, 'y': 0.95})
    return fig