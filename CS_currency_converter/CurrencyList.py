import requests
import json

# Get the supported currencies from the api
def CurrencyListGenerate():
    CurrencyList = {}
    response = requests.get("https://v6.exchangerate-api.com/v6/4137ba268245a1ba148250e4/codes")
    jsonString = json.loads(response.text)

    ResultList = list(jsonString["supported_codes"])
    # exclude the unsupported api from another api website to make the currencies synchronize since we are using 2 apis
    notsupported = ['FOK', 'KID', 'MRU', 'SSP', 'STN', 'TVD']

    # Put the result into the CurrencyList
    for i in range(len(ResultList)):
        if not(ResultList[i][0] in notsupported):
            CurrencyList.update({("(" + str(ResultList[i][0])  + ") " +str(ResultList[i][1])):str(ResultList[i][0])})

    return CurrencyList