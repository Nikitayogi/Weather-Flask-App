from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_KEY = "1d60e12fb8d33cb82bc8167e388af642"  # Your API key

@app.route("/", methods=["GET", "POST"])
def index():
    weather_data = None
    if request.method == "POST":
        city = request.form.get("city")
        if city:
            # Append country code for reliability
            city_query = f"{city},IN"
            url = f"https://api.openweathermap.org/data/2.5/weather?q={city_query}&appid={API_KEY}&units=metric"
            response = requests.get(url)
            data = response.json()
            print(data)  # Debug
            if response.status_code == 200:
                weather_data = {
                    "city": data["name"],
                    "temperature": data["main"]["temp"],
                    "description": data["weather"][0]["description"].title(),
                    "humidity": data["main"]["humidity"],
                    "wind": data["wind"]["speed"]
                }
            else:
                weather_data = {"error": data.get("message", "City not found!")}

    return render_template("index.html", weather=weather_data)

if __name__ == "__main__":
    app.run(debug=True)
