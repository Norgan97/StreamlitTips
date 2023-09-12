import math

import numpy as np
import pandas as pd

import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import plotly.express as px

tips = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv')
num_orders = st.sidebar.slider("Выберите количество заказов для анализа", 1, len(tips), 100)
selected_tips = tips.head(num_orders)
st.write("""
# Анализ датасета с чаевыми   
""")
st.write("""
## Гистограмма общего счета  
""")
#pic1 = plt.figure(figsize = (10,6))
#sns.histplot(data=selected_tips, x='total_bill', bins=20, kde=True)
#plt.xlabel('Total Bill Amount')
#plt.ylabel('Frequency')
#plt.title('Histogram of Total Bill Amount')
#st.pyplot(pic1)
fig1 = px.histogram(selected_tips, x='total_bill', nbins=20, title='Гистограмма общего счета')
st.plotly_chart(fig1)

st.write("""
## Связь между общим счетом и чаевыми 
""")
# pic2 = plt.figure(figsize = (10,6))
# plt.scatter(selected_tips['total_bill'], selected_tips['tip'], alpha=0.5)
# plt.xlabel('total_bill')
# plt.ylabel('tip')
# plt.title('связь между total_bill and tip');
# st.pyplot(pic2)
fig2 = px.scatter(selected_tips, x='total_bill', y='tip', title='Связь между общим счетом и чаевыми')
st.plotly_chart(fig2)

st.write("""
## Связь общего счета, чаевых и размера группы
""")
# pic3 = plt.figure(figsize=(10, 6))
# #plt.scatter(selected_tips['total_bill'], selected_tips['tip'], s=selected_tips['size'], alpha=0.6)
# sns.scatterplot(x='total_bill', y='tip', hue='size', data=selected_tips, alpha=0.7, palette='bright')
# plt.xlabel('Total Bill')
# plt.ylabel('Tip')
# plt.title('Total Bill vs Tip (Size as Marker Size)')
# st.pyplot(pic3)
fig3 = px.scatter(selected_tips, x='total_bill', y='tip', color='size', title='Связь общего счета, чаевых и размера группы')
st.plotly_chart(fig3)

st.write("""
## Связь дня недели и размера счета
""")
days = selected_tips.groupby('day')['total_bill'].sum()
# pic4 = plt.figure(figsize = (10,6))
# days.plot(kind = 'bar', color = 'skyblue')
# plt.xlabel('День недели')
# plt.ylabel('Суммарный размер счета')
# plt.title('Cвязь между днем недели и размером счета');
# plt.xticks(rotation = 0);
# st.pyplot(pic4)
fig4 = px.bar(days, x=days.index, y='total_bill', title='Связь дня недели и размера счета')
st.plotly_chart(fig4)

st.write("""
## График чаевых по дню недели отностиельно пола
""")
# pic5 = plt.figure(figsize = (10,6))
# sns.scatterplot(x='tip', y='day', hue='sex', data=selected_tips, alpha=0.7)
# plt.title('График чаевых по дню недели отностиельно пола')
# plt.xlabel('Чаевые')
# plt.ylabel('День недели');
# st.pyplot(pic5)
fig5 = px.scatter(selected_tips, x='tip', y='day', color='sex', title='График чаевых по дню недели относительно пола')
st.plotly_chart(fig5)

st.write("""
## Сумма счетов по дням и времени
""")
# pic6 = plt.figure(figsize=(10, 6))
# sns.boxplot(x='day', y='total_bill', hue='time', data=selected_tips)
# plt.xlabel('День')
# plt.ylabel('Сумма счета')
# plt.title('Box Plot: Сумма счетов по дням и времени');
# st.pyplot(pic6)
fig6 = px.box(selected_tips, x='day', y='total_bill', color='time', title='Box Plot: Сумма счетов по дням и времени')
st.plotly_chart(fig6)

st.write("""
## Гистограммы чаевых за обед и ужин
""")
lunch_data = selected_tips[selected_tips['time'] == 'Lunch']
dinner_data = selected_tips[selected_tips['time'] == 'Dinner']
# Создаем фигуру с двумя графиками
fig, axes = plt.subplots(1, 2, figsize=(12, 5))
pic7 = fig
# Гистограмма чаевых на обед
sns.histplot(lunch_data['tip'], bins=10, ax=axes[0], color='skyblue')
axes[0].set_title('Гистограмма чаевых на обед')
axes[0].set_xlabel('Чаевые')
axes[0].set_ylabel('Частота')
# Гистограмма чаевых на ужин
sns.histplot(dinner_data['tip'], bins=10, ax=axes[1], color='salmon')
axes[1].set_title('Гистограмма чаевых на ужин')
axes[1].set_xlabel('Чаевые')
axes[1].set_ylabel('Частота');
st.pyplot(pic7)

st.write("""
## Связь размера счета и чаевых курящих и некурящих
""")
fig, axes = plt.subplots(1, 2, figsize=(12, 5))
pic8 = fig
# Plot for males
axes[0].scatter(
    selected_tips[(selected_tips['sex'] == 'Male') & (selected_tips['smoker'] == 'Yes')]['total_bill'],
    selected_tips[(selected_tips['sex'] == 'Male') & (selected_tips['smoker'] == 'Yes')]['tip'],
    label='Male Smoker',
    color='blue',
    marker='o',
)
axes[0].scatter(
    selected_tips[(selected_tips['sex'] == 'Male') & (selected_tips['smoker'] == 'No')]['total_bill'],
    selected_tips[(selected_tips['sex'] == 'Male') & (selected_tips['smoker'] == 'No')]['tip'],
    label='Male Non-Smoker',
    color='red',
    marker='x',
)
axes[0].set_xlabel('Total Bill')
axes[0].set_ylabel('Tip')
axes[0].set_title('Scatter Plot for Males')
axes[0].legend()
# Plot for females
axes[1].scatter(
    selected_tips[(selected_tips['sex'] == 'Female') & (selected_tips['smoker'] == 'Yes')]['total_bill'],
    selected_tips[(selected_tips['sex'] == 'Female') & (selected_tips['smoker'] == 'Yes')]['tip'],
    label='Female Smoker',
    color='blue',
    marker='o',
)
axes[1].scatter(
    selected_tips[(selected_tips['sex'] == 'Female') & (selected_tips['smoker'] == 'No')]['total_bill'],
    selected_tips[(selected_tips['sex'] == 'Female') & (selected_tips['smoker'] == 'No')]['tip'],
    label='Female Non-Smoker',
    color='red',
    marker='x',
)
axes[1].set_xlabel('Total Bill')
axes[1].set_ylabel('Tip')
axes[1].set_title('Scatter Plot for Females')
axes[1].legend();
st.pyplot(pic8)

st.write("""
## Разница средних значений чаевых в зависимости от пола
""")
# selected_tips.groupby('sex')['tip'].mean()
# pic9 = plt.figure(figsize = (10,6))
# selected_tips.groupby('sex')['tip'].mean().plot(kind = 'bar', color = 'skyblue')
# plt.xlabel('Среднее значение чаевых')
# plt.ylabel('Пол')
# plt.title('Разница средних значений чаевых в зависимости от пола')
# plt.xticks(rotation = 0);
# st.pyplot(pic9)
fig10 = px.bar(selected_tips.groupby('sex')['tip'].mean(), x=selected_tips.groupby('sex')['tip'].mean().index, y='tip', title='Разница средних значений чаевых в зависимости от пола')
st.plotly_chart(fig10)