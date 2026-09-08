from flask import Flask, jsonify

app = Flask(__name__)


@app.get("/health")
def health():
    return jsonify({"status": "UP"})


if __name__ == "__main__":
    app.run()
