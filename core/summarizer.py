import nltk
from nltk.tokenize import sent_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def summarize_text(text, num_sentences=3):
    sentences = sent_tokenize(text)

    if len(sentences) <= num_sentences:
        return text

    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(sentences)
    similarity_matrix = cosine_similarity(X)
    scores = similarity_matrix.sum(axis=1)

    ranked_sentences = sorted(
        ((scores[i], s) for i, s in enumerate(sentences)),
        reverse=True
    )

    summary = " ".join([ranked_sentences[i][1] for i in range(num_sentences)])
    return summary