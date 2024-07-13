import streamlit as st
import pandas as pd #for chart
import numpy as np #for chart
import altair as alt #for chart

st.title("My first app")

st.write('This is a simple example of a Streamlit app.')

########## Radio button for status ##########
st.header("Radio button")
status = st.radio('Set status', ['Success', 'Failed'])
placeholder = st.empty()

if status == 'Success': 
    placeholder.success('Success!')
else:
    placeholder.error('Failed!')
#เลือกได้ว่า success หรือ failed

########## Message boxes ##########
st.header("Message boxes")
st.info('This is an informational message')

st.success('This is a success message')

st.warning('This is a warning message')

st.error('This is an error message')

########## Area chart ##########
st.header('Area Chart') #ชื่อchart
chart_data = pd.DataFrame(
        np.random.randn(20, 3),
        columns=['a', 'b', 'c']) #create data frame, random 20 rows, 3 columns
st.area_chart(chart_data) #เอาข้อมูลจาก chart data to create area chart

########## Altair chart ##########
st.header('Altair Chart')
#อ่าน csv data
source = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/penguins.csv')

# assign data in scatter plot
chart_data_2 = alt.Chart(source).mark_circle(size =60).encode(
    x='flipper_length_mm',
    y='bill_length_mm',
    color='species',
    #hover mouse แล้ว display label
    tooltip=['species', 'bill_length_mm', 'flipper_length_mm']
).interactive()

#display chart in app
st.altair_chart(chart_data_2, use_container_width=True)



