import soundcard as sc
import numpy as np


class AudioManager:
    def __init__(self, SAMPLE_RATE, CHUNK, SYMBL_AI_APP_ID, SYMBL_AI_APP_SECRET) -> None:
        self.SAMPLE_RATE = SAMPLE_RATE
        self.CHUNK = CHUNK
        self.SYMBL_AI_APP_ID = SYMBL_AI_APP_ID
        self.SYMBL_AI_APP_SECRET = SYMBL_AI_APP_SECRET

        self.source = None

    def selectSource(self) -> None:
        speakers = sc.all_speakers()

        for index, speaker in enumerate(speakers):
            print(f"{index} : {speaker.name}")

        choice = int(input("Select a source: "))

        try:
            if choice > 0:
                self.source = speakers[choice]
            else:
                raise IndexError
        except IndexError:
            print("Invalid choice")
            exit()

    def getSourceStream(self, conn) -> None:
        if self.source is None:
            raise ValueError("No source selected")

        with sc.get_microphone(id=str(self.source.name), include_loopback=True).recorder(
            samplerate=self.SAMPLE_RATE,
            blocksize=self.CHUNK,
        ) as mic:
            print("Listening...")

            while True:
                stream = mic.record()

                converted_stream = stream.copy().tobytes()

                if converted_stream:
                    conn.send_audio(converted_stream)

                mic.flush()
