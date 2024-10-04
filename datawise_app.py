import pandas as pd
from langchain_text_splitters import RecursiveCharacterTextSplitter
import streamlit as st
import os
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain_core.prompts import ChatPromptTemplate
from openai import OpenAI

df = pd.read_csv("FlowerDatabase.csv")
df = df.drop(
    [
        'Desc',
        # 'PlantType',
        # 'HardinessZones',
        # 'BloomsIn',
        'SoilNeeds',
        # 'SunNeeds',
        # 'WaterNeeds',
        # 'Maintenance',
        'RelatedFlowers'
    ],
    axis=1,
)

df.to_csv("FlowerDatasetReduced.csv")

context = ""
for row in df.to_dict('records'):
    context += str(row) + "\n"


text_splitter = RecursiveCharacterTextSplitter(separators=["\n"])

chunked_context = text_splitter.create_documents(context)

st.title("💬 DataWise App")
st.write(
    "This Gradio-powered Q&A app, enhanced by Langchain, is designed to efficiently handle any dataset,"
    "including large-scale datasets with complex values such as sentences or phrases.\n"
)

open_api_key_container = st.empty()
OPEN_API_KEY = open_api_key_container.text_input("OpenAI API Key", type="password")
os.environ["OPENAI_API_KEY"] = OPEN_API_KEY
if not os.environ["OPENAI_API_KEY"]:
    st.info("Please add your OpenAI API key to continue.", icon="🗝️")
else:
    open_api_key_container.empty()
    OPEN_API_KEY = "OPEN_API_KEY"
    assert OPEN_API_KEY != os.environ["OPENAI_API_KEY"]
    st.write("Successfully added OPENAI API KEY.\n\n")

    model = ChatOpenAI(
        model="gpt-4o-mini",
        api_key=os.environ["OPENAI_API_KEY"],
    )

    prompt = ChatPromptTemplate.from_messages([
        (
            "system",
            "You are a helpful assistant. You will be given a query to answer, and a context to help you answer the query." +
            "Try to use the provided context to answer the query, and do not try to guess if you don't have the needed information."
        ),
        (
            "human",
            "Context: {context}\n\n###\n\nQuery: {query}"
        )
    ])
    chain = prompt | model

    if "messages" not in st.session_state:
        st.session_state.messages = []

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if query := st.chat_input("What is up?"):
        st.session_state.messages.append({"role": "user", "content": query})
        with st.chat_message("user"):
            st.markdown(query)

        stream = chain.invoke({
            "query": query,
            "context": context
        }).content

        with st.chat_message("assistant"):
            st.write(stream)
        st.session_state.messages.append({"role": "assistant", "content": stream})    
