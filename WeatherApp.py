import tkinter as tk
import requests

HEIHGT = 500
WIDTH = 600


def format_info(weather):
	try:
		name = weather['name']
		desc = weather['weather'][0]['description']
		temp = round(weather['main']['temp']-273.15)
		humidity = weather['main']['humidity']
		temp_mix = round(weather['main']['temp_max']-273.15)
		temp_min = round(weather['main']['temp_min']-273.15)

		final_result = 'City: %s \nConditions: %s \nTemperature (°C): %s \nhumidity: %s \nmax temp: %s \nmin temp:%s' % (name, desc, temp,humidity,temp_mix,temp_min)
	except Exception as e:
		raise e

	return final_result





def get_weather(city):
	weather_key = 'c356072142be5dc0a75182ebce4466ee'
	url = 'http://api.openweathermap.org/data/2.5/weather'
	params = {'APPID':weather_key,'q':city}
	response = requests.get(url,params=params)
	weather = response.json()

	print(weather)
	label['text'] = format_info(weather)


root = tk.Tk()
root.title("Get Weather Application")

canvas = tk.Canvas(root, height=HEIHGT, width=WIDTH)
canvas.pack()

frame = tk.Frame(root, bg='#DC7633', bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

entry = tk.Entry(frame, font=40)
entry.place(relwidth=0.65, relheight=1)

button = tk.Button(frame, text="Get Weather", font=40, command=lambda: get_weather(entry.get()))
button.place(relx=0.7, relheight=1, relwidth=0.3)

lower_frame = tk.Frame(root, bg='#DC7633', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

label = tk.Label(lower_frame,text='enter city or zip')
label.place(relwidth=1, relheight=1)





root.mainloop()