from faster_whisper import WhisperModel
model = WhisperModel("large-v3", compute_type="float16")
import os 
def transc(audio):
    # Continue with the transcription
    segments, _ = model.transcribe(audio)
    transcriptions_time = []
    transcriptionst = ""
    for segment in segments:
        start_time = "{:02}:{:02}:{:.2f}".format(int(segment.start // 3600), int((segment.start % 3600) // 60), segment.start % 60)
        end_time = "{:02}:{:02}:{:.2f}".format(int(segment.end // 3600), int((segment.end % 3600) // 60), segment.end % 60)
        duration = round(segment.end - segment.start, 2)

        # Construct the formatted transcription
        formatted_transcription = "[{} -> {}]({}) {}".format(start_time, end_time, duration, segment.text)
        transcriptions_time.append(formatted_transcription)
        transcriptionst += segment.text

    # Save the transcription to a file
    output_file_path = "transcription_output.txt"
    with open(output_file_path, "w", encoding="utf-8") as output_file:
        output_file.write(transcriptionst)

    return transcriptionst
    #return transcriptions_time

if __name__ == "__main__":
    audio_data = r"output_audio/audio_weladrezq.mp3"
    transcription_result = transc(audio_data)
    print(transcription_result)