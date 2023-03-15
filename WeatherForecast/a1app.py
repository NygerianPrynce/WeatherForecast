import a1
def play():
    city = input("What city would you like to check the weather for? ")
    system = input("What system of measurement do you use (Metric/US standard system? ")
    json = a1.weather_response(city)
    while True:
        if system.lower() == "metric":
            print("As of " + str(a1.get_time(json)) + " it is " +str(a1.get_condition(json)).lower()+" in "+ (city)+ " with a temperature of "+ str(a1.get_tempc(json)) +" degrees celsius, but feels like it is "+ str(a1.get_feelc(json)) + " degrees. The humidity is at "+str(a1.get_humidity(json))+"% and there is "+str(a1.get_precipmm(json))+" millimeters of precipitation in your city. Finally, Wind speeds are at "+str(a1.get_windkph(json))+" kilometers per hour moving "+str(a1.get_winddir(json)))
            break
        if system.lower() == "us standard system":
            print("As of " + str(a1.get_time(json)) + " it is " +str(a1.get_condition(json)).lower()+" in "+ (city)+ " with a temperature of "+ str(a1.get_tempf(json)) +" degrees celsius, but feels like it is "+ str(a1.get_feelf(json)) + " degrees. The humidity is at "+str(a1.get_humidity(json))+"% and there is "+str(a1.get_precipin(json))+" inches of precipitation in your city. Finally, Wind speeds are at "+str(a1.get_windmph(json))+" miles per hour moving "+str(a1.get_winddir(json)))
            break
        else:
            print("Please make sure to input the correct measurement system(*pay attention to spelling*)")
while True:
    play()
    check = input("Would you like to check the weather again? ")
    if check.lower() == "no":
        break

