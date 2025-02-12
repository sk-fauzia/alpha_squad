# Symptom Checker and Advisor

# Sample dictionary of common symptoms and possible conditions
symptom_conditions = {
    "fever": ["flu", "cold", "COVID-19", "malaria", "chickenpox"],
    "cough": ["flu", "cold", "COVID-19", "pneumonia"],
    "headache": ["migraine", "stress", "cold", "COVID-19"],
    "sore throat": ["cold", "flu", "COVID-19"],
    "fatigue": ["flu", "COVID-19", "anemia", "depression"],
    "shortness of breath": ["COVID-19", "asthma", "pneumonia"],
    "chest pain": ["heart attack", "angina", "pneumonia"],
    "runny nose": ["cold", "flu", "allergies"],
    "body aches": ["flu", "cold", "COVID-19"],
    "nausea": ["flu", "food poisoning", "pregnancy", "stress"],
    "vomiting": ["food poisoning", "flu", "gastritis"],
    "rash": ["chickenpox", "measles", "allergies", "eczema"],
    "diarrhea": ["food poisoning", "gastroenteritis", "stress"],
}

def check_symptoms():
    print("Welcome to the Symptom Checker!")
    print("Please enter your symptoms from the list: fever, cough, headache, sore throat, fatigue, shortness of breath, chest pain, runny nose, body aches, nausea, vomiting, rash, diarrhea")
    print("You can enter multiple symptoms, separated by commas.")
    
    # User input
    user_input = input("Enter your symptoms: ").lower()
    
    # Split symptoms into a list
    symptoms = [symptom.strip() for symptom in user_input.split(',')]
    
    # Store possible conditions based on symptoms
    possible_conditions = set()
    
    for symptom in symptoms:
        if symptom in symptom_conditions:
            possible_conditions.update(symptom_conditions[symptom])
        else:
            print(f"Symptom '{symptom}' is not in the database. Please check your input.")
    
    # Output results
    if possible_conditions:
        print("\nBased on your symptoms, the possible conditions could be:")
        for condition in possible_conditions:
            print(f"- {condition}")
        
        print("\nHowever, it's important to consult a healthcare provider for an accurate diagnosis.")
    else:
        print("No conditions found for the entered symptoms. Please try again.")

def main():
    while True:
        check_symptoms()
        another_check = input("\nWould you like to check symptoms again? (yes/no): ").lower()
        if another_check != 'yes':
            print("Thank you for using the Symptom Checker. Stay healthy!")
            break

# Run the program
if __name__ == "__main__":
    main()
