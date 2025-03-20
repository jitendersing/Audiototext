import SpeechRecognition as sr  
from pydub import AudioSegment

#mp3_file = "/home/kali/Downloads/dimpal.mp3"
mp3_file = input("Enter complete file path : ")
wav_file = "converted_audio.wav"

audio = AudioSegment.from_mp3(mp3_file)
audio.export(wav_file, format="wav")

recognizer = sr.Recognizer()

audio_file = "converted_audio.wav"  

# Open the file and recognize speech
with sr.AudioFile(audio_file) as source:
    print("Processing audio file...")
    audio = recognizer.record(source)  # Read the entire file

    try:
        text = recognizer.recognize_google(audio)
        print("Transcribed Text:", text)
    except sr.UnknownValueError:
        print("Sorry, could not understand the audio.")
    except sr.RequestError:
        print("Error with the speech recognition service.")

