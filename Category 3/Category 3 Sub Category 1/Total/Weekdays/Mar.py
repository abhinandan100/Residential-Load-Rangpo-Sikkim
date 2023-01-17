#One-Room Minimum Connected Load
#Create new user classes
OR = User("Case1",1,1)
User_list.append(OR)
OR1 = User("Case2",3,1)
User_list.append(OR1)
OR2 = User("Case3",1,1)
User_list.append(OR2)
OR3 = User("Case4",3,1)
User_list.append(OR3)
OR4 = User("Case5",2,1)
User_list.append(OR4)
OR5 = User("Case6",2,1)
User_list.append(OR5)

#CASE1
OR_indoor_Tubelight1 = OR.Appliance(OR,1,55,2,420,0.15,15)
OR_indoor_Tubelight1.windows([1080,1440],[300,420],0.1)
OR_indoor_Tubelight2 = OR.Appliance(OR,1,55,2,120,0.15,15, occasional_use = 0.5)
OR_indoor_Tubelight2.windows([1080,1440],[300,420],0.3)
OR_indoor_Tubelight3 = OR.Appliance(OR,1,55,2,420,0.15,1)
OR_indoor_Tubelight3.windows([1080,1440],[300,420],0.1)
OR_indoor_Tubelight4 = OR.Appliance(OR,1,55,2,120,0.15,15, occasional_use = 0.5)
OR_indoor_Tubelight4.windows([1080,1440],[300,420],0.3)
OR_indoor_Tubelight5 = OR.Appliance(OR,1,55,2,420,0.15,1, occasional_use = 0.75)
OR_indoor_Tubelight5.windows([1080,1440],[300,420],0.1)
OR_indoor_Tubelight6 = OR.Appliance(OR,1,55,2,120,0.15,15, occasional_use = 0.5)
OR_indoor_Tubelight6.windows([1080,1440],[300,420],0.3)
OR_lavatory_Tubelight = OR.Appliance(OR,1,55,2,45,0.2,5)
OR_lavatory_Tubelight.windows([1080,1440],[300,540],0.1)
OR_lavatory_Tubelight1 = OR.Appliance(OR,1,55,2,30,0.2,5)
OR_lavatory_Tubelight1.windows([1080,1440],[300,540],0.1)
OR_Phone_charger = OR.Appliance(OR,4,5,2,120,0.3,15)
OR_Phone_charger.windows([1080,1440],[300,480],0.35)
OR_TV=OR.Appliance(OR,2,60,2,180,0.2,30)
OR_TV.windows([1080,1199],[1201,1440], 0.15)
OR_GameConsole = OR.Appliance(OR,1,120,2,120,0.15,15, occasional_use = 0.5)
OR_GameConsole.windows([1080,1440],[300,420],0.3)
OR_KitchenTubelight=OR.Appliance(OR,1,40,2,180,0.15,15)
OR_KitchenTubelight.windows([1140,1380],[360,540],0.2)
OR_KitchenExhaustFan=OR.Appliance(OR,1,40,2,180,0.15,15)
OR_KitchenExhaustFan.windows([1140,1380],[420,540],0.2)
OR_balcony_LED = OR.Appliance(OR,1,9,2,30,0.15,5)
OR_balcony_LED.windows([1080,1159],[1201,1440],0.1)
OR_laptop = OR.Appliance(OR,1,50,2,60,0.15,30,occasional_use = 0.33)
OR_laptop.windows([1080,1440],[300,540],0.1)
OR_hairtrimmercharger = OR.Appliance(OR,1,5,2,30,0.15,15,occasional_use = 0.2)
OR_hairtrimmercharger.windows([300,480],[0,0],0.1)
OR_WashingMachine=OR.Appliance(OR,1,600,2,30,0.2,30, occasional_use=0.5)
OR_WashingMachine.windows([1080,1380],[360,540], 0.15)
OR_VacuumCleaner=OR.Appliance(OR,1,1000,2,30,0.2,30, occasional_use=0.5)
OR_VacuumCleaner.windows([360,540],[0,0], 0.15)
OR_MicroWaveOven=OR.Appliance(OR,1,1200,2,60,0.2,15, occasional_use=0.5)
OR_MicroWaveOven.windows([1080,1320],[360,540], 0.15)
OR_OvenToasterGriller=OR.Appliance(OR,1,1200,2,60,0.2,15, occasional_use=0.5)
OR_OvenToasterGriller.windows([1080,1320],[360,540], 0.15)
OR_Fridge = OR.Appliance(OR,2,200,1,1440,0,45, 'yes',1)
OR_Fridge.windows([0,1440],[0,0])
OR_Fridge.specific_cycle_1(5,45,200,45)
OR_Fridge.cycle_behaviour([0,720],[721,1440])
OR_MixerGrinder = OR.Appliance(OR,1,500,2,60,0.15,15,occasional_use = 0.33)
OR_MixerGrinder.windows([1080,1320],[360,540],0.3)
OR_WaterPurifier = OR.Appliance(OR,1,60,2,60,0.15,15)
OR_WaterPurifier.windows([1080,1380],[360,540],0.3)
OR_Iron = OR.Appliance(OR,1,1200,2,30,0.15,15, occasional_use=0.5)
OR_Iron.windows([1080,1320],[360,540],0.3)
OR_MusicSystem = OR.Appliance(OR,1,200,1,60,0.15,15, occasional_use=0.25)
OR_MusicSystem.windows([1080,1380],[0,0],0.3)
OR_InkjetPrinter = OR.Appliance(OR,1,30,1,30,0.15,15, occasional_use=0.1)
OR_InkjetPrinter.windows([1080,1380],[0,0],0.3)
OR_WaterPump = OR.Appliance(OR,1,500,2,30,0.15,15)
OR_WaterPump.windows([360,540],[1080,1140],0.3)
OR_SetTopBox = OR.Appliance(OR,1,10,2,210,0.15,15)
OR_SetTopBox.windows([1080,1199],[1201,1440],0.3)
OR_MosquitoRepellent = OR.Appliance(OR,1,7,2,480,0.15,30)
OR_MosquitoRepellent.windows([1200,1440],[0,360],0.35)
OR_MosquitoRepellent1 = OR.Appliance(OR,1,7,2,480,0.15,30, occasional_use=0.5)
OR_MosquitoRepellent1.windows([1080,1440],[0,0],0.35)
OR_InductionCooktop = OR.Appliance(OR,1,2000,3,150,0.1,15, 'yes',1)
OR_InductionCooktop.windows([1110,1170],[1230,1350],0.15, [360,480])
OR_InductionCooktop.specific_cycle_1(500,15,2000,15)
OR_InductionCooktop.cycle_behaviour([1080,1320],[360,480])
OR_BathroomGeyser = OR.Appliance(OR,1,2000,2,60,0.1,15, 'yes',1, occasional_use=.5)
OR_BathroomGeyser.windows([1080,1140],[360,540],0.1)
OR_BathroomGeyser.specific_cycle_1(2000,10,10,5)
OR_BathroomGeyser.cycle_behaviour([1080,1140],[360,540])


#CASE2
OR1_indoor_LEDBulb = OR1.Appliance(OR1,1,7,2,300,0.15,15)
OR1_indoor_LEDBulb.windows([1080,1440],[0,0],0.1)
OR1_indoor_LEDBulb1 = OR1.Appliance(OR1,1,7,2,360,0.15,15,occasional_use=0.5)
OR1_indoor_LEDBulb1.windows([1080,1440],[0,0],0.1)
OR1_indoor_LEDBulb2 = OR1.Appliance(OR1,1,7,2,360,0.15,15,occasional_use=0.5)
OR1_indoor_LEDBulb2.windows([1080,1440],[0,0],0.1)
OR1_lavatory_LEDBulb = OR1.Appliance(OR1,1,5,2,45,0.2,5)
OR1_lavatory_LEDBulb.windows([1080,1440],[360,540],0.1)
OR1_Phone_charger = OR1.Appliance(OR1,2,5,2,180,0.3,15)
OR1_Phone_charger.windows([1080,1440],[360,540],0.35)
OR1_KitchenLED=OR1.Appliance(OR1,1,7,2,180,0.15,15)
OR1_KitchenLED.windows([1080,1380],[360,540],0.2)
OR1_KitchenExhaustFan=OR1.Appliance(OR1,1,40,2,180,0.15,15)
OR1_KitchenExhaustFan.windows([1140,1380],[420,540],0.2)
OR1_TV=OR1.Appliance(OR1,1,60,2,180,0.2,30)
OR1_TV.windows([1080,1199],[1201,1440], 0.15)
OR1_SetTopBox = OR1.Appliance(OR1,1,10,2,210,0.15,15)
OR1_SetTopBox.windows([1080,1199],[1201,1440],0.3)
OR1_MosquitoRepellent = OR1.Appliance(OR1,2,7,2,480,0.15,30)
OR1_MosquitoRepellent.windows([1200,1440],[0,360],0.35)
OR1_Fridge = OR1.Appliance(OR1,1,200,1,1440,0,45, 'yes',1)
OR1_Fridge.windows([0,1440],[0,0])
OR1_Fridge.specific_cycle_1(5,45,200,45)
OR1_Fridge.cycle_behaviour([0,1440],[0,0])

#CASE3
OR2_indoor_Tubelight1 = OR2.Appliance(OR2,1,55,2,420,0.15,15)
OR2_indoor_Tubelight1.windows([1080,1440],[300,420],0.1)
OR2_indoor_Tubelight2 = OR2.Appliance(OR2,1,55,2,120,0.15,15, occasional_use = 0.5)
OR2_indoor_Tubelight2.windows([1080,1440],[300,420],0.3)
OR2_indoor_Tubelight3 = OR2.Appliance(OR2,1,55,2,420,0.15,1)
OR2_indoor_Tubelight3.windows([1080,1440],[300,420],0.1)
OR2_indoor_Tubelight4 = OR2.Appliance(OR2,1,55,2,120,0.15,15, occasional_use = 0.5)
OR2_indoor_Tubelight4.windows([1080,1440],[300,420],0.3)
OR2_indoor_Tubelight5 = OR2.Appliance(OR2,1,55,2,420,0.15,1, occasional_use = 0.75)
OR2_indoor_Tubelight5.windows([1080,1440],[300,420],0.1)
OR2_indoor_Tubelight6 = OR2.Appliance(OR2,1,55,2,120,0.15,15, occasional_use = 0.5)
OR2_indoor_Tubelight6.windows([1080,1440],[300,420],0.3)
OR2_lavatory_Tubelight = OR2.Appliance(OR2,1,55,2,45,0.2,5)
OR2_lavatory_Tubelight.windows([1080,1440],[300,540],0.1)
OR2_lavatory_Tubelight1 = OR2.Appliance(OR2,1,55,2,30,0.2,5)
OR2_lavatory_Tubelight1.windows([1080,1440],[300,540],0.1)
OR2_Phone_charger = OR2.Appliance(OR2,2,5,2,120,0.3,15)
OR2_Phone_charger.windows([1080,1440],[300,480],0.35)
OR2_TV=OR.Appliance(OR2,2,60,2,180,0.2,30)
OR2_TV.windows([1080,1199],[1201,1440], 0.15)
OR2_KitchenTubelight=OR2.Appliance(OR2,1,40,2,180,0.15,15)
OR2_KitchenTubelight.windows([1140,1380],[360,540],0.2)
OR2_KitchenExhaustFan=OR2.Appliance(OR2,1,40,2,180,0.15,15)
OR2_KitchenExhaustFan.windows([1140,1380],[420,540],0.2)
OR2_balcony_LED = OR2.Appliance(OR2,2,9,2,30,0.15,5)
OR2_balcony_LED.windows([1080,1159],[1201,1440],0.1)
OR2_laptop = OR2.Appliance(OR2,1,50,2,60,0.15,30,occasional_use = 0.33)
OR2_laptop.windows([1080,1440],[300,540],0.1)
OR2_WashingMachine=OR2.Appliance(OR2,1,600,2,30,0.2,30, occasional_use=0.5)
OR2_WashingMachine.windows([1080,1380],[360,540], 0.15)
OR2_VacuumCleaner=OR2.Appliance(OR2,1,1000,2,30,0.2,30, occasional_use=0.5)
OR2_VacuumCleaner.windows([360,540],[0,0], 0.15)
OR2_MicroWaveOven=OR2.Appliance(OR2,1,1200,2,60,0.2,15, occasional_use=0.5)
OR2_MicroWaveOven.windows([1080,1320],[360,540], 0.15)
OR2_Fridge = OR2.Appliance(OR2,2,200,1,1440,0,45, 'yes',1)
OR2_Fridge.windows([0,1440],[0,0])
OR2_Fridge.specific_cycle_1(5,45,200,45)
OR2_Fridge.cycle_behaviour([0,720],[721,1440])
OR2_MixerGrinder = OR2.Appliance(OR2,1,500,2,60,0.15,15,occasional_use = 0.33)
OR2_MixerGrinder.windows([1080,1320],[360,540],0.3)
OR2_WaterPurifier = OR2.Appliance(OR2,1,60,2,60,0.15,15)
OR2_WaterPurifier.windows([1080,1380],[360,540],0.3)
OR2_Iron = OR2.Appliance(OR2,1,1200,2,30,0.15,15, occasional_use=0.5)
OR2_Iron.windows([1080,1320],[360,540],0.3)
OR2_SetTopBox = OR2.Appliance(OR2,1,10,2,210,0.15,15)
OR2_SetTopBox.windows([1080,1199],[1201,1440],0.3)
OR2_MosquitoRepellent = OR2.Appliance(OR2,1,7,2,480,0.15,30)
OR2_MosquitoRepellent.windows([1200,1440],[0,360],0.35)
OR2_MosquitoRepellent1 = OR2.Appliance(OR2,1,7,2,480,0.15,30, occasional_use=0.5)
OR2_MosquitoRepellent1.windows([1080,1440],[0,0],0.35)
OR2_BathroomGeyser = OR2.Appliance(OR2,1,2000,2,60,0.1,15, 'yes',1, occasional_use=.5)
OR2_BathroomGeyser.windows([1080,1140],[360,540],0.1)
OR2_BathroomGeyser.specific_cycle_1(2000,10,10,5)
OR2_BathroomGeyser.cycle_behaviour([1080,1140],[360,540])
OR2_ElectricKettle = OR2.Appliance(OR2,1,1200,2,20,0.15,15)
OR2_ElectricKettle.windows([1080,1320],[360,540],0.3)
OR2_Toaster = OR2.Appliance(OR2,1,550,2,20,0.15,15, occasional_use=0.33)
OR2_Toaster.windows([1080,1320],[360,540],0.3)

#CASE4
OR3_indoor_Tubelight1 = OR3.Appliance(OR3,1,55,2,420,0.15,15)
OR3_indoor_Tubelight1.windows([1080,1440],[300,420],0.1)
OR3_indoor_Tubelight2 = OR3.Appliance(OR3,1,55,2,120,0.15,15, occasional_use = 0.5)
OR3_indoor_Tubelight2.windows([1080,1440],[300,420],0.3)
OR3_indoor_Tubelight3 = OR3.Appliance(OR3,1,55,2,420,0.15,1)
OR3_indoor_Tubelight3.windows([1080,1440],[300,420],0.1)
OR3_indoor_Tubelight4 = OR3.Appliance(OR3,1,55,2,120,0.15,15, occasional_use = 0.5)
OR3_indoor_Tubelight4.windows([1080,1440],[300,420],0.3)
OR3_indoor_Tubelight5 = OR3.Appliance(OR3,1,55,2,420,0.15,1, occasional_use = 0.75)
OR3_indoor_Tubelight5.windows([1080,1440],[300,420],0.1)
OR3_indoor_Tubelight6 = OR3.Appliance(OR3,1,55,2,120,0.15,15, occasional_use = 0.5)
OR3_indoor_Tubelight6.windows([1080,1440],[300,420],0.3)
OR3_lavatory_Tubelight = OR3.Appliance(OR3,1,55,2,45,0.2,5)
OR3_lavatory_Tubelight.windows([1080,1440],[300,540],0.1)
OR3_lavatory_Tubelight1 = OR3.Appliance(OR3,1,55,2,30,0.2,5)
OR3_lavatory_Tubelight1.windows([1080,1440],[300,540],0.1)
OR3_Phone_charger = OR3.Appliance(OR3,2,5,2,120,0.3,15)
OR3_Phone_charger.windows([1080,1440],[300,480],0.35)
OR3_TV=OR.Appliance(OR3,1,60,2,180,0.2,30)
OR3_TV.windows([1080,1199],[1201,1440], 0.15)
OR3_KitchenTubelight=OR3.Appliance(OR3,1,40,2,180,0.15,15)
OR3_KitchenTubelight.windows([1140,1380],[360,540],0.2)
OR3_KitchenExhaustFan=OR3.Appliance(OR3,1,40,2,180,0.15,15)
OR3_KitchenExhaustFan.windows([1140,1380],[420,540],0.2)
OR3_balcony_LED = OR3.Appliance(OR3,2,9,2,30,0.15,5)
OR3_balcony_LED.windows([1080,1159],[1201,1440],0.1)
OR3_WashingMachine=OR3.Appliance(OR3,1,600,2,30,0.2,30, occasional_use=0.5)
OR3_WashingMachine.windows([1080,1380],[360,540], 0.15)
OR3_MicroWaveOven=OR3.Appliance(OR3,1,1200,2,60,0.2,15, occasional_use=0.5)
OR3_MicroWaveOven.windows([1080,1320],[360,540], 0.15)
OR3_Fridge = OR3.Appliance(OR3,1,200,1,1440,0,45, 'yes',1)
OR3_Fridge.windows([0,1440],[0,0])
OR3_Fridge.specific_cycle_1(5,45,200,45)
OR3_Fridge.cycle_behaviour([0,720],[721,1440])
OR3_MixerGrinder = OR3.Appliance(OR3,1,500,2,60,0.15,15,occasional_use = 0.33)
OR3_MixerGrinder.windows([1080,1320],[360,540],0.3)
OR3_WaterPurifier = OR3.Appliance(OR3,1,60,2,60,0.15,15)
OR3_WaterPurifier.windows([1080,1380],[360,540],0.3)
OR3_Iron = OR3.Appliance(OR3,1,1200,2,30,0.15,15, occasional_use=0.5)
OR3_Iron.windows([1080,1320],[360,540],0.3)
OR3_SetTopBox = OR3.Appliance(OR3,1,10,2,210,0.15,15)
OR3_SetTopBox.windows([1080,1199],[1201,1440],0.3)
OR3_MosquitoRepellent = OR3.Appliance(OR3,1,7,2,480,0.15,30)
OR3_MosquitoRepellent.windows([1200,1440],[0,360],0.35)
OR3_MosquitoRepellent1 = OR3.Appliance(OR3,1,7,2,480,0.15,30, occasional_use=0.5)
OR3_MosquitoRepellent1.windows([1080,1440],[0,0],0.35)

#CASE5
OR4_indoor_Tubelight1 = OR4.Appliance(OR4,1,55,2,420,0.15,15)
OR4_indoor_Tubelight1.windows([1080,1440],[300,420],0.1)
OR4_indoor_Tubelight2 = OR4.Appliance(OR4,1,55,2,120,0.15,15, occasional_use = 0.5)
OR4_indoor_Tubelight2.windows([1080,1440],[300,420],0.3)
OR4_indoor_Tubelight3 = OR4.Appliance(OR4,1,55,2,420,0.15,1)
OR4_indoor_Tubelight3.windows([1080,1440],[300,420],0.1)
OR4_indoor_Tubelight4 = OR4.Appliance(OR4,1,55,2,120,0.15,15, occasional_use = 0.5)
OR4_indoor_Tubelight4.windows([1080,1440],[300,420],0.3)
OR4_indoor_Tubelight5 = OR4.Appliance(OR4,1,55,2,420,0.15,1, occasional_use = 0.75)
OR4_indoor_Tubelight5.windows([1080,1440],[300,420],0.1)
OR4_indoor_Tubelight6 = OR4.Appliance(OR4,1,55,2,120,0.15,15, occasional_use = 0.5)
OR4_indoor_Tubelight6.windows([1080,1440],[300,420],0.3)
OR4_lavatory_LEDBulb = OR4.Appliance(OR4,1,5,2,45,0.2,5)
OR4_lavatory_LEDBulb.windows([1080,1440],[360,540],0.1)
OR4_lavatory_LEDBulb1 = OR4.Appliance(OR4,1,5,2,45,0.2,5)
OR4_lavatory_LEDBulb1.windows([1080,1440],[360,540],0.1)
OR4_Phone_charger = OR4.Appliance(OR4,2,5,2,120,0.3,15)
OR4_Phone_charger.windows([1080,1440],[300,480],0.35)
OR4_TV=OR.Appliance(OR4,1,60,2,180,0.2,30)
OR4_TV.windows([1080,1199],[1201,1440], 0.15)
OR4_KitchenTubelight=OR4.Appliance(OR4,1,40,2,180,0.15,15)
OR4_KitchenTubelight.windows([1140,1380],[360,540],0.2)
OR4_KitchenExhaustFan=OR4.Appliance(OR4,1,40,2,180,0.15,15)
OR4_KitchenExhaustFan.windows([1140,1380],[420,540],0.2)
OR4_WashingMachine=OR4.Appliance(OR4,1,600,2,30,0.2,30, occasional_use=0.5)
OR4_WashingMachine.windows([1080,1380],[360,540], 0.15)
OR4_Fridge = OR4.Appliance(OR4,1,200,1,1440,0,45, 'yes',1)
OR4_Fridge.windows([0,1440],[0,0])
OR4_Fridge.specific_cycle_1(5,45,200,45)
OR4_Fridge.cycle_behaviour([0,720],[721,1440])
OR4_MixerGrinder = OR4.Appliance(OR4,1,500,2,60,0.15,15,occasional_use = 0.33)
OR4_MixerGrinder.windows([1080,1320],[360,540],0.3)
OR4_WaterPurifier = OR4.Appliance(OR4,1,60,2,60,0.15,15)
OR4_WaterPurifier.windows([1080,1380],[360,540],0.3)
OR4_Iron = OR4.Appliance(OR4,1,1200,2,30,0.15,15, occasional_use=0.5)
OR4_Iron.windows([1080,1320],[360,540],0.3)
OR4_SetTopBox = OR4.Appliance(OR4,1,10,2,210,0.15,15)
OR4_SetTopBox.windows([1080,1199],[1201,1440],0.3)
OR4_MosquitoRepellent = OR4.Appliance(OR4,2,7,2,480,0.15,30)
OR4_MosquitoRepellent.windows([1200,1440],[0,360],0.35)
OR4_Desktopcomputer = OR4.Appliance(OR4,1,120,2,60,0.15,30,occasional_use = 0.33)
OR4_Desktopcomputer.windows([1080,1440],[300,540],0.1)

#CASE6
OR5_indoor_Tubelight1 = OR5.Appliance(OR5,1,55,2,420,0.15,15)
OR5_indoor_Tubelight1.windows([1080,1440],[300,420],0.1)
OR5_indoor_Tubelight2 = OR5.Appliance(OR5,1,55,2,120,0.15,15, occasional_use = 0.5)
OR5_indoor_Tubelight2.windows([1080,1440],[300,420],0.3)
OR5_indoor_Tubelight3 = OR5.Appliance(OR5,1,55,2,420,0.15,1)
OR5_indoor_Tubelight3.windows([1080,1440],[300,420],0.1)
OR5_indoor_Tubelight4 = OR5.Appliance(OR5,1,55,2,120,0.15,15, occasional_use = 0.5)
OR5_indoor_Tubelight4.windows([1080,1440],[300,420],0.3)
OR5_indoor_LEDBulb = OR5.Appliance(OR5,1,7,2,420,0.15,1, occasional_use = 0.75)
OR5_indoor_LEDBulb.windows([1080,1440],[300,420],0.1)
OR5_lavatory_LEDBulb = OR5.Appliance(OR5,1,5,2,45,0.2,5)
OR5_lavatory_LEDBulb.windows([1080,1440],[360,540],0.1)
OR5_Phone_charger = OR5.Appliance(OR5,2,5,2,120,0.3,15)
OR5_Phone_charger.windows([1080,1440],[300,480],0.35)
OR5_TV=OR.Appliance(OR5,1,60,2,180,0.2,30)
OR5_TV.windows([1080,1199],[1201,1440], 0.15)
OR5_KitchenTubelight=OR5.Appliance(OR5,1,40,2,180,0.15,15)
OR5_KitchenTubelight.windows([1140,1380],[360,540],0.2)
OR5_KitchenExhaustFan=OR5.Appliance(OR5,1,40,2,180,0.15,15)
OR5_KitchenExhaustFan.windows([1140,1380],[420,540],0.2)
OR5_WashingMachine=OR5.Appliance(OR5,1,600,2,30,0.2,30, occasional_use=0.5)
OR5_WashingMachine.windows([1080,1380],[360,540], 0.15)
OR5_Fridge = OR5.Appliance(OR5,1,200,1,1440,0,45, 'yes',1)
OR5_Fridge.windows([0,1440],[0,0])
OR5_Fridge.specific_cycle_1(5,45,200,45)
OR5_Fridge.cycle_behaviour([0,720],[721,1440])
OR5_MixerGrinder = OR5.Appliance(OR5,1,500,2,60,0.15,15,occasional_use = 0.33)
OR5_MixerGrinder.windows([1080,1320],[360,540],0.3)
OR5_WaterPurifier = OR5.Appliance(OR5,1,60,2,60,0.15,15)
OR5_WaterPurifier.windows([1080,1380],[360,540],0.3)
OR5_Iron = OR5.Appliance(OR5,1,1200,2,30,0.15,15, occasional_use=0.5)
OR5_Iron.windows([1080,1320],[360,540],0.3)
OR5_SetTopBox = OR5.Appliance(OR5,1,10,2,210,0.15,15)
OR5_SetTopBox.windows([1080,1199],[1201,1440],0.3)
OR5_MosquitoRepellent = OR5.Appliance(OR5,2,7,2,480,0.15,30)
OR5_MosquitoRepellent.windows([1200,1440],[0,360],0.35)



