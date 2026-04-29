# app.py

from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# Replace with your real NewsAPI key
API_KEY = "6579c1aa00274bfb9bea10bc633d52d7"


# Login + Signup Page
@app.route("/", methods=["GET"])
def login_page():
    return render_template("login_signup.html")


# News Home Page
@app.route("/home", methods=["GET", "POST"])
def home():
    articles = []
    query = ""

    if request.method == "POST":
        query = request.form.get("query", "").strip()

        if query:
            url = f"https://newsapi.org/v2/everything?q={query}&sortBy=publishedAt&apiKey={API_KEY}"

            try:
                response = requests.get(url)
                data = response.json()

                if data.get("status") == "ok":
                    articles = data.get("articles", [])[:10]

            except Exception as e:
                print("Error:", e)

    return render_template("index.html", articles=articles, query=query)


if __name__ == "__main__":
    app.run(debug=True)