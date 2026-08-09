from flask import Flask, request, jsonify, render_template_string
import pickle

app = Flask(__name__)

# Load model
model = pickle.load(open("model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

# ✅ HTML Page (for GET)
HTML_PAGE = """
<!DOCTYPE html>
<html>
<head>
    <title>Sentiment Analysis</title>
</head>
<body>
    <h2>Sentiment Analysis</h2>
    <form method="post" action="/predict">
        <input type="text" name="text" placeholder="Enter text" required>
        <button type="submit">Predict</button>
    </form>
</body>
</html>
"""

# Home route
@app.route('/')
def home():
    return "Go to /predict"

# ✅ GET + POST
@app.route('/predict', methods=['GET', 'POST'])
def predict():
    try:
        # ✅ GET → show UI page
        if request.method == 'GET':
            return render_template_string(HTML_PAGE)

        # ✅ POST → get input from form or JSON
        text = request.form.get('text')

        if not text:
            data = request.get_json(silent=True) or {}
            text = data.get('text')

        if not text:
            return jsonify({"error": "Enter text"}), 400

        # Prediction
        transformed = vectorizer.transform([text])
        prediction = model.predict(transformed)[0]

        sentiment = "Positive" if int(prediction) == 1 else "Negative"

        # ✅ Return result in browser
        return f"<h3>Input: {text}</h3><h2>Sentiment: {sentiment}</h2>"

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)