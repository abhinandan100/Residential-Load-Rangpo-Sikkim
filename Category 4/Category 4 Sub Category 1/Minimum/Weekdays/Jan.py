#Create new user classes
OR = User("Two room minimal",1,1)
User_list.append(OR)
#One-Room Minimum Connected Load
OR_indoor_LEDBulb = OR.Appliance(OR,2,7,2,240,0.15,15)
OR_indoor_LEDBulb.windows([1050,1380],[0,0],0.1)
OR_indoor_LEDBulb1 = OR.Appliance(OR,2,7,2,240,0.15,15,occasional_use=0.5)
OR_indoor_LEDBulb1.windows([1050,1380],[0,0],0.1)
OR_lavatory_LEDBulb = OR.Appliance(OR,1,5,2,45,0.2,5)
OR_lavatory_LEDBulb.windows([1080,1440],[0,0],0.1)
OR_Phone_charger = OR.Appliance(OR,2,5,2,180,0.3,15)
OR_Phone_charger.windows([1080,1440],[360,540],0.35)
OR_KitchenLED=OR.Appliance(OR,2,7,2,180,0.15,15)
OR_KitchenLED.windows([1080,1380],[360,540],0.2)
OR_KitchenExhaustFan=OR.Appliance(OR,1,40,2,180,0.15,15)
OR_KitchenExhaustFan.windows([1140,1380],[420,540],0.2)
OR_TV=OR.Appliance(OR,1,60,2,180,0.2,30)
OR_TV.windows([1080,1199],[1201,1380], 0.15)
OR_SetTopBox = OR.Appliance(OR,1,10,2,180,0.15,30)
OR_SetTopBox.windows([1080,1199],[1201,1380],0.15)
OR_MosquitoRepellent = OR.Appliance(OR,1,7,2,480,0.15,30, occasional_use=0.5)
OR_MosquitoRepellent.windows([1200,1440],[0,360],0.35)
OR_Fridge = OR.Appliance(OR,1,200,1,1440,0,45, 'yes',1)
OR_Fridge.windows([0,1440],[0,0])
OR_Fridge.specific_cycle_1(5,45,200,45)
OR_Fridge.cycle_behaviour([0,1440],[0,0])
OR_Balcony_LEDBulb = OR.Appliance(OR,1,7,2,60,0.15,15)
OR_Balcony_LEDBulb.windows([1080,1440],[0,0],0.1)
OR_MixerGrinder = OR.Appliance(OR,1,500,2,30,0.15,5,occasional_use = 0.2)
OR_MixerGrinder.windows([1080,1320],[0,0],0.3)
OR_BathroomGeyser = OR.Appliance(OR,1,1500,2,60,0.1,15, 'yes',1, occasional_use=0.5)
OR_BathroomGeyser.windows([360,540],[0,0],0.1)
OR_BathroomGeyser.specific_cycle_1(1500,15,10,30)
OR_BathroomGeyser.cycle_behaviour([360,540],[0,0])
