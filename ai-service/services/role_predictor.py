import joblib

model = joblib.load("models/role_model.pkl")
vectorizer = joblib.load("models/vectorizer.pkl")

def predict_role(text):

    text_vector = vectorizer.transform([text])

    prediction = model.predict(text_vector)

    return prediction[0]