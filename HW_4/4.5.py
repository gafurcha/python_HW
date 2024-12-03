import time
import requests

if __name__ == '__main__':
    url = ("https://api.openweathermap.org/data/2.5/weather?lat=55.7522&lon=37.6156&appid"
           "=b7a81f1f92b648111c02c4d885d0f582")
    for i in range(4):
        request = requests.get(url)
        if request.status_code != 200:
            request = request.json()
            print(request["message"])
            time.sleep(2)
        else:
            print(request.text)
            break
