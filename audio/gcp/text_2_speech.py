import datetime

from google.cloud import texttospeech

text = """
当ホテルの駐車場についてご案内いたします。


駐車場は2台分ご用意しており、料金は1泊1,500円（税込）です。
ご利用時間は15:00から翌朝10:00までとなっております。
車高制限はございませんが、大型トラックはご利用いただけません。
駐車場のご利用には事前の電話予約が必要です。
連泊でのご利用はできず、1泊のみのご利用となります。
満車の場合は、近隣のコインパーキングをご利用いただくことになりますが、提携はございませんのでご了承ください。

駐車場の予約やキャンセルについては、直接店舗へお電話にてお問い合わせください。その他ご不明な点がございましたら、お気軽にお問い合わせくださいませ。
"""

# クライアントの生成
client = texttospeech.TextToSpeechClient()

# 入力の生成
synthesis_input = texttospeech.SynthesisInput(text=text)

# 声設定の生成
voice = texttospeech.VoiceSelectionParams(
    language_code="ja-JP", ssml_gender=texttospeech.SsmlVoiceGender.NEUTRAL
)

# オーディオ設定の生成
audio_config = texttospeech.AudioConfig(audio_encoding=texttospeech.AudioEncoding.MP3)

start = datetime.datetime.now()
# 音声合成のリクエスト
response = client.synthesize_speech(
    input=synthesis_input, voice=voice, audio_config=audio_config
)
end = datetime.datetime.now()

# レスポンスをファイル出力
with open("output.mp3", "wb") as out:
    print("Time: ", end - start)
    out.write(response.audio_content)
