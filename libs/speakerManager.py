import time
import boto3
from botocore.exceptions import BotoCoreError, ClientError
from contextlib import closing
import os
import sys
from tempfile import gettempdir
from pygame import mixer


class SpeakerManager:
    def __init__(self):
        self.polly = boto3.client("polly")

        self.finished = True
        self.toRead = []

    def read(self, text, targetLang):
        self.toRead.append(text)

        if self.finished:
            # voice id to change selon self.targetLang
            try:
                response = self.polly.synthesize_speech(Text=self.toRead[-1], OutputFormat="mp3", VoiceId="Joanna")
            except (BotoCoreError, ClientError) as error:
                print(error)
                sys.exit(-1)

            if "AudioStream" in response:
                with closing(response["AudioStream"]) as stream:
                    output = os.path.join(gettempdir(), "667-transcription.mp3")
                    try:
                        with open(output, "wb") as file:
                            file.write(stream.read())
                    except IOError as error:
                        print(error)
                        sys.exit(-1)
            else:
                print("Could not stream audio")
                sys.exit(-1)

            del self.toRead[-1]
            self.play()

    def play(self):
        self.finished = False

        mixer.init(devicename="CABLE Input (VB-Audio Virtual Cable)")
        mixer.music.load(os.path.join(gettempdir(), "667-transcription.mp3"))
        mixer.music.play()

        while mixer.music.get_busy():
            time.sleep(0.1)

        mixer.quit()

        self.finished = True
