import sys
import sounddevice as sd
import symbl


class AudioManager:
    def __init__(self, translationManager, speakerManager, SYMBL_AI_APP_ID, SYMBL_AI_APP_SECRET) -> None:
        self.translationManager = translationManager
        self.speakerManager = speakerManager
        self.SYMBL_AI_APP_ID = SYMBL_AI_APP_ID
        self.SYMBL_AI_APP_SECRET = SYMBL_AI_APP_SECRET

        self.source = None

    def selectSource(self) -> None:
        sources = sd.query_devices()
        
        inputs = []

        for index, source in enumerate(sources):
            if source["max_input_channels"] != 0 and source["max_output_channels"] == 0:
                inputs.append(source)

        for index, input_ in enumerate(inputs):
            print(f"{index} : {input_['name']}")

        choice = int(input("Select a source: "))

        try:
            if choice >= 0:
                self.source = inputs[choice]
                self.source = inputs[choice]
            else:
                raise IndexError
        except IndexError:
            print("Invalid choice")
            sys.exit(-1)

    def getSourceStream(self) -> None:
        if self.source is None:
            raise ValueError("No source selected")

        def callback(response) -> None:
            print("------------------------------")

            phrases = [message["payload"]["content"] for message in response["messages"]]

            toTranslate = " ".join(phrases)

            translated = self.translationManager.translateText(toTranslate)

            self.speakerManager.read(translated, self.translationManager.targetLang)
            print(translated)

        events = {"message_response": lambda response: callback(response)}

        conn = symbl.Streaming.start_connection(
            credentials={"app_id": self.SYMBL_AI_APP_ID, "app_secret": self.SYMBL_AI_APP_SECRET},
        )

        conn.subscribe(events)

        conn.send_audio_from_mic(device=self.source["index"])
