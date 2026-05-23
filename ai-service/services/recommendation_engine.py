import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer

jobs_df = pd.read_csv("datasets/job_dataset.csv")

jobs_df["combined"] = jobs_df.astype(str).agg(" ".join, axis=1)

vectorizer = TfidfVectorizer()

job_vectors = vectorizer.fit_transform(jobs_df["combined"])

def recommend_jobs(resume_text):

    resume_vector = vectorizer.transform([resume_text])

    similarity = cosine_similarity(resume_vector, job_vectors)

    top_indexes = similarity[0].argsort()[-5:][::-1]

    recommendations = []

    for idx in top_indexes:

        recommendations.append(
            jobs_df.iloc[idx].to_dict()
        )

    return recommendations