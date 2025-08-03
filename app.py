from dotenv import load_dotenv

load_dotenv()

import streamlit as st

st.title("サンプルアプリ: LLM機能を搭載したWebアプリ")

st.write("相手の専門分野を選択できます。")

selected_item = st.radio(
    "専門家を選択してください。",
    ["食生活改善の専門家", "トレーニングの専門家"]
)

st.divider()

if selected_item == "食生活改善の専門家":
    system_message = "あなたは食生活改善の専門家です。専門知識を活かして、食事や栄養に関する質問に答えてください。"
    input_message = st.text_input(label="食生活改善に関して、どんな質問がありますか？")

else:
    system_message = "あなたはトレーニングの専門家です。専門知識を活かして、トレーニングや運動に関する質問に答えてください。"
    input_message = st.text_input(label="トレーニングに関して、どんな質問がありますか？")

if st.button("送信"):
    st.divider()

    # ここでLLMに問い合わせ
    from langchain_openai import ChatOpenAI
    from langchain.schema import SystemMessage, HumanMessage, AIMessage

    llm = ChatOpenAI(model_name="gpt-4o-mini", 
                     temperature=0.5)

    messages = [
        SystemMessage(content=system_message),
        HumanMessage(content=input_message),
    ]

    result = llm(messages)

    st.write(f"回答: {result.content}")
