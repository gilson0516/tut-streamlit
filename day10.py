import streamlit as st

st.header('st.selectbox')

option = st.selectbox(
    'What is your favorite color?',
    ('Blue','Red','Green')
)
st.write('Your favorite color is ', option)

st.header('st.multiselect')

options = st.multiselect(
    'What are your favorite colors',
    ['Green', 'Yellow', 'Red','Blue'],
    ['Yellow', 'Red']
)
st.write('You selected:', options)

st.header('st.checkbox')

st.write('Way would you like to order?')
icecream = st.checkbox('Ice cream')
coffee = st.checkbox('Coffee')
cola = st.checkbox('Cola')

if icecream:
    st.write("Great! here's some more :icecream:")
if coffee:
    st.write("Okay, here's some coffee :coffee:")
if cola:
    st.write("Here you go :coffee:")