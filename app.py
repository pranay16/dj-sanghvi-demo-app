from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "Hello from the Engineering Class 👋"

if __name__ == "__main__":
    # 0.0.0.0 so it's reachable from outside the server, port 5001
    app.run(host="0.0.0.0", port=5001)

