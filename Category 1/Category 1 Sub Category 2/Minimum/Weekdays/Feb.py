# -*- coding: utf-8 -*-

#%% Definition of the inputs
'''
Input data definition 
'''


from core import User, np
User_list = []

'''
This example input file represents an whole village-scale community,
adapted from the data used for the Journal publication. It should provide a 
complete guidance to most of the possibilities ensured by RAMP for inputs definition,
including specific modular duty cycles and cooking cycles. 
For examples related to "thermal loads", see the "input_file_2".
'''

#Create new user classes
OR = User("One room minimal",1,1)
User_list.append(OR)

#Single Room Least Connected Load Dayshift Weekdays
OR_indoor_LEDBulb = OR.Appliance(OR,1,7,2,240,0.15,15)
OR_indoor_LEDBulb.windows([1080,1260],[360,420],0.1)
OR_lavatory_LEDBulb = OR.Appliance(OR,1,5,2,45,0.2,15)
OR_lavatory_LEDBulb.windows([360,1260],0.1)
OR_Phone_charger = OR.Appliance(OR,1,5,1,150,0.3,15)
OR_Phone_charger.windows([360,900],[901,1230],0.35)





