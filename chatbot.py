from MachineLearning import predict_risk_level, model, rf_model
from symptom_mapper import symptoms_to_array, symptoms_list


def chatbot():


    print("Available symptoms:", ", ".join(symptoms_list))
    user_symptoms = input("Enter your symptoms, separated by commas: ").split(",")
    user_symptoms = [symptom.strip() for symptom in user_symptoms]  # Clean up spaces

    # Debugging: Print the user-selected symptoms
    print("User-selected symptoms after cleaning:", user_symptoms)

    # Convert to binary array
    symptom_array = symptoms_to_array(user_symptoms, symptoms_list)

    # Predict risk level using both models
    predicted_risk_tree = model.predict([symptom_array])[0]
    predicted_risk_rf = rf_model.predict([symptom_array])[0]

    print(f"Predicted Risk Level (Decision Tree): {predicted_risk_tree}")
    print(f"Predicted Risk Level (Random Forest): {predicted_risk_rf}")
'''
    # Ask for user feedback
    print("\nDid the prediction match your expectations?")
    print(f"1. {predicted_risk_tree}")
    print(f"2. {predicted_risk_rf}")
    print("3. Neither of the above")
    print("4. Provide your own diagnosis")

    user_feedback = input("Choose an option (1-4): ")

    if user_feedback == "1":
        print("Thank you for confirming the Decision Tree model's prediction!")
    elif user_feedback == "2":
        print("Thank you for confirming the Random Forest model's prediction!")
    elif user_feedback == "3":
        print("Sorry for the mismatch. We’ll work on improving the model!")
    elif user_feedback == "4":
        true_risk = input("Please provide your diagnosis or risk level: ")
        print(f"Thank you for your feedback: '{true_risk}'. We’ll use this for improvement.")
    else:
        print("Invalid input. Feedback not recorded.")
'''

# Run the chatbot
if __name__ == "__main__":
    chatbot()
