# openweather api로 요청을 해서 
# 그 결과를 csv로 저장하는 py

import requests
import csv
from datetime import datetime
import os

API_KEY = os.getenv("OPENWEATHER_API_KEY")
CITY = "Seoul"
URL = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"

response = (requests.get(URL))
data = response.json()
print(data)

# main -> temp
# main -> humidity
# weather -> description
temp = data["main"]["temp"]
humidity = data["main"]["humidity"]
description = data["weather"][0]["description"]
timezone = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
print(timezone)

# 위의 4개의 데이터를 가지는 csv파일 생성
csv_filename = "seoul_weather.csv"
header = ["timezone", "temp", "humidity", "description"]

# csv가 존재 -> True
# csv가 존재 X -> False 
file_exist = os.path.isfile(csv_filename)

# mode = "a" 
# -> if is not file -> create
# if is file -> write
with open(csv_filename, "a", newline="") as file:
    writer = csv.writer(file)

    # 파일이 존재하지 않는다( = 헤더가 없다) -> 헤더 추가 필요
    if not file_exist:
        writer.writerow(header)

    writer.writerow([timezone, temp, humidity, description])

