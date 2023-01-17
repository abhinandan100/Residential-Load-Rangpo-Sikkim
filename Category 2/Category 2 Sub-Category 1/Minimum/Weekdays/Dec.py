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
OR = User("Two room minimal",1,1)
User_list.append(OR)
#One-Room Minimum Connected Load
OR_indoor_LEDBulb = OR.Appliance(OR,1,7,2,300,0.15,15)
OR_indoor_LEDBulb.windows([1080,1440],[0,0],0.1)
OR_indoor_LEDBulb1 = OR.Appliance(OR,1,7,2,360,0.15,15,occasional_use=0.5)
OR_indoor_LEDBulb1.windows([1080,1440],[0,0],0.1)
OR_lavatory_LEDBulb = OR.Appliance(OR,1,5,2,45,0.2,5)
OR_lavatory_LEDBulb.windows([1080,1440],[360,540],0.1)
OR_Phone_charger = OR.Appliance(OR,1,5,2,180,0.3,15)
OR_Phone_charger.windows([1080,1440],[360,540],0.35)
OR_KitchenLED=OR.Appliance(OR,1,7,2,180,0.15,15)
OR_KitchenLED.windows([1080,1380],[360,540],0.2)



