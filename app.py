from flask import Flask, render_template, request, jsonify
from googletrans import Translator

app = Flask(__name__)
translator = Translator()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/translate", methods=["POST"])
def translate():
    data = request.get_json()
    text = data.get("text", "")
    src = data.get("src", "auto")
    dest = data.get("dest", "en")

    if not text.strip():
        return jsonify({"error": "Text is empty"}), 400

    result = translator.translate(text, src=src, dest=dest)
    return jsonify({"translated": result.text})

if __name__ == "__main__":
    app.run(debug=True, port=5001)
