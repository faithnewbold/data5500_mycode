#find a specific month of a specific year - know the month and the year - Utahs highest was March 2021, the lowest was March 2020.
#ways to calculate - store all the new covid cases in a list and add them up. Or use a dictionary with the month and year as a key and then the cases as the value

import requests
import json
from datetime import datetime


file = open("/home/ubuntu/data5500_mycode/hw5/states_territories.txt") #connecting to the file with all the state abbreviations.
lines = file.readlines()
states = [line.strip() for line in lines] #using the .strip() allows me to remove the \n character between the state and the second part of the url


for state in states:
    url1 = "https://api.covidtracking.com/v1/states/"
    url2 = "/daily.json"

    url = url1 + state + url2 #creating the url including each state

    req = requests.get(url)

    # print(req.text)

    data = req.json()


    #what keys do I need?
    date_key = "date"
    positives_key = "positiveIncrease"


    daily_cases = [(entry[date_key], entry.get(positives_key, 0)) for entry in data] 

    #calculate the average number of cases
    total_cases = sum(c[1] for c in daily_cases) #since daily cases are list tuples, c[1] takes the positives from the list.
    avg_cases = total_cases / len(daily_cases) if daily_cases else 0


    #create variables to keep track of the day with the highest number of cases
    highest_date = None
    highest_cases = 0
    # Loop through daily_cases to find the maximum
    for date, cases in daily_cases:
        if cases > highest_cases:
            highest_cases = cases
            highest_date = date


    #find most recent date with no new covid cases
    no_cases_dates = [date for date, cases in daily_cases if cases == 0] #making a list of the days that didn't have any cases
    most_recent_no_case = max(no_cases_dates) if no_cases_dates else "None" #the most recent date is the maximum date in the list


    #create a dictionary to store the monthly case data
    monthly_cases = {}

    for date, cases in daily_cases:
        date_conversion = datetime.strptime(str(date), "%Y%m%d") #converting the date to be a datetime
        month_year = date_conversion.strftime("%B %Y") #format the date to be Month Year

        #add cases to the dictionary
        if month_year in monthly_cases:
            monthly_cases[month_year] += cases
        else:
            monthly_cases[month_year] = cases

    #find the Months with the highest and lowest number of cases:
    highest_month = None
    lowest_month = None
    highest_month_cases = 0
    lowest_cases = 100000 #start at a very high number so it can track ones that are lower  

    for month, cases in monthly_cases.items():
        if cases > highest_month_cases:
            highest_month_cases = cases
            highest_month = month
        if cases < lowest_cases:
            lowest_cases = cases
            lowest_month = month

    #print all the results
    print("State:", state.upper())
    print("Average Number of Cases:", avg_cases)
    print("Date with Highest Number of New Cases:", highest_date, "(with", highest_cases, "new cases)")
    print("Last Day with No Positive Cases", most_recent_no_case)
    print("Month and Year with Highest Number of New Cases:", highest_month)
    print("Month and Year with Lowest Number of New Cases:", lowest_month)
    print("_________________________")


   #put all the results in a dictionary to be able to save it to a json file

    results = {
        "State": state.upper(),
        "Average Number of Cases": avg_cases,
        "Date with Highest Number of New Cases": {
            "Date": highest_date,
            "Cases": highest_cases
        },
        "Last Day with No Positive Cases": most_recent_no_case,
        "Month and Year with Highest Number of New Cases": {
            "Month and Year": highest_month,
            "Cases": highest_month_cases
        },
        "Month and Year with Lowest Number of New Cases": {
            "Month and Year": lowest_month,
            "Cases": lowest_cases
        }
    }


    with open("/home/ubuntu/data5500_mycode/hw5/" +state+ ".json", "w") as file: #saving json data from the API to json files
        json.dump(results, file, indent=4)