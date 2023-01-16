#One-Room Minimum Connected Load
#Create new user classes
OR = User("One room minimal",1,1)
User_list.append(OR)

##One-Room Minimum Connected Load
OR_indoor_Tubelight1 = OR.Appliance(OR,1,55,2,240,0.15,15,occasional_use = 0.75)
OR_indoor_Tubelight1.windows([1050,1260],[360,420],0.1)
OR_indoor_Tubelight2 = OR.Appliance(OR,1,55,2,120,0.15,15,occasional_use = 0.167)
OR_indoor_Tubelight2.windows([1050,1260],[330,390],0.3)
OR_lavatory_LEDBulb = OR.Appliance(OR,1,5,1,60,0.2,15, occasional_use = 0.75)
OR_lavatory_LEDBulb.windows([360,1260],[0,0],0.1)
OR_Phone_charger = OR.Appliance(OR,1,5,1,150,0.3,15)
OR_Phone_charger.windows([360,1260],[0,0],0.35)
OR_Fan = OR.Appliance(OR,1,70, 2, 780,0.15,15,occasional_use = 0.75)
OR_Fan.windows([360,1260],[0,0],0.2 )
OR_TV=OR.Appliance(OR,1,60,1,180,0.25,30)
OR_TV.windows([840,1260],[0,0], 0.15)
OR_KitchenTubelight=OR.Appliance(OR,1,40,2,240,0.15,15)
OR_KitchenTubelight.windows([1050,1230],[720,900],0.2)
OR_KitchenExhaustFan=OR.Appliance(OR,1,40,2,240,0.15,15)
OR_KitchenExhaustFan.windows([1050,1230],[720,900],0.2)
OR_balcony_LED = OR.Appliance(OR,1,9,1,30,0.15,5)
OR_balcony_LED.windows([1080,1230],[0,0],0.1)
OR_Fridge = OR.Appliance(OR,1,200,1,1440,0,45, 'yes',1)
OR_Fridge.windows([0,1440],[0,0])
OR_Fridge.specific_cycle_1(5,45,200,45)
OR_Fridge.cycle_behaviour([0,720],[721,1440])
OR_MixerGrinder = OR.Appliance(OR,1,500,2,60,0.15,15,occasional_use = 0.33 )
OR_MixerGrinder.windows([750,900],[1080,1200],0.3)
OR_SetTopBox = OR.Appliance(OR,1,10,2,180,0.15,15)
OR_SetTopBox.windows([840,1230],[0,0],0.3)
OR_InductionCooktop = OR.Appliance(OR,1,2000,2,180,0.1,15, 'yes',1)
OR_InductionCooktop.windows([720,900],[1080,1200],0.15)
OR_InductionCooktop.specific_cycle_1(500,15,2000,5)
OR_InductionCooktop.cycle_behaviour([1080,1200],[750,900])
OR_Waterpurifier=OR.Appliance(OR,1,50,2,45,0.35, 15)
OR_Waterpurifier.windows([720,1230],[0,0], 0.35)
OR_Iron=OR.Appliance(OR,1,50,1,30,0.35, 15,occasional_use = 0.3)
OR_Iron.windows([900,1230],[0,0], 0.35)
