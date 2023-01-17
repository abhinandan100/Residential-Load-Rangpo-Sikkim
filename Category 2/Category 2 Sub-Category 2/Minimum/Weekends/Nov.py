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

#One-Room Minimum Connected Load
OR_indoor_LEDBulb = OR.Appliance(OR,1,7,2,480,0.35,15,occasional_use = 0.5)
OR_indoor_LEDBulb.windows([1080,1440],[300,420],0.3)
OR_indoor_LEDBulb1 = OR.Appliance(OR,1,7,2,480,0.35,15,occasional_use = 0.5)
OR_indoor_LEDBulb1.windows([1080,1440],[300,420],0.3)
OR_lavatory_LEDBulb = OR.Appliance(OR,1,5,2,60,0.35,5,occasional_use = 0.5)
OR_lavatory_LEDBulb.windows([360,1440],[0,120], 0.35)
OR_Phone_charger = OR.Appliance(OR,1,5,2,180,0.35,15,occasional_use = 0.5)
OR_Phone_charger.windows([0,1440],[0,0],0.35)
OR_TV=OR.Appliance(OR,1,60,2,180,0.25,30, occasional_use = 0.5)
OR_TV.windows([360,1440],[0,0], 0.15)
OR_ImmersionHeater = OR.Appliance(OR,1,1000,2,45,0.3,15, occasional_use = 0.5)
OR_ImmersionHeater.windows([360,1440],[0,0],0.35)

