print("🏥 Healthcare AI Assistant")
print("Welcome!")

symptoms = input("Enter your symptoms: ").lower()

if "fever" in symptoms:
    print("Possible condition: Fever-related illness")
    print("Advice: Rest, drink enough fluids, and monitor your temperature.")

elif "cough" in symptoms:
    print("Possible condition: Common respiratory illness")
    print("Advice: Stay hydrated and get adequate rest.")

elif "headache" in symptoms:
    print("Possible condition: Common headache")
    print("Advice: Rest, drink water, and avoid excessive screen time.")

elif "stomach pain" in symptoms:
    print("Possible condition: Digestive problem")
    print("Advice: Drink water and eat light food.")

else:
    print("I don't have enough information about these symptoms.")
    print("Please consult a qualified medical professional.")

print("\n⚠️ This project is for educational purposes only.")
