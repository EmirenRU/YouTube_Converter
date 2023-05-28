import os
import pytube
from pydub import AudioSegment

def convert_yt_to_mp3(url):
    yt = pytube.YouTube(url)
    stream = yt.streams.get_audio_only()
    stream.download()

    mp4_file = stream.default_filename
    mp3_file = os.path.splitext(mp4_file)[0] + '.mp3'

    os.rename(mp4_file, mp3_file)

    return mp3_file

def convert_mp3_to_wav(mp3_file):
    wav_file = os.path.splitext(mp3_file)[0] + '.wav'

    audio = AudioSegment.from_file(mp3_file)
    audio.export(wav_file, format='wav')

    return wav_file

def main():
    url = input("Enter the YouTube URL: ")

    # Convert YouTube video to MP3
    mp3_file = convert_yt_to_mp3(url)
    print(f"MP3 conversion completed: {mp3_file}")

    flag = input("Do you want to convert to .wav?\nWrite Yes or No: ")
    if (flag in ["YES", "Yes", "Y", "y"]):
        # Convert MP3 to WAV
        wav_file = convert_mp3_to_wav(mp3_file)
        print(f"WAV conversion completed: {wav_file}")


if __name__ == "__main__":
    main()