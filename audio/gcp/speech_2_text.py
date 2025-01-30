import datetime
import io

from google.cloud import speech


def transcribe_gcs(path):

    # クライアントの生成
    client = speech.SpeechClient()

    # 音声ファイルの読み込み
    with io.open(path, "rb") as audio_file:
        content = audio_file.read()
        audio = speech.RecognitionAudio(content=content)

    # 音声ファイルをテキストに変換
    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.MP3,
        sample_rate_hertz=16000,
        enable_automatic_punctuation=True,
        language_code="ja-JP",
    )
    start = datetime.datetime.now()
    response = client.recognize(config=config, audio=audio)
    end = datetime.datetime.now()

    print(response)
    # 出力
    for result in response.results:
        print(result.alternatives[0].transcript)
    print("Time: ", end - start)


if __name__ == "__main__":
    transcribe_gcs("test.mp3")
