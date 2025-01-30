from pydub import AudioSegment
from tqdm import tqdm

file_name = "output.wav"

split_time = 30  # seconds

audio_segment = AudioSegment.from_wav(file_name)

chunk_count = len(audio_segment) // (split_time * 1000)
print(chunk_count)

for i in tqdm(range(chunk_count)):
    start_time = i * split_time * 1000
    end_time = (i + 1) * split_time * 1000
    audio_chunk = audio_segment[start_time:end_time]
    audio_chunk.export(f"output_{i}.wav", format="wav")
