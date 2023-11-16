from langchain.memory import ConversationBufferMemory
from langchain.memory.chat_message_histories import StreamlitChatMessageHistory
from data_loader import load_zendesk_data
from langchain.document_loaders import DirectoryLoader
import streamlit as st
import os, tempfile
import constants

from data_processing import DataPipe
from rag_llm import RAG_LLM

def load_data(rag_llm, data_pipe):
    documents = load_zendesk_data()
    print('Loaded data.')
    data_pipe.chunker(documents)
    
    rag_llm.vectorise(data_pipe.chunks)
    rag_llm.initialize_llm()
    print('Data vectorised.')
    # return rag_llm, data_pipe


if __name__ =='__main__':
    # st.session_state.messages = [] 
    rag_llm = RAG_LLM()
    data_pipe = DataPipe()

    # st.session_state.source_docs = st.file_uploader(label="Upload Documents", type="txt", accept_multiple_files=True)
    # st.button("Load data", on_click=load_data(rag_llm, data_pipe))
    load_data(rag_llm, data_pipe)
    

    if "messages" not in st.session_state:
        st.session_state.messages = []    
    #
    print('Ready to use.')
    for message in st.session_state.messages:
        st.chat_message('human').write(message[0])
        st.chat_message('ai').write(message[1])    
    #
    if query := st.chat_input():
        st.chat_message("human").write(query)
        response = rag_llm.query_llm(query)
        st.chat_message("ai").write(response)