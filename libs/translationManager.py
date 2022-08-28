import json
import requests as req


class TranslationManager:
    def __init__(self, DEEPL_API_KEY) -> None:
        self.DEEPL_API_KEY = DEEPL_API_KEY

        with open("langs.json") as f:
            self.langs = json.load(f)

        self.targetLang = None

    def getTargetLang(self) -> None:
        for index, lang in enumerate(self.langs):
            print(f"{index} : {lang}")

        choice = int(input("Select the target lang: "))

        try:
            if choice >= 0:
                self.targetLang = self.langs[list(self.langs.keys())[choice]]
            else:
                raise IndexError
        except IndexError:
            print("Invalid choice")
            exit()

    def translateText(self, text) -> str:
        if self.targetLang is None:
            raise ValueError("No target lang selected")

        url = f"https://api-free.deepl.com/v2/translate?auth_key={self.DEEPL_API_KEY}&text={text}&target_lang={self.targetLang}"

        res = req.get(url)

        translated = res.json()["translations"][0]["text"]

        return translated
