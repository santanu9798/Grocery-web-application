from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to Grocery Web App!"

if __name__ == "__main__":
    app.run(debug=True)
    app.run(host="0.0.0.0", port=10000)