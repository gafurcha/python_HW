import pandas as pd
import requests

if __name__ == '__main__':
    data = pd.DataFrame(columns=['Температура', 'Влажность'])
    url = ("https://api.openweathermap.org/data/2.5/weather?lat=55.7522&lon=37.6156&appid"
           "=b7a81f1f92b648111c02c4d885d0f582")
    request = requests.get(url).json()
    temp = (float(request["main"]["temp"]) - 273.15)
    temp = round(temp, 2)
    humidity = (request["main"]["humidity"])
    data.loc[len(data)] = [temp, humidity]
    print(data)
