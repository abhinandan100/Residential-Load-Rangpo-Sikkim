#One-Room Minimum Connected Load
#Create new user classes
OR = User("One room minimal",1,1)
User_list.append(OR)

#One-Room Minimum Connected Load


OR_indoor_Tubelights1 = OR.Appliance(OR,5,55,3,480,0.15,15)
OR_indoor_Tubelights1.windows([1020,1440],[300,420],0.1, [720,900])
OR_indoor_Tubelights2 = OR.Appliance(OR,2,55,2,120,0.15,15,occasional_use = 0.5)
OR_indoor_Tubelights2.windows([1020,1440],[300,420],0.3)
OR_indoor_Nightlights3 = OR.Appliance(OR,7,55,2,420,0.15,15, occasional_use = 0.2)
OR_indoor_Nightlights3.windows([1020,1440],[300,420],0.1)
OR_lavatory_Tubelights = OR.Appliance(OR,4,55,2,60,0.2,5)
OR_lavatory_Tubelights.windows([0,1440],[0,0],0.2)
OR_lavatory_ExhaustFan = OR.Appliance(OR,4,40,2,30,0.2,5)
OR_lavatory_ExhaustFan.windows([0,1440],[0,0],0.2)
OR_Phone_charger = OR.Appliance(OR,10,5,2,180,0.3,15)
OR_Phone_charger.windows([0,1440],[0,0],0.35)
OR_Camera_charger = OR.Appliance(OR,3,5,2,180,0.3,15,occasional_use=0.25)
OR_Camera_charger.windows([0,1440],[0,0],0.35)
OR_TV=OR.Appliance(OR,2,60,2,720,0.2,30)
OR_TV.windows([540,1440],[0,0], 0.35)
OR_KitchenTubelight=OR.Appliance(OR,2,40,3,300,0.15,15)
OR_KitchenTubelight.windows([1140,1380],[360,600],0.25,[720,900])
OR_KitchenExhaustFan=OR.Appliance(OR,2,40,2,180,0.15,15)
OR_KitchenExhaustFan.windows([1140,1380],[360,600],0.2,[720,900])
OR_balcony_LED = OR.Appliance(OR,2,9,2,30,0.15,5)
OR_balcony_LED.windows([1080,1159],[1201,1440],0.1)
OR_laptop = OR.Appliance(OR,2,50,1,240,0.15,30, occasional_use = 0.75)
OR_laptop.windows([1080,1440],[0,0],0.1)
OR_hairtrimmercharger = OR.Appliance(OR,2,5,2,30,0.15,15,occasional_use = 0.2)
OR_hairtrimmercharger.windows([300,480],[0,0],0.1)
OR_hairdrier = OR.Appliance(OR,2,800,2,30,0.15,15,occasional_use = 0.2)
OR_hairdrier.windows([480,600],[601,900],0.1)
OR_Fridge = OR.Appliance(OR,2,200,1,1440,0,45, 'yes',1)
OR_Fridge.windows([0,1440],[0,0])
OR_Fridge.specific_cycle_1(5,45,200,45)
OR_Fridge.cycle_behaviour([0,1440],[0,0])
OR_WashingMachine=OR.Appliance(OR,2,600,2,120,0.2,30, occasional_use=0.75)
OR_WashingMachine.windows([420,840],[0,0],0.25)
OR_VacuumCleaner=OR.Appliance(OR,1,1000,2,30,0.2,30, occasional_use=0.5)
OR_VacuumCleaner.windows([480,720],[0,0], 0.15)
OR_MicroWaveOven=OR.Appliance(OR,1,1200,3,60,0.2,15, occasional_use=0.75)
OR_MicroWaveOven.windows([1080,1320],[420,600], 0.15, [720,900])
OR_OTG=OR.Appliance(OR,1,1200,3,60,0.2,15, occasional_use=0.75)
OR_OTG.windows([1080,1320],[420,600], 0.15, [720,900])
OR_GameConsole = OR.Appliance(OR,2,120,2,120,0.15,15, occasional_use = 0.5)
OR_GameConsole.windows([1080,1440],[900,1080],0.3)
OR_MixerGrinder = OR.Appliance(OR,1,500,2,60,0.15,15,occasional_use = 0.33)
OR_MixerGrinder.windows([1080,1320],[420,600],0.3, [720,900])
OR_WaterPurifier = OR.Appliance(OR,2,60,2,60,0.15,15)
OR_WaterPurifier.windows([1080,1380],[420,900],0.3)
OR_Iron = OR.Appliance(OR,2,1200,1,30,0.15,15, occasional_use=0.5)
OR_Iron.windows([900,1320],[0,0],0.3)
OR_MusicSystem = OR.Appliance(OR,2,200,1,60,0.15,15, occasional_use=0.25)
OR_MusicSystem.windows([1080,1380],[480,900],0.3)
OR_InkjetPrinter = OR.Appliance(OR,1,30,1,30,0.15,15, occasional_use=0.1)
OR_InkjetPrinter.windows([420,900],[0,0],0.3)
OR_WaterPump = OR.Appliance(OR,1,500,2,45,0.15,15,occasional_use=0.25)
OR_WaterPump.windows([360,540],[1080,1140],0.3, [720,900])
OR_SetTopBox = OR.Appliance(OR,2,10,2,360,0.2,30,occasional_use=0.5)
OR_SetTopBox.windows([540,1400],[0,0],0.35)
OR_MosquitoRepellent = OR.Appliance(OR,1,7,2,480,0.15,30, occasional_use=0.5)
OR_MosquitoRepellent.windows([1200,1440],[0,360],0.35)
OR_MosquitoRepellent1 = OR.Appliance(OR,4,7,2,480,0.15,30, occasional_use=0.5)
OR_MosquitoRepellent1.windows([1080,1440],[0,0],0.35)
OR_InductionCooktop = OR.Appliance(OR,1,2000,3,150,0.1,15, 'yes',1,occasional_use=0.1)
OR_InductionCooktop.windows([720,900],[1080,1320],0.15, [360,480])
OR_InductionCooktop.specific_cycle_1(500,15,2000,15)
OR_InductionCooktop.cycle_behaviour([1080,1320],[720,900])
OR_BathroomGeyser = OR.Appliance(OR,4,2000,2,60,0.1,15, 'yes',1,occasional_use=0.9)
OR_BathroomGeyser.windows([420,900],[0,0],0.2)
OR_BathroomGeyser.specific_cycle_1(2000,10,10,5)
OR_BathroomGeyser.cycle_behaviour([420,900],[0,0])
OR_Toaster = OR.Appliance(OR,1,550,2,20,0.15,15, occasional_use=0.25)
OR_Toaster.windows([1080,1320],[360,600],0.3)
OR_ElectricKettle = OR.Appliance(OR,1,1200,2,30,0.15,15)
OR_ElectricKettle.windows([1080,1320],[360,600],0.3)
OR_Treadmill = OR.Appliance(OR,1,200,2,60,0.15,15, occasional_use=0.75)
OR_Treadmill.windows([1080,1320],[360,600],0.3)
OR_RoomHeater = OR.Appliance(OR,3,2000,2,120,0.1,30, 'yes',1, occasional_use=0.75)
OR_RoomHeater.windows([1080,1440],[0,0],0.1)
OR_RoomHeater.specific_cycle_1(2000,10,10,10)
OR_RoomHeater.cycle_behaviour([1080,1440],[0,0],[0,0],[0,0])
OR_KitchenGeyser = OR.Appliance(OR,2,2000,2,30,0.1,15, 'yes',1, occasional_use=0.75)
OR_KitchenGeyser.windows([1200,1380],[360,540],0.1)
OR_KitchenGeyser.specific_cycle_1(2000,10,10,5)
OR_KitchenGeyser.cycle_behaviour([1200,1380],[360,540])

#One-Room Minimum Connected Load
#Create new user classes
OR1= User("One room minimal",1,1)
User_list.append(OR1)

#One-Room Minimum Connected Load

OR1_indoor_Tubelights1 = OR1.Appliance(OR1,4,55,3,480,0.15,15)
OR1_indoor_Tubelights1.windows([1080,1440],[300,420],0.1, [720,900])
OR1_indoor_Tubelights2 = OR1.Appliance(OR1,2,55,2,120,0.15,15,occasional_use = 0.5)
OR1_indoor_Tubelights2.windows([1080,1440],[300,420],0.3)
OR1_indoor_Lamps3 = OR1.Appliance(OR1,2,30,2,420,0.15,15, occasional_use = 0.2)
OR1_indoor_Lamps3.windows([1080,1440],[0,0],0.1)
OR1_lavatory_Tubelights = OR1.Appliance(OR1,2,55,2,60,0.2,5)
OR1_lavatory_Tubelights.windows([541,1440],[360,540],0.1)
OR1_lavatory_ExhaustFan1 = OR1.Appliance(OR1,2,40,2,30,0.2,5)
OR1_lavatory_ExhaustFan1.windows([541,1440],[360,540],0.1)
OR1_Phone_charger = OR1.Appliance(OR1,4,5,2,180,0.3,15)
OR1_Phone_charger.windows([0,1440],[0,0],0.35)
OR1_TV=OR1.Appliance(OR1,1,60,2,360,0.2,30)
OR1_TV.windows([480,1440],[0,0], 0.35)
OR1_KitchenTubelight=OR1.Appliance(OR1,1,40,3,300,0.15,15,occasional_use = 0.2 )
OR1_KitchenTubelight.windows([1140,1380],[360,600],0.25,[720,900])
OR1_KitchenLED=OR1.Appliance(OR1,1,7,3,300,0.15,15)
OR1_KitchenLED.windows([1140,1380],[360,600],0.25,[720,900])
OR1_KitchenExhaustFan=OR1.Appliance(OR1,1,40,2,180,0.15,15)
OR1_KitchenExhaustFan.windows([1140,1380],[360,600],0.2,[720,900])
OR1_balcony_LED = OR1.Appliance(OR1,2,9,2,30,0.15,5)
OR1_balcony_LED.windows([1080,1320],[0,0],0.1)
OR1_Fridge = OR1.Appliance(OR1,1,200,1,1440,0,45, 'yes',1)
OR1_Fridge.windows([0,1440],[0,0])
OR1_Fridge.specific_cycle_1(5,45,200,45)
OR1_Fridge.cycle_behaviour([0,1440],[0,0])
OR1_WashingMachine=OR1.Appliance(OR1,1,600,2,120,0.2,30, occasional_use=0.75)
OR1_WashingMachine.windows([420,840],[0,0],0.25)
OR1_VacuumCleaner=OR1.Appliance(OR1,1,1000,2,30,0.2,30, occasional_use=0.5)
OR1_VacuumCleaner.windows([480,720],[0,0], 0.15)
OR1_MicroWaveOven=OR1.Appliance(OR1,1,1200,3,60,0.2,15, occasional_use=0.5)
OR1_MicroWaveOven.windows([1080,1320],[420,600], 0.15, [720,900])
OR1_MixerGrinder = OR1.Appliance(OR1,1,500,2,60,0.15,15,occasional_use = 0.33)
OR1_MixerGrinder.windows([1080,1320],[420,600],0.3, [720,900])
OR1_WaterPurifier = OR1.Appliance(OR1,1,60,2,60,0.15,15)
OR1_WaterPurifier.windows([1080,1380],[420,900],0.3)
OR1_Iron = OR1.Appliance(OR1,1,1200,1,30,0.15,15, occasional_use=0.5)
OR1_Iron.windows([900,1320],[0,0],0.3)
OR1_SetTopBox = OR1.Appliance(OR1,1,10,2,360,0.2,30,occasional_use=0.5)
OR1_SetTopBox.windows([480,1400],[0,0],0.35)
OR1_MosquitoRepellent = OR1.Appliance(OR1,2,7,2,480,0.15,30, occasional_use=0.5)
OR1_MosquitoRepellent.windows([1200,1440],[0,360],0.35)
OR1_BathroomGeyser = OR1.Appliance(OR1,1,2000,2,60,0.1,15, 'yes',1,occasional_use=0.75)
OR1_BathroomGeyser.windows([420,900],[0,0],0.1)
OR1_BathroomGeyser.specific_cycle_1(2000,10,10,5)
OR1_BathroomGeyser.cycle_behaviour([420,900],[0,0])
OR1_BathroomGeyser1 = OR1.Appliance(OR1,1,2000,2,60,0.1,15, 'yes',1,occasional_use=0.5)
OR1_BathroomGeyser1.windows([420,900],[0,0],0.1)
OR1_BathroomGeyser1.specific_cycle_1(2000,10,10,5)
OR1_BathroomGeyser1.cycle_behaviour([420,900],[0,0])


#One-Room Minimum Connected Load
#Create new user classes
OR3 = User("One room minimal",3,1)
User_list.append(OR3)

#One-Room Minimum Connected Load

OR3_indoor_Tubelights1 = OR3.Appliance(OR3,5,55,2,480,0.15,15)
OR3_indoor_Tubelights1.windows([1080,1440],[0,0],0.1)
OR3_indoor_Tubelights2 = OR3.Appliance(OR3,2,55,2,120,0.15,15,occasional_use = 0.5)
OR3_indoor_Tubelights2.windows([1080,1440],[0,0],0.3)
OR3_lavatory_Tubelights = OR3.Appliance(OR3,4,55,2,60,0.2,5)
OR3_lavatory_Tubelights.windows([360,1440],[0,0],0.1)
OR3_lavatory_ExhaustFan = OR3.Appliance(OR3,4,40,2,120,0.2,5)
OR3_lavatory_ExhaustFan.windows([0,1440],[0,0],0.1)
OR3_Phone_charger = OR3.Appliance(OR3,4,5,2,180,0.3,15)
OR3_Phone_charger.windows([0,1440],[0,0],0.35)
OR3_Camera_charger = OR3.Appliance(OR3,3,5,2,180,0.3,15,occasional_use=0.25)
OR3_Camera_charger.windows([0,1440],[0,0],0.35)
OR3_TV=OR.Appliance(OR3,2,60,2,720,0.2,30)
OR3_TV.windows([480,1440],[0,0], 0.35)
OR3_KitchenTubelight=OR3.Appliance(OR3,2,40,3,300,0.15,15)
OR3_KitchenTubelight.windows([1140,1380],[480,600],0.25,[720,900])
OR3_KitchenExhaustFan=OR3.Appliance(OR3,2,40,2,180,0.15,15)
OR3_KitchenExhaustFan.windows([1140,1380],[480,600],0.2,[720,900])
OR3_balcony_LED = OR3.Appliance(OR3,2,9,2,30,0.15,5)
OR3_balcony_LED.windows([1080,1159],[1201,1440],0.1)
OR3_Fridge = OR3.Appliance(OR3,2,200,1,1440,0,45, 'yes',1)
OR3_Fridge.windows([0,1440],[0,0])
OR3_Fridge.specific_cycle_1(5,45,200,45)
OR3_Fridge.cycle_behaviour([0,1440],[0,0])
OR3_WashingMachine=OR3.Appliance(OR3,2,600,2,120,0.2,30, occasional_use=0.75)
OR3_WashingMachine.windows([420,840],[0,0],0.25)
OR3_VacuumCleaner=OR3.Appliance(OR3,1,1000,2,30,0.2,30, occasional_use=0.5)
OR3_VacuumCleaner.windows([480,720],[0,0], 0.15)
OR3_MicroWaveOven=OR3.Appliance(OR3,1,1200,3,60,0.2,15, occasional_use=0.75)
OR3_MicroWaveOven.windows([1080,1320],[420,600], 0.15, [720,900])
OR3_MixerGrinder = OR3.Appliance(OR3,1,500,2,60,0.15,15,occasional_use = 0.33)
OR3_MixerGrinder.windows([1080,1320],[420,600],0.3, [720,900])
OR3_WaterPurifier = OR3.Appliance(OR3,2,60,2,60,0.15,15)
OR3_WaterPurifier.windows([1080,1380],[420,900],0.3)
OR3_Iron = OR3.Appliance(OR3,2,1200,1,30,0.15,15, occasional_use=0.5)
OR3_Iron.windows([900,1320],[0,0],0.3)
OR3_MusicSystem = OR3.Appliance(OR3,2,200,1,60,0.15,15, occasional_use=0.2)
OR3_MusicSystem.windows([1080,1380],[480,900],0.3)
OR3_WaterPump = OR3.Appliance(OR3,1,500,2,45,0.15,15,occasional_use=0.25)
OR3_WaterPump.windows([360,540],[1080,1140],0.3, [720,900])
OR3_SetTopBox = OR3.Appliance(OR3,2,10,2,360,0.2,30,occasional_use=0.5)
OR3_SetTopBox.windows([540,1400],[0,0],0.35)
OR3_MosquitoRepellent = OR3.Appliance(OR3,1,7,2,480,0.15,30, occasional_use=0.5)
OR3_MosquitoRepellent.windows([1200,1440],[0,360],0.35)
OR3_BathroomGeyser = OR.Appliance(OR,1,2000,2,60,0.1,15, 'yes',1,occasional_use=0.25)
OR3_BathroomGeyser.windows([420,900],[0,0],0.1)
OR3_BathroomGeyser.specific_cycle_1(2000,10,10,5)
OR3_BathroomGeyser.cycle_behaviour([420,900],[0,0])
OR3_Toaster = OR.Appliance(OR,1,550,2,20,0.15,15, occasional_use=0.25)
OR3_Toaster.windows([1080,1320],[360,600],0.3)
OR3_ElectricKettle = OR.Appliance(OR,1,700,2,30,0.15,15)
OR3_ElectricKettle.windows([1080,1320],[360,600],0.3)
OR3_BathroomGeyser = OR3.Appliance(OR3,1,2000,2,60,0.1,15, 'yes',1,occasional_use=0.75)
OR3_BathroomGeyser.windows([420,900],[0,0],0.1)
OR3_BathroomGeyser.specific_cycle_1(2000,10,10,5)
OR3_BathroomGeyser.cycle_behaviour([420,900],[0,0])
OR3_RoomHeater = OR3.Appliance(OR3,3,2000,2,120,0.1,30, 'yes',1, occasional_use=0.75)
OR3_RoomHeater.windows([1080,1440],[0,0],0.1)
OR3_RoomHeater.specific_cycle_1(2000,10,10,10)
OR3_RoomHeater.cycle_behaviour([1080,1440],[0,0],[0,0],[0,0])

#One-Room Minimum Connected Load
#Create new user classes
OR5 = User("One room minimal",2,1)
User_list.append(OR5)

#One-Room Minimum Connected Load

OR5_indoor_Tubelights1 = OR5.Appliance(OR5,5,55,3,480,0.15,15)
OR5_indoor_Tubelights1.windows([1080,1440],[300,420],0.1, [720,900])
OR5_indoor_Tubelights2 = OR5.Appliance(OR5,2,55,2,120,0.15,15,occasional_use = 0.5)
OR5_indoor_Tubelights2.windows([1080,1440],[300,420],0.3)
OR5_indoor_Nightlights3 = OR5.Appliance(OR5,2,55,2,420,0.15,15, occasional_use = 0.2)
OR5_indoor_Nightlights3.windows([1080,1440],[0,0],0.1)
OR5_lavatory_Tubelights = OR5.Appliance(OR5,4,55,2,60,0.2,5)
OR5_lavatory_Tubelights.windows([360,1440],[0,0],0.1)
OR5_lavatory_ExhaustFan = OR5.Appliance(OR5,4,40,2,60,0.2,5)
OR5_lavatory_ExhaustFan.windows([360,1440],[0,0],0.1)
OR5_Phone_charger = OR5.Appliance(OR5,4,5,2,180,0.3,15)
OR5_Phone_charger.windows([0,1440],[0,0],0.35)
OR5_Camera_charger = OR5.Appliance(OR5,3,5,2,180,0.3,15,occasional_use=0.25)
OR5_Camera_charger.windows([0,1440],[0,0],0.35)
OR5_TV=OR4.Appliance(OR5,2,60,2,720,0.2,30)
OR5_TV.windows([540,1440],[0,0], 0.35)
OR5_KitchenTubelight=OR5.Appliance(OR5,2,40,3,300,0.15,15)
OR5_KitchenTubelight.windows([1140,1380],[360,600],0.25,[720,900])
OR5_KitchenExhaustFan=OR5.Appliance(OR5,2,40,2,180,0.15,15)
OR5_KitchenExhaustFan.windows([1140,1380],[360,600],0.2,[720,900])
OR5_balcony_LED = OR5.Appliance(OR5,2,9,2,30,0.15,5)
OR5_balcony_LED.windows([1080,1159],[1201,1440],0.1)
OR5_laptop = OR5.Appliance(OR5,2,50,1,240,0.15,30, occasional_use = 0.75)
OR5_laptop.windows([1080,1440],[0,0],0.1)
OR5_hairtrimmercharger = OR5.Appliance(OR5,2,5,2,30,0.15,15,occasional_use = 0.2)
OR5_hairtrimmercharger.windows([300,480],[0,0],0.1)
OR5_hairdrier = OR5.Appliance(OR5,2,800,2,30,0.15,15,occasional_use = 0.2)
OR5_hairdrier.windows([480,600],[601,900],0.1)
OR5_Fridge = OR5.Appliance(OR5,2,200,1,1440,0,45, 'yes',1)
OR5_Fridge.windows([0,1440],[0,0])
OR5_Fridge.specific_cycle_1(5,45,200,45)
OR5_Fridge.cycle_behaviour([0,1440],[0,0])
OR5_WashingMachine=OR5.Appliance(OR5,2,600,2,120,0.2,30, occasional_use=0.75)
OR5_WashingMachine.windows([420,840],[0,0],0.25)
OR5_VacuumCleaner=OR5.Appliance(OR5,1,1000,2,30,0.2,30, occasional_use=0.5)
OR5_VacuumCleaner.windows([480,720],[0,0], 0.15)
OR5_MicroWaveOven=OR5.Appliance(OR5,1,1200,3,60,0.2,15, occasional_use=0.75)
OR5_MicroWaveOven.windows([1080,1320],[420,600], 0.15, [720,900])
OR5_MixerGrinder = OR5.Appliance(OR5,1,500,2,60,0.15,15,occasional_use = 0.33)
OR5_MixerGrinder.windows([1080,1320],[420,600],0.3, [720,900])
OR5_WaterPurifier = OR5.Appliance(OR5,2,60,2,60,0.15,15)
OR5_WaterPurifier.windows([1080,1380],[420,900],0.3)
OR5_Iron = OR5.Appliance(OR5,2,1200,1,30,0.15,15, occasional_use=0.5)
OR5_Iron.windows([900,1320],[0,0],0.3)
OR5_MusicSystem = OR5.Appliance(OR5,2,200,1,60,0.15,15, occasional_use=0.25)
OR5_MusicSystem.windows([1080,1380],[480,900],0.3)
OR5_WaterPump = OR5.Appliance(OR5,1,500,2,45,0.15,15,occasional_use=0.25)
OR5_WaterPump.windows([360,540],[1080,1140],0.3, [720,900])
OR5_SetTopBox = OR5.Appliance(OR5,2,10,2,360,0.2,30,occasional_use=0.5)
OR5_SetTopBox.windows([540,1400],[0,0],0.35)
OR5_MosquitoRepellent = OR5.Appliance(OR5,1,7,2,480,0.15,30, occasional_use=0.5)
OR5_MosquitoRepellent.windows([1200,1440],[0,360],0.35)
OR5_RiceCooker = OR5.Appliance(OR5,1,700,2,60,0.15,25)
OR5_RiceCooker.windows([1200,1380],[720,900],0.3)
OR5_BathroomGeyser = OR5.Appliance(OR5,1,2000,2,60,0.1,15, 'yes',1,occasional_use=0.75)
OR5_BathroomGeyser.windows([420,900],[0,0],0.1)
OR5_BathroomGeyser.specific_cycle_1(2000,10,10,5)
OR5_BathroomGeyser.cycle_behaviour([420,900],[0,0])

#One-Room Minimum Connected Load
#Create new user classes
OR4 = User("One room minimal",2,1)
User_list.append(OR4)

#One-Room Minimum Connected Load

OR4_indoor_Tubelights1 = OR4.Appliance(OR4,5,55,3,480,0.15,15)
OR4_indoor_Tubelights1.windows([1080,1440],[300,420],0.1, [720,900])
OR4_indoor_Tubelights2 = OR4.Appliance(OR4,2,55,2,120,0.15,15,occasional_use = 0.5)
OR4_indoor_Tubelights2.windows([1080,1440],[300,420],0.3)
OR4_indoor_Nightlights3 = OR4.Appliance(OR4,2,55,2,420,0.15,15, occasional_use = 0.2)
OR4_indoor_Nightlights3.windows([1080,1440],[300,420],0.1)
OR4_lavatory_Tubelights = OR4.Appliance(OR4,4,55,2,90,0.2,5)
OR4_lavatory_Tubelights.windows([0,1440],[0,0],0.1)
OR4_lavatory_ExhaustFan = OR4.Appliance(OR4,4,40,2,60,0.2,5)
OR4_lavatory_ExhaustFan.windows([360,1440],[0,0],0.1)
OR4_Phone_charger = OR4.Appliance(OR4,4,5,2,180,0.3,15)
OR4_Phone_charger.windows([0,1440],[0,0],0.35)
OR4_Camera_charger = OR4.Appliance(OR4,3,5,2,180,0.3,15,occasional_use=0.25)
OR4_Camera_charger.windows([0,1440],[0,0],0.35)
OR4_TV=OR4.Appliance(OR4,2,60,2,720,0.2,30)
OR4_TV.windows([540,1440],[0,0], 0.35)
OR4_KitchenTubelight=OR4.Appliance(OR4,2,40,3,300,0.15,15)
OR4_KitchenTubelight.windows([1140,1380],[360,600],0.25,[720,900])
OR4_KitchenExhaustFan=OR4.Appliance(OR4,2,40,2,180,0.15,15)
OR4_KitchenExhaustFan.windows([1140,1380],[360,600],0.2,[720,900])
OR4_balcony_LED = OR4.Appliance(OR4,2,9,2,30,0.15,5)
OR4_balcony_LED.windows([1080,1159],[1201,1440],0.1)
OR4_laptop = OR4.Appliance(OR4,2,50,1,240,0.15,30, occasional_use = 0.75)
OR4_laptop.windows([1080,1440],[0,0],0.1)
OR4_hairtrimmercharger = OR4.Appliance(OR4,2,5,2,30,0.15,15,occasional_use = 0.2)
OR4_hairtrimmercharger.windows([300,480],[0,0],0.1)
OR4_hairdrier = OR4.Appliance(OR4,2,800,2,30,0.15,15,occasional_use = 0.2)
OR4_hairdrier.windows([480,600],[601,900],0.1)
OR4_Fridge = OR4.Appliance(OR4,2,200,1,1440,0,45, 'yes',1)
OR4_Fridge.windows([0,1440],[0,0])
OR4_Fridge.specific_cycle_1(5,45,200,45)
OR4_Fridge.cycle_behaviour([0,1440],[0,0])
OR4_WashingMachine=OR4.Appliance(OR4,2,600,2,120,0.2,30, occasional_use=0.75)
OR4_WashingMachine.windows([420,840],[0,0],0.25)
OR4_VacuumCleaner=OR4.Appliance(OR4,1,1000,2,30,0.2,30, occasional_use=0.5)
OR4_VacuumCleaner.windows([480,720],[0,0], 0.15)
OR4_MicroWaveOven=OR4.Appliance(OR4,1,1200,3,60,0.2,15, occasional_use=0.75)
OR4_MicroWaveOven.windows([1080,1320],[420,600], 0.15, [720,900])
OR4_MixerGrinder = OR4.Appliance(OR4,1,500,2,60,0.15,15,occasional_use = 0.33)
OR4_MixerGrinder.windows([1080,1320],[420,600],0.3, [720,900])
OR4_WaterPurifier = OR4.Appliance(OR4,2,60,2,60,0.15,15)
OR4_WaterPurifier.windows([1080,1380],[420,900],0.3)
OR4_Iron = OR4.Appliance(OR4,2,1200,1,30,0.15,15, occasional_use=0.5)
OR4_Iron.windows([900,1320],[0,0],0.3)
OR4_MusicSystem = OR4.Appliance(OR4,2,200,1,60,0.15,15, occasional_use=0.25)
OR4_MusicSystem.windows([1080,1380],[480,900],0.3)
OR4_WaterPump = OR4.Appliance(OR4,1,500,2,45,0.15,15,occasional_use=0.25)
OR4_WaterPump.windows([360,540],[1080,1140],0.3, [720,900])
OR4_SetTopBox = OR4.Appliance(OR4,2,10,2,360,0.2,30,occasional_use=0.5)
OR4_SetTopBox.windows([540,1400],[0,0],0.35)
OR4_MosquitoRepellent = OR4.Appliance(OR4,1,7,2,480,0.15,30, occasional_use=0.5)
OR4_MosquitoRepellent.windows([1200,1440],[0,360],0.35)
OR4_BathroomGeyser = OR4.Appliance(OR4,3,2000,3,60,0.1,15, 'yes',1,occasional_use=0.75)
OR4_BathroomGeyser.windows([420,540],[541,900],0.1,[1080,1200])
OR4_BathroomGeyser.specific_cycle_1(2000,10,10,5)
OR4_BathroomGeyser.cycle_behaviour([420,900],[0,0])
OR4_KitchenGeyser = OR4.Appliance(OR4,1,2000,2,30,0.1,15, 'yes',1, occasional_use=0.75)
OR4_KitchenGeyser.windows([1200,1380],[360,540],0.1)
OR4_KitchenGeyser.specific_cycle_1(2000,10,10,5)
OR4_KitchenGeyser.cycle_behaviour([1200,1380],[360,540])