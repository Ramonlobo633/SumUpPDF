from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import joblib

def train(texts, labels):
    vectorizer = TfidfVectorizer(
        analyzer="char",
        ngram_range=(3, 5),
        min_df=2
    )

    X = vectorizer.fit_transform(texts)

    clf = LogisticRegression(max_iter=1000)
    clf.fit(X, labels)

    joblib.dump(vectorizer, "vectorizer.joblib")
    joblib.dump(clf, "model.joblib")
