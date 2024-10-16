from sklearn.tree import DecisionTreeClassifier # decision tree model from scikit - learn where scikit learn is a python library for machine learning
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Example data: Symptoms and corresponding risk levels
# Symptoms: [Wheezing, Shortness of Breath, Chest Tightness, Cough, Fever, Chills, Abdominal Pain, Headaches, Nausea, Joint Pain, Skin Rash]
symptoms = [
    # Respiratory diseases
    [1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0],  # Asthma: Wheezing, Shortness of Breath, Chest Tightness, Cough
    [0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0],  # Pneumonia: Shortness of Breath, Cough, Fever, Chills

    # Digestive disorders
    [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],  # GERD: Abdominal pain, Heartburn
    [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],  # IBS: Abdominal pain, bloating, diarrhea

    # Cardiovascular diseases
    [0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0],  # Heart Attack: Chest pain, shortness of breath, nausea, lightheadedness
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0],  # Hypertension: Asymptomatic or headaches

    # Neurological disorders
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0],  # Migraine: Headaches, nausea, sensitivity to light
    [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],  # Multiple sclerosis: Fatigue, numbness, difficulty walking

    # Infectious diseases
    [0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0],  # COVID-19: Fever, cough, fatigue
    [0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0],  # Tuberculosis: Persistent cough, weight loss, night sweats, fever

    # Autoimmune diseases
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],  # Rheumatoid Arthritis: Joint pain, swelling, stiffness
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],  # Lupus: Fatigue, joint pain, skin rash, fever

    # Endocrine disorders
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Diabetes: Thirst, frequent urination, fatigue, blurred vision
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Hypothyroidism: Fatigue, weight gain, cold intolerance, depression

    # Mental health disorders
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],  # Depression: Sadness, loss of interest, appetite changes
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],  # Anxiety: Excessive worry, restlessness

    # Skin conditions
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],  # Psoriasis: Red patches with silvery scales
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],  # Eczema: Itchy, inflamed skin

    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], # no symptoms and risk
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0]
]
# Corresponding risk levels for the above symptoms# Mathi jati ota symptoms haru xa teti ota risk level banaunu pryo (21=21) and they are corresponding
risk_levels = [
    'medium', 'high',  # Respiratory diseases
    'low', 'medium',   # Digestive disorders
    'very high', 'high',  # Cardiovascular diseases
    'medium', 'high',  # Neurological disorders
    'medium', 'high',  # Infectious diseases
    'low', 'medium',  # Autoimmune diseases
    'low', 'low',     # Endocrine disorders
    'medium', 'medium',  # Mental health disorders
    'low', 'low',    # Skin conditions
    'no risk','no risk','no risk'
]

# Step 1: Create a DecisionTreeClassifier model
model = DecisionTreeClassifier()

#create the random forest model
rf_model = RandomForestClassifier(n_estimators=20,random_state=42)

#step2 : training the model (fitting the model on example data)
model.fit(symptoms,risk_levels)

#train the rf model  (fitting the model on example data)
rf_model.fit(symptoms,risk_levels)

#step3 : making predictions
#suppose a new user reports fever,cough,and fatigue but not remaining others
new_symptom=[1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0]
new_symptom1=[0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0]

#step4: predicting the risk levels for new user with decision tree
predicted_risk = model.predict([new_symptom])
predicted_risk1 =model.predict([new_symptom1])

#predicting with the rf model
predicted_risk_rf = rf_model.predict([new_symptom])
predicted_risk1_rf = rf_model.predict([new_symptom1])

# Predicted risk levels for all the training data
train_predictions = model.predict(symptoms)
train_predictions_rf = rf_model.predict(symptoms)

# Check accuracy on training data on rf model
accuracy = accuracy_score(risk_levels, train_predictions_rf)
print(f"Accuracy on training data of rf: {accuracy * 100}%")

# Check accuracy on training data on tree
accuracy = accuracy_score(risk_levels, train_predictions)
#print(f"Accuracy on training data of tree: {accuracy * 100}%")

#giving output of predicted risk level with decision tree model
#print("predicted risk level:",predicted_risk[0])
#print("predicted risk level:",predicted_risk1[0])

#giving output of predicted risk level with random forest model

print("predicted risk level:",predicted_risk_rf[0])
print("predicted risk level:",predicted_risk1_rf[0])