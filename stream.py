import symbl

# START changing values here.

app_id = "7433624d4367486372624573506a7654566b726434716747554f546b66486546"
app_secret = "48414d786f4c2d796936397768304574506630682d4a644e4568376e62443539534f425a564e53585838524c495a6657384e78633739306b7954542d725f456e"

config = {
  "meetingTitle": "appel slovaquie",
  
}

speaker = {
  "name": "grigor",
  "email": "vladimirjurien@gmail.com"
}

# STOP changing values here.

events = {
    "message_response": lambda response: print(
        "Final Messages -> ",
        [message["payload"]["content"] for message in response["messages"]],
    ),
    "message": lambda response: print(
        "live transcription : {}".format(
            response["message"]["punctuated"]["transcript"]
        )
    )
    if "punctuated" in response["message"]
    else print(response),
    "insight_response": lambda response: [
        print(
            "Insights Item of type {} detected -> {}".format(
                insight["type"], insight["payload"]["content"]
            )
        )
        for insight in response["insights"]
    ],
    "topic_response": lambda response: [
        print(
            "Topic detected -> {} with root words, {}".format(
                topic["phrases"], topic["rootWords"]
            )
        )
        for topic in response["topics"]
    ],
}

connection_object = symbl.Streaming.start_connection(
    credentials={"app_id": app_id, "app_secret": app_secret},
    insight_types=["question", "action_item", "follow_up", "topic"],
    speaker=speaker,
    config=config
)

connection_object.subscribe(events)
connection_object.send_audio_from_mic()

# connection_object.stop() # ends the connection.