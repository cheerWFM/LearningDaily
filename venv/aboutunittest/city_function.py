#!/usr/bin/env python 
# coding:utf-8

def get_city(city,country,population = ""):
    while True:
        # print("You can input 'q' to quit anytime")
        # city = input("\nPlease give me a city name:")
        # country = input("Please give me the country of the city you input:")
        if population:
            city_country = city + "," + country+"-population"+" "+population
        else:
            city_country = city+","+country
        return city_country
