from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings
from langchain.chains import RetrievalQA, ConversationalRetrievalChain
from langchain import OpenAI
from langchain.llms.openai import OpenAIChat
import os
import streamlit as st
import constants
from dotenv import load_dotenv

load_dotenv(constants.ENVIRONMENT_FILE)

class RAG_LLM:
    def __init__(self) -> None:
        self.openai_embeddings = OpenAIEmbeddings(openai_api_key=os.environ.get(constants.CHATGPT_API_KEY_FIELD))
        self.embeddings = None
        self.retriever = None
        self.qa_chain = None
        self.prompt = ""

    def vectorise(self, text_chunks):
        self.embeddings = FAISS.from_documents(text_chunks, self.openai_embeddings)
        self.embeddings.save_local(constants.EMBEDDINGS_SAVE_PATH)

        self.retriever = self.embeddings.as_retriever(search_kwargs={'k': 3})


    def initialize_llm(self):
        self.qa_chain = ConversationalRetrievalChain.from_llm(
            llm=OpenAIChat(openai_api_key=os.environ.get(constants.CHATGPT_API_KEY_FIELD)),
            retriever=self.retriever,
            return_source_documents=True,
            # condense_question_prompt
            combine_docs_chain_kwargs={"prompt": self.prompt}
        )

    def query_llm(self, query):
        result = self.qa_chain({'question': query, 'chat_history': st.session_state.messages})
        sources= ['['+sources.metadata['title']+']('+sources.metadata['source']+')' for sources in result['source_documents']]
        result = result['answer']+'  \nSources:  \n- '+'  \n- '.join(sources)
        st.session_state.messages.append((query, result))
        return result
