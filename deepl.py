### Made by vlad !!!!!!! aka mosh

import requests
import json


api_key = '3f7220e6-f6dd-d70d-e1e4-a1401f760f42:fx'
url_de_deepl = 'https://api-free.deepl.com/v2/translate'
mock_text = "you fuck my wife ? you fuck my wife i fuck your wife!"


available_langs = {
        "Bulgarian" : "BG" ,
        "Czech" : "CS" ,
        "Danish" : "DA" ,
        "German" :"DE" ,
        "Greek" : "EL",
        "Spanish" : "ES" ,
        "Estonian" : "ET",
        "English" : "EN",
        "Finnish" :"FI" ,
        "French" :"FR" ,
        "Hungarian" : "HU",
        "Indonesian" : "ID" ,
        "Italian" : "IT",
        "Japanese" : "JA",
        "Lithuanian" : "LT",
        "Latvian" : "LV",
        "Dutch" : "NL",
        "Polish" : "PL",
        "Portuguese" : "PT",
        "Romanian" : "RO",
        "Russian" : "RU",
        "Slovak" : "SK",
        "Slovenian" : "SL",
        "Swedish" : "SV",
        "Turkish" : "TR",
        "Chinese" : "ZH"
} 



for langs in available_langs:
    print(langs)
lang_choosed = input("dans quelle langue souhaitez vous traduire ? ")



if lang_choosed.capitalize() in available_langs:
    lang_code = available_langs[lang_choosed.capitalize()]
        


url = f"https://api-free.deepl.com/v2/translate?auth_key={api_key}&text={mock_text}&target_lang={lang_code}"
print(url)

output1= requests.get(url)
final_output = output1.json()["translations"][0]["text"]

print(final_output)
        









    
