from sklearn.metrics.pairwise import cosine_similarity
from sentence_transformers import SentenceTransformer
import pandas as pd

model = SentenceTransformer("all-MiniLM-L6-v2")

jobs_df = pd.read_csv("datasets/job_dataset.csv")

jobs_texts = jobs_df.astype(str).agg(" ".join, axis=1).tolist()

job_embeddings = model.encode(jobs_texts)

def match_jobs(resume_text):

    resume_embedding = model.encode([resume_text])

    similarities = cosine_similarity(
        resume_embedding,
        job_embeddings
    )[0]

    top_indices = similarities.argsort()[-5:][::-1]

    matched_jobs = []

    for idx in top_indices:

        matched_jobs.append({
            "job": jobs_texts[idx],
            "score": float(similarities[idx])
        })

    return matched_jobs