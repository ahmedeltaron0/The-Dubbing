def separate_vocals(input_file, output_vocals, output_music):
    import os
    from spleeter.separator import Separator

    # Load the spleeter separator model
    separator = Separator('spleeter:2stems')
    
    try:
        # Separate vocals and accompaniment
        separator.separate_to_file(input_file, output_music)

        # Check if the generated files exist
        vocals_file = os.path.join(output_music, 'vocals.wav')
        music_file = os.path.join(output_music, 'accompaniment.wav')
        if os.path.exists(vocals_file) and os.path.exists(music_file):
            # Rename the generated files with appropriate filenames
            os.rename(vocals_file, os.path.join(output_vocals, 'output_vocals.wav'))
            os.rename(music_file, os.path.join(output_music, 'output_music.wav'))
            return os.path.join(output_vocals, 'output_vocals.wav'), os.path.join(output_music, 'output_music.wav')
        else:
            raise FileNotFoundError("Generated files not found.")
    except Exception as e:
        print("An error occurred:", e)
        return None, None

if __name__ == "__main__":
    input_file = r'output_audio/ولاد رزق 8ث.wav'
    output_vocals = r'output_speelter/vocals'
    output_music = r'output_speelter/music'

    vocals_file, music_file = separate_vocals(input_file, output_vocals, output_music)

    if vocals_file and music_file:
        print("Separation successful.")
    else:
        print("Separation failed. Check for errors.")
