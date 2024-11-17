import json

# Початкові дані
data = {
    "Passengers": [
        {"Surname": "Jackson", "Pieces_baggage": 3, "Weight": 20.5},
        {"Surname": "Chetwynd", "Pieces_baggage": 1, "Weight": 4.3},
        {"Surname": "Pisarev", "Pieces_baggage": 5, "Weight": 15.0},
    ]
}

# Записуємо початкові дані у файл
with open("passengers.json", "w", encoding="utf-8") as file:
    json.dump(data, file, ensure_ascii=False, indent=4)

# Меню
while True:
    print("\nMenu:")
    print("1 - Add data")
    print("2 - View data")
    print("3 - Find passengers with two and more pieces of baggage")
    print("4 - Analyze passengers by weight categories")
    print("5 - Exit")
    option = int(input("Choose option: "))

    if option == 1:  # Додавання даних
        with open("passengers.json", "r", encoding="utf-8") as file:
            data = json.load(file)

        def add_passenger(data):
            print("Add new passenger:")
            surname = input("Surname: ")
            items = int(input("Pieces of baggage: "))
            weight = float(input("Weight (kg): "))
            data["Passengers"].append({"Surname": surname, "Pieces_baggage": items, "Weight": weight})
            return data

        data = add_passenger(data)
        with open("passengers.json", "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)
        print("Data added.")

    elif option == 2:  # Перегляд даних
        with open("passengers.json", "r", encoding="utf-8") as file:
            data = json.load(file)
        print("Passenger data:")
        for passenger in data["Passengers"]:
            print(passenger)

    elif option == 3:  # Пошук пасажирів із більше ніж двома речами
        with open("passengers.json", "r", encoding="utf-8") as file:
            data = json.load(file)
        result = [p for p in data["Passengers"] if p["Pieces_baggage"] > 2]
        print("Passengers with two and more pieces of baggage:")
        print(*result, sep='\n')

    elif option == 4:  # Визначення кількості пасажирів за ваговими категоріями
        with open("passengers.json", "r", encoding="utf-8") as file:
            data = json.load(file)

        categories = {
            "less than 5 kg": len([p for p in data["Passengers"] if p["Weight"] < 5]),
            "from 5 to 25 kg": len([p for p in data["Passengers"] if 5 <= p["Weight"] <= 25]),
            "over 25 kg": len([p for p in data["Passengers"] if p["Weight"] > 25]),
        }

        print("Number of passengers by weight categories:")
        for category, count in categories.items():
            print(f"{category}: {count} passengers")

    elif option == 5:  # Вихід
        print("Exit. Thank you!")
        break

    else:
        print("Error. Enter the correct number for the option.")
