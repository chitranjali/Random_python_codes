"""
To Get the wearther info for a for Zipcode form Wunderground site
"""
import requests
from bs4 import BeautifulSoup
from collections import namedtuple
import sys

# Can access just as key-value pairs
WeatherReport = namedtuple('WeatherReport',
                                       'area, temp, scale, cond ')

def main():
    zipcode = get_user_loc()
    html_response = get_html_from_web(zipcode)
    WeatherReport = get_temp_data(html_response)
    print_output(WeatherReport)

def get_temp_data(html_response):
    weather_soup = BeautifulSoup(html_response,'html.parser')
    # temp =  weather_soup.find('div',{'class': 'current-temp'}).text.strip()
    # Error handling for soup?
    temp = weather_soup.find(class_='wu-unit-temperature').find(class_='wu-value').get_text().strip()
    scale = weather_soup.find(class_='wu-unit-temperature').find(class_='wu-label').get_text().strip()
    cond = weather_soup.find('div',{'class': 'condition-icon'}).text.strip()
    area = weather_soup.find('div',{'class': 'region-content-header'}).find('h1').text.strip()
    return  WeatherReport(cond=cond, temp=temp, scale=scale, area=area)

def print_output(WeatherReport):
    print("The weather in {} is {}{} and {}".format(
        WeatherReport.area,
        WeatherReport.temp,
        WeatherReport.scale,
        WeatherReport.cond
    ))

def get_html_from_web(zipcode):
    url = 'http://www.wunderground.com/weather-forecast/{}'.format(zipcode)
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        print(e)
        sys.exit(1)

def get_user_loc():
    return input("Enter zipcode :").strip()

main()