from flask import Flask, render_template, request
import requests

app = Flask(__name__)

def get_country_info(country_code):
    url = f"https://restcountries.com/v3.1/alpha/{country_code}"
    response = requests.get(url)

    if response.status_code == 200:
        country_data = response.json()[0]
        return country_data
    else:
        return None

@app.route("/", methods=["GET", "POST"])
def index():
    country_info = None

    if request.method == "POST":
        country_code = request.form["country_code"].upper()
        country_info = get_country_info(country_code)

    return render_template("index.html", country_info=country_info)

if __name__ == "__main__":
    app.run(debug=True)
