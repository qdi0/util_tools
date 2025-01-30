import re

import polars as pl
from langchain_community.document_loaders import (
    CSVLoader,
    PyMuPDFLoader,
    TextLoader,
    UnstructuredPowerPointLoader,
    UnstructuredWordDocumentLoader,
)
from langchain_core.documents import Document

from .logger import log_debug, log_error


def single_pdf_loader(target_path: str) -> list[Document]:
    # vision loader flown
    pdf_loader = PyMuPDFLoader(target_path)
    documents = pdf_loader.load()
    document_content = [doc.page_content for doc in documents]
    if any(string != "" for string in document_content):
        log_debug(f"Loaded documents from PDF. Document count: {len(documents)}")
        return documents
    else:
        log_error(f"Failed to load PDF: {target_path}")
        return []


def single_csv_loader(target_path: str):
    csv_loader = CSVLoader(target_path)
    documents = csv_loader.load()

    empty_filtered_documents = list(
        filter(lambda doc: doc.page_content != "", documents)
    )
    return empty_filtered_documents


def single_powerpoint_loader(target_path: str) -> list[Document]:
    pptx_loader = UnstructuredPowerPointLoader(target_path)
    return pptx_loader.load()


def single_word_loader(target_path: str) -> list[Document]:
    word_loader = UnstructuredWordDocumentLoader(target_path)
    return word_loader.load()


def single_excel_loader(target_path: str):
    def _convert_to_documents_from_excel(target_path: str):
        dfs = pl.read_excel(
            target_path,
            sheet_id=0,
            infer_schema_length=0,
        )  # Read all sheets when multiple sheets exist
        documents = []
        for df in dfs.values():
            if df.is_empty():
                return
            current_documents = _execute_to_documents_from_df(df)
            documents.extend(current_documents)
        return documents

    def _execute_to_documents_from_df(df: pl.DataFrame) -> list[Document]:
        documents = []
        for row_dict in df.iter_rows(named=True):
            pair_content = [
                f"{re.sub('_duplicated_', '',k)}: {v}" if v is not None else " "
                for k, v in row_dict.items()
            ]
            document = Document(
                page_content=",".join(pair_content)
            )  # for tokenization separation
            documents.append(document)
        return documents

    documents = _convert_to_documents_from_excel(target_path)
    if documents is None:
        raise Exception("Excel file is empty")
    return documents


def single_text_loader(target_path: str) -> list[Document]:
    text_loader = TextLoader(target_path, encoding="utf-8")
    return text_loader.load()
