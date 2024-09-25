import requests
import matplotlib.pyplot as plt
from datetime import datetime
from datetime import timedelta
from tkinter import messagebox


def yearly_rates_graph(base_currency, convert_to_currency, DateList,SelectedPeriod):
    # change the format of the date to make it acceptable to the api request
    Date1 = datetime.strptime(DateList[0],"%m/%d/%y").strftime("%Y-%m-%d")
    
    Date2 = datetime.strptime(DateList[1],"%m/%d/%y").strftime("%Y-%m-%d")

    # find the start and end
    if Date1 >= Date2:
        start_date = Date2
        end_date = Date1
    else:
        start_date = Date1
        end_date = Date2

    # Making request to the exchange rate api from API Layers
    
    url = f"https://api.apilayer.com/exchangerates_data/timeseries?start_date={start_date}&end_date={end_date}"
    payload = {"base": base_currency}
    headers = {
        "apikey": "ZAHEanC9UBLd0vBDG6Ov0kBqfs2NASb8"
    }
    response = requests.get(url, headers=headers, params=payload)
    data = response.json()
    status_code = response.status_code

    if status_code == 200:
        historical_rate_array = []

        # Iterates through the data["rates"] dictionary using for loop.
        # Then stores the currency rates of each date with the convert_to_currency_key.
        for date in data["rates"]:
            rate_of_currency = data["rates"][date][convert_to_currency]
            historical_rate_array.append(rate_of_currency)

        # Plot the graph using Matplotlib module
        plt.plot(historical_rate_array)
        plt.title(f"Exchange rates of {base_currency} to {convert_to_currency} from {start_date} to {end_date}")
        plt.xlabel("Days")
        plt.ylabel(f"{base_currency} to {convert_to_currency} exchange rates")
        plt.show()
        
    elif status_code == 400:
        messagebox.showerror("Wrong Input Parameter")
    elif status_code == 401:
        messagebox.showerror("Invalid API key")
    elif status_code == 404:
        messagebox.showerror("The requested resource doesn't exist.")
    elif status_code == 429:
        messagebox.showerror("Request quota has been used up")
    elif status_code >= 500 and status_code < 600:
        messagebox.showerror("Server failed to process request(Server-Side problem)") 

    DateList.clear()
    SelectedPeriod.set("Histoical rate between  and .")
# Call the yearly_rates_graph() function
# yearly_rates_graph("USD", "HKD", 365)