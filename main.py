##I ntegrate our code OpenAI API
import os
from constants import openai_key
from langchain.llms import openai

import streamlit as st

os.environ["OPENAI_API_KEY"]=openai_key

#Streamlit framework

st.title('Langchain Demo with OPENAI API')
input_text=st.text_input("Search the topic u want")

##OPENAI LLMS

llm=openai.OpenAI(temperature=0.8)


if input_text:
    st.write(llm(input_text))
