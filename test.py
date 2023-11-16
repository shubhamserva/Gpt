from langchain.document_loaders import UnstructuredURLLoader, WebBaseLoader
import json

docs = []

url = ["https://apty717.zendesk.com/api/v2/help_center/articles"]

while(url[0]!=None):
    loader = WebBaseLoader(url)
    data = json.loads(loader.load()[0].page_content)
    docs.append(data)
    url = [data['next_page']]

print(len(docs))
