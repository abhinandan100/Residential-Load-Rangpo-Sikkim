#One-Room Minimum Connected Load
#Create new user classes
OR = User("One room minimal",1,1)
User_list.append(OR)

#One-Room Minimum Connected Load
OR_Fans0 = OR.Appliance(OR,4,70, 2, 960,0.15, occasional_use=0.15)
OR_Fans0.windows([480,1440],[0,0],0.2)
OR_Fans1 = OR.Appliance(OR,4,70, 2, 360,0.15,15,occasional_use=0.5)
OR_Fans1.windows([1080,1440],[0,480],0.2)
OR_indoor_Tubelights1 = OR.Appliance(OR,5,55,3,480,0.15,15)
OR_indoor_Tubelights1.windows([1080,1440],[300,420],0.1, [720,900])
OR_indoor_Tubelights2 = OR.Appliance(OR,3,55,2,120,0.15,15,occasional_use = 0.5)
OR_indoor_Tubelights2.windows([1080,1440],[300,420],0.3)
OR_indoor_Tubelights3 = OR.Appliance(OR,8,55,2,420,0.15,15, occasional_use = 0.2)
OR_indoor_Tubelights3.windows([1080,1440],[300,420],0.1)
OR_lavatory_Tubelights = OR.Appliance(OR,5,55,2,60,0.2,5)
OR_lavatory_Tubelights.windows([541,1440],[360,540],0.1)
OR_lavatory_ExhaustFan = OR.Appliance(OR,5,40,2,30,0.2,5)
OR_lavatory_ExhaustFan.windows([541,1440],[360,540],0.1)
OR_Phone_charger = OR.Appliance(OR,12,5,2,180,0.3,15)
OR_Phone_charger.windows([0,1440],[0,0],0.35)
OR_Camera_charger = OR.Appliance(OR,3,5,2,180,0.3,15,occasional_use=0.25)
OR_Camera_charger.windows([0,1440],[0,0],0.35)
OR_TV=OR.Appliance(OR,2,60,2,360,0.2,30)
OR_TV.windows([540,1440],[0,0], 0.35)
OR_KitchenTubelight=OR.Appliance(OR,2,40,3,300,0.15,15)
OR_KitchenTubelight.windows([1140,1380],[360,600],0.25,[720,900])
OR_KitchenExhaustFan=OR.Appliance(OR,4,40,2,180,0.15,15)
OR_KitchenExhaustFan.windows([1140,1380],[360,600],0.2,[720,900])
OR_balcony_LED = OR.Appliance(OR,3,9,2,30,0.15,5)
OR_balcony_LED.windows([1080,1159],[1201,1440],0.1)
OR_laptop = OR.Appliance(OR,3,50,1,240,0.15,30, occasional_use = 0.75)
OR_laptop.windows([1080,1440],[0,0],0.1)
OR_hairtrimmercharger = OR.Appliance(OR,3,5,2,30,0.15,15,occasional_use = 0.2)
OR_hairtrimmercharger.windows([300,480],[0,0],0.1)
OR_hairdrier = OR.Appliance(OR,3,800,2,30,0.15,15,occasional_use = 0.2)
OR_hairdrier.windows([480,600],[601,900],0.1)
OR_Fridge = OR.Appliance(OR,2,200,1,1440,0,45, 'yes',1)
OR_Fridge.windows([0,1440],[0,0])
OR_Fridge.specific_cycle_1(5,45,200,45)
OR_Fridge.cycle_behaviour([0,1440],[0,0])
OR_WashingMachine=OR.Appliance(OR,2,600,2,120,0.2,30, occasional_use=0.75)
OR_WashingMachine.windows([420,840],[0,0],0.25)
OR_VacuumCleaner=OR.Appliance(OR,2,1000,2,30,0.2,30, occasional_use=0.5)
OR_VacuumCleaner.windows([480,720],[0,0], 0.15)
OR_MicroWaveOven=OR.Appliance(OR,2,1200,3,60,0.2,15, occasional_use=0.75)
OR_MicroWaveOven.windows([1080,1320],[420,600], 0.15, [720,900])
OR_OTG=OR.Appliance(OR,2,1200,3,60,0.2,15, occasional_use=0.75)
OR_OTG.windows([1080,1320],[420,600], 0.15, [720,900])
OR_GameConsole = OR.Appliance(OR,1,120,2,120,0.15,15, occasional_use = 0.5)
OR_GameConsole.windows([1080,1440],[900,1080],0.3)
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
OR_WaterPump = OR.Appliance(OR,1,500,2,45,0.15,15,occasional_use=0.25)
OR_WaterPump.windows([360,540],[1080,1140],0.3, [720,900])
OR_SetTopBox = OR.Appliance(OR,1,10,2,360,0.2,30,occasional_use=0.5)
OR_SetTopBox.windows([540,1400],[0,0],0.35)
OR_MosquitoRepellent = OR.Appliance(OR,4,7,2,480,0.15,30, occasional_use=0.5)
OR_MosquitoRepellent.windows([1200,1440],[0,360],0.35)
OR_MosquitoRepellent1 = OR.Appliance(OR,1,7,2,480,0.15,30, occasional_use=0.5)
OR_MosquitoRepellent1.windows([1080,1440],[0,0],0.35)
OR_InductionCooktop = OR.Appliance(OR,1,2000,3,150,0.1,15, 'yes',1,occasional_use=0.1)
OR_InductionCooktop.windows([720,900],[1080,1320],0.15, [360,480])
OR_InductionCooktop.specific_cycle_1(500,15,2000,15)
OR_InductionCooktop.cycle_behaviour([1080,1320],[720,900])
OR_BathroomGeyser = OR.Appliance(OR,5,2000,2,60,0.1,15, 'yes',1,occasional_use=0.25)
OR_BathroomGeyser.windows([420,540],[541,900],0.1,[1080,1200])
OR_BathroomGeyser.specific_cycle_1(2000,10,10,5)
OR_BathroomGeyser.cycle_behaviour([420,900],[0,0])
OR_AirConditioner = OR.Appliance(OR,3,500,2,480,0.1,15, 'yes',1, occasional_use=.75)
OR_AirConditioner.windows([840,1440],[0,480],0.1)
OR_AirConditioner.specific_cycle_1(500,15,10,45)
OR_AirConditioner.cycle_behaviour([1080,1440],[0,480])
OR_Toaster = OR.Appliance(OR,1,550,2,20,0.15,15, occasional_use=0.5)
OR_Toaster.windows([1080,1320],[360,600],0.3)
OR_ElectricKettle = OR.Appliance(OR,1,1200,2,30,0.15,15)
OR_ElectricKettle.windows([1080,1320],[360,600],0.3)
OR_Treadmill = OR.Appliance(OR,1,200,2,30,0.15,15, occasional_use=0.75)
OR_Treadmill.windows([1080,1320],[360,600],0.3)

OR4 = User("One room minimal",1,1)
User_list.append(OR4)

#One-Room Minimum Connected Load
OR4_Fans0 = OR4.Appliance(OR4,3,70, 2, 960,0.15)
OR4_Fans0.windows([480,1440],[0,0],0.2)
OR4_Fans1 = OR4.Appliance(OR4,2,70, 2, 360,0.15,15,occasional_use=0.5)
OR4_Fans1.windows([1080,1440],[0,480],0.2)
OR4_Fans2 = OR4.Appliance(OR4,3,70, 2, 360,0.15,15,occasional_use=0.2)
OR4_Fans2.windows([1080,1440],[0,480],0.2)
OR4_indoor_Tubelights1 = OR4.Appliance(OR4,5,55,3,480,0.15,15)
OR4_indoor_Tubelights1.windows([1080,1440],[300,420],0.1, [720,900])
OR4_indoor_Tubelights2 = OR4.Appliance(OR4,3,55,2,120,0.15,15,occasional_use = 0.5)
OR4_indoor_Tubelights2.windows([1080,1440],[300,420],0.3)
OR4_indoor_Lamps3 = OR4.Appliance(OR4,3,30,2,420,0.15,15, occasional_use = 0.2)
OR4_indoor_Lamps3.windows([1080,1440],[0,0],0.1)
OR4_lavatory_Tubelights = OR4.Appliance(OR4,1,55,2,60,0.2,5)
OR4_lavatory_Tubelights.windows([541,1440],[360,540],0.1)
OR4_lavatory_ExhaustFan1 = OR4.Appliance(OR4,1,40,2,30,0.2,5)
OR4_lavatory_ExhaustFan1.windows([541,1440],[360,540],0.1)
OR4_lavatory_Tubelights1 = OR4.Appliance(OR4,2,55,2,60,0.2,5, occasional_use = 0.2)
OR4_lavatory_Tubelights1.windows([541,1440],[360,540],0.1)
OR4_lavatory_ExhaustFan = OR4.Appliance(OR4,2,40,2,30,0.2,5,occasional_use = 0.2)
OR4_lavatory_ExhaustFan.windows([541,1440],[360,540],0.1)
OR4_Phone_charger = OR4.Appliance(OR4,4,5,2,180,0.3,15)
OR4_Phone_charger.windows([0,1440],[0,0],0.35)
OR4_TV=OR4.Appliance(OR4,1,60,2,360,0.2,30)
OR4_TV.windows([540,1440],[0,0], 0.35)
OR4_KitchenTubelight=OR4.Appliance(OR4,1,40,3,300,0.15,15,occasional_use = 0.2 )
OR4_KitchenTubelight.windows([1140,1380],[360,600],0.25,[720,900])
OR4_KitchenLED=OR4.Appliance(OR4,1,7,3,300,0.15,15)
OR4_KitchenLED.windows([1140,1380],[360,600],0.25,[720,900])
OR4_KitchenExhaustFan=OR4.Appliance(OR4,1,40,2,180,0.15,15)
OR4_KitchenExhaustFan.windows([1140,1380],[360,600],0.2,[720,900])
OR4_balcony_LED = OR4.Appliance(OR4,2,9,2,30,0.15,5)
OR4_balcony_LED.windows([1080,1320],[0,0],0.1)
OR4_Desktopcomputer = OR4.Appliance(OR4,1,150,1,60,0.15,30, occasional_use = 0.25)
OR4_Desktopcomputer.windows([1080,1440],[0,0],0.1)
OR4_hairtrimmercharger = OR4.Appliance(OR4,1,5,2,30,0.15,15,occasional_use = 0.2)
OR4_hairtrimmercharger.windows([300,480],[0,0],0.1)
OR4_Fridge = OR4.Appliance(OR4,1,200,1,1440,0,45, 'yes',1)
OR4_Fridge.windows([0,1440],[0,0])
OR4_Fridge.specific_cycle_1(5,45,200,45)
OR4_Fridge.cycle_behaviour([0,1440],[0,0])
OR4_WashingMachine=OR4.Appliance(OR4,1,600,2,120,0.2,30, occasional_use=0.75)
OR4_WashingMachine.windows([420,840],[0,0],0.25)
OR4_VacuumCleaner=OR4.Appliance(OR4,1,1000,2,30,0.2,30, occasional_use=0.5)
OR4_VacuumCleaner.windows([480,720],[0,0], 0.15)
OR4_MicroWaveOven=OR4.Appliance(OR4,1,1200,3,60,0.2,15, occasional_use=0.5)
OR4_MicroWaveOven.windows([1080,1320],[420,600], 0.15, [720,900])
OR4_MixerGrinder = OR4.Appliance(OR4,1,500,2,60,0.15,15,occasional_use = 0.33)
OR4_MixerGrinder.windows([1080,1320],[420,600],0.3, [720,900])
OR4_WaterPurifier = OR4.Appliance(OR4,1,60,2,60,0.15,15)
OR4_WaterPurifier.windows([1080,1380],[420,900],0.3)
OR4_Iron = OR4.Appliance(OR4,1,1200,1,30,0.15,15, occasional_use=0.5)
OR4_Iron.windows([900,1320],[0,0],0.3)
OR4_MusicSystem = OR4.Appliance(OR4,1,200,1,60,0.15,15, occasional_use=0.25)
OR4_MusicSystem.windows([1080,1380],[480,900],0.3)
OR4_SetTopBox = OR4.Appliance(OR4,1,10,2,360,0.2,30,occasional_use=0.5)
OR4_SetTopBox.windows([540,1400],[0,0],0.35)
OR4_MosquitoRepellent = OR4.Appliance(OR4,1,7,2,480,0.15,30, occasional_use=0.5)
OR4_MosquitoRepellent.windows([1200,1440],[0,360],0.35)
OR4_MosquitoRepellent1 = OR4.Appliance(OR4,2,7,2,480,0.15,30, occasional_use=0.5)
OR4_MosquitoRepellent1.windows([1080,1440],[0,0],0.35)
OR4_indoor_Lamps3 = OR4.Appliance(OR4,3,30,2,420,0.15,15, occasional_use = 0.2)
OR4_indoor_Lamps3.windows([1080,1440],[0,0],0.1)

#One-Room Minimum Connected Load
#Create new user classes
OR1 = User("One room maximum",1,1)
User_list.append(OR1)

#One-Room Minimum Connected Load
OR1_Fans0 = OR1.Appliance(OR1,4,70, 2, 960,0.15,occasional_use=0.75)
OR1_Fans0.windows([480,1440],[0,0],0.2)
OR1_Fans1 = OR1.Appliance(OR1,4,70, 2, 360,0.15,15,occasional_use=0.5)
OR1_Fans1.windows([1080,1440],[0,480],0.2)
OR1_indoor_Tubelights1 = OR1.Appliance(OR1,3,55,3,480,0.15,15)
OR1_indoor_Tubelights1.windows([1080,1440],[300,420],0.1, [720,900])
OR1_indoor_Tubelights2 = OR1.Appliance(OR1,5,55,2,120,0.15,15,occasional_use = 0.5)
OR1_indoor_Tubelights2.windows([1080,1440],[300,420],0.3)
OR1_indoor_Tubelights3 = OR1.Appliance(OR1,8,55,2,420,0.15,15, occasional_use = 0.2)
OR1_indoor_Tubelights3.windows([1080,1440],[300,420],0.1)
OR1_lavatory_Tubelights = OR1.Appliance(OR1,3,55,2,60,0.2,5)
OR1_lavatory_Tubelights.windows([541,1440],[360,540],0.1)
OR1_lavatory_ExhaustFan = OR1.Appliance(OR1,3,40,2,30,0.2,5)
OR1_lavatory_ExhaustFan.windows([541,1440],[360,540],0.1)
OR1_Phone_charger = OR1.Appliance(OR1,8,5,2,180,0.3,15)
OR1_Phone_charger.windows([0,1440],[0,0],0.35)
OR1_Camera_charger = OR1.Appliance(OR1,2,5,2,180,0.3,15,occasional_use=0.25)
OR1_Camera_charger.windows([0,1440],[0,0],0.35)
OR1_TV=OR1.Appliance(OR1,1,60,2,360,0.2,30)
OR1_TV.windows([540,1440],[0,0], 0.35)
OR1_KitchenTubelight=OR1.Appliance(OR1,2,40,3,300,0.15,15)
OR1_KitchenTubelight.windows([1140,1380],[360,600],0.25,[720,900])
OR1_KitchenExhaustFan=OR1.Appliance(OR1,2,40,2,180,0.15,15)
OR1_KitchenExhaustFan.windows([1140,1380],[360,600],0.2,[720,900])
OR1_balcony_LED = OR1.Appliance(OR1,2,9,2,30,0.15,5)
OR1_balcony_LED.windows([1080,1159],[1201,1440],0.1)
OR1_laptop = OR1.Appliance(OR1,1,50,1,240,0.15,30, occasional_use = 0.5)
OR1_laptop.windows([1080,1440],[0,0],0.1)
OR1_hairtrimmercharger = OR1.Appliance(OR1,2,5,2,30,0.15,15,occasional_use = 0.2)
OR1_hairtrimmercharger.windows([300,480],[0,0],0.1)
OR1_hairdrier = OR1.Appliance(OR1,2,800,2,30,0.15,15,occasional_use = 0.2)
OR1_hairdrier.windows([480,600],[601,900],0.1)
OR1_Fridge = OR1.Appliance(OR1,1,200,1,1440,0,45, 'yes',1)
OR1_Fridge.windows([0,1440],[0,0])
OR1_Fridge.specific_cycle_1(5,45,200,45)
OR1_Fridge.cycle_behaviour([0,1440],[0,0])
OR1_WashingMachine=OR1.Appliance(OR1,2,600,2,120,0.2,30, occasional_use=0.75)
OR1_WashingMachine.windows([420,840],[0,0],0.25)
OR1_VacuumCleaner=OR1.Appliance(OR1,2,1000,2,30,0.2,30, occasional_use=0.5)
OR1_VacuumCleaner.windows([480,720],[0,0], 0.15)
OR1_MicroWaveOven=OR1.Appliance(OR1,2,1200,3,60,0.2,15, occasional_use=0.75)
OR1_MicroWaveOven.windows([1080,1320],[420,600], 0.15, [720,900])
OR1_OTG=OR1.Appliance(OR1,2,1200,3,60,0.2,15, occasional_use=0.75)
OR1_OTG.windows([1080,1320],[420,600], 0.15, [720,900])
OR1_MixerGrinder = OR1.Appliance(OR1,1,500,2,60,0.15,15,occasional_use = 0.33)
OR1_MixerGrinder.windows([1080,1320],[420,600],0.3, [720,900])
OR1_WaterPurifier = OR1.Appliance(OR1,2,60,2,60,0.15,15)
OR1_WaterPurifier.windows([1080,1380],[420,900],0.3)
OR1_Iron = OR1.Appliance(OR1,1,1200,1,30,0.15,15, occasional_use=0.5)
OR1_Iron.windows([900,1320],[0,0],0.3)
OR1_MusicSystem = OR1.Appliance(OR1,1,200,1,60,0.15,15, occasional_use=0.25)
OR1_MusicSystem.windows([1080,1380],[480,900],0.3)
OR1_SetTopBox = OR1.Appliance(OR1,1,10,2,360,0.2,30,occasional_use=0.5)
OR1_SetTopBox.windows([540,1400],[0,0],0.35)
OR1_MosquitoRepellent = OR1.Appliance(OR1,1,7,2,480,0.15,30, occasional_use=0.5)
OR1_MosquitoRepellent.windows([1200,1440],[0,360],0.35)
OR1_MosquitoRepellent1 = OR1.Appliance(OR1,5,7,2,480,0.15,30, occasional_use=0.5)
OR1_MosquitoRepellent1.windows([1080,1440],[0,0],0.35)
OR1_InductionCooktop = OR1.Appliance(OR1,1,2000,3,150,0.1,15, 'yes',1,occasional_use=0.1)
OR1_InductionCooktop.windows([720,900],[1080,1320],0.15, [360,480])
OR1_InductionCooktop.specific_cycle_1(500,15,2000,15)
OR1_InductionCooktop.cycle_behaviour([1080,1320],[720,900])
OR1_BathroomGeyser = OR1.Appliance(OR1,1,2000,2,60,0.1,15, 'yes',1,occasional_use=0.25)
OR1_BathroomGeyser.windows([420,540],[541,900],0.1,[1080,1200])
OR1_BathroomGeyser.specific_cycle_1(2000,10,10,5)
OR1_BathroomGeyser.cycle_behaviour([420,900],[0,0])
OR1_AirConditioner = OR1.Appliance(OR1,1,500,2,480,0.1,15, 'yes',1, occasional_use=.25)
OR1_AirConditioner.windows([840,1440],[0,480],0.1)
OR1_AirConditioner.specific_cycle_1(500,15,10,45)
OR1_AirConditioner.cycle_behaviour([1080,1440],[0,480])
OR1_Toaster = OR1.Appliance(OR1,1,550,2,20,0.15,15, occasional_use=0.5)
OR1_Toaster.windows([1080,1320],[360,600],0.3)
OR1_ElectricKettle = OR1.Appliance(OR1,1,1200,2,30,0.15,15)
OR1_ElectricKettle.windows([1080,1320],[360,600],0.3)


#One-Room Minimum Connected Load
#Create new user classes
OR2 = User("One room maximum",1,1)
User_list.append(OR2)

#One-Room Minimum Connected Load
OR2_Fans0 = OR2.Appliance(OR2,4,70, 2, 960,0.15,occasional_use=0.75)
OR2_Fans0.windows([480,1440],[0,0],0.2)
OR2_Fans1 = OR2.Appliance(OR2,4,70, 2, 360,0.15,15,occasional_use=0.5)
OR2_Fans1.windows([1080,1440],[0,480],0.2)
OR2_indoor_Tubelights1 = OR2.Appliance(OR2,5,55,3,480,0.15,15)
OR2_indoor_Tubelights1.windows([1080,1440],[300,420],0.1, [720,900])
OR2_indoor_Tubelights2 = OR2.Appliance(OR2,3,55,2,120,0.15,15,occasional_use = 0.5)
OR2_indoor_Tubelights2.windows([1080,1440],[300,420],0.3)
OR2_indoor_Tubelights3 = OR2.Appliance(OR2,8,55,2,420,0.15,15, occasional_use = 0.2)
OR2_indoor_Tubelights3.windows([1080,1440],[300,420],0.1)
OR2_lavatory_Tubelights = OR2.Appliance(OR2,3,55,2,60,0.2,5)
OR2_lavatory_Tubelights.windows([541,1440],[360,540],0.1)
OR2_lavatory_ExhaustFan = OR2.Appliance(OR2,3,40,2,30,0.2,5)
OR2_lavatory_ExhaustFan.windows([541,1440],[360,540],0.1)
OR2_Phone_charger = OR2.Appliance(OR2,8,5,2,180,0.3,15)
OR2_Phone_charger.windows([0,1440],[0,0],0.35)
OR2_Camera_charger = OR2.Appliance(OR2,1,5,2,180,0.3,15,occasional_use=0.25)
OR2_Camera_charger.windows([0,1440],[0,0],0.35)
OR2_TV=OR2.Appliance(OR2,1,60,2,360,0.2,30)
OR2_TV.windows([540,1440],[0,0], 0.35)
OR2_KitchenTubelight=OR2.Appliance(OR2,1,40,3,300,0.15,15)
OR2_KitchenTubelight.windows([1140,1380],[360,600],0.25,[720,900])
OR2_KitchenExhaustFan=OR2.Appliance(OR2,1,40,2,180,0.15,15)
OR2_KitchenExhaustFan.windows([1140,1380],[360,600],0.2,[720,900])
OR2_balcony_LED = OR2.Appliance(OR2,2,9,2,30,0.15,5)
OR2_balcony_LED.windows([1080,1159],[1201,1440],0.1)
OR2_laptop = OR2.Appliance(OR2,2,50,1,240,0.15,30, occasional_use = 0.75)
OR2_laptop.windows([1080,1440],[0,0],0.1)
OR2_hairtrimmercharger = OR2.Appliance(OR2,1,5,2,30,0.15,15,occasional_use = 0.2)
OR2_hairtrimmercharger.windows([300,480],[0,0],0.1)
OR2_hairdrier = OR2.Appliance(OR2,1,800,2,30,0.15,15,occasional_use = 0.2)
OR2_hairdrier.windows([480,600],[601,900],0.1)
OR2_Fridge = OR2.Appliance(OR2,1,200,1,1440,0,45, 'yes',1)
OR2_Fridge.windows([0,1440],[0,0])
OR2_Fridge.specific_cycle_1(5,45,200,45)
OR2_Fridge.cycle_behaviour([0,1440],[0,0])
OR2_WashingMachine=OR2.Appliance(OR2,1,600,2,120,0.2,30, occasional_use=0.75)
OR2_WashingMachine.windows([420,840],[0,0],0.25)
OR2_VacuumCleaner=OR2.Appliance(OR2,1,1000,2,30,0.2,30, occasional_use=0.5)
OR2_VacuumCleaner.windows([480,720],[0,0], 0.15)
OR2_MicroWaveOven=OR2.Appliance(OR2,1, 1200,3,60,0.2,15, occasional_use=0.75)
OR2_MicroWaveOven.windows([1080,1320],[420,600], 0.15, [720,900])
OR2_OTG=OR.Appliance(OR2,1,1200,3,60,0.2,15, occasional_use=0.75)
OR2_OTG.windows([1080,1320],[420,600], 0.15, [720,900])
OR2_MixerGrinder = OR2.Appliance(OR2,1,500,2,60,0.15,15,occasional_use = 0.33)
OR2_MixerGrinder.windows([1080,1320],[420,600],0.3, [720,900])
OR2_WaterPurifier = OR2.Appliance(OR2,1,60,2,60,0.15,15)
OR2_WaterPurifier.windows([1080,1380],[420,900],0.3)
OR2_Iron = OR2.Appliance(OR2,1,1200,1,30,0.15,15, occasional_use=0.5)
OR2_Iron.windows([900,1320],[0,0],0.3)
OR2_MusicSystem = OR2.Appliance(OR2,1,200,1,60,0.15,15, occasional_use=0.25)
OR2_MusicSystem.windows([1080,1380],[480,900],0.3)
OR2_WaterPump = OR2.Appliance(OR2,1,500,2,45,0.15,15,occasional_use=0.25)
OR2_WaterPump.windows([360,540],[1080,1140],0.3, [720,900])
OR2_SetTopBox = OR2.Appliance(OR2,1,10,2,360,0.2,30,occasional_use=0.5)
OR2_SetTopBox.windows([540,1400],[0,0],0.35)
OR2_MosquitoRepellent = OR2.Appliance(OR2,1,7,2,480,0.15,30, occasional_use=0.5)
OR2_MosquitoRepellent.windows([1200,1440],[0,360],0.35)
OR2_MosquitoRepellent1 = OR2.Appliance(OR2,5,7,2,480,0.15,30, occasional_use=0.5)
OR2_MosquitoRepellent1.windows([1080,1440],[0,0],0.35)
OR2_ElectricKettle = OR2.Appliance(OR2,1,1200,2,30,0.15,15,occasional_use=0.25)
OR2_ElectricKettle.windows([1080,1320],[360,600],0.3)
