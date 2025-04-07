import streamlit as st
import pandas as pd
import time


st.title('Apurba1903')
st.header('I am learning streamlit')
st.subheader("Let's get started")


email = st.text_input('Enter email')
password = st.text_input('Enter password')
gender = st.selectbox('Select gender',['Male','Female','Other'])

btn = st.button('Login')
if btn:
    if email == 'Apurba' and password == '1234':
        st.success('Login Successful')
        st.balloons()
        st.write(gender)
    else:
        st.error('Login Failed')


file = st.file_uploader('Upload a CSV File')
if file is not None:
    df = pd.read_csv(file)
    st.dataframe(df.describe())


st.write('This is a normal text.')
st.markdown("""
### My favourite movies.
- Race 3
- 3 Idiots
- Housefull
""")


st.code("""
def foo(input):
    return foo**2

x = foo(2)
""")


st.latex('a^2 + b^2 = c^2')


df = pd.DataFrame({
    'name': ['Apurba', 'Tahjib', 'Shams'],
    'marks': [50, 60, 70],
    'package': [7, 9, 12]
})

st.dataframe(df)


st.metric('Revenue', '3K Taka', '3%')


st.json({
    'name': ['Apurba', 'Tahjib', 'Shams'],
    'marks': [50, 60, 70],
    'package': [7, 9, 12]
})


st.image('tulip.jpg')


st.video('theblurb.mp4')


st.sidebar.title('Workflow')


col1, col2, col3 = st.columns(3)

with col1:
    st.latex('a^2 + b^2 = c^2')

with col2:
    st.latex('a^2 + 2ab + b^2 = (a+b)^2')

with col3:
    st.latex('a^2 - 2ab + b^2 = (a-b)^2')


st.error('Login Failed')


st.success('Login Successful')


st.info('Login Successful')


st.warning('Login Successful')


bar = st.progress(0)

for i in range(1, 101):
    time.sleep(0.0000000001)
    bar.progress(i)


email = st.text_input('Enter email')
number = st.number_input('Enter age')
date = st.date_input('Enter registration date')