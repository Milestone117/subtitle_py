import speech_recognition as sr

def perform_realtime_speech_recognition(recognizer, stream):
    # Continuously stream and process audio for real-time speech recognition
    while True:
        try:
            # Read audio data from the stream
            audio_data = stream.read(1024)  # Adjust the chunk size as needed

            # Perform speech recognition on the audio data
            text = recognizer.recognize_google(audio_data)

            # Print the transcribed text
            print(text)

        except sr.UnknownValueError:
            # If speech is not recognized
            print("Could not understand audio")

        except sr.RequestError as e:
            # If there is an error with the speech recognition service
            print(f"Error: {str(e)}")
            break

def run_realtime_speech_recognition():
    # Create a recognizer instance
    recognizer = sr.Recognizer()

    # Use the default microphone as the audio source
    with sr.Microphone() as source:
        # Adjust for ambient noise, if necessary
        recognizer.adjust_for_ambient_noise(source)

        # Start the audio stream
        stream = recognizer.open(source)

        # Perform real-time speech recognition
        perform_realtime_speech_recognition(recognizer, stream)