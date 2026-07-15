country_code = {"India": "0091", "Australia": "0025", "Nepal": "0097"}
print("The country code for Australia is", country_code.get("Australia", "Not found"))
print("The country code for Italy is", country_code.get("Italy", "not found"))


O = {"Colour": "Orange", "Fruit": "Orange", "City": "Orange", "Dessert": "Chiffon Cake"} 
print(O)
element = "Orange"
result = 0
for i in O:
    if O [i]== element:
        result = result + 1
print(result)