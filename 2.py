names =['carmen','Alice', 'eve', 'bob', 'nav', 'payman']
phone =['3489467', '5284690', '1892531']



numbers = {
    "Viivi": "050-1234567",
    "Ahmed": "040-1112223",
    "Pekka": "050-7564321",
    "George": "040-75274572"
}

phone=input('please give the george number') 


    
for item in numbers:
    if numbers[item] == phone:  
        print(f'{item} available')
        break    
    

        
       
        