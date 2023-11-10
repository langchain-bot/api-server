from flask import Flask, jsonify, request
import chatgpt

app = Flask(__name__)


@app.route("/")
def index():
    return jsonify({"status": "healthy"})


@app.route("/items", methods=["POST"])
def chat():
    text = request.json["text"]
    result = chatgpt.query_question(text)
    return jsonify({"message": result})


if __name__ == "__main__":
    app.run(debug=True)
