import pandas as pd
import numpy as np
import plotly.express as px
import streamlit as st
import os

#1. load the data
def load_data():
    df= pd.read_excel('canada.xlsx',
                      sheet_name=1,
                      skiprows=20,
                      skipfooter=2)
    
    #rename columns
    df = df.rename(columns={
        'OdName'   : 'country',
        'AreaName':'continent',
        'RegName'  :'region',
        'DevName'  :'status'
    })
    #add a total column
    years = list(range(1980,2014))
    df['total'] = df[years].sum(axis=1)
    df.set_index('country',inplace=True)
    return df