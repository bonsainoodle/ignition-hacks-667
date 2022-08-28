import json

from audioManager import AudioManager


with open("credentials.json") as f:
    credentials = json.load(f)

SYMBL_AI_APP_ID = credentials["SYMBL_AI_APP_ID"]
SYMBL_AI_APP_SECRET = credentials["SYMBL_AI_APP_SECRET"]


audioManager = AudioManager(
    SAMPLE_RATE=48000, CHUNK=1024, SYMBL_AI_APP_ID=SYMBL_AI_APP_ID, SYMBL_AI_APP_SECRET=SYMBL_AI_APP_SECRET
)

audioManager.selectSource()

audioManager.getSourceStream()
