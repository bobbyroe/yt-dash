import streamlit as st
import pandas as pd

data = pd.read_csv('./yt-data.csv')

totals = data[data['Content'] == 'Total'] # get totals row

data = data.drop(columns=['Content'])
data = data.dropna() # Removes "Total" row
data['Watch time (hours)'] = data['Watch time (hours)'].round(0) # round hours value
data['Duration'] = (data['Duration'] / 60).round(1) # convert to minutes
data = data.iloc[:, [1, 0, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]] # integer location based indexing

st.title("🤖 Robot Bobby YouTube Dashboard")
colL, colM, colR = st.columns(3)
colL.metric("Total Views", totals['Views'])
colM.metric("Subscribers", totals['Subscribers'])
colR.metric("Videos", data.shape[0])

st.subheader("Data Preview")
st.write(data.head())

threshold = 50
filtered_data = data[data['Watch time (hours)'] > threshold]
columns = ['Video title', 'Comments added', 'Shares', 'Likes',] #'Watch time (hours)', ] # 'Average view duration']
filtered_data = pd.DataFrame(filtered_data, columns=columns)
st.subheader('Likes / Comments / Watch time')
st.bar_chart(filtered_data, x='Video title', horizontal=True)