#One-Room Minimum Connected Load
OR = User("One room minimal",1,1)
User_list.append(OR)

#One-Room Minimum Connected Load
OR_indoor_LEDBulb = OR.Appliance(OR,2,7,2,240,0.15,15)
OR_indoor_LEDBulb.windows([1080,1200],[360,420],0.1)
OR_indoor_LEDBulb1 = OR.Appliance(OR,2,7,2,240,0.15,15, occasional_use=0.5)
OR_indoor_LEDBulb1.windows([1080,1200],[360,420],0.1)
OR_kitchen_LEDBulb1 = OR.Appliance(OR,1,7,2,240,0.15,15, occasional_use=0.25)
OR_kitchen_LEDBulb1.windows([1080,1200],[360,420],0.1)
OR_kitchen_ExhaustFan = OR.Appliance(OR,1,40,2,180,0.15,15, occasional_use=0.25)
OR_kitchen_ExhaustFan.windows([1080,1200],[840,960],0.1)
OR_lavatory_LEDBulb = OR.Appliance(OR,1,5,2,45,0.2,15)
OR_lavatory_LEDBulb.windows([360,1200],[0,0], 0.1)
OR_Phone_charger = OR.Appliance(OR,1,5,2,150,0.3,15)
OR_Phone_charger.windows([360,1260],[0,0],0.35)
OR_TV=OR.Appliance(OR,1,60,2,300,0.25,30)
OR_TV.windows([840,1260],[0,0], 0.15)
OR_SetTopBox = OR.Appliance(OR,1,10,2,300,0.25,30)
OR_SetTopBox.windows([840,1260],[0,0],0.15)
OR_Fridge = OR.Appliance(OR,1,200,1,1440,0,45, 'yes',1)
OR_Fridge.windows([0,1440],[0,0])
OR_Fridge.specific_cycle_1(5,45,200,45)
OR_Fridge.cycle_behaviour([0,720],[721,1440])
OR_Waterpurifier=OR.Appliance(OR,1,50,2,45,0.35, 15)
OR_Waterpurifier.windows([720,1260],[360,480], 0.35)
