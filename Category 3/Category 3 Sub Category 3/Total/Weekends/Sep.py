#One-Room Minimum Connected Load
OR = User("Case1",2,1)
User_list.append(OR)
#One-Room Minimum Connected Load
OR_indoor_Tubelight1 = OR.Appliance(OR,1,55,2,420,0.15,15, occasional_use = 0.5)
OR_indoor_Tubelight1.windows([1080,1440],[300,420],0.1)
OR_indoor_Tubelight2 = OR.Appliance(OR,1,55,2,120,0.15,15, occasional_use = 0.25)
OR_indoor_Tubelight2.windows([1080,1440],[300,420],0.3)
OR_indoor_Tubelight3 = OR.Appliance(OR,1,55,2,420,0.15,15, occasional_use = 0.5)
OR_indoor_Tubelight3.windows([1080,1440],[300,420],0.1)
OR_indoor_Tubelight4 = OR.Appliance(OR,1,55,2,420,0.15,15, occasional_use = 0.25)
OR_indoor_Tubelight4.windows([1080,1440],[300,420],0.1)
OR_indoor_Tubelight5 = OR.Appliance(OR,1,55,2,120,0.15,15, occasional_use = 0.5)
OR_indoor_Tubelight5.windows([1080,1440],[300,420],0.3)
OR_indoor_Tubelight6 = OR.Appliance(OR,1,55,2,420,0.15,15, occasional_use = 0.25)
OR_indoor_Tubelight6.windows([1080,1440],[300,420],0.1)
OR_lavatory_Tubelight = OR.Appliance(OR,1,55,2,45,0.2,5,occasional_use = 0.5)
OR_lavatory_Tubelight.windows([0,1440],[0,0],0.1)
OR_lavatory_Tubelight1 = OR.Appliance(OR,1,55,2,30,0.2,5,occasional_use = 0.5)
OR_lavatory_Tubelight1.windows([0,1440],[0,0],0.1)
OR_Phone_charger = OR.Appliance(OR,4,5,1,180,0.3,15, occasional_use = 0.5)
OR_Phone_charger.windows([0,1440],[0,0],0.35)
OR_Fan = OR.Appliance(OR,1,70, 2, 720,0.15, occasional_use=0.5)
OR_Fan.windows([480,1440],[0,0],0.2)
OR_Fan1 = OR.Appliance(OR,1,70, 2, 720,0.15,15,occasional_use=0.25)
OR_Fan1.windows([0,1440],[0,0],0.2)
OR_Fan2 = OR.Appliance(OR,1,70, 2, 720,0.15,15,occasional_use=0.25)
OR_Fan2.windows([0,1440],[0,0],0.2)
OR_TV=OR.Appliance(OR,2,60,2,360,0.2,30,occasional_use = 0.5)
OR_TV.windows([540,1440],[0,0], 0.35)
OR_KitchenTubelight=OR.Appliance(OR,1,40,3,300,0.15,15,occasional_use = 0.5)
OR_KitchenTubelight.windows([1140,1380],[420,600],0.25,[720,900])
OR_KitchenExhaustFan=OR.Appliance(OR,1,40,2,180,0.15,15,occasional_use = 0.5)
OR_KitchenExhaustFan.windows([1140,1380],[420,600],0.2,[720,900])
OR_balcony_LED = OR.Appliance(OR,1,9,2,30,0.15,5, occasional_use = 0.5)
OR_balcony_LED.windows([1080,1159],[1201,1440],0.1)
OR_laptop = OR.Appliance(OR,1,50,1,240,0.15,30,occasional_use = 0.15)
OR_laptop.windows([540,1440],[0,0],0.1)
OR_GameConsole = OR.Appliance(OR,1,120,2,360,0.15,15, occasional_use = 0.5)
OR_GameConsole.windows([540,1440],[0,0],0.3)
OR_hairtrimmercharger = OR.Appliance(OR,1,5,2,30,0.15,15,occasional_use = 0.1)
OR_hairtrimmercharger.windows([300,480],[0,0],0.1)
OR_hairdrier = OR.Appliance(OR,1,800,2,30,0.15,15,occasional_use = 0.25)
OR_hairdrier.windows([480,600],[601,900],0.1)
OR_Fridge = OR.Appliance(OR,1,200,1,1440,0,45, 'yes',1)
OR_Fridge.windows([0,1440],[0,0])
OR_Fridge.specific_cycle_1(5,45,200,45)
OR_Fridge.cycle_behaviour([0,720],[721,1440])
OR_WashingMachine=OR.Appliance(OR,1,600,2,120,0.2,30, occasional_use=0.5)
OR_WashingMachine.windows([480,720],[0,0],0.25)
OR_VacuumCleaner=OR.Appliance(OR,1,1000,2,30,0.2,30, occasional_use=0.5)
OR_VacuumCleaner.windows([480,720],[0,0], 0.15)
OR_MicroWaveOven=OR.Appliance(OR,1,1200,3,60,0.2,15, occasional_use=0.5)
OR_MicroWaveOven.windows([1080,1320],[420,600], 0.15, [720,900])
OR_OvenToasterGriller=OR.Appliance(OR,1,1200,3,60,0.2,15, occasional_use=0.5)
OR_OvenToasterGriller.windows([1080,1320],[420,600], 0.15, [720,900])
OR_MixerGrinder = OR.Appliance(OR,1,500,2,60,0.15,15,occasional_use = 0.33)
OR_MixerGrinder.windows([1080,1320],[420,600],0.3, [720,900])
OR_WaterPurifier = OR.Appliance(OR,1,60,2,60,0.15,15)
OR_WaterPurifier.windows([1080,1380],[420,900],0.3)
OR_Iron = OR.Appliance(OR,1,1200,1,30,0.15,15, occasional_use=0.5)
OR_Iron.windows([900,1320],[0,0],0.3)
OR_MusicSystem = OR.Appliance(OR,1,200,1,60,0.15,15, occasional_use=0.25)
OR_MusicSystem.windows([1080,1380],[480,900],0.3)
OR_InkjetPrinter = OR.Appliance(OR,1,30,1,30,0.15,15, occasional_use=0.1)
OR_InkjetPrinter.windows([420,900],[0,0],0.3)
OR_WaterPump = OR.Appliance(OR,1,500,2,45,0.15,15,occasional_use=0.5)
OR_WaterPump.windows([360,540],[1080,1140],0.3, [720,900])
OR_SetTopBox = OR.Appliance(OR,1,10,2,360,0.2,30,occasional_use=0.5)
OR_SetTopBox.windows([540,1400],[0,0],0.35)
OR_MosquitoRepellent = OR.Appliance(OR,1,7,2,480,0.15,30,occasional_use=0.5)
OR_MosquitoRepellent.windows([1200,1440],[0,360],0.35)
OR_MosquitoRepellent1 = OR.Appliance(OR,1,7,2,480,0.15,30, occasional_use=0.5)
OR_MosquitoRepellent1.windows([1080,1440],[0,0],0.35)
OR_InductionCooktop = OR.Appliance(OR,1,2000,3,150,0.1,15, 'yes',1,occasional_use=0.5)
OR_InductionCooktop.windows([1110,1170],[1230,1350],0.15, [360,480])
OR_InductionCooktop.specific_cycle_1(500,15,2000,15)
OR_InductionCooktop.cycle_behaviour([1080,1320],[360,480])
OR_BathroomGeyser = OR.Appliance(OR,1,2000,2,60,0.1,15, 'yes',1,occasional_use=0.5)
OR_BathroomGeyser.windows([420,900],[0,0],0.1)
OR_BathroomGeyser.specific_cycle_1(2000,10,10,5)
OR_BathroomGeyser.cycle_behaviour([420,900],[0,0])
OR_AirConditioner = OR.Appliance(OR,1,500,2,600,0.1,15, 'yes',1, occasional_use=.25)
OR_AirConditioner.windows([480,1440],[0,0],0.1)
OR_AirConditioner.specific_cycle_1(500,15,10,45)
OR_AirConditioner.cycle_behaviour([480,1440],[0,0])
OR_Toaster = OR.Appliance(OR,1,550,2,20,0.15,15, occasional_use=0.5)
OR_Toaster.windows([1080,1320],[360,600],0.3)


#Create new user classes
OR1 = User("One room minimal",6,1)
User_list.append(OR1)
#One-Room Minimum Connected Load
OR1_indoor_LEDBulb1 = OR1.Appliance(OR1,1,7,2,420,0.15,15, occasional_use = 0.25)
OR1_indoor_LEDBulb1.windows([1080,1440],[300,420],0.1)
OR1_indoor_LEDBulb2 = OR1.Appliance(OR1,1,7,2,120,0.15,15, occasional_use=0.5)
OR1_indoor_LEDBulb2.windows([1080,1440],[300,420],0.3)
OR1_indoor_LEDBulb3 = OR1.Appliance(OR1,1,7,2,120,0.15,15,occasional_use=0.25)
OR1_indoor_LEDBulb3.windows([1080,1440],[300,420],0.3)
OR1_lavatory_LEDBulb = OR1.Appliance(OR1,1,5,2,60,0.2,5, occasional_use=0.5)
OR1_lavatory_LEDBulb.windows([360,1440],[0,0],0.1)
OR1_Fan = OR1.Appliance(OR1,1,30, 2, 720,0.15, occasional_use=0.5)
OR1_Fan.windows([480,1440],[0,0],0.2)
OR1_Fan1 = OR1.Appliance(OR1,1,30, 2, 720,0.15,15,occasional_use=0.5)
OR1_Fan1.windows([0,1440],[0,0],0.2)
OR1_Fan2 = OR1.Appliance(OR1,1,30, 2, 720,0.15,15,occasional_use=0.5)
OR1_Fan2.windows([0,1440],[0,0],0.2)
OR1_TV=OR1.Appliance(OR1,1,60,2,360,0.2,30)
OR1_TV.windows([540,1440],[0,0], 0.35)
OR1_SetTopBox = OR1.Appliance(OR1,1,10,2,360,0.2,30,occasional_use=0.5)
OR1_SetTopBox.windows([540,1400],[0,0],0.35)
OR1_KitchenLED=OR1.Appliance(OR1,1,7,3,300,0.15,15)
OR1_KitchenLED.windows([1140,1380],[360,540],0.25,[720,900])
OR1_KitchenExhaustFan=OR1.Appliance(OR1,1,40,2,180,0.15,15)
OR1_KitchenExhaustFan.windows([1140,1380],[360,540],0.2,[720,900])
OR1_Fridge = OR1.Appliance(OR1,1,200,1,1440,0,45, 'yes',1)
OR1_Fridge.windows([0,1440],[0,0])
OR1_Fridge.specific_cycle_1(5,45,200,45)
OR1_Fridge.cycle_behaviour([0,1440],[0,0])
OR1_MosquitoRepellent = OR1.Appliance(OR1,2,7,2,480,0.15,30, occasional_use=0.5)
OR1_MosquitoRepellent.windows([1200,1440],[0,360],0.35)
OR1_Phone_charger = OR1.Appliance(OR1,2,5,2,180,0.3,15)
OR1_Phone_charger.windows([0,1440],[0,0],0.35)
OR1_MixerGrinder = OR1.Appliance(OR1,1,500,2,60,0.15,15,occasional_use = 0.33)
OR1_MixerGrinder.windows([1080,1320],[420,600],0.3, [720,900])
OR1_WaterPurifier = OR1.Appliance(OR1,1,60,2,60,0.15,15)
OR1_WaterPurifier.windows([1080,1380],[420,900],0.3)




#One-Room Minimum Connected Load
OR2 = User("Case3",7,1)
User_list.append(OR2)
#One-Room Minimum Connected Load
OR2_indoor_Tubelight1 = OR2.Appliance(OR,1,55,2,420,0.15,15, occasional_use = 0.5)
OR2_indoor_Tubelight1.windows([1080,1440],[300,420],0.1)
OR2_indoor_Tubelight2 = OR2.Appliance(OR,1,55,2,120,0.15,15, occasional_use = 0.25)
OR2_indoor_Tubelight2.windows([1080,1440],[300,420],0.3)
OR2_indoor_Tubelight3 = OR2.Appliance(OR,1,55,2,420,0.15,15, occasional_use = 0.5)
OR2_indoor_Tubelight3.windows([1080,1440],[300,420],0.1)
OR2_indoor_Tubelight4 = OR2.Appliance(OR,1,55,2,420,0.15,15, occasional_use = 0.25)
OR2_indoor_Tubelight4.windows([1080,1440],[300,420],0.1)
OR2_indoor_Tubelight5 = OR2.Appliance(OR,1,55,2,120,0.15,15, occasional_use = 0.5)
OR2_indoor_Tubelight5.windows([1080,1440],[300,420],0.3)
OR2_indoor_Tubelight6 = OR2.Appliance(OR,1,55,2,420,0.15,15, occasional_use = 0.25)
OR2_indoor_Tubelight6.windows([1080,1440],[300,420],0.1)
OR2_lavatory_Tubelight = OR2.Appliance(OR,1,55,2,45,0.2,5,occasional_use = 0.5)
OR2_lavatory_Tubelight.windows([0,1440],[0,0],0.1)
OR2_lavatory_Tubelight1 = OR2.Appliance(OR,1,55,2,30,0.2,5,occasional_use = 0.5)
OR2_lavatory_Tubelight1.windows([0,1440],[0,0],0.1)
OR2_lavatory_ExhaustFan = OR2.Appliance(OR2,1,40,2,30,0.2,5, occasional_use=0.5)
OR2_lavatory_ExhaustFan.windows([0,1440],[0,0],0.1)
OR2_lavatory_ExhaustFan1 = OR2.Appliance(OR2,1,40,2,30,0.2,5, occasional_use=0.5)
OR2_lavatory_ExhaustFan1.windows([0,1440],[0,0],0.1)
OR2_Phone_charger = OR2.Appliance(OR2,3,5,2,180,0.3,15, occasional_use=0.5)
OR2_Phone_charger.windows([0,1440],[0,0],0.35)
OR2_Camera_charger = OR2.Appliance(OR2,2,5,2,180,0.3,15,occasional_use=0.25)
OR2_Camera_charger.windows([0,1440],[0,0],0.35)
OR2_Fan = OR2.Appliance(OR2,1,70, 2, 720,0.15, occasional_use=0.5)
OR2_Fan.windows([480,1440],[0,0],0.2)
OR2_Fan1 = OR2.Appliance(OR2,1,70, 2, 720,0.15,15,occasional_use=0.75)
OR2_Fan1.windows([0,1440],[0,0],0.2)
OR2_Fan2 = OR2.Appliance(OR2,1,70, 2, 720,0.15,15,occasional_use=0.75)
OR2_Fan2.windows([0,1440],[0,0],0.2)
OR2_TV=OR2.Appliance(OR2,1,60,2,360,0.2,30)
OR2_TV.windows([540,1440],[0,0], 0.35)
OR2_KitchenTubelight=OR2.Appliance(OR2,1,40,3,300,0.15,15)
OR2_KitchenTubelight.windows([1140,1380],[360,600],0.25,[720,900])
OR2_KitchenExhaustFan=OR2.Appliance(OR2,1,40,2,180,0.15,15)
OR2_KitchenExhaustFan.windows([1140,1380],[360,600],0.2,[720,900])
OR2_balcony_LED = OR2.Appliance(OR2,1,9,2,30,0.15,5)
OR2_balcony_LED.windows([1080,1159],[1201,1440],0.1)
OR2_DesktopComputer = OR2.Appliance(OR2,1,120,1,360,0.15,30, occasional_use = 0.75)
OR2_DesktopComputer.windows([480,1440],[0,0],0.1)
OR2_hairtrimmercharger = OR2.Appliance(OR2,1,5,2,30,0.15,15,occasional_use = 0.1)
OR2_hairtrimmercharger.windows([420,900],[0,0],0.1)
OR2_hairdrier = OR2.Appliance(OR2,1,800,2,30,0.15,15,occasional_use = 0.1)
OR2_hairdrier.windows([480,600],[601,900],0.1)
OR2_Fridge = OR2.Appliance(OR2,1,200,1,1440,0,45, 'yes',1)
OR2_Fridge.windows([0,1440],[0,0])
OR2_Fridge.specific_cycle_1(5,45,200,45)
OR2_Fridge.cycle_behaviour([0,1440],[0,0])
OR2_WashingMachine=OR2.Appliance(OR2,1,600,2,120,0.2,30, occasional_use=0.75)
OR2_WashingMachine.windows([420,840],[0,0],0.25)
OR2_VacuumCleaner=OR2.Appliance(OR2,1,1000,2,30,0.2,30, occasional_use=0.75)
OR2_VacuumCleaner.windows([480,720],[0,0], 0.15)
OR2_MicroWaveOven=OR2.Appliance(OR2,1,1200,3,60,0.2,15, occasional_use=0.75)
OR2_MicroWaveOven.windows([1080,1320],[420,600], 0.15, [720,900])
OR2_OTG=OR2.Appliance(OR2,1,1200,3,60,0.2,15, occasional_use=0.75)
OR2_OTG.windows([1080,1320],[420,600], 0.15, [720,900])
OR2_GameConsole = OR2.Appliance(OR2,1,120,2,120,0.15,15, occasional_use = 0.5)
OR2_GameConsole.windows([1080,1440],[600,1080],0.3)
OR2_MixerGrinder = OR2.Appliance(OR2,1,500,2,60,0.15,15,occasional_use = 0.33)
OR2_MixerGrinder.windows([1080,1320],[420,600],0.3, [720,900])
OR2_WaterPurifier = OR2.Appliance(OR2,1,60,2,60,0.15,15)
OR2_WaterPurifier.windows([1080,1380],[420,900],0.3)
OR2_Iron = OR2.Appliance(OR2,1,1200,1,30,0.15,15, occasional_use=0.5)
OR2_Iron.windows([900,1320],[0,0],0.3)
OR2_MusicSystem = OR2.Appliance(OR2,1,200,1,60,0.15,15, occasional_use=0.25)
OR2_MusicSystem.windows([1080,1380],[480,900],0.3)
OR2_InkjetPrinter = OR2.Appliance(OR2,1,30,1,30,0.15,15, occasional_use=0.1)
OR2_InkjetPrinter.windows([420,900],[0,0],0.3)
OR2_WaterPump = OR2.Appliance(OR2,1,500,2,45,0.15,15,occasional_use=0.5)
OR2_WaterPump.windows([360,540],[1080,1140],0.3, [720,900])
OR2_SetTopBox = OR2.Appliance(OR2,1,10,2,360,0.2,30,occasional_use=0.5)
OR2_SetTopBox.windows([540,1400],[0,0],0.35)
OR2_MosquitoRepellent = OR2.Appliance(OR2,1,7,2,480,0.15,30, occasional_use=0.5)
OR2_MosquitoRepellent.windows([1200,1440],[0,360],0.35)
OR2_MosquitoRepellent1 = OR2.Appliance(OR2,1,7,2,480,0.15,30, occasional_use=0.5)
OR2_MosquitoRepellent1.windows([1080,1440],[0,0],0.35)
OR2_BathroomGeyser = OR2.Appliance(OR2,1,2000,2,60,0.1,15, 'yes',1,occasional_use=0.5)
OR2_BathroomGeyser.windows([420,900],[0, 0],0.1)
OR2_BathroomGeyser.specific_cycle_1(2000,10,10,5)
OR2_BathroomGeyser.cycle_behaviour([420,900],[0,0])
OR2_Toaster = OR2.Appliance(OR2,1,550,2,20,0.15,15, occasional_use=0.5)
OR2_Toaster.windows([1080,1320],[360,600],0.3)


#One-Room Minimum Connected Load
OR3 = User("Case4",8,1)
User_list.append(OR3)
#One-Room Minimum Connected Load
OR3_indoor_Tubelight1 = OR3.Appliance(OR3,1,55,2,420,0.15,15, occasional_use = 0.5)
OR3_indoor_Tubelight1.windows([1080,1440],[300,420],0.1)
OR3_indoor_Tubelight2 = OR3.Appliance(OR3,1,55,2,120,0.15,15)
OR3_indoor_Tubelight2.windows([1080,1440],[300,420],0.3)
OR3_indoor_Tubelight3 = OR3.Appliance(OR3,1,55,2,420,0.15,15, occasional_use = 0.5)
OR3_indoor_Tubelight3.windows([1080,1440],[300,420],0.1)
OR3_indoor_Tubelight4 = OR3.Appliance(OR3,1,55,2,120,0.15,15)
OR3_indoor_Tubelight4.windows([1080,1440],[300,420],0.3)
OR3_indoor_Tubelight5 = OR3.Appliance(OR3,1,55,2,420,0.15,15, occasional_use = 0.5)
OR3_indoor_Tubelight5.windows([1080,1440],[300,420],0.1)
OR3_indoor_Tubelight6 = OR3.Appliance(OR3,1,55,2,120,0.15,15)
OR3_indoor_Tubelight6.windows([1080,1440],[300,420],0.3)
OR3_lavatory_LEDBulb = OR3.Appliance(OR3,1,5,2,60,0.2,5)
OR3_lavatory_LEDBulb.windows([541,1440],[360,540],0.1)
OR3_lavatory_LEDBulb1 = OR3.Appliance(OR3,1,5,2,60,0.2,5)
OR3_lavatory_LEDBulb1.windows([541,1440],[360,540],0.1)
OR3_Phone_charger = OR3.Appliance(OR3,2,5,2,180,0.3,15)
OR3_Phone_charger.windows([0,1440],[0,0],0.35)
OR3_Fan = OR3.Appliance(OR3,1,70, 2, 720,0.15)
OR3_Fan.windows([480,1440],[0,0],0.2)
OR3_Fan1 = OR3.Appliance(OR3,1,70, 2, 720,0.15,15,occasional_use=0.75)
OR3_Fan1.windows([0,1440],[0,0],0.2)
OR3_Fan2 = OR3.Appliance(OR3,1,70, 2, 720,0.15,15,occasional_use=0.75)
OR3_Fan2.windows([0,1440],[0,0],0.2)
OR3_TV=OR3.Appliance(OR3,1,60,2,480,0.2,30)
OR3_TV.windows([540,1440],[0,0], 0.35)
OR3_KitchenTubelight=OR3.Appliance(OR3,1,40,3,300,0.15,15)
OR3_KitchenTubelight.windows([1140,1380],[360,600],0.25,[720,900])
OR3_KitchenExhaustFan=OR3.Appliance(OR3,1,40,2,180,0.15,15)
OR3_KitchenExhaustFan.windows([1140,1380],[360,600],0.2,[720,900])
OR3_balcony_LED = OR3.Appliance(OR3,1,9,2,30,0.15,5)
OR3_balcony_LED.windows([1080,1159],[1201,1440],0.1)
OR3_laptop = OR3.Appliance(OR3,1,50,1,240,0.15,30, occasional_use = 0.75)
OR3_laptop.windows([480,1440],[0,0],0.1)
OR3_WifiRouter = OR3.Appliance(OR3,2,3,2,240,0.3,15)
OR3_WifiRouter.windows([480,1440],[0,0],0.35)
OR3_Fridge = OR3.Appliance(OR3,1,200,1,1440,0,45, 'yes',1)
OR3_Fridge.windows([0,1440],[0,0])
OR3_Fridge.specific_cycle_1(5,45,200,45)
OR3_Fridge.cycle_behaviour([0,1440],[0,0])
OR3_WashingMachine=OR3.Appliance(OR3,1,600,2,120,0.2,30, occasional_use=0.75)
OR3_WashingMachine.windows([420,840],[0,0],0.25)
OR3_VacuumCleaner=OR3.Appliance(OR3,1,1000,2,30,0.2,30, occasional_use=0.75)
OR3_VacuumCleaner.windows([480,720],[0,0], 0.15)
OR3_MicroWaveOven=OR3.Appliance(OR3,1,1200,3,60,0.2,15, occasional_use=0.75)
OR3_MicroWaveOven.windows([1080,1320],[420,600], 0.15, [720,900])
OR3_MixerGrinder = OR3.Appliance(OR3,1,500,2,60,0.15,15,occasional_use = 0.33)
OR3_MixerGrinder.windows([1080,1320],[420,600],0.3, [720,900])
OR3_WaterPurifier = OR3.Appliance(OR3,1,60,2,60,0.15,15)
OR3_WaterPurifier.windows([1080,1380],[420,900],0.3)
OR3_Iron = OR3.Appliance(OR3,1,1200,1,30,0.15,15, occasional_use=0.5)
OR3_Iron.windows([900,1320],[0,0],0.3)
OR3_MusicSystem = OR3.Appliance(OR3,1,200,1,60,0.15,15, occasional_use=0.25)
OR3_MusicSystem.windows([1080,1380],[480,900],0.3)
OR3_SetTopBox = OR3.Appliance(OR3,1,10,2,480,0.2,30,occasional_use=0.5)
OR3_SetTopBox.windows([540,1440],[0,0],0.35)
OR3_MosquitoRepellent = OR3.Appliance(OR3,2,7,2,480,0.15,30, occasional_use=0.5)
OR3_MosquitoRepellent.windows([1200,1440],[0,360],0.35)


#One-Room Minimum Connected Load
OR4 = User("Case5",8,1)
User_list.append(OR4)
#One-Room Minimum Connected Load
OR4_indoor_Tubelight1 = OR4.Appliance(OR4,1,55,2,420,0.15,15, occasional_use = 0.5)
OR4_indoor_Tubelight1.windows([1080,1440],[300,420],0.1)
OR4_indoor_Tubelight2 = OR4.Appliance(OR4,1,55,2,120,0.15,15)
OR4_indoor_Tubelight2.windows([1080,1440],[300,420],0.3)
OR4_indoor_Tubelight3 = OR4.Appliance(OR4,1,55,2,120,0.15,15)
OR4_indoor_Tubelight3.windows([1080,1440],[300,420],0.3)
OR4_lavatory_LEDBulb = OR4.Appliance(OR4,1,5,2,60,0.2,5)
OR4_lavatory_LEDBulb.windows([541,1440],[360,540],0.1)
OR4_Phone_charger = OR4.Appliance(OR4,2,5,2,180,0.3,15)
OR4_Phone_charger.windows([0,1440],[0,0],0.35)
OR4_Fan = OR4.Appliance(OR4,1,70, 2, 720,0.15)
OR4_Fan.windows([480,1440],[0,0],0.2)
OR4_Fan1 = OR4.Appliance(OR4,1,70, 2, 720,0.15,15,occasional_use=0.75)
OR4_Fan1.windows([0,1440],[0,0],0.2)
OR4_Fan2 = OR4.Appliance(OR4,1,70, 2, 720,0.15,15,occasional_use=0.75)
OR4_Fan2.windows([0,1440],[0,0],0.2)
OR4_TV=OR4.Appliance(OR4,1,60,2,600,0.2,30)
OR4_TV.windows([480,1440],[0,0], 0.35)
OR4_KitchenLED=OR4.Appliance(OR4,1,7,3,300,0.15,15)
OR4_KitchenLED.windows([1140,1380],[360,600],0.25,[720,900])
OR4_KitchenExhaustFan=OR4.Appliance(OR4,1,40,2,180,0.15,15)
OR4_KitchenExhaustFan.windows([1140,1380],[360,600],0.2,[720,900])
OR4_balcony_LED = OR4.Appliance(OR4,1,9,2,30,0.15,5)
OR4_balcony_LED.windows([1080,1159],[1201,1440],0.1)
OR4_laptop = OR4.Appliance(OR4,1,50,1,240,0.15,30, occasional_use = 0.75)
OR4_laptop.windows([1080,1440],[0,0],0.1)
OR4_Fridge = OR4.Appliance(OR4,1,200,1,1440,0,45, 'yes',1)
OR4_Fridge.windows([0,1440],[0,0])
OR4_Fridge.specific_cycle_1(5,45,200,45)
OR4_Fridge.cycle_behaviour([0,1440],[0,0])
OR4_WashingMachine=OR4.Appliance(OR4,1,600,2,120,0.2,30, occasional_use=0.75)
OR4_WashingMachine.windows([420,840],[0,0],0.25)
OR4_MicroWaveOven=OR4.Appliance(OR4,1,1200,3,60,0.2,15, occasional_use=0.75)
OR4_MicroWaveOven.windows([1080,1320],[420,600], 0.15, [720,900])
OR4_MixerGrinder = OR4.Appliance(OR4,1,500,2,60,0.15,15,occasional_use = 0.33)
OR4_MixerGrinder.windows([1080,1320],[420,600],0.3, [720,900])
OR4_WaterPurifier = OR4.Appliance(OR4,1,60,2,60,0.15,15)
OR4_WaterPurifier.windows([1080,1380],[420,900],0.3)
OR4_Iron = OR4.Appliance(OR4,1,1200,1,30,0.15,15, occasional_use=0.5)
OR4_Iron.windows([900,1320],[0,0],0.3)
OR4_SetTopBox = OR4.Appliance(OR4,1,10,2,600,0.2,30,occasional_use=0.5)
OR4_SetTopBox.windows([480,1400],[0,0],0.35)
OR4_MosquitoRepellent = OR4.Appliance(OR4,2,7,2,480,0.15,30, occasional_use=0.5)
OR4_MosquitoRepellent.windows([1200,1440],[0,360],0.35)
OR4_Toaster = OR4.Appliance(OR4,1,550,2,20,0.15,15, occasional_use=0.5)
OR4_Toaster.windows([1080,1320],[360,600],0.3)


#One-Room Minimum Connected Load
OR5 = User("Case6",6,1)
User_list.append(OR5)
#One-Room Minimum Connected Load
OR5_indoor_Tubelight1 = OR5.Appliance(OR5,1,55,2,420,0.15,15, occasional_use = 0.5)
OR5_indoor_Tubelight1.windows([1080,1440],[300,420],0.1)
OR5_indoor_Tubelight2 = OR5.Appliance(OR5,1,55,2,120,0.15,15)
OR5_indoor_Tubelight2.windows([1080,1440],[300,420],0.3)
OR5_indoor_LED = OR5.Appliance(OR5,1,9,2,120,0.15,15)
OR5_indoor_LED.windows([1080,1440],[300,420],0.3)
OR5_lavatory_LEDBulb = OR5.Appliance(OR5,1,5,2,60,0.2,5)
OR5_lavatory_LEDBulb.windows([541,1440],[360,540],0.1)
OR5_Phone_charger = OR5.Appliance(OR5,2,5,2,180,0.3,15)
OR5_Phone_charger.windows([0,1440],[0,0],0.35)
OR5_Fan = OR5.Appliance(OR5,1,70, 2, 720,0.15)
OR5_Fan.windows([480,1440],[0,0],0.2)
OR5_Fan1 = OR5.Appliance(OR5,1,70, 2, 720,0.15,15,occasional_use=0.75)
OR5_Fan1.windows([0,1440],[0,0],0.2)
OR5_Fan2 = OR5.Appliance(OR5,1,70, 2, 720,0.15,15,occasional_use=0.75)
OR5_Fan2.windows([0,1440],[0,0],0.2)
OR5_TV=OR5.Appliance(OR5,1,60,2,600,0.2,30)
OR5_TV.windows([540,1440],[0,0], 0.35)
OR5_SetTopBox = OR5.Appliance(OR5,1,10,2,600,0.2,30,occasional_use=0.5)
OR5_SetTopBox.windows([480,1400],[0,0],0.35)
OR5_KitchenLED=OR5.Appliance(OR5,1,7,3,300,0.15,15)
OR5_KitchenLED.windows([1140,1380],[360,600],0.25,[720,900])
OR5_KitchenExhaustFan=OR5.Appliance(OR5,1,40,2,180,0.15,15)
OR5_KitchenExhaustFan.windows([1140,1380],[360,600],0.2,[720,900])
OR5_Fridge = OR5.Appliance(OR5,1,200,1,1440,0,45, 'yes',1)
OR5_Fridge.windows([0,1440],[0,0])
OR5_Fridge.specific_cycle_1(5,45,200,45)
OR5_Fridge.cycle_behaviour([0,1440],[0,0])
OR5_WashingMachine=OR5.Appliance(OR5,1,600,2,120,0.2,30, occasional_use=0.75)
OR5_WashingMachine.windows([420,840],[0,0],0.25)
OR5_OvenToasterGriller=OR5.Appliance(OR5,1,1200,3,60,0.2,15, occasional_use=0.75)
OR5_OvenToasterGriller.windows([1080,1320],[420,600], 0.15, [720,900])
OR5_MixerGrinder = OR5.Appliance(OR5,1,500,2,60,0.15,15,occasional_use = 0.33)
OR5_MixerGrinder.windows([1080,1320],[420,600],0.3, [720,900])
OR5_WaterPurifier = OR5.Appliance(OR5,1,60,2,60,0.15,15)
OR5_WaterPurifier.windows([1080,1380],[420,900],0.3)
OR5_Iron = OR5.Appliance(OR5,1,1200,1,30,0.15,15, occasional_use=0.5)
OR5_Iron.windows([900,1320],[0,0],0.3)
OR5_MosquitoRepellent = OR5.Appliance(OR5,2,7,2,480,0.15,30, occasional_use=0.5)
OR5_MosquitoRepellent.windows([1200,1440],[0,360],0.35)

#One-Room Minimum Connected Load
OR6 = User("Case7",6,1)
User_list.append(OR6)
#One-Room Minimum Connected Load
OR6_indoor_LEDBulb1 = OR6.Appliance(OR6,1,7,2,420,0.15,15, occasional_use = 0.5)
OR6_indoor_LEDBulb1.windows([1080,1440],[300,420],0.1)
OR6_indoor_LEDBulb2 = OR6.Appliance(OR6,1,7,2,120,0.15,15)
OR6_indoor_LEDBulb2.windows([1080,1440],[300,420],0.3)
OR6_indoor_LEDBulb3 = OR6.Appliance(OR6,1,7,2,120,0.15,15)
OR6_indoor_LEDBulb3.windows([1080,1440],[300,420],0.3)
OR6_lavatory_LEDBulb = OR6.Appliance(OR6,1,5,2,60,0.2,5)
OR6_lavatory_LEDBulb.windows([360,540],[541,1440],0.1)
OR6_Fan = OR6.Appliance(OR6,1,30, 2, 720,0.15)
OR6_Fan.windows([480,1440],[0,0],0.2)
OR6_Fan1 = OR6.Appliance(OR6,1,30, 2, 720,0.15,15,occasional_use=0.75)
OR6_Fan1.windows([0,1440],[0,0],0.2)
OR6_Fan2 = OR6.Appliance(OR6,1,30, 2, 720,0.15,15,occasional_use=0.75)
OR6_Fan2.windows([0,1440],[0,0],0.2)
OR6_TV=OR6.Appliance(OR6,1,60,2,480,0.2,30)
OR6_TV.windows([540,1440],[0,0], 0.35)
OR6_SetTopBox = OR6.Appliance(OR6,1,10,2,480,0.2,30,occasional_use=0.5)
OR6_SetTopBox.windows([540,1400],[0,0],0.35)
OR6_KitchenLED=OR6.Appliance(OR6,1,7,3,300,0.15,15)
OR6_KitchenLED.windows([1140,1380],[360,600],0.25,[720,900])
OR6_KitchenExhaustFan=OR6.Appliance(OR6,1,40,2,180,0.15,15)
OR6_KitchenExhaustFan.windows([1140,1380],[360,600],0.2,[720,900])
OR6_Fridge = OR6.Appliance(OR6,1,200,1,1440,0,45, 'yes',1)
OR6_Fridge.windows([0,1440],[0,0])
OR6_Fridge.specific_cycle_1(5,45,200,45)
OR6_Fridge.cycle_behaviour([0,1440],[0,0])
OR6_MosquitoRepellent = OR6.Appliance(OR6,2,7,2,480,0.15,30, occasional_use=0.5)
OR6_MosquitoRepellent.windows([1200,1440],[0,360],0.35)
OR6_MixerGrinder = OR6.Appliance(OR6,1,500,2,60,0.15,15,occasional_use = 0.33)
OR6_MixerGrinder.windows([1080,1320],[420,600],0.3, [720,900])
OR6_Phone_charger = OR6.Appliance(OR6,2,5,2,180,0.3,15)
OR6_Phone_charger.windows([0,1440],[0,0],0.35)
OR6_WaterPurifier = OR6.Appliance(OR6,1,60,2,60,0.15,15)
OR6_WaterPurifier.windows([1080,1380],[420,900],0.3)
OR6_Toaster = OR6.Appliance(OR6,1,550,2,20,0.15,15, occasional_use=0.5)
OR6_Toaster.windows([1080,1320],[360,600],0.3)
OR6_ElectricKettle = OR6.Appliance(OR6,1,1200,2,20,0.15,15)
OR6_ElectricKettle.windows([1080,1320],[360,600],0.3)
