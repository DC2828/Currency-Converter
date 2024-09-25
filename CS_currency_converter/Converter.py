from tkinter import *
import requests
import json

# get result from the api
def convert_currency(SF,ST,Amount,Error):

    API_Key = "4137ba268245a1ba148250e4"

    API_URL = 'https://v6.exchangerate-api.com/v6/{3}/pair/{0}/{1}/{2}'.format(SF,ST,Amount,API_Key)
    
    response = requests.get(API_URL)
    # convert a json string into  a dictionary
    Result = json.loads(response.text)
    if str(Result["result"]) == "success":
        return Result


    else:
        Error.set("Error:" + str(response.status_code) + str(response.text))
    



