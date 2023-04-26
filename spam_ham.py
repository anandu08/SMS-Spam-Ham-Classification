import joblib
model=joblib.load('model.joblib')
text="You have won 100000"
def predict_spam_ham(text):
    text=text_process(text)
    pred=model.predict([text])[0]
    if pred==0:
        return 'ham'
    else:
        return 'spam'
print(predict_spam_ham)