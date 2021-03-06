import requests, json, sys
import config
 
api_key = config.API_KEY
  
url = "https://api.openweathermap.org/data/2.5/weather?q="

while True:
    city_name = input("Enter city name ('q' to quit): ") 
    if city_name == 'q':
        print("Program ended, Thank you for using.............")
        break
    # complete url address 
    final = url + city_name+"&appid="+api_key 

    response = requests.get(final) 
      
    # json method of response object convert json format data into python 
    #format data 
    
    x = response.json() 
    
    # check the return status code
    
    if x["cod"] != "404": 
      
        # store the value of "main" key in variable y
         
        y = x["main"] 
       
        current_temperature = y["temp"] 
      
        current_pressure = y["pressure"] 
      
        current_humidiy = y["humidity"] 
      
        # store the value of "weather" 
        # key in variable z 
        z = x["weather"] 
    
        weather_description = z[0]["description"] 
      
        # print following values 
        print(" Temperature (in kelvin unit) = " +
                        str(current_temperature) + 
              "\n atmospheric pressure (in hPa unit) = " +
                        str(current_pressure) +
              "\n humidity (in percentage) = " +
                        str(current_humidiy) +
              "\n description = " +
                        str(weather_description))  
      
    else: 
        print(" City Not Found ") 
        
