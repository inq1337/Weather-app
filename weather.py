import json
import requests
import time
from datetime import datetime
from tkinter import Tk, Label, Frame, Button, Entry, TOP, BOTH, PhotoImage, W
appi = 'appid=36271b233b57e9943b4f883e0d6a19bb'
param = '&units=metric&lang=ru&'


def center(win):
    win.update_idletasks()
    width = win.winfo_width()
    frm_width = win.winfo_rootx() - win.winfo_x()
    win_width = width + 2 * frm_width
    height = win.winfo_height()
    title_bar_height = win.winfo_rooty() - win.winfo_y()
    win_height = height + title_bar_height + frm_width
    x = win.winfo_screenwidth() // 2 - win_width // 2
    y = win.winfo_screenheight() // 2 - win_height // 2
    win.geometry('{}x{}+{}+{}'.format(width, height, x, y))
    win.deiconify()


def DateTranslate(date: str, posix_time: int) -> str:
	if (date == str(datetime.utcfromtimestamp(posix_time).strftime('%A'))):
		if(date == "Monday"):
			date = date.replace(date, "Понедельник")
		elif(date == "Tuesday"):
			date = date.replace(date, "Вторник")
		elif(date == "Wednesday"):
			date = date.replace(date, "Среда")
		elif(date == "Thursday"):
			date = date.replace(date, "Четверг")
		elif(date == "Friday"):
			date = date.replace(date, "Пятница")
		elif(date == "Saturday"):
			date = date.replace(date, "Суббота")
		elif(date == "Sunday"):
			date = date.replace(date, "Воскресенье")
	else:
		change_week = str(datetime.utcfromtimestamp(posix_time).strftime('%B'))
		if(change_week == "January"):
			date = date.replace(change_week, "января")
		elif(change_week == "February"):
			date = date.replace(change_week, "февраля")
		elif(change_week == "March"):
			date = date.replace(change_week, "марта")
		elif(change_week == "April"):
			date = date.replace(change_week, "апреля")
		elif(change_week == "May"):
			date = date.replace(change_week, "мая")
		elif(change_week == "June"):
			date = date.replace(change_week, "июня")
		elif(change_week == "July"):
			date = date.replace(change_week, "июля")
		elif(change_week == "August"):
			date = date.replace(change_week, "августа")
		elif(change_week == "September"):
			date = date.replace(change_week, "сентября")
		elif(change_week == "October"):
			date = date.replace(change_week, "октября")
		elif(change_week == "November"):
			date = date.replace(change_week, "ноября")
		elif(change_week == "December"):
			date = date.replace(change_week, "декабря")
	return date


def OutCurrentWeather(temp, f_l, desc, wnd, ctime: str) -> None:
    temperature.config(text=temp)
    feels_like.config(text='Ощущается как ' + f_l)
    description.config(text=desc)
    wind.config(text='Скорость ветра '+ wnd)
    dtime.config(text=ctime)
    StartButton.config(text='Обновить')

def OutWeatherForecast(w: list) -> None:
    Info1.config(text='Погода')
    Info2.config(text=' Утро')
    Info3.config(text=' День')
    Info4.config(text=' Вечер')
    Info5.config(text=' Ночь')

    Date1.config(text=w[0][0])
    Date2.config(text=w[1][0])
    Date3.config(text=w[2][0])
    Date4.config(text=w[3][0])
    Date5.config(text=w[4][0])
    Date6.config(text=w[5][0])
    Date7.config(text=w[6][0])

    '''Picture1.config(text=w[0][0])
    Picture2.config(text=w[1][0])
    Picture3.config(text=w[2][0])
    Picture4.config(text=w[3][0])
    Picture5.config(text=w[4][0])
    Picture6.config(text=w[5][0])
    Picture7.config(text=w[6][0])'''

    Morning1.config(text=w[0][2])
    Morning2.config(text=w[1][2])
    Morning3.config(text=w[2][2])
    Morning4.config(text=w[3][2])
    Morning5.config(text=w[4][2])
    Morning6.config(text=w[5][2])
    Morning7.config(text=w[6][2])

    Day1.config(text=w[0][3])
    Day2.config(text=w[1][3])
    Day3.config(text=w[2][3])
    Day4.config(text=w[3][3])
    Day5.config(text=w[4][3])
    Day6.config(text=w[5][3])
    Day7.config(text=w[6][3])

    Evening1.config(text=w[0][4])
    Evening2.config(text=w[1][4])
    Evening3.config(text=w[2][4])
    Evening4.config(text=w[3][4])
    Evening5.config(text=w[4][4])
    Evening6.config(text=w[5][4])
    Evening7.config(text=w[6][4])

    Night1.config(text=w[0][5])
    Night2.config(text=w[1][5])
    Night3.config(text=w[2][5])
    Night4.config(text=w[3][5])
    Night5.config(text=w[4][5])
    Night6.config(text=w[5][5])
    Night7.config(text=w[6][5])


def GetWeatherForecast(coord: str, tz: int) -> None:
    serv = 'https://api.openweathermap.org/data/2.5/onecall?'
    excl = '&exclude=current,minutely,hourly,alerts'
    req = serv + coord + excl + param + appi
    try:
        res = requests.get(req).content.decode("UTF8")
        data = json.loads(res)
        weather = []
        weatheri = []
        for i in range(7):
            posix_time = data['daily'][i+1]['dt'] + tz
            ctime = str(datetime.utcfromtimestamp(posix_time).strftime('%A'))
            ctime = DateTranslate(ctime, posix_time)
            weath = data['daily'][i+1]['weather'][0]['main']
            morn = round(data['daily'][i+1]['temp']['morn'])
            day = round(data['daily'][i+1]['temp']['day'])
            eve = round(data['daily'][i+1]['temp']['eve'])
            night = round(data['daily'][i+1]['temp']['night'])

            if morn >= 0:
                morn = ' ' + str(morn)
            else: 
                morn = str(morn)
            if day >= 0:
                day = ' ' + str(day)
            else: 
                day = str(day)
            if eve >= 0:
                eve = ' ' + str(eve)
            else: 
                eve = str(eve)
            if night >= 0:
                night = ' ' + str(night)
            else: 
                night = str(night)
            
            weatheri.append(ctime)  #0 - дата
            weatheri.append(weath)  #1 - погода
            weatheri.append(morn)   #3 - утро
            weatheri.append(day)    #4 - день
            weatheri.append(eve)    #5 - вечер
            weatheri.append(night)  #6 - ночь
            weather.append(weatheri)
            weatheri = []

        OutWeatherForecast(weather)
    except Exception as e:
        print('Exception (find) in forecast:', e)
        pass


def GetCurrentWeather() -> None:
    serv = 'http://api.openweathermap.org/data/2.5/weather?q='
    city = cityname.get()
    req = serv + city + param + appi
    try:
        res = requests.get(req).content.decode("UTF8")
        data = json.loads(res)
        lat = str(data['coord']['lat'])
        lon = str(data['coord']['lon'])
        coord = 'lat=' + lat + '&lon=' + lon

        temp = str(round(data['main']['temp'])) + '°C'
        f_l = str(round(data['main']['feels_like'])) + '°C'
        desc = data['weather'][0]['description']
        wnd = str(round(data['wind']['speed'])) + ' м/с'
        dt = data['dt']
        tz = data['timezone']
        posix_time = dt + tz
        ctime = str(datetime.utcfromtimestamp(posix_time).strftime('%d %B, %H:%M'))
        ctime = DateTranslate(ctime, posix_time)

        GetWeatherForecast(coord, tz)
        OutCurrentWeather(temp, f_l, desc, wnd, ctime)
    except Exception as e:
        print('Exception (find) in current:', e)
        pass

root = Tk()
root.title("Погода")
root.resizable(False, False)
root.geometry('435x465')

StartFrame = Frame(root)
CurrentFrame = Frame(root)
ForecastFrame = Frame(root)

StartFrame.pack(side=TOP, fill=BOTH)
CurrentFrame.pack(fill=BOTH)
ForecastFrame.pack(fill=BOTH)

cityname = Entry(StartFrame, font=("Google Sans", 11))
cityname.pack()

StartButton = Button(StartFrame, text='Получить', font=("Google Sans", 10), command=GetCurrentWeather)
StartButton.pack()

dtime = Label(CurrentFrame, font=("Google Sans", 10))
temperature = Label(CurrentFrame, font=("Google Sans", 46))
feels_like = Label(CurrentFrame, font=("Google Sans", 13))
description = Label(CurrentFrame, font=("Google Sans", 12))
wind = Label(CurrentFrame, font=("Google Sans", 12))

dtime.pack()
temperature.pack()
feels_like.pack()
description.pack()
wind.pack()

Info0 = Label(ForecastFrame, font=("Google Sans", 14))
Info1 = Label(ForecastFrame, font=("Google Sans", 14))
Info2 = Label(ForecastFrame, font=("Google Sans", 14))
Info3 = Label(ForecastFrame, font=("Google Sans", 14))
Info4 = Label(ForecastFrame, font=("Google Sans", 14))
Info5 = Label(ForecastFrame, font=("Google Sans", 14))
Info0.grid(row=0, column=0)
Info1.grid(row=0, column=1)
Info2.grid(row=0, column=2)
Info3.grid(row=0, column=3)
Info4.grid(row=0, column=4)
Info5.grid(row=0, column=5)

Date1 = Label(ForecastFrame, font=("Google Sans", 14))
Date2 = Label(ForecastFrame, font=("Google Sans", 14))
Date3 = Label(ForecastFrame, font=("Google Sans", 14))
Date4 = Label(ForecastFrame, font=("Google Sans", 14))
Date5 = Label(ForecastFrame, font=("Google Sans", 14))
Date6 = Label(ForecastFrame, font=("Google Sans", 14))
Date7 = Label(ForecastFrame, font=("Google Sans", 14))

Date1.grid(row=1, column=0, sticky=W, pady=1, padx=2)
Date2.grid(row=2, column=0, sticky=W, pady=1, padx=2)
Date3.grid(row=3, column=0, sticky=W, pady=1, padx=2)
Date4.grid(row=4, column=0, sticky=W, pady=1, padx=2)
Date5.grid(row=5, column=0, sticky=W, pady=1, padx=2)
Date6.grid(row=6, column=0, sticky=W, pady=1, padx=2)
Date7.grid(row=7, column=0, sticky=W, pady=1, padx=2)

'''Picture1 = Label(ForecastFrame, font=("Google Sans", 11))
Picture2 = Label(ForecastFrame, font=("Google Sans", 11))
Picture3 = Label(ForecastFrame, font=("Google Sans", 11))
Picture4 = Label(ForecastFrame, font=("Google Sans", 11))
Picture5 = Label(ForecastFrame, font=("Google Sans", 11))
Picture6 = Label(ForecastFrame, font=("Google Sans", 11))
Picture7 = Label(ForecastFrame, font=("Google Sans", 11))

Picture1.grid(row=1, column=1)
Picture2.grid(row=2, column=1)
Picture3.grid(row=3, column=1)
Picture4.grid(row=4, column=1)
Picture5.grid(row=5, column=1)
Picture6.grid(row=6, column=1)
Picture7.grid(row=7, column=1)'''

Morning1 = Label(ForecastFrame, font=("Google Sans", 14), pady=1, padx=2)
Morning2 = Label(ForecastFrame, font=("Google Sans", 14), pady=1, padx=2)
Morning3 = Label(ForecastFrame, font=("Google Sans", 14), pady=1, padx=2)
Morning4 = Label(ForecastFrame, font=("Google Sans", 14), pady=1, padx=2)
Morning5 = Label(ForecastFrame, font=("Google Sans", 14), pady=1, padx=2)
Morning6 = Label(ForecastFrame, font=("Google Sans", 14), pady=1, padx=2)
Morning7 = Label(ForecastFrame, font=("Google Sans", 14), pady=1, padx=2)

Morning1.grid(row=1, column=2)
Morning2.grid(row=2, column=2)
Morning3.grid(row=3, column=2)
Morning4.grid(row=4, column=2)
Morning5.grid(row=5, column=2)
Morning6.grid(row=6, column=2)
Morning7.grid(row=7, column=2)

Day1 = Label(ForecastFrame, font=("Google Sans", 14), pady=1, padx=2)
Day2 = Label(ForecastFrame, font=("Google Sans", 14), pady=1, padx=2)
Day3 = Label(ForecastFrame, font=("Google Sans", 14), pady=1, padx=2)
Day4 = Label(ForecastFrame, font=("Google Sans", 14), pady=1, padx=2)
Day5 = Label(ForecastFrame, font=("Google Sans", 14), pady=1, padx=2)
Day6 = Label(ForecastFrame, font=("Google Sans", 14), pady=1, padx=2)
Day7 = Label(ForecastFrame, font=("Google Sans", 14), pady=1, padx=2)

Day1.grid(row=1, column=3)
Day2.grid(row=2, column=3)
Day3.grid(row=3, column=3)
Day4.grid(row=4, column=3)
Day5.grid(row=5, column=3)
Day6.grid(row=6, column=3)
Day7.grid(row=7, column=3)

Evening1 = Label(ForecastFrame, font=("Google Sans", 14), pady=1, padx=2)
Evening2 = Label(ForecastFrame, font=("Google Sans", 14), pady=1, padx=2)
Evening3 = Label(ForecastFrame, font=("Google Sans", 14), pady=1, padx=2)
Evening4 = Label(ForecastFrame, font=("Google Sans", 14), pady=1, padx=2)
Evening5 = Label(ForecastFrame, font=("Google Sans", 14), pady=1, padx=2)
Evening6 = Label(ForecastFrame, font=("Google Sans", 14), pady=1, padx=2)
Evening7 = Label(ForecastFrame, font=("Google Sans", 14), pady=1, padx=2)

Evening1.grid(row=1, column=4)
Evening2.grid(row=2, column=4)
Evening3.grid(row=3, column=4)
Evening4.grid(row=4, column=4)
Evening5.grid(row=5, column=4)
Evening6.grid(row=6, column=4)
Evening7.grid(row=7, column=4)

Night1 = Label(ForecastFrame, font=("Google Sans", 14), pady=1, padx=2)
Night2 = Label(ForecastFrame, font=("Google Sans", 14), pady=1, padx=2)
Night3 = Label(ForecastFrame, font=("Google Sans", 14), pady=1, padx=2)
Night4 = Label(ForecastFrame, font=("Google Sans", 14), pady=1, padx=2)
Night5 = Label(ForecastFrame, font=("Google Sans", 14), pady=1, padx=2)
Night6 = Label(ForecastFrame, font=("Google Sans", 14), pady=1, padx=2)
Night7 = Label(ForecastFrame, font=("Google Sans", 14), pady=1, padx=2)

Night1.grid(row=1, column=5)
Night2.grid(row=2, column=5)
Night3.grid(row=3, column=5)
Night4.grid(row=4, column=5)
Night5.grid(row=5, column=5)
Night6.grid(row=6, column=5)
Night7.grid(row=7, column=5)

center(root)
root.mainloop()