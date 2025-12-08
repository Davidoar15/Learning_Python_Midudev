persona = {
    "name": "davidoar",
    "age": 23,
    "socials": {
        "instagram": "davidoar15",
        "smogon": "Davidoar15"
    },
    "is_married": False,
    "best_months_of_the_year": [2, 5, 7, 8, 10, 12]
}

print(persona["name"]) # davidoar
print(persona["best_months_of_the_year"][2]) # 7
print(persona["socials"]["smogon"]) # Davidoar15
print(type(persona)) # <class 'dict'>

persona["name"] = "David"
print(persona["name"]) # David


del persona["age"]
print(persona) # {'name': 'David', 'socials': {'instagram': 'davidoar15', 'smogon': 'Davidoar15'}, 'is_married': False, 'best_months_of_the_year': [2, 5, 7, 8, 10, 12]}

is_married = persona.pop("is_married")
print(f"Is married? { "YES" if is_married else "NO" }") # Is married? NO
print(persona) # {'name': 'David', 'socials': {'instagram': 'davidoar15', 'smogon': 'Davidoar15'}, 'best_months_of_the_year': [2, 5, 7, 8, 10, 12]}


persona_a = { "name": "locura", "age": 23 }
persona_b = { "name": "David", "is_married": False }

persona_a.update(persona_b) # a <- b
print(persona_a) # {'name': 'David', 'age': 23, 'is_married': False}


print(persona.keys()) # dict_keys(['name', 'socials', 'best_months_of_the_year'])
print(persona.values()) # dict_values(['David', {'instagram': 'davidoar15', 'smogon': 'Davidoar15'}, [2, 5, 7, 8, 10, 12]])
print(persona.items()) # dict_items([('name', 'David'), ('socials', {'instagram': 'davidoar15', 'smogon': 'Davidoar15'}), ('best_months_of_the_year', [2, 5, 7, 8, 10, 12])])
