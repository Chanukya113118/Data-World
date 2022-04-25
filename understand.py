import pandas as pd
import streamlit as st
import plotly.express as plt
class analyse_class:
    def analyse_fun(data):
        data=data
        col1,col2=st.columns(2)
        if col1.button('Describe'):
            st.write(data.describe())
        if col2.button('Missing value Information'):
            st.write(data.isnull().sum())
        if col1.button('Correlation Values'):
            st.write(data.corr())
        if col2.button('Distribution'):
            opt=col1.selectbox('Choose column',options=data.columns)
            col1.write(plt.histogram(data[opt]))
            
