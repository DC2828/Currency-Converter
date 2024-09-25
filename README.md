Currency Converter




API:
This project is a currency converter that applied 2 APIs for converting a currency to other currencies:
        here are the websites if the 2 APIs:
                1--- https://www.exchangerate-api.com/ ---for standard conversion
                2--- https://apilayer.com/marketplace/exchangerates_data-api ---for conversion in historical rates
        
        **Because of the free plan our group is using, both of the APIs will have limited request quotas every month, which means there are a limited quota every month of using this program.
                The 1st API provides 1500 requests each month
                The 2nd API provides 100 requests each month:(
                
                To help with this problem we have sign up for more than one accounts to get more keys and here are the keys:
                        1st API:
                                4137ba268245a1ba148250e4 --- in use
                                17facf9824c957b2fd88d09e
                                
                                To change the key of this API user can go to the Converter.py module of the program and copy the key into line 8 API_Key = **key


                        2nd API:
                                ZAHEanC9UBLd0vBDG6Ov0kBqfs2NASb8 --- in use
                                bHW7XlUxy1DwX4hQQP31Dr1ukjVCen1P
                                gn48XP27wyrLJ6BW8gcywaBwLnIRB2kb


                                To change the key of this API user can go to the Graph.py module of the program and copy the key into line 25 "apikey: **key"
Run:
Before running the program make sure to have all the external module installed:
        If any of the external packages have not been installed, please install it by typing the following command in the terminal according the package that you haven't install
        tkcalendar:
                pip install tkcalendar
        requests:
                pip install requests
        matplotlib:
                pip install matplotlib


        The rest of the modules in the program should be built-in,so no install is required.
