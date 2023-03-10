#One-Room Minimum Connected Load
#Create new user classes
OR = User("One room minimal",1,1)
User_list.append(OR)


#One-Room Minimum Connected Load
OR_indoor_Tubelight1 = OR.Appliance(OR,1,55,2,420,0.15,15)
OR_indoor_Tubelight1.windows([1080,1440],[300,420],0.1)
OR_indoor_Tubelight2 = OR.Appliance(OR,1,55,2,180,0.15,15,occasional_use = 0.33)
OR_indoor_Tubelight2.windows([1080,1440],[300,420],0.3)
OR_lavatory_LEDBulb = OR.Appliance(OR,1,5,1,90,0.2,5)
OR_lavatory_LEDBulb.windows([360,1440],[0,0],0.3)
OR_Phone_charger = OR.Appliance(OR,1,5,2,200,0.3,15)
OR_Phone_charger.windows([1082,1440],[480,1078],0.35)
OR_Fan = OR.Appliance(OR,1,70,1,1200,0.15,15)
OR_Fan.windows([0,1440],[0,0],0.2)
OR_TV=OR.Appliance(OR,1,60,1,720,0.2,30)
OR_TV.windows([480,1440],[0,0],0.15)
OR_KitchenTubelight=OR.Appliance(OR,1,40,2,300,0.15,15)
OR_KitchenTubelight.windows([1140,1380],[360,540],0.2)
OR_KitchenExhaustFan=OR.Appliance(OR,1,40,3,240,0.15,15)
OR_KitchenExhaustFan.windows([720,900],[1140,1380],0.2,[420,600])
OR_balcony_LED = OR.Appliance(OR,1,9,1,30,0.15,5)
OR_balcony_LED.windows([1080,1440],[0,0],0.1)
OR_Fridge = OR.Appliance(OR,1,200,1,1440,0,45, 'yes',1)
OR_Fridge.windows([0,1440],[0,0])
OR_Fridge.specific_cycle_1(5,45,200,45)
OR_Fridge.cycle_behaviour([0,1440],[0,0])
OR_MixerGrinder = OR.Appliance(OR,1,500,2,90,0.15,15,occasional_use = 0.33)
OR_MixerGrinder.windows([720,900],[1080,1380],0.35)
OR_SetTopBox = OR.Appliance(OR,1,10,1,720,0.15,15)
OR_SetTopBox.windows([480,1440],[0,0],0.35)
OR_MosquitoRepellent = OR.Appliance(OR,1,7,2,480,0.15,30)
OR_MosquitoRepellent.windows([1200,1440],[0,360],0.35)
OR_InductionCooktop = OR.Appliance(OR,1,2000,3,300,0.1,15, 'yes',1)
OR_InductionCooktop.windows([720,900],[1110,1350],0.15,[480,540])
OR_InductionCooktop.specific_cycle_1(500,15,2000,15)
OR_InductionCooktop.cycle_behaviour([1110,1350],[480,900])
OR_Waterpurifier=OR.Appliance(OR,1,50,2,45,0.35, 15)
OR_Waterpurifier.windows([720,1230],[0,0], 0.35)
OR_Iron=OR.Appliance(OR,1,50,1,30,0.35, 15,occasional_use = 0.3)
OR_Iron.windows([900,1230],[0,0], 0.35)
