from langchain_core.prompts import (
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
    SystemMessagePromptTemplate,
)
from langchain_openai import ChatOpenAI

SYSTEM_TEMPLATE = """
与えられた文章からカンマ区切りになるように質疑表を作成しなさい。
与えるデータは要件定義書です。
要件定義書のフォーマットに関する質問を含めなさい。
質問は文章の内容に関連するものとする。
満遍なく質問を作成しなさい。
データはFine turningを行うためのデータセットとして使用する。
出力はCSV形式で保存すること。

header: 質問,回答

"""


def create_qa_prompt(system_template) -> ChatPromptTemplate:
    message = [
        SystemMessagePromptTemplate.from_template(system_template),
        HumanMessagePromptTemplate.from_template("original_text: {original_text}\n"),
    ]

    return ChatPromptTemplate.from_messages(message)


llm = ChatOpenAI(model="gpt-4o")

chain = create_qa_prompt(SYSTEM_TEMPLATE) | llm
