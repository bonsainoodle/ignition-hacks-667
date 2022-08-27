import soundcard as sc


class AudioManager:
    def __init__(self, SAMPLE_RATE, CHUNK) -> None:
        self.SAMPLE_RATE = SAMPLE_RATE
        self.CHUNK = CHUNK
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
            self.selectSource()
        with sc.get_microphone(id=str(self.source.name), include_loopback=True).recorder(
            samplerate=self.SAMPLE_RATE
        ) as mic:

            while True:
                stream = mic.record(numframes=self.CHUNK).tolist()

                for frame in stream:
                    self.stream.append(frame)


audioManager = AudioManager(SAMPLE_RATE=48000, CHUNK=1024)

audioManager.selectSource()

audioManager.getSourceStream()
