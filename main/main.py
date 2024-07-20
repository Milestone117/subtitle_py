import kivy
kivy.require('2.0.0')

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

from video.video_processing import process_video
from audio.audio_processing import process_music
from speech.speech_recognition import run_realtime_speech_recognition


class SubtitlesAndLyricsApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')
        
        video_button = Label(text='Process Video', size_hint=(None, None), size=(200, 50))
        video_button.bind(on_release=self.process_video)
        layout.add_widget(video_button)
        
        music_button = Label(text='Process Music', size_hint=(None, None), size=(200, 50))
        music_button.bind(on_release=self.process_music)
        layout.add_widget(music_button)
        
        return layout
    
    def process_video(self, instance):
        # Call the video processing code
        try:
            process_video()
            print("Video processed successfully!")
        except Exception as e:
            print(f"Error processing video: {str(e)}")
    
    def process_music(self, instance):
        # Call the music processing code
        try:
            process_music()
            print("Music processed successfully!")
        except Exception as e:
            print(f"Error processing music: {str(e)}")
    
    def run_speech_recognition(self):
        try:
            run_realtime_speech_recognition()
        except Exception as e:
            print(f"Error running speech recognition: {str(e)}")


if __name__ == '__main__':
    SubtitlesAndLyricsApp().run()