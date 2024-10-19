import tkinter as tk
from tkinter import messagebox
from geopy.geocoders import nominatim
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz


def get_weather():
    try:
        city = textfield.get()
        geolocator = nominatim.Nominatim(user_agent="geoapiExercises")

        location = geolocator.geocode(city)
        lat = location.latitude
        lng = location.longitude
        obj = TimezoneFinder()
        result = obj.timezone_at(lng=lng, lat=lat)
        city_label.config(text=result.split('/')[1])
        print(result)

        home = pytz.timezone(result)
        now = datetime.now(home)
        current_time = now.strftime("%I : %M : %p")
        time_label.config(text=current_time)

        api_key = '2ed00e044d8205d02d879e1cc9309971'
        api = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lng}&appid={api_key}'

        json_data = requests.get(api).json()

        condition = json_data['weather'][0]['main']
        description = json_data['weather'][0]['description']
        temp = int(json_data['main']['temp']-273.15)
        humidity = json_data['main']['humidity']
        pressure = json_data['main']['pressure']
        wind = json_data['wind']['speed']
        temp_label.config(text=f"{temp}°")
        condition_label.config(text=f"{condition} | FEELS LIKE {temp}°")
        humidity_label.config(text=humidity)
        pressure_label.config(text=pressure)
        wind_label.config(text=wind)
        description_label.config(text=description)

    except Exception as errors:
        print(errors)
        messagebox.showerror('Weather App', 'Inavalid Entry')


root = tk.Tk()
root.title('Weather App')
root.geometry('800x500')
search_image = tk.PhotoImage(file=r'D:\vscode_update\PYqt\search.png')
search_image_label = tk.Label(root, image=search_image)
search_image_label.pack(pady=20, side=tk.TOP)


textfield = tk.Entry(root, justify='center', width=17, font=(
    'poppins', 25, 'bold'), bg='#404040', fg='white', border=0)
textfield.place(x=240, y=40)


search_icon = tk.PhotoImage(file=r'D:\vscode_update\PYqt\search_icon.png')
search_icon_button = tk.Button(
    root, image=search_icon, border=0, cursor='hand2', bg='#404040', command=get_weather)
search_icon_button.place(x=540, y=34)


logo_image = tk.PhotoImage(file=r'D:\vscode_update\PYqt\logo.png')
logo_label = tk.Label(root, image=logo_image)
logo_label.pack(side=tk.TOP)

frame_img = tk.PhotoImage(file=r'D:\vscode_update\PYqt\box.png')
frame_img_label = tk.Label(root, image=frame_img)
frame_img_label.pack(side=tk.TOP)


city_label = tk.Label(root, font=('arial', 40, 'bold'), fg='#e355cd')
city_label.place(x=50, y=180)


time_label = tk.Label(root, font=('arial', 20, 'bold'), fg='#4b4bcc')
time_label.place(x=80, y=270)

clock = tk.Label(root, font=('Helvetica', 40), fg='#4b4bcc')
clock.place(x=120, y=250)


label1 = tk.Label(root, text="WIND", font=(
    'Helvetica', 15, 'bold'), fg='white', bg='#1ab5ef')
label1.place(x=90, y=400)


label2 = tk.Label(root, text="HUMIDITY", font=(
    'Helvetica', 15, 'bold'), fg='white', bg='#1ab5ef')
label2.place(x=220, y=400)

label3 = tk.Label(root, text="DESCRIPTION", font=(
    'Helvetica', 15, 'bold'), fg='white', bg='#1ab5ef')
label3.place(x=390, y=400)

label4 = tk.Label(root, text="PRESSURE", font=(
    'Helvetica', 15, 'bold'), fg='white', bg='#1ab5ef')
label4.place(x=600, y=400)


temp_label = tk.Label(root, font=('arial', 70, 'bold'), fg='#e355cd')
temp_label.place(x=590, y=170)


condition_label = tk.Label(root, font=('arial', 15, 'bold'), fg='#4b4bcc')
condition_label.place(x=560, y=270)


wind_label = tk.Label(root, text='...', font=(
    'arial', 15, 'bold'), bg='#1ab5ef', fg='#404040')
wind_label.place(x=100, y=430)


humidity_label = tk.Label(root, text='...', font=(
    'arial', 15, 'bold'), bg='#1ab5ef', fg='#404040')
humidity_label.place(x=250, y=430)


description_label = tk.Label(root, text='...', font=(
    'arial', 15, 'bold'), bg='#1ab5ef', fg='#404040')
description_label.place(x=410, y=430)


pressure_label = tk.Label(root, text='...', font=(
    'arial', 15, 'bold'), bg='#1ab5ef', fg='#404040')
pressure_label.place(x=640, y=430)


root.mainloop()
