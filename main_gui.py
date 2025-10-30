import requests
import os
from dotenv import load_dotenv
import tkinter as tk
from tkinter import messagebox

# Load API key
load_dotenv()
API_KEY = os.getenv("OPENWEATHER_API_KEY")

# Function to get weather
def get_weather():
    city = city_entry.get().strip()
    if not city:
        messagebox.showwarning("Warning", "Please enter a city name!")
        return

    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {"q": city, "appid": API_KEY, "units": "metric"}
    response = requests.get(base_url, params=params)

    if response.status_code == 404:
        messagebox.showerror("Error", "City not found! Try again.")
        return
    elif response.status_code != 200:
        messagebox.showerror("Error", "Something went wrong. Try again later.")
        return

    data = response.json()
    show_weather(data)

# Function to display weather info
def show_weather(data):
    city = data["name"]
    country = data["sys"]["country"]
    temp = data["main"]["temp"]
    desc = data["weather"][0]["description"].capitalize()
    humidity = data["main"]["humidity"]
    wind = data["wind"]["speed"]

    result = (
        f"🌤 Weather in {city}, {country}\n"
        f"🌡 Temperature: {temp}°C\n"
        f"💧 Humidity: {humidity}%\n"
        f"💨 Wind Speed: {wind} m/s\n"
        f"☁ Condition: {desc}"
    )
    output_label.config(text=result)

# Create GUI window
root = tk.Tk()
root.title("WeatherNow App")
root.geometry("400x350")
root.resizable(False, False)
root.configure(bg="#101820")

# Heading
heading = tk.Label(root, text="🌦 WeatherNow", font=("Segoe UI", 18, "bold"), bg="#101820", fg="#FEE715")
heading.pack(pady=10)

# Entry box
city_entry = tk.Entry(root, font=("Segoe UI", 12), justify="center", width=25)
city_entry.pack(pady=10)

# Button
get_btn = tk.Button(root, text="Get Weather", font=("Segoe UI", 11, "bold"),
                    bg="#FEE715", fg="#101820", command=get_weather)
get_btn.pack(pady=5)

# Output area
output_label = tk.Label(root, text="", font=("Consolas", 11), bg="#101820", fg="white", justify="left")
output_label.pack(pady=20)

# Run app
root.mainloop()
