from langchain.memory import ConversationBufferMemory
from langchain.memory.chat_message_histories import StreamlitChatMessageHistory
from langchain.document_loaders import DirectoryLoader
import streamlit as st
import os, tempfile
import constants

from data_processing import DataPipe
from rag_llm import RAG_LLM

def load_data(rag_llm, data_pipe):
    for file in st.session_state.source_docs:
        with tempfile.NamedTemporaryFile(delete=False, dir=constants.TMP_SAVE_PATH.as_posix(), suffix='.txt') as tmp_file:
            tmp_file.write(file.read())
        
        loader = DirectoryLoader(constants.TMP_SAVE_PATH.as_posix(), glob='**/*.txt')
        documents = loader.load()
        data_pipe.chunker(documents)

        for _file in constants.TMP_SAVE_PATH.iterdir():
                temp_file = constants.TMP_SAVE_PATH.joinpath(_file)
                temp_file.unlink()
    
    rag_llm.vectorise(data_pipe.chunks)
    rag_llm.initialize_llm()

    # return rag_llm, data_pipe


if __name__ =='__main__':
    # st.session_state.messages = [] 
    rag_llm = RAG_LLM()
    data_pipe = DataPipe()

    st.session_state.source_docs = st.file_uploader(label="Upload Documents", type="txt", accept_multiple_files=True)
    st.button("Submit Documents", on_click=load_data(rag_llm, data_pipe))

    if "messages" not in st.session_state:
        st.session_state.messages = []    
    #
    for message in st.session_state.messages:
        st.chat_message('human').write(message[0])
        st.chat_message('ai').write(message[1])    
    #
    if query := st.chat_input():
        st.chat_message("human").write(query)
        response = rag_llm.query_llm(query)
        st.chat_message("ai").write(response)