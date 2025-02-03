symptoms_list = [
    "Wheezing", "Shortness of Breath", "Chest Tightness", "Cough", "Fever",
    "Chills", "Abdominal Pain", "Headaches", "Nausea", "Joint Pain", "Skin Rash"
]


def symptoms_to_array(selected_symptoms, symptoms_list):
    # Create a binary array based on reported symptoms
    return [1 if symptom in selected_symptoms else 0 for symptom in symptoms_list]



