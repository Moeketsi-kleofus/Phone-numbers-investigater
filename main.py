from phonenumbers import geocoder,parse,carrier,timezone,carrierdata,can_be_internationally_dialled,is_valid_number
try:
    #get user number
    user_number=input("Enter phone numbers(Note:You have to start with the country code eg:+27) :")
    #parse entered numbers
    parsing_numbers=parse(user_number)
    #determine if the numbers is valid
    is_valid=is_valid_number(parsing_numbers)
    #get location of phone numbers entered
    number_location=geocoder.description_for_number(parsing_numbers,"en")
    #get the service provider
    service_privider=carrier.name_for_number(parsing_numbers,"en")
    #get phone numbers timezone
    Timezone=timezone.time_zones_for_number(parsing_numbers)
    #determine if number can internationally be dialled
    can_dial_internationally=can_be_internationally_dialled(parsing_numbers)
    #results
    print("Is the number valid : {0} \nNumber phones entered are from : {1} \nService provider : {2} \nTimezone : {3} \nCan dial internationally : {4}".format(is_valid,number_location,service_privider,Timezone,can_dial_internationally))
except Exception as e:
    print(e)

