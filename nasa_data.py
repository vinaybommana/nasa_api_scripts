import requests
import json
import chardet
import os

url = "https://api.nasa.gov/EPIC/api/natural/images?api_key=m98ln1zU4BjOZySGrbGjNSWNOKV5pGiSbdSfEynu"
request = requests.get(url)
# print(request)
content = json.loads(request.content.decode(chardet.detect(request.content)["encoding"]))
image_url = "https://api.nasa.gov/EPIC/archive/enhanced/2018/08/09/png/epic_1b_20180809004554.png?api_key=m98ln1zU4BjOZySGrbGjNSWNOKV5pGiSbdSfEynu"

# request = request.json()

# 20180809004554
# print(content)
for i in content:
    print(i["image"])
    print(i["caption"])

# os.system("wget {}".format(image_url))
# url_available_dates = "https://epic.gsfc.nasa.gov/api/images.php?available_dates"
# request = requests.get(url_available_dates)
# content = content = json.loads(request.content.decode(chardet.detect(request.content)["encoding"]))
# print(content)


url_date = "https://epic.gsfc.nasa.gov/api/images.php?date=2018-08-09"
request = requests.get(url_date)
content = json.loads(request.content.decode(chardet.detect(request.content)["encoding"]))
print(content)

os.system('wget "http://epic.gsfc.nasa.gov/epic-archive/jpg/epic_1b_20180809160222.jpg"')
