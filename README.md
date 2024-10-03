# 💬 DataWise Chatbot

A simple Streamlit app that shows how to build a chatbot using OpenAI's GPT-4o-mini.


## Introducction

This Gradio-powered Q&A app, enhanced by Langchain, is designed to efficiently handle any dataset, including large-scale datasets with complex values such as sentences or phrases.

The app simplifies the process of querying even the most extensive and intricate datasets, streamlining the search for meaningful insights. Powered by a sophisticated Langchain setup and integrated with a ChatOpenAI model, it ensures accurate and timely responses to user queries.

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