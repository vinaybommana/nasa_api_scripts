'''
program to gather images from nasa epic api

# for gathering every day images
``get_every_day_image()``

# step 1
gather the latest image posting date
get the image ids from that date
get the images from wget
'''

import requests
import json
import os
import chardet
from configparser import ConfigParser
from datetime import datetime
parser = ConfigParser()
parser.read('constants.properties')


api_key = parser.get('nasa_api', 'api_key')
# print(api_key)

def get_json_data(url):
    '''
    :input: url <class 'str'>
    :return: list of dictionaries
    '''
    request = requests.get(url)
    content = json.loads(request.content.decode(chardet.detect(request.content)["encoding"]))
    return content

def main():
    '''
    first download every day image
    # get hd_url
    '''
    # get_every_day_image()
    latest_date = get_latest_date()
    get_images(latest_date)


def get_latest_date():
    url_available_dates = "https://epic.gsfc.nasa.gov/api/images.php?available_dates"
    content = get_json_data(url_available_dates)
    latest_date = content.pop()
    return latest_date


def get_images(date):
    url_date = "https://epic.gsfc.nasa.gov/api/images.php?date={}".format(date)
    content = get_json_data(url_date)
    images = []
    for data in content:
        images.append(data["image"])

    os.system("mkdir {}".format(date))

    for image in images:
        # os.system("wget 'http://epic.gsfc.nasa.gov/epic-archive/jpg/{}.jpg'".format(image))
        image_name = image.split("_")[2]
        image_name += ".jpg"
        os.system("mv {}.jpg {}/{}".format(image, date, image_name))


def get_every_day_image():
    url = "https://api.nasa.gov/planetary/apod?api_key={}".format(api_key)
    content = get_json_data(url)
    date = content['date']
    file_name = str(content['hdurl']).split("/")
    file_name = file_name.pop()
    print(file_name)
    os.system("wget {} && mv {} {}.jpg".format(content['hdurl'], file_name, date))

if __name__ == '__main__':
    main()
