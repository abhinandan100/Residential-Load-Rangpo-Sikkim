#One-Room Minimum Connected Load
#Create new user classes
OR = User("One room minimal",1,1)
User_list.append(OR)

#One-Room Minimum Connected Load
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
OR_Fridge.cycle_behaviour([0,1440],[0,0])
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
OR_BathroomGeyser = OR.Appliance(OR,1,2000,2,60,0.1,15, 'yes',1)
OR_BathroomGeyser.windows([1080,1140],[360,540],0.1)
OR_BathroomGeyser.specific_cycle_1(2000,10,10,5)
OR_BathroomGeyser.cycle_behaviour([1080,1140],[360,540])
OR_RoomHeater = OR.Appliance(OR,1,2000,2,240,0.1,30, 'yes',1)
OR_RoomHeater.windows([1080,1440],[0,0],0.1)
OR_RoomHeater.specific_cycle_1(2000,10,10,10)
OR_RoomHeater.cycle_behaviour([1080,1440],[0,0],[0,0],[0,0])
OR_KitchenGeyser = OR.Appliance(OR,1,2000,2,60,0.1,15, 'yes',1, occasional_use=0.75)
OR_KitchenGeyser.windows([1200,1380],[360,540],0.1)
OR_KitchenGeyser.specific_cycle_1(2000,10,10,5)
OR_KitchenGeyser.cycle_behaviour([1200,1380],[360,540])
