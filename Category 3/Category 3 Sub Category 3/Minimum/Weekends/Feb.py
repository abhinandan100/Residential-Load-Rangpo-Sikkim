#One-Room Minimum Connected Load
#Create new user classes
OR = User("One room minimal",1,1)
User_list.append(OR)

#One-Room Minimum Connected Load
OR_indoor_LEDBulb1 = OR.Appliance(OR,1,7,2,420,0.15,15, occasional_use = 0.25)
OR_indoor_LEDBulb1.windows([1080,1440],[300,420],0.1)
OR_indoor_LEDBulb2 = OR.Appliance(OR,1,7,2,120,0.15,15, occasional_use=0.5)
OR_indoor_LEDBulb2.windows([1080,1440],[300,420],0.3)
OR_indoor_LEDBulb3 = OR.Appliance(OR,1,7,2,120,0.15,15,occasional_use=0.25)
OR_indoor_LEDBulb3.windows([1080,1440],[300,420],0.3)
OR_lavatory_LEDBulb = OR.Appliance(OR,1,5,2,60,0.2,5, occasional_use=0.5)
OR_lavatory_LEDBulb.windows([360,1440],[0,0],0.1)
OR_Fan = OR.Appliance(OR,1,30, 2, 720,0.15, occasional_use=0.5)
OR_Fan.windows([480,1440],[0,0],0.2)
OR_Fan1 = OR.Appliance(OR,1,30, 2, 720,0.15,15,occasional_use=0.5)
OR_Fan1.windows([0,1440],[0,0],0.2)
OR_Fan2 = OR.Appliance(OR,1,30, 2, 720,0.15,15,occasional_use=0.5)
OR_Fan2.windows([0,1440],[0,0],0.2)
OR_TV=OR.Appliance(OR,1,60,2,360,0.2,30)
OR_TV.windows([540,1440],[0,0], 0.35)
OR_SetTopBox = OR.Appliance(OR,1,10,2,360,0.2,30,occasional_use=0.5)
OR_SetTopBox.windows([540,1400],[0,0],0.35)
OR_KitchenLED=OR.Appliance(OR,1,7,3,300,0.15,15)
OR_KitchenLED.windows([1140,1380],[360,540],0.25,[720,900])
OR_KitchenExhaustFan=OR.Appliance(OR,1,40,2,180,0.15,15)
OR_KitchenExhaustFan.windows([1140,1380],[360,540],0.2,[720,900])
OR_Fridge = OR.Appliance(OR,1,200,1,1440,0,45, 'yes',1)
OR_Fridge.windows([0,1440],[0,0])
OR_Fridge.specific_cycle_1(5,45,200,45)
OR_Fridge.cycle_behaviour([0,1440],[0,0])
OR_MosquitoRepellent = OR.Appliance(OR,2,7,2,480,0.15,30, occasional_use=0.5)
OR_MosquitoRepellent.windows([1200,1440],[0,360],0.35)
OR_Phone_charger = OR.Appliance(OR,2,5,2,180,0.3,15)
OR_Phone_charger.windows([0,1440],[0,0],0.35)
OR_MixerGrinder = OR.Appliance(OR,1,500,2,60,0.15,15,occasional_use = 0.33)
OR_MixerGrinder.windows([1080,1320],[420,600],0.3, [720,900])
OR_WaterPurifier = OR.Appliance(OR,1,60,2,60,0.15,15)
OR_WaterPurifier.windows([1080,1380],[420,900],0.3)
OR_BathroomGeyser = OR.Appliance(OR,1,2000,2,60,0.1,15, 'yes',1,occasional_use=0.5)
OR_BathroomGeyser.windows([420,540],[541,900],0.1,[1080,1200])
OR_BathroomGeyser.specific_cycle_1(2000,10,10,5)
OR_BathroomGeyser.cycle_behaviour([420,900],[0,0])
