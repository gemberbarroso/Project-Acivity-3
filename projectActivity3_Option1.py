import urllib.parse
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)
from pip._vendor import requests

main_api = "https://www.mapquestapi.com/directions/v2/route?"
key = "QAWzHgeqVXpkMAWzKGojDst5CNgXiAq1"
while True:
    orig = input("Starting Location: ")
    if orig == "quit" or orig == "q":
        break
    dest = input("Destination: ")
    if dest == "quit" or dest == "q":
        break
    
    url = main_api + urllib.parse.urlencode({"key":key, "from":orig, "to":dest})
    print("URL: " + (url))
    json_data = requests.get(url).json()
    json_status = json_data["info"]["statuscode"]

#Colors and Effects for Foreground, Background and Style
#Foreground: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
#Background: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
#Style: DIM, NORMAL, BRIGHT, RESET_ALL

    if json_status == 0:
        print("API Status: " + str(json_status) + " = A successful route call.\n")
        print(Fore.YELLOW +"~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print(Fore.CYAN + Style.BRIGHT + Back.MAGENTA + "Directions from " + (orig) + " to " + (dest))
        print(Fore.BLACK+ Style.DIM + Back.WHITE + "Trip Duration: " + Fore.BLUE + (json_data["route"]["formattedTime"]))
        print(Fore.BLACK+ Style.DIM + Back.WHITE + "Kilometers: " + Fore.BLUE + str("{:.2f}".format(json_data["route"]["distance"] * 1.6 ))) #changed into KM
        print(Fore.BLACK+ Style.DIM + Back.WHITE + "Fuel Used (Liters): " + Fore.BLUE + str("{:.2f}".format(json_data["route"]["fuelUsed"] * 3.78 ))) #changed into Liters
        
        #additional feature: displaying longitude and latitude
        print(Fore.YELLOW + "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print(Fore.CYAN + Style.BRIGHT + Back.MAGENTA + "DISPLAY LONGITUDE and LATITUDE") 
        for each in json_data["route"]["locations"][0]["latLng"]:
            print (Fore.BLACK+ Style.DIM + Back.WHITE + "Location -> " + Fore.BLUE + str(json_data["route"]["locations"][0]["latLng"] ) )
        #additional feature: toll roads and route type
        print(Fore.BLACK+ Style.DIM + Back.WHITE + "Toll Roads between: " + Fore.BLUE + str(json_data["route"]["hasTollRoad"])) 
        print(Fore.BLACK+ Style.DIM + Back.WHITE + "Route Type: " + Fore.BLUE + str(json_data["route"]["options"]["routeType"]))
        print(Fore.YELLOW +"~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")

        #additional feature: travel narrations 
        print(Fore.CYAN + Style.BRIGHT + Back.MAGENTA + "Travel narrations of " + (orig) + " to " + (dest))
        for each in json_data["route"]["legs"][0]["maneuvers"]:
            print(Fore.GREEN + (each["narrative"]) + " (" + str("{:.2f}".format((each["distance"])*1.61) + " km)"))
        print(Fore.YELLOW +"~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")

        
 
                
          #colorama error code      
    elif json_status == 402:
        print(Fore.YELLOW + "**********************************************")
        print(Fore.YELLOW + "Status Code: " + str(json_status) + "; Invalid user inputs for one or both locations.")
        print(Fore.YELLOW + "**********************************************\n")
    elif json_status == 611:
        print(Fore.YELLOW + "**********************************************")
        print(Fore.YELLOW + "Status Code: " + str(json_status) + "; Missing an entry for one or both locations.")
        print(Fore.YELLOW + "**********************************************\n")
    else:
        print(Fore.BLUE + "************************************************************************")
        print(Fore.BLUE + "For Status Code: " + str(json_status) + "; Refer to:")
        print(Fore.BLUE + "https://developer.mapquest.com/documentation/directions-api/status-codes")
        print(Fore.BLUE + "************************************************************************\n")