#One-Room Minimum Connected Load
#Create new user classes
OR = User("One room minimal",2,1)
User_list.append(OR)

#One-Room Minimum Connected Load
OR_indoor_Tubelight1 = OR.Appliance(OR,1,55,2,420,0.15,15)
OR_indoor_Tubelight1.windows([1020,1320],[240,330],0.1)
OR_indoor_Tubelight2 = OR.Appliance(OR,1,55,2,360,0.15,15, occasional_use = 0.5)
OR_indoor_Tubelight2.windows([1020,1320],[240,360],0.3)
OR_lavatory_LEDBulb = OR.Appliance(OR,1,5,1,60,0.2,15)
OR_lavatory_LEDBulb.windows([870,1440],[0,360],0.1)
OR_Phone_charger = OR.Appliance(OR,4,5,2,120,0.3,15)
OR_Phone_charger.windows([870,1320],[240,360],0.35)
OR_TV=OR.Appliance(OR,1,60,2,180,0.2,30)
OR_TV.windows([900,1199],[1201,1320], 0.15)
OR_SetTopBox = OR.Appliance(OR,1,10,2,210,0.15,15)
OR_SetTopBox.windows([900,1199],[1201,1320],0.3)
OR_KitchenTubelight=OR.Appliance(OR,1,40,2,180,0.15,15)
OR_KitchenTubelight.windows([1140,1320],[240,360],0.2)
OR_KitchenExhaustFan=OR.Appliance(OR,1,40,2,180,0.15,15)
OR_KitchenExhaustFan.windows([1140,1380],[240,360],0.2)
OR_balcony_LED = OR.Appliance(OR,1,9,2,30,0.15,5)
OR_balcony_LED.windows([1080,1320],[240,360],0.1)
OR_Fridge = OR.Appliance(OR,1,200,1,1440,0,45, 'yes',1)
OR_Fridge.windows([0,1440],[0,0])
OR_Fridge.specific_cycle_1(5,45,200,45)
OR_Fridge.cycle_behaviour([0,720],[721,1440])
OR_MixerGrinder = OR.Appliance(OR,1,500,2,60,0.15,15,occasional_use = 0.33)
OR_MixerGrinder.windows([1080,1320],[0,0],0.3)
OR_InductionCooktop = OR.Appliance(OR,1,2000,3,150,0.1,15, 'yes',1)
OR_InductionCooktop.windows([900,960],[1140,1260],0.15, [240,360])
OR_InductionCooktop.specific_cycle_1(500,15,2000,15)
OR_InductionCooktop.cycle_behaviour([1140,1260],[0,0])
OR_WaterPurifier = OR.Appliance(OR,1,50,2,60,0.15,15)
OR_WaterPurifier.windows([870,1320],[240,360],0.3)
OR_Iron = OR.Appliance(OR,1,1200,2,30,0.15,15, occasional_use=0.5)
OR_Iron.windows([1080,1320],[360,540],0.3)
OR_MosquitoRepellent = OR.Appliance(OR,1,7,2,480,0.15,30)
OR_MosquitoRepellent.windows([1200,1440],[0,360],0.35)

#One-Room Minimum Connected Load
#Create new user classes
OR1 = User("One room minimal",4,1)
User_list.append(OR1)

#One-Room Minimum Connected Load
OR1_indoor_Tubelight1 = OR1.Appliance(OR1,1,55,2,420,0.15,15)
OR1_indoor_Tubelight1.windows([1020,1320],[240,330],0.1)
OR1_indoor_Tubelight2 = OR1.Appliance(OR1,1,55,2,360,0.15,15, occasional_use = 0.5)
OR1_indoor_Tubelight2.windows([1020,1320],[240,360],0.3)
OR1_lavatory_LEDBulb = OR1.Appliance(OR1,1,5,1,60,0.2,15)
OR1_lavatory_LEDBulb.windows([870,1440],[0,360],0.1)
OR1_Phone_charger = OR1.Appliance(OR1,4,5,2,120,0.3,15)
OR1_Phone_charger.windows([870,1320],[240,360],0.35)
OR1_TV=OR1.Appliance(OR1,1,60,2,180,0.2,30)
OR1_TV.windows([900,1199],[1201,1320], 0.15)
OR1_SetTopBox = OR1.Appliance(OR1,1,10,2,210,0.15,15)
OR1_SetTopBox.windows([900,1199],[1201,1320],0.3)
OR1_KitchenTubelight=OR1.Appliance(OR1,1,40,2,180,0.15,15)
OR1_KitchenTubelight.windows([1140,1320],[240,360],0.2)
OR1_KitchenExhaustFan=OR1.Appliance(OR1,1,40,2,180,0.15,15)
OR1_KitchenExhaustFan.windows([1140,1380],[240,360],0.2)
OR1_balcony_LED = OR1.Appliance(OR1,1,9,2,30,0.15,5)
OR1_balcony_LED.windows([1080,1320],[240,360],0.1)
OR1_Fridge = OR1.Appliance(OR1,1,200,1,1440,0,45, 'yes',1)
OR1_Fridge.windows([0,1440],[0,0])
OR1_Fridge.specific_cycle_1(5,45,200,45)
OR1_Fridge.cycle_behaviour([0,720],[721,1440])
OR1_MixerGrinder = OR1.Appliance(OR1,1,500,2,60,0.15,15,occasional_use = 0.33)
OR1_MixerGrinder.windows([1080,1320],[0,0],0.3)
OR1_WaterPurifier = OR1.Appliance(OR1,1,50,2,60,0.15,15)
OR1_WaterPurifier.windows([870,1320],[240,360],0.3)
OR1_Iron = OR1.Appliance(OR1,1,1200,2,30,0.15,15, occasional_use=0.5)
OR1_Iron.windows([1080,1320],[360,540],0.3)
OR1_MosquitoRepellent = OR1.Appliance(OR1,1,7,2,480,0.15,30)
OR1_MosquitoRepellent.windows([1200,1440],[0,360],0.35)

#One-Room Minimum Connected Load
#Create new user classes
OR2 = User("One room minimal",3,1)
User_list.append(OR2)

#One-Room Minimum Connected Load
OR2_indoor_Tubelight1 = OR2.Appliance(OR2,1,55,2,420,0.15,15)
OR2_indoor_Tubelight1.windows([1020,1320],[240,330],0.1)
OR2_lavatory_LEDBulb = OR2.Appliance(OR2,1,5,1,60,0.2,15)
OR2_lavatory_LEDBulb.windows([870,1440],[0,360],0.1)
OR2_Phone_charger = OR2.Appliance(OR2,4,5,2,120,0.3,15)
OR2_Phone_charger.windows([870,1320],[240,360],0.35)
OR2_balcony_LED = OR2.Appliance(OR2,1,9,2,30,0.15,5)
OR2_balcony_LED.windows([1080,1320],[240,360],0.1)
OR2_WaterPurifier = OR2.Appliance(OR2,1,50,2,60,0.15,15)
OR2_WaterPurifier.windows([870,1320],[240,360],0.3)
OR2_MosquitoRepellent = OR2.Appliance(OR2,1,7,2,480,0.15,30)
OR2_MosquitoRepellent.windows([1200,1440],[0,360],0.35)
OR2_Laptop=OR2.Appliance(OR2,1,50,1,180,0.25,30)
OR2_Laptop.windows([900,1260],[0,0], 0.15)

#One-Room Minimum Connected Load
#Create new user classes
OR3 = User("One room minimal",3,1)
User_list.append(OR3)

#One-Room Minimum Connected Load
OR3_indoor_Tubelight1 = OR3.Appliance(OR3,1,55,2,420,0.15,15)
OR3_indoor_Tubelight1.windows([1020,1320],[240,330],0.1)
OR3_lavatory_LEDBulb = OR3.Appliance(OR3,1,5,1,60,0.2,15)
OR3_lavatory_LEDBulb.windows([870,1440],[0,360],0.1)
OR3_Phone_charger = OR3.Appliance(OR3,4,5,2,120,0.3,15)
OR3_Phone_charger.windows([870,1320],[240,360],0.35)
OR3_TV=OR3.Appliance(OR3,1,60,2,180,0.2,30)
OR3_TV.windows([900,1199],[1201,1320], 0.15)
OR3_SetTopBox = OR3.Appliance(OR3,1,10,2,210,0.15,15)
OR3_SetTopBox.windows([900,1199],[1201,1320],0.3)
OR3_MosquitoRepellent = OR3.Appliance(OR3,1,7,2,480,0.15,30)
OR3_MosquitoRepellent.windows([1200,1440],[0,360],0.35)


#One-Room Minimum Connected Load
#Create new user classes
OR4 = User("One room minimal",2,1)
User_list.append(OR4)

#One-Room Minimum Connected Load
OR4_indoor_Tubelight1 = OR4.Appliance(OR4,1,55,2,420,0.15,15)
OR4_indoor_Tubelight1.windows([1020,1320],[240,330],0.1)
OR4_lavatory_LEDBulb = OR4.Appliance(OR4,1,5,1,60,0.2,15)
OR4_lavatory_LEDBulb.windows([870,1440],[0,360],0.1)
OR4_Phone_charger = OR4.Appliance(OR4,4,5,2,120,0.3,15)
OR4_Phone_charger.windows([870,1320],[240,360],0.35)
OR4_MosquitoRepellent = OR4.Appliance(OR4,1,7,2,480,0.15,30)
OR4_MosquitoRepellent.windows([1200,1440],[0,360],0.35)
OR4_InductionCooktop = OR4.Appliance(OR4,1,1500,3,150,0.1,15)
OR4_InductionCooktop.windows([900,960],[1140,1260],0.15, [240,360])


#One-Room Minimum Connected Load
#Create new user classes
OR5 = User("One room minimal",3,1)
User_list.append(OR5)

#One-Room Minimum Connected Load
OR5_indoor_LEDlight1 = OR5.Appliance(OR5,1,7,2,420,0.15,15)
OR5_indoor_LEDlight1.windows([1020,1320],[240,330],0.1)
OR5_lavatory_LEDBulb = OR5.Appliance(OR5,1,5,1,60,0.2,15)
OR5_lavatory_LEDBulb.windows([870,1440],[0,360],0.1)
OR5_Phone_charger = OR5.Appliance(OR5,4,5,2,120,0.3,15)
OR5_MosquitoRepellent = OR5.Appliance(OR5,1,7,2,480,0.15,30)
OR5_MosquitoRepellent.windows([1200,1440],[0,360],0.35)
