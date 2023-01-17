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
OR_indoor_LEDBulb = OR.Appliance(OR,1,7,2,360,0.15,15,occasional_use=0.5)
OR_indoor_LEDBulb.windows([1080,1440],[0,0],0.1)
OR_indoor_LEDBulb1 = OR.Appliance(OR,1,7,2,360,0.15,15,occasional_use=0.5)
OR_indoor_LEDBulb1.windows([1080,1440],[0,0],0.1)
OR_indoor_LEDBulb2 = OR.Appliance(OR,1,7,2,360,0.15,15,occasional_use=0.5)
OR_indoor_LEDBulb2.windows([1080,1440],[0,0],0.1)
OR_indoor_LEDBulb3 = OR.Appliance(OR,1,7,2,360,0.15,15,occasional_use=0.5)
OR_indoor_LEDBulb3.windows([1080,1440],[0,0],0.1)
OR_lavatory_LEDBulb = OR.Appliance(OR,1,5,2,45,0.2,5,occasional_use=0.5)
OR_lavatory_LEDBulb.windows([0,1440],[0,0],0.1)
OR_Phone_charger = OR.Appliance(OR,2,5,2,180,0.3,15, occasional_use=0.5)
OR_Phone_charger.windows([0,1440],[0,0],0.35)
OR_KitchenLED=OR.Appliance(OR,1,7,2,180,0.15,15, occasional_use=0.5)
OR_KitchenLED.windows([1080,1380],[360,420],0.2)
OR_KitchenExhaustFan=OR.Appliance(OR,1,40,2,180,0.15,15,occasional_use = 0.5)
OR_KitchenExhaustFan.windows([1140,1380],[420,600],0.2,[720,900])
OR_TV=OR.Appliance(OR,1,60,2,360,0.2,30,occasional_use = 0.5)
OR_TV.windows([540,1440],[0,0], 0.35)
OR_SetTopBox = OR.Appliance(OR,1,10,2,360,0.2,30,occasional_use=0.5)
OR_SetTopBox.windows([540,1400],[0,0],0.35)
OR_MosquitoRepellent = OR.Appliance(OR,2,7,2,480,0.15,30,occasional_use=0.5)
OR_MosquitoRepellent.windows([1200,1440],[0,360],0.35)
OR_Fridge = OR.Appliance(OR,1,200,1,1440,0,45, 'yes',1)
OR_Fridge.windows([0,1440],[0,0])
OR_Fridge.specific_cycle_1(5,45,200,45)
OR_Fridge.cycle_behaviour([0,1440],[0,0])
