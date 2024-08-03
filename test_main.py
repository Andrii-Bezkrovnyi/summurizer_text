import requests
import json

url = "http://127.0.0.1:8000/summarizer"
text = {"text": """Here is text example for checking work of the code is. You can add any text here.
                    It’s seven o’clock now and I have to make dinner for me and Jon. Mum and Dad are too ill to cook. 
                    I have made some mint tea for Dad because he shouldn’t eat anything today. 
                    Mum’s had some tomato soup and toast. I’ve boiled some spaghetti and 
                    I have made tomato sauce for me and Jon.
                    And after dinner I’m going to bed. I’ve got a headache!"""}

text = json.dumps(text)
response = requests.post(url, data=text).json()
print(f"Text summary -> {response['summary']}")
