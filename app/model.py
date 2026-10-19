import pickle

vec, clf = pickle.load(open("ml/registry/spam_model.pkl", "rb"))


def predict(text):
    x = vec.transform([text])
    label_id = clf.predict(x)[0]
    proba = clf.predict_proba(x)[0]
    label = "spam" if label_id == 1 else "ham"
    confidence = round(max(proba), 4)
    return {"label": label, "confidence": confidence}
