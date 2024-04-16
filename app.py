
import google.generativeai as genai
import streamlit as st

# Reading OpenAI Key into code
f=open('keys/key.txt')
API_KEY=f.read()

# setting client
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-pro')

#Taking prompt from user interface
prompt=st.text_area("Paste your code here")

#instructions
instruction='''
            you are an good AI Assistant ,
            your job is to evaluate the code and produce output in the format:
            list of errors
            resolved code
            if code has no errors return your code has no issues to be resolved'''

#if button clicked in UI
if st.button('Evaluate')==True:
    response = model.generate_content(instruction+'evaluate the code'+prompt)

    #Showing the evaluated output of code
    st.write(response.text)


