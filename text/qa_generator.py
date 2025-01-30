import re

import click
from langchain_core.prompts import (
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
    SystemMessagePromptTemplate,
)
from langchain_openai import ChatOpenAI
from utils.data_loader import single_pdf_loader


def create_qa_prompt(system_template) -> ChatPromptTemplate:
    message = [
        SystemMessagePromptTemplate.from_template(system_template),
        HumanMessagePromptTemplate.from_template("original_text: {original_text}\n"),
    ]

    return ChatPromptTemplate.from_messages(message)


ANALYZE_SYSTEM_TEMPLATE = """
与えられた文章について分析をしなさい。
下記の要素に分解しなさい

# キーワード
# 文章の構造
# 文章の意図
# 文章のカテゴリ
- メモ、質問、感想、クライアントの要望のいずれかに分類すること
# 全体の要約
"""

QA_GENERATOR_SYSTEM_TEMPLATE = """
与えられてた文章について質問を作成しなさい。
必ずアウトプットはCSV形式で保存できる形にすること
加工しやすい形で出力すること
まーうダウン
生成するのは質問と回答のペアであること
ヘッダーは不要です
なるべく多くの質問を作成すること
質問の内容はユーザーが送ってきそうな質問を想定すること
必ず文章の内容に関連する質問を作成すること
"""


@click.command()
@click.option(
    "--path", type=str, help="Target file path. expected pdf file type", required=True
)
def main(path: str):
    llm = ChatOpenAI(model="gpt-4o")
    chain = create_qa_prompt(QA_GENERATOR_SYSTEM_TEMPLATE) | llm
    if not path.endswith(".pdf"):
        print("Target file must be pdf type")
        return
    documents = single_pdf_loader(path)
    generated_questions = []
    pattern = re.compile(r"```(.*?)```")
    for doc in documents:
        result = chain.invoke({"original_text": doc.page_content})
        content = re.sub(pattern, "", str(result.content))
        prepare_content = content.split("\n")
        for line in prepare_content:
            line = re.sub('"', "", line)
            if line == "":
                continue
            generated_questions.append(line.split(","))
        print(generated_questions[0])
        break


if __name__ == "__main__":
    main()
