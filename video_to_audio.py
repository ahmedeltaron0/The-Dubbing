import os
from pytube import YouTube

def download_audio_from_youtube(youtube_url):
    yt = YouTube(youtube_url)
    # Select the audio stream (you may want to choose the best quality)
    audio_stream = yt.streams.filter(only_audio=True).first()
    save_path = f'output_audio/audio.mp3'
    # Get the actual file name downloaded by pytube
    actual_file_name = audio_stream.default_filename
    audio_stream.download(output_path=f'output_audio', filename='audio.mp3')
    # Rename the downloaded file to your preferred name
    # os.rename(os.path.join('', actual_file_name), save_path)
    print("Youtube Video was Downloaded Successfully")
    return save_path, f'output_audio'
audio_data = r"E:\Lip Sync\output_audio\audio.mp3"
if not os.path.exists(audio_data):
    download_audio_from_youtube("https://www.youtube.com/watch?v=TI0TfaIpr9s")