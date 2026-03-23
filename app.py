import pickle

model_hw = pickle.load(open("model_height_to_weight.pkl", "rb"))
model_wh = pickle.load(open("model_weight_to_height.pkl", "rb"))

print("----- HEIGHT & WEIGHT PREDICTION SYSTEM -----")

while True:
    print("\n1. Predict Weight from Height")
    print("2. Predict Height from Weight")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == '1':
        height = float(input("Enter Height (cm): "))
        age = float(input("Enter Age: "))
        gender = int(input("Enter Gender (0=Female, 1=Male): "))

        result = model_hw.predict([[height, age, gender]])
        print(f"Predicted Weight: {result[0]:.2f} kg")

    elif choice == '2':
        weight = float(input("Enter Weight (kg): "))
        age = float(input("Enter Age: "))
        gender = int(input("Enter Gender (0=Female, 1=Male): "))

        result = model_wh.predict([[weight, age, gender]])
        print(f"Predicted Height: {result[0]:.2f} cm")

    elif choice == '3':
        break