import json
import requests as rq
import tkinter as tk
from tkinter import Label, Entry, Button, messagebox

def get_weather():
    city = city_entry.get()
    url = "https://weatherapi-com.p.rapidapi.com/current.json"
    querystring = {"q": f"{city}"}
    headers = {
        "X-RapidAPI-Key": "6a95dd69f5mshdca9bf0e039114dp1111a3jsn95d3c023c38b",
        "X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com"
    }
    response = rq.get(url, headers=headers, params=querystring)
    resp = response.text

    try:
        data = json.loads(resp)
        city_name = data["location"]["name"]
        temperature = data["current"]["temp_c"]
        wind_speed = data["current"]["wind_kph"]
        result_str = f"{city_name}'s weather is ({temperature}°C) and wind speed is {wind_speed} KPH"
        result_label.config(text=result_str)
    except json.JSONDecodeError:
        messagebox.showerror("Error", "Invalid response from the API. Please try again.")


app = tk.Tk()
app.title("Weather App")


city_label = Label(app, text="Enter City:")
city_label.pack(pady=10)

city_entry = Entry(app)
city_entry.pack(pady=10)

get_weather_button = Button(app, text="Get Weather", command=get_weather)
get_weather_button.pack(pady=10)

result_label = Label(app, text="")
result_label.pack(pady=10)

app.mainloop()

