from langchain.text_splitter import RecursiveCharacterTextSplitter


class DataPipe:
    def __init__(self) -> None:
        self.text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
        self.chunks = None

    def chunker(self, documents):
        # print(documents)
        # for docs in documents:
        self.chunks = [*self.text_splitter.split_documents(documents)]

    def processor(self):
        pass


