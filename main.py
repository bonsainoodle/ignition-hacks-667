import json
import symbl
from audioManager import AudioManager


with open("credentials.json") as f:
    credentials = json.load(f)

SYMBL_AI_APP_ID = credentials["SYMBL_AI_APP_ID"]
SYMBL_AI_APP_SECRET = credentials["SYMBL_AI_APP_SECRET"]


audioManager = AudioManager(SYMBL_AI_APP_ID=SYMBL_AI_APP_ID, SYMBL_AI_APP_SECRET=SYMBL_AI_APP_SECRET)

audioManager.selectSource()

audioManager.getSourceStream()
