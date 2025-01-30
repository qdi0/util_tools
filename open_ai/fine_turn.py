import os

# from llms.chains import chain
import sys

import openai
from dotenv import load_dotenv

print(sys.path)


load_dotenv()

# output_file = "fine_tuned_model.json"
# target_file = "rdds"

# path_lists = glob.glob(f"{target_file}/*.txt")
# print(path_lists)

qa_data = []

# for path in path_lists:
#     with open(path, "r") as file:
#         text_list = file.readlines()
#         text_list = "\n".join(text_list)
#         data = {
#             "messages": [
#                 {"role": "system", "content": "You are a helpful assistant. Answer in Japanese! Your task is creating a requirement definition document."},
#                 {"role": "user", "content": "要件定義書を作ってください。"},
#                 {"role": "assistant", "content":text_list }
#             ]
#         }
#         jsonl = json.dumps(data, ensure_ascii=False) + "\n"
#         qa_data.append(jsonl)

# results = chain.invoke({"original_text": text_list})
# print(results.content)
# date = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
# col = results.content.split("\n")  # type: ignore
# col = [c.split(",") for c in col]
# df = pd.DataFrame(col)
# df.to_csv(f"datasets/qa_{date}.csv", index=False)
# print("Saved as qa_{date}.csv")


# with open("dataset_rdd.jsonl", "w") as file:
#     for data in qa_data:
#         file.write(data)

# file_paths = glob.glob("datasets/*.csv")
# jsonl_file = open("qa_2.jsonl", "w")

# outputs = ""
# for file_path in file_paths:
#     print(file_path)
#     df = pd.read_csv(file_path)
#     for index, row in df.iterrows():
#         if index == 0 or index == 1:
#             continue
#         data = {
#             "messages": [
#                 {"role": "system", "content": "You are a helpful assistant. Answer in Japanese!"},
#                 {"role": "user", "content": str(row.iloc[0])},
#                 {"role": "assistant", "content": str(row.iloc[1])}
#             ]
#         }
#         jsonl = json.dumps(data, ensure_ascii=False) + "\n"
#         jsonl_file.write(jsonl)

# jsonl_file.close()

# with open("sg_2.jsonl", "w") as file:
#     data_json = json.dumps(outputs)
#     file.write(data_json)

openai.api_key = os.getenv("OPENAI_API_KEY")

# 学習データのアップロード


# openai.File.create(
#     api_key=os.getenv("OPENAI_API_KEY"),
#     file=open("dataset_rdd.jsonl", "rb"),
#     purpose="fine-tune"
# )

# print(openai.File.list())

# openai.FineTuningJob.create(
#     # model="gpt-4o-mini-2024-07-18",
#     model="gpt-4o-2024-08-06",
#     training_file="file-5auZ71IB1SoeRaFqPfPumYWC",
#     hyperparameters={"n_epochs": 25,}
# )

# print(openai.FineTuningJob.list(limit=10))
