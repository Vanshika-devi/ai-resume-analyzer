import joblib

model = joblib.load("models/ats_model.pkl")
vectorizer = joblib.load("models/vectorizer.pkl")

def predict_ats_score(text):

    text_vector = vectorizer.transform([text])

    score = model.predict(text_vector)

    return round(float(score[0]), 2)