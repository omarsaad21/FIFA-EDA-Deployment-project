import numpy as np 
import pandas as pd
import streamlit as st

# import sys
# sys.path.append(r'D:\New_Projects\Visuallization\Projects\fifa_class')
import MEDA as md

df2 = pd.read_csv('./Sources/fifa_cleaned.csv')

tab_1, tab_2 = st.tabs(['Tab_1', 'Tab_2'])

with tab_1:
    tab3, tab4 = st.tabs(['tab3', 'tab4'])
    with tab3:
        st.title('Tab 1 Hello')
        st.write('Parag. tab 1')

        fact = st.radio('Choose Fact', df2.select_dtypes(include= 'number').columns, horizontal= True)

        st.plotly_chart(md.best_10_players(fact))

        col1, col2, col3 = st.columns(3)
        col2.metric('Wind', '10 mph', '-1 mph')
        col3.metric('Hum', '50 %', '0 %')

        col1.metric('Temp', '40 C', '2 C')

    if st.button('Click me'):
        st.write('Clicked')

    agree = st.checkbox('I agree')    
    if agree:
        st.write('Congratulations')

    drop_options = st.selectbox('Select color', ['red', 'blue', 'green'])
    if drop_options:
        st.write('You selected',drop_options)

    multi_options = st.multiselect('Select colors', ['red', 'blue', 'black', 'white', 'yellow'])
    if multi_options:
        for i in (multi_options):
            st.write(i)

    age = st.slider('How old are you?', min_value= 0, max_value= 100, value= 20, step= 1)  
    st.write(f"I'm {age} years old")

with tab_2:
    num = st.number_input('Enter a number: ')
    st.write('Your number is ', num)

    date = st.date_input('Enter a Date')
    st.write(date.month)

    color = st.color_picker('color')
    st.write(color)

    st.sidebar.selectbox('sidebar', ('mail', 'facebook'))
    st.subheader('Subheader')
    data = np.random.randn(10, 1)
    st.line_chart(data)