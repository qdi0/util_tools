import glob

import soundfile as sf
import torch
from transformers import pipeline

# config
model_id = "kotoba-tech/kotoba-whisper-v2.0"
torch_dtype = torch.bfloat16 if torch.cuda.is_available() else torch.float32
device = "cuda:0" if torch.cuda.is_available() else "cpu"
model_kwargs = (
    {"attn_implementation": "sdpa"}
    if torch.cuda.is_available()
    else {"max_length": 1000000000000}
)
generate_kwargs = {"language": "ja", "task": "transcribe", "return_timestamps": True}

# load model
pipe = pipeline(
    "automatic-speech-recognition",
    model=model_id,
    torch_dtype=torch_dtype,
    device=device,
    model_kwargs=model_kwargs,
)
print(pipe.model.config)

path_list = glob.glob("raw/*.wav")
for path in path_list:
    print(path)
    audio, sr = sf.read(path)
    # run inference
    result = pipe(audio, generate_kwargs=generate_kwargs)
    with open("esd.list", "a") as f:
        f.write(f"Data/戌亥とこ/{path}|戌亥とこ|JP|{result['text']}\n")  # type: ignore
    print(result)

audio, sr = sf.read("output.wav")
# run inference
result = pipe(audio, generate_kwargs=generate_kwargs)
print(result)


trans_text = []

# audio_path = "datas"
# target_paths = glob.glob(audio_path + "/*.wav")
# target_paths.sort()
# for path in tqdm(target_paths):
#     audio, sr = sf.read(path)
#     # run inference
#     result = pipe(audio, generate_kwargs=generate_kwargs)
#     print(path)
#     # run inference
#     result = pipe(audio, generate_kwargs=generate_kwargs)
#     print(path)
#     print(result)
#     print(result["text"]) # type: ignore
#     trans_text.append(result["text"]) # type: ignore

# print(trans_text)
