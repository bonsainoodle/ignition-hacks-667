import sounddevice as sd
import symbl
import numpy as np


class AudioManager:
    def __init__(self, SYMBL_AI_APP_ID, SYMBL_AI_APP_SECRET) -> None:
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
<<<<<<< HEAD
                self.source = speakers[choice]
=======
                self.source = sources[choice]
>>>>>>> 56fd027f559e0e02137361525b58ca4199c02cc2
            else:
                raise IndexError
        except IndexError:
            print("Invalid choice")
            exit()

    def getSourceStream(self) -> None:
        if self.source is None:
            raise ValueError("No source selected")

        events = {
            "message_response": lambda response: print(
                "Final Messages -> ",
                [message["payload"]["content"] for message in response["messages"]],
            ),
            "message": lambda response: print(
                "live transcription : {}".format(response["message"]["punctuated"]["transcript"])
            )
            if "punctuated" in response["message"]
            else print(response),
            "insight_response": lambda response: [
                print("Insights Item of type {} detected -> {}".format(insight["type"], insight["payload"]["content"]))
                for insight in response["insights"]
            ],
            "topic_response": lambda response: [
                print("Topic detected -> {} with root words, {}".format(topic["phrases"], topic["rootWords"]))
                for topic in response["topics"]
            ],
        }

        SYMBL_CONFIG = {
            "confidenceThreshold": 0.5,
            "speechRecognition": {"sampleRateHertz": 44100},
        }

        conn = symbl.Streaming.start_connection(
            credentials={"app_id": self.SYMBL_AI_APP_ID, "app_secret": self.SYMBL_AI_APP_SECRET},
            insight_types=["question", "action_item", "follow_up", "topic"],
            config=SYMBL_CONFIG,
        )

        conn.subscribe(events)

        conn.send_audio_from_mic(device=self.source["index"])
