import symbl


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
    "speechRecognition": {"sampleRateHertz": 44100},
}

SYMBL_AI_APP_ID = "7433624d4367486372624573506a7654566b726434716747554f546b66486546"
SYMBL_AI_APP_SECRET = "48414d786f4c2d796936397768304574506630682d4a644e4568376e62443539534f425a564e53585838524c495a6657384e78633739306b7954542d725f456e"

conn = symbl.Streaming.start_connection(
    credentials={"app_id": SYMBL_AI_APP_ID, "app_secret": SYMBL_AI_APP_SECRET},
    insight_types=["question", "action_item", "follow_up", "topic"],
    config=SYMBL_CONFIG,
)

conn.subscribe(events)

conn.send_audio_from_mic()
