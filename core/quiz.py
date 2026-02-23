import random
from nltk.tokenize import sent_tokenize, word_tokenize

def generate_quiz(text):
    sentences = sent_tokenize(text)
    quiz_questions = []

    for sentence in sentences[:5]:
        words = word_tokenize(sentence)
        if len(words) > 6:
            answer = random.choice(words)
            question = sentence.replace(answer, "_____")
            quiz_questions.append((question, answer))

    return quiz_questions