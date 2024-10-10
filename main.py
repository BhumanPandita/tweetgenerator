import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain import PromptTemplate
from langchain import LLMChain
import os

os.environ['GOOGLE_API_KEY'] = st.secrets('GOOGLE_API_KEY')

model = ChatGoogleGenerativeAI(model = "gemini-1.5-flash-latest")

tweet_template = "Write me {number} tweets on the topic {topic}."

tweet_prompt = PromptTemplate(template = tweet_template,inputs  = ['number','topic'])

tweet_chain = tweet_prompt | model

st.header("Tweet Generator")

st.subheader("Generate tweets using Generative AI")

topic = st.text_input("Topic")

number = st.number_input("Number of tweets",min_value = 1,max_value = 10,value = 1,step = 1)

if st.button("Generate"):
    st.write(tweet_chain.invoke({"number":number,"topic":topic}).content)