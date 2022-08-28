import json
import symbl
from audioManager import AudioManager


with open("credentials.json") as f:
    credentials = json.load(f)

SYMBL_AI_APP_ID = credentials["SYMBL_AI_APP_ID"]
SYMBL_AI_APP_SECRET = credentials["SYMBL_AI_APP_SECRET"]


audioManager = AudioManager(
    SAMPLE_RATE=48000, CHUNK=1024, SYMBL_AI_APP_ID=SYMBL_AI_APP_ID, SYMBL_AI_APP_SECRET=SYMBL_AI_APP_SECRET
)

audioManager.selectSource()

events = {
    "message_response": lambda response: print(
        "Final Messages -> ",
        [message["payload"]["content"] for message in response["messages"]],
    ),
    "message": lambda response: print("live transcription : {}".format(response["message"]["punctuated"]["transcript"]))
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
    "speechRecognition": {"sampleRateHertz": 48000},
}

conn = symbl.Streaming.start_connection(
    credentials={"app_id": SYMBL_AI_APP_ID, "app_secret": SYMBL_AI_APP_SECRET},
    insight_types=["question", "action_item", "follow_up", "topic"],
    config=SYMBL_CONFIG,
)

conn.subscribe(events)

audioManager.selectSource()

audioManager.getSourceStream()
