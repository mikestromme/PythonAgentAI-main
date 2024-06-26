import os
from llama_index import StorageContext, VectorStoreIndex, load_index_from_storage
from llama_index.readers.file import DocxReader


def get_index(data, index_name):
    index = None
    if not os.path.exists(index_name):
        print("building index", index_name)
        index = VectorStoreIndex.from_documents(data, show_progress=True)
        index.storage_context.persist(persist_dir=index_name)
    else:
        index = load_index_from_storage(
            StorageContext.from_defaults(persist_dir=index_name)
        )

    return index


doc_path = os.path.join("data", "knowledge.docx")
solar_doc = DocxReader().load_data(file=doc_path)
solar_index = get_index(solar_doc, "solar")
solar_engine = solar_index.as_query_engine()