'''import os
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
audio_data = r"E:\Lip Sync\output_audio\audio [vocals].mp3"
if not os.path.exists(audio_data):
    download_audio_from_youtube("https://www.youtube.com/watch?v=vJiYplCLvzg")
    '''
from moviepy.editor import *
import os

def convert_video_to_audio(local_video_path):
    output_directory = 'E:\\The-Dubbing\\output_audio'
    # Ensure the output directory exists
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    # Check if the local video file exists
    if not os.path.exists(local_video_path):
        print(f"Error: The specified video file does not exist: {local_video_path}")
        return None, None

    # Construct the output audio file path
    output_file_name = os.path.splitext(os.path.basename(local_video_path))[0] + '.wav'
    output_audio_path = os.path.join(output_directory, output_file_name)

    try:
        # Load the video file
        video = VideoFileClip(local_video_path)
        # Extract audio from the video
        audio = video.audio
        # Write the audio to a WAV file
        audio.write_audiofile(output_audio_path)
        # Close the video and audio objects to free resources
        video.close()
        audio.close()
        print("Video was successfully converted to audio")
    except Exception as e:
        print(f"An error occurred during conversion: {e}")
        return None, None

    return output_audio_path, output_directory

# Example usage
local_video_path = r"E:\The-Dubbing\welad_rezk 3\english\scene 1\ولاد رزق 8ث.mp4"
output_audio_path, output_directory = convert_video_to_audio(local_video_path)

if output_audio_path:
    print(f"Audio file was saved to: {output_audio_path}")
else:
    print("There was an error converting the video to audio.")
