# Created by : Sidney Kang
# Created on : 12 Dec. 2017
# Created for : ICS3UR
# Daily Assignment - Unit 6-06
# This program

from enum import Enum

Street = Enum('ST', 'DR', 'AVE', 'CRES', 'GRV')

class Address():
      def __init__(self, unit_number, street_name, street_type):
          
          self.unit_number = unit_number
          self.street_name = street_name               
          self.street_type = street_type  
      
      def street_address(self):
          
          self.street_name = (address.unit_number + ' ' + address.street_name + ' ' + address.street_type)
          
          return self.street_name                                                                          
           
unit_number = raw_input("What is their unit number? ")
unit_number = unit_number.upper()      
street_name = raw_input("What is the name of the street? ")
street_name = street_name.upper()    
street_type = raw_input("What is their street type? ")  
street_type = street_type.upper()  
while street_type not in Street:
    street_type = raw_input("Please enter their street type. (ex: Dr) ")     
    street_type = street_type.upper()
            
address = Address(unit_number, street_name, street_type)

print(address.street_address())      
#print(address.unit_number + ' ' + mailing_address.street_name + ' ' + mailing_address.street_type)          
