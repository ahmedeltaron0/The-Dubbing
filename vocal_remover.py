def separate_vocals(input_file, output_vocals, output_music):
    import os
    from spleeter.separator import Separator

    # Load the spleeter separator model
    separator = Separator('spleeter:2stems')
    
    try:
        # Separate vocals and accompaniment
        separator.separate_to_file(input_file, output_music)

       # Rename the generated accompaniment file to output_music
        os.rename(os.path.join(output_music, 'accompaniment.wav'), os.path.join(output_music, 'output_accompaniment.wav'))

    # Rename the generated vocals file to output_vocals
        os.rename(os.path.join(output_music, 'vocals.wav'), os.path.join(output_music, 'output_vocals.wav'))

        return output_vocals, output_music
    except Exception as e:
        print("An error occurred:", e)
        return None, None

if __name__ == "__main__":
    input_file = r'output_audio/ولاد رزق 8ث.wav'
    output_vocals = r'output_audio/vocals'
    output_music = r'output_audio/music'

    vocals_file, music_file = separate_vocals(input_file, output_vocals, output_music)

    if vocals_file and music_file:
        print("Separation successful.")
    else:
        print("Separation failed. Check for errors.")
