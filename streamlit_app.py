import streamlit as st
from langchain.llms import OpenAI
st.title(' Hệ thống sinh đề kiểm tra tại Học viện Ngân hàng')
text_input = st.text_area( label = 'Nhập prompt sinh câu hỏi: ')

button = st.button("Submit", key="button")
if button:
  completion = 
