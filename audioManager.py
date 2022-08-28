import soundcard as sc


class AudioManager:
    def __init__(self, SAMPLE_RATE, CHUNK, SYMBL_AI_APP_ID, SYMBL_AI_APP_SECRET) -> None:
        self.SAMPLE_RATE = SAMPLE_RATE
        self.CHUNK = CHUNK
        self.SYMBL_AI_APP_ID = SYMBL_AI_APP_ID
        self.SYMBL_AI_APP_SECRET = SYMBL_AI_APP_SECRET
        
        self.source = None
        self.stream = []

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

    def getSourceStream(self) -> None:
        if self.source is None:
            raise ValueError("No source selected")

        with sc.get_microphone(id=str(self.source.name), include_loopback=True).recorder(
            samplerate=self.SAMPLE_RATE
        ) as mic:

            print("Listening...")

            while True:
                stream = mic.record(numframes=self.CHUNK).tolist()

                for frame in stream:
                    self.stream.append(frame)

    def stream2Text(self) -> None:
        if not self.stream:
            raise ValueError("No stream data")
        else:
            pass
