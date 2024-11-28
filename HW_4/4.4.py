import pandas as pd
import requests

if __name__ == '__main__':
    data = pd.DataFrame(columns=['Температура', 'Влажность'])
    #следующий юрл был доработан под персональный апи код, координаты взять из открытых источникоd
    url = ("https://api.openweathermap.org/data/2.5/weather?lat=55.7522&lon=37.6156&appid"
           "=ce9f26431abc8888a5b3571c1fa08049")
    request = requests.get(url).json()
    temp = (float(request["main"]["temp"]) - 273.15)
    temp = round(temp, 2)
    humidity = (request["main"]["humidity"])
    data.loc[len(data)] = [temp, humidity]
    print(data)