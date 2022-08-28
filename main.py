import json

from libs.audioManager import AudioManager
from libs.translationManager import TranslationManager


with open("credentials.json") as f:
    credentials = json.load(f)

SYMBL_AI_APP_ID = credentials["SYMBL_AI_APP_ID"]
SYMBL_AI_APP_SECRET = credentials["SYMBL_AI_APP_SECRET"]
DEEPL_API_KEY = credentials["DEEPL_API_KEY"]


translationManager = TranslationManager(DEEPL_API_KEY=DEEPL_API_KEY)

print("------------------------------")

translationManager.getTargetLang()


audioManager = AudioManager(
    translationManager=translationManager, SYMBL_AI_APP_ID=SYMBL_AI_APP_ID, SYMBL_AI_APP_SECRET=SYMBL_AI_APP_SECRET
)

print("------------------------------")

audioManager.selectSource()

print("------------------------------")

audioManager.getSourceStream()
