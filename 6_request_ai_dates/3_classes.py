class Car:
    type = "4-wheel vehicle"
    wheels = 4

    def __init__(self, brand, model, color):
        self.brand = brand        
        self.model = model        
        self.color = color    

    def start(self):
        print(f"The car { self.brand } { self.model } started!")
    
my_car = Car("Toyota", "Corolla", "Red")
friend_car = Car("Ford", "Fiesta", "Blue")
my_car.start() # The car Toyota Corolla started!
friend_car.start() # The car Ford Fiesta started!

import requests
class AI_API:
    def __init__(self, api_key, url, model):
        self.api_key = api_key
        self.url = url
        self.model = model

    def call(self, prompt):
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer { self.api_key }"
        }
        data = {
            "model": self.model,
            "messages": [{ "role": "user", "content": prompt }]
        }
        try:
            response = requests.post(self.url, json=data, headers=headers)
            res_json = response.json()
            print(res_json["choices"][0]["message"]["content"])
        except requests.exceptions.RequestException as e:
            print(f"ERROR OF REQUEST: { e }")

openai_api = AI_API(OPENAI_KEY, "https://api.openai.com/v1/chat/completions", "gpt-4o-mini")
openai_api.call("Escribe un breve poema sobre la vida")

deepseek_api = AI_API(DEEPSEEK_KEY, "https://api.deepseek.com/chat/completions", "deepseek-chat")
deepseek_api.call("Escribe un breve poema sobre la vida")
