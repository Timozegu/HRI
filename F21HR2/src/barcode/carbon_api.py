import requests
import cozmo

# request to an external api :  https://rapidapi.com/bulat.yauheni/api/dietagram
def get_carbon_value(value):
    url = "https://dietagram.p.rapidapi.com/apiBarcode.php"

    querystring = {"name": value}  #value = barcode data

    headers = {
        "X-RapidAPI-Key": "c0485fbbfcmsh7c0f44d5ef7bd1ap14e659jsnc711394b1970",
        "X-RapidAPI-Host": "dietagram.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    response_dict = response.json()
    dishes = response_dict.get("dishes")
    if dishes == []:
        print("No dishes found")
        exit(0)
    print(f"There are {dishes[0].get('carbon')} g of carbon in this food ")
    return dishes[0].get('carbon')  #,dishes[0].get('fat'),dishes[0].get('protein')

#compare the carbon level
def inspect_carbon(robot: cozmo.robot.Robot, carbon):
    if carbon < 20:
        robot.say_text("carbohydrates are low").wait_for_completed()
        robot.say_text(str(carbon)).wait_for_completed()
        robot.say_text("This food is good").wait_for_completed()
        print("LOW")
    else:
        robot.say_text("carbohydrates are").wait_for_completed()
        robot.say_text(str(carbon)).wait_for_completed()
        robot.say_text("This food is bad").wait_for_completed()
        print("HIGH")
    return