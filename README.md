# 💬 DataWise Chatbot

A simple Streamlit app that shows how to build a chatbot using OpenAI's GPT-4o-mini.


## Introduction

DataWise is an intelligent and user-friendly Q&A platform designed for handling large-scale datasets with complex values. Powered by Langchain and OpenAI, this app allows for seamless interaction with data, enabling questions to be asked and precise, context-aware responses to be received. Whether intricate datasets or simple queries are involved, DataWise simplifies the experience by transforming complex data into clear, actionable insights.

How it works:

- First, the dataset is downloaded and prepared with careful attention to detail, ensuring optimal processing.
- Next, a Langchain chain is configured, utilizing a custom prompt template tailored to manage the complexity of the dataset and deliver precise results.
  Finally, a user-friendly Gradio interface is provided, allowing users to input queries via a text box and receive answers almost instantaneously in a clear, concise format.
- This app is engineered to simplify the analysis of large-scale datasets, offering an efficient and intuitive solution for extracting accurate information, regardless of the dataset’s size or complexity.


## Dataset Information

This app utilizes the "A to Z Flowers Features & Images" dataset, sourced from Kaggle. The dataset includes detailed features and images of various flowers, making it ideal for demonstrating complex queries involving both textual and visual data.

You can find the dataset here: A to Z Flowers Features & Images.

The dataset was downloaded and integrated into this app to allow users to query detailed flower characteristics with ease. By leveraging this dataset, the app can handle a wide range of queries, showcasing its ability to manage both structured and unstructured data effectively.

### How to run it on your own machine

1. Install the requirements

   ```
   $ pip install -r requirements.txt
   ```

2. Run the app

   ```
   $ streamlit run streamlit_app.py
   ```

Or run this link thru your browser:
https://special-tribble-667rwqp97g4h4xq7-8501.app.github.dev/