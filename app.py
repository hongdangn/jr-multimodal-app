import streamlit as st
from qa import QuestionAnswer
from obj import vector_store

task_type = st.sidebar.selectbox("あなたの好きなチャットボット", [
    "テキストチャットボット", "音声チャットボット"
])

if "text_messages" not in st.session_state:
    st.session_state.text_messages = [{"role": "assistant", "content": "何でも聞いてください！"}]

if "speech_messages" not in st.session_state:
    st.session_state.speech_messages = [{"role": "assistant", "content": "何でも聞いてください！"}]

if 'qa' not in st.session_state:
    st.session_state.qa = QuestionAnswer(vector_store)

if task_type == '音声チャットボット':
    st.header('あなたの声で私に質問してください!!')
    with st.form("stsForm"):
        uploaded_file = st.file_uploader('ここにファイルをアップロードしてください', ["mp3","mp4","mpeg","mpga","m4a","wav","webm"])
        submitted = st.form_submit_button('送信')

        transcription = "dcm dang gioi vay" if uploaded_file else None

    for msg in st.session_state.speech_messages:
        with st.chat_message(msg["role"]):
            st.write(msg["content"])

    if submitted and transcription:
        st.session_state.speech_messages.append({"role": "user", "content": transcription})

        with st.chat_message("user"):
            st.write(transcription)
            
        with st.spinner("ちょっと待って..."):
            response = "dang ky nay 4.0"
            st.session_state.speech_messages.append({"role": "assistant", "content": response})
            st.chat_message("assistant").write(response)

if task_type == 'テキストチャットボット':
    st.header("何でも聞いてください!!")

    for msg in st.session_state.text_messages:
        with st.chat_message(msg["role"]):
            st.write(msg["content"])

    if prompt := st.chat_input("ここに質問を入力してください..."):
        
        st.session_state.text_messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.write(prompt)
            
        with st.spinner("ちょっと待って..."):
            response = st.session_state.qa.get_answer(prompt)
            st.session_state.text_messages.append({"role": "assistant", "content": response})
            st.chat_message("assistant").write(response)

    
            

