from langchain_helpper import get_llm_chain

import streamlit as strl

strl.title("ZARA SALES DATA CHAT : 👕🧥")
Question = strl.text_input("Question : ")

if Question:
    chain = get_llm_chain()
    result = chain(Question)
    strl.header("Answer :")
    strl.text_area(label='Answer',value=result['result'],label_visibility="hidden")