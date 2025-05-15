from dotenv import load_dotenv
load_dotenv()

import streamlit as st
from langchain_openai import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage

st.title("初めてのLLMアプリ")
st.write("###### 動作モードA : 天才フォトグラファーが、あなたの写真を劇的にアップデート")
st.write("###### 動作モードB : 有名トレーダーが語る、勝ち続けるデイトレの真髄")

st.write("####")

selected_item = st.radio(
    "動作モードを選択してください。",
    ["A : 天才フォトグラファー・モード", "B : 有名トレーダー・モード"]
)

st.divider()

if selected_item == "A : 天才フォトグラファー・モード":
    input_message = st.text_input(label="「写真やカメラ」に関する疑問を入力して、実行ボタンを押してください")

    llm = ChatOpenAI(model_name="gpt-4o-mini", temperature=0)
    messages = [
        SystemMessage(content="あなたはカメラ知識が豊富なフォトグラファーです、フォトグラファーとしての経験と知識を活用し、優しく質問に答えてください。写真やカメラ以外の逸紋にはわからないと答えてください"),
        HumanMessage(content=input_message),
    ]
    result_A = llm(messages)
   
else:
    input_message = st.text_input(label="「株・デイトレ」に関する疑問を入力して、実行ボタンを押してください")

    llm = ChatOpenAI(model_name="gpt-4o-mini", temperature=0)
    messages = [
        SystemMessage(content="あなたは有名な株のトレーダーです、投資やトレードの経験と知識を活用し、優しく質問に答えてください。投資やトレード以外の逸紋にはわからないと答えてください"),
        HumanMessage(content=input_message),
    ]
    result_B = llm(messages)

if st.button("実行"):
    st.divider()

    if selected_item == "A : 天才フォトグラファー・モード":
        if input_message:
             st.write(result_A.content)

        else:
            st.error("エラー : 入力欄に質問を入力してから、実行ボタンを押してください")

    else:
        if input_message:
             st.write(result_B.content)

        else:
            st.error("エラー : 入力欄に質問を入力してから、実行ボタンを押してください")