from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

model = pickle.load(open("spam_model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

@app.route("/", methods=["GET", "POST"])
def home():
    prediction = ""

    if request.method == "POST":
        email = request.form["email"]

        data = vectorizer.transform([email])

        result = model.predict(data)[0]

        if result == 1:
            prediction = "⚠️ Spam ⚠️"
        else:
            prediction = "✔️ Not Spam ✔️"

    return render_template("index.html",
                           prediction=prediction)

if __name__ == "__main__":
    app.run(debug=True)