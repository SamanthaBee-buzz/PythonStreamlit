This project allows a user to plan a 2-5 day long vacation in a European city. It includes the 5 most populated cities of over 40 European countries. It includes tag selection so the user only gets suggestions for activities that interest them. The user can select a starting time and duration. They can decide how many activities they want in a day, which ranges from 1to 3. Google Gemini uses the country, city, date, tags, duration, and starting time to generate a numbered list of 5 activities that fit that criteria. The user can select one of the 5 activities to add to their schedule. The final output is a schedule for each day that includes the activity’s name, start time, and end time.

Import the following:

import streamlit as st
  • import pandas as pd
  •	import numpy as np
  •	from streamlit_option_menu import option_menu
  •	import os
  •	import google.generativeai as genai
  •	from datetime import date
  •	from datetime import time
  •	from datetime import timedelta

How to Plan Your European Vacation (Run the Streamlit App)
  Choosing a Date and Location
    1.	select country and city with dropdown menu
    2.	select the first day and last day you will be in your selected city
  Planning a Day
    1.	make sure you’re on the tab that says ‘Day 1 Plan’
    2.	select 1-3 tags that describe what kind of activities you would like for that day
    3.	Select the number of activities you would like on that day.
    4.	When asked “Are you ready to find activities?”, choose “Yes” to see a list of 5 attractions.
    5.	Use the slider to choose what time the first activity will start
    6.	Choose the duration of the first activity
    7.	There will be a numbered list of 5 options. Select the number that corresponds to the activity you would like to do.
    8.	Repeat steps 2-8 for each activity in day 1
    9.	Go to the ‘Day 2 Plan’ tab and repeat steps 2-3 there to plan the second day. Do this for all other days
    10.	 After planning all days, click on the ‘Vacation Plan’ tab to see your final schedule.

My name and GitHub username
  Samantha Baker SamanthaBee-buzz

API and data source details
  I used gemini 2.5 flash. I got city names and country populations from https://worldpopulationreview.com/countries/[country name] and checked for special characters like è and ä using 
  https://en.wikipedia.org/wiki/List_of_cities_in_[country name].
  To be more specific, my sources are:
  https://simple.wikipedia.org/wiki/List_of_European_countries
  https://worldpopulationreview.com/countries/albania
  https://worldpopulationreview.com/countries/austria
  https://worldpopulationreview.com/countries/belarus
  https://en.wikipedia.org/wiki/List_of_cities_and_towns_in_Belarus#List
  https://worldpopulationreview.com/countries/belgium
  https://en.wikipedia.org/wiki/List_of_cities_in_Belgium
  https://worldpopulationreview.com/countries/bosnia-and-herzegovina
  https://worldpopulationreview.com/countries/bulgaria
  https://worldpopulationreview.com/countries/croatia
  https://worldpopulationreview.com/countries/czechia
  https://worldpopulationreview.com/countries/denmark
  https://worldpopulationreview.com/countries/estonia
  https://en.wikipedia.org/wiki/List_of_cities_and_towns_in_Estonia#List
  https://worldpopulationreview.com/countries/finland
  https://worldpopulationreview.com/countries/france
  https://worldpopulationreview.com/countries/germany
  https://en.wikipedia.org/wiki/List_of_cities_in_Germany_by_population#List
  https://worldpopulationreview.com/countries/greece
  https://en.wikipedia.org/wiki/List_of_cities_and_towns_in_Greece#Census-designated_places
  https://worldpopulationreview.com/countries/hungary
  https://en.wikipedia.org/wiki/List_of_cities_and_towns_of_Hungary#Over_100,000_(large_cities)
  https://worldpopulationreview.com/countries/ireland
  https://en.wikipedia.org/wiki/Tourism_in_Italy#Italian_cities_by_number_of_visitors
  https://worldpopulationreview.com/countries/latvia
  https://en.wikipedia.org/wiki/List_of_cities_and_towns_in_Latvia#State_cities
  https://worldpopulationreview.com/countries/lithuania
  https://en.wikipedia.org/wiki/List_of_cities_in_Lithuania#Cities_with_over_50,000_inhabitants
  https://worldpopulationreview.com/countries/moldova
  https://en.wikipedia.org/wiki/List_of_cities_and_towns_in_Moldova
  https://worldpopulationreview.com/countries/netherlands
  https://worldpopulationreview.com/countries/north-macedonia
  https://worldpopulationreview.com/countries/norway
  https://worldpopulationreview.com/countries/poland
  https://en.wikipedia.org/wiki/List_of_cities_and_towns_in_Poland
  https://worldpopulationreview.com/countries/portugal
  https://en.wikipedia.org/wiki/List_of_cities_in_Portugal#Urban_areas
  https://worldpopulationreview.com/countries/romania
  https://en.wikipedia.org/wiki/List_of_cities_and_towns_in_Romania#Complete_list
  https://worldpopulationreview.com/countries/russia
  https://worldpopulationreview.com/countries/serbia
  https://en.wikipedia.org/wiki/List_of_cities_and_towns_in_Serbia
  https://worldpopulationreview.com/countries/slovakia
  https://en.wikipedia.org/wiki/List_of_cities_and_towns_in_Slovakia#List
  https://en.wikipedia.org/wiki/Tourism_in_Slovenia#Overnight_stays_2
  https://worldpopulationreview.com/countries/spain
  https://en.wikipedia.org/wiki/List_of_municipalities_of_Spain#By_population
  https://worldpopulationreview.com/countries/sweden
  https://en.wikipedia.org/wiki/List_of_cities_in_Sweden#List
  https://worldpopulationreview.com/countries/switzerland
  https://en.wikipedia.org/wiki/List_of_cities_in_Switzerland#List_of_towns_and_cities
  https://worldpopulationreview.com/countries/turkey
  https://en.wikipedia.org/wiki/List_of_largest_cities_and_towns_in_Turkey#Cities_and_towns_with_more_than_7,000_inhabitants
  https://worldpopulationreview.com/countries/ukraine
  https://en.wikipedia.org/wiki/List_of_cities_in_Ukraine#Table_of_cities
