from translation_history import TranslationHistory
import requests
import json

# class ApiInterface:


url = 'https://api.restful-api.dev/objects'
obj = {
    'name': "Jack",
    "data": {
        "history1": {
            "src_text": "hello", "trg_lang": "fa", "src_lang": "en", "trg_text": "", "date": "2014"
        }
    }
}

y = requests.post(url, json=obj)
print(y.json())
x = requests.get(url)
# x = requests.get(url+"?id=ff8081818ead0ebb018ead5881e0033e")
# print(x.json())
print(x)
