from gtts import gTTS
import os

def text_to_speech(text, language='en'):
    
    tts = gTTS(text=text, lang=language, slow=False)
    # Save the audio to a file
    tts.save("output.mp3")
    # Play the audio file
    os.system("start output.mp3")  

if __name__ == "__main__":
    text = input("Enter the text you want to convert to speech: ")
    text_to_speech(text)
