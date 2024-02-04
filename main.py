from video_to_audio import download_audio_from_youtube
from transcription import transc
from translation import translate


youtube_url = "https://www.youtube.com/watch?v=TI0TfaIpr9s"

    # Download audio
audio_path = download_audio_from_youtube(youtube_url)

    # Transcribe audio
transcription_result = transc(audio_path)

    # Translate and save the result
translated_result = translate(transcription_result)
print("Translated Result:", translated_result)