from langchain.document_loaders import WebBaseLoader
from langchain.document_transformers import Html2TextTransformer
from langchain.docstore.document import Document
import json

def load_zendesk_data():
    docs = []
    url = ["https://apty717.zendesk.com/api/v2/help_center/articles"]

    while(url[0]!=None):
        loader = WebBaseLoader(url)
        data = json.loads(loader.load()[0].page_content)
        for d in data['articles']:
            docs.append(Document(page_content=d['body'], metadata={"source": d['html_url'], "title":d['title']}))
        url = [data['next_page']]

    html2text = Html2TextTransformer()
    docs_transformed = html2text.transform_documents(docs)
    return docs_transformed