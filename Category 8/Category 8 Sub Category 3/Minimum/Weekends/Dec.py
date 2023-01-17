#One-Room Minimum Connected Load
#Create new user classes
OR = User("One room minimal",1,1)
User_list.append(OR)

#One-Room Minimum Connected Load
OR_indoor_Tubelights1 = OR.Appliance(OR,5,55,3,480,0.15,15)
OR_indoor_Tubelights1.windows([1080,1440],[300,420],0.1, [720,900])
OR_indoor_Tubelights2 = OR.Appliance(OR,3,55,2,120,0.15,15,occasional_use = 0.5)
OR_indoor_Tubelights2.windows([1080,1440],[300,420],0.3)
OR_indoor_Lamps3 = OR.Appliance(OR,3,30,2,420,0.15,15, occasional_use = 0.2)
OR_indoor_Lamps3.windows([1080,1440],[0,0],0.1)
OR_lavatory_Tubelights = OR.Appliance(OR,1,55,2,60,0.2,5)
OR_lavatory_Tubelights.windows([541,1440],[360,540],0.1)
OR_lavatory_ExhaustFan1 = OR.Appliance(OR,1,40,2,30,0.2,5)
OR_lavatory_ExhaustFan1.windows([541,1440],[360,540],0.1)
OR_lavatory_Tubelights1 = OR.Appliance(OR,2,55,2,60,0.2,5, occasional_use = 0.2)
OR_lavatory_Tubelights1.windows([541,1440],[360,540],0.1)
OR_lavatory_ExhaustFan = OR.Appliance(OR,2,40,2,30,0.2,5,occasional_use = 0.2)
OR_lavatory_ExhaustFan.windows([541,1440],[360,540],0.1)
OR_Phone_charger = OR.Appliance(OR,4,5,2,180,0.3,15)
OR_Phone_charger.windows([0,1440],[0,0],0.35)
OR_TV=OR.Appliance(OR,1,60,2,360,0.2,30)
OR_TV.windows([540,1440],[0,0], 0.35)
OR_KitchenTubelight=OR.Appliance(OR,1,40,3,300,0.15,15,occasional_use = 0.2)
OR_KitchenTubelight.windows([1140,1380],[360,600],0.25,[720,900])
OR_KitchenLED=OR.Appliance(OR,1,7,3,300,0.15,15)
OR_KitchenLED.windows([1140,1380],[360,600],0.25,[720,900])
OR_KitchenExhaustFan=OR.Appliance(OR,1,40,2,180,0.15,15)
OR_KitchenExhaustFan.windows([1140,1380],[360,600],0.2,[720,900])
OR_balcony_LED = OR.Appliance(OR,2,9,2,30,0.15,5)
OR_balcony_LED.windows([1080,1159],[1201,1440],0.1)
OR_Desktopcomputer = OR.Appliance(OR,1,150,1,60,0.15,30, occasional_use = 0.25)
OR_Desktopcomputer.windows([1080,1440],[0,0],0.1)
OR_hairtrimmercharger = OR.Appliance(OR,1,5,2,30,0.15,15,occasional_use = 0.2)
OR_hairtrimmercharger.windows([300,480],[0,0],0.1)
OR_Fridge = OR.Appliance(OR,1,200,1,1440,0,45, 'yes',1)
OR_Fridge.windows([0,1440],[0,0])
OR_Fridge.specific_cycle_1(5,45,200,45)
OR_Fridge.cycle_behaviour([0,1440],[0,0])
OR_WashingMachine=OR.Appliance(OR,1,600,2,120,0.2,30, occasional_use=0.75)
OR_WashingMachine.windows([420,840],[0,0],0.25)
OR_VacuumCleaner=OR.Appliance(OR,1,1000,2,30,0.2,30, occasional_use=0.25)
OR_VacuumCleaner.windows([480,720],[0,0], 0.15)
OR_MicroWaveOven=OR.Appliance(OR,1,1200,3,60,0.2,15, occasional_use=0.5)
OR_MicroWaveOven.windows([1080,1320],[420,600], 0.15, [720,900])
OR_MixerGrinder = OR.Appliance(OR,1,500,2,60,0.15,15,occasional_use = 0.33)
OR_MixerGrinder.windows([1080,1320],[420,600],0.3, [720,900])
OR_WaterPurifier = OR.Appliance(OR,1,60,2,60,0.15,15)
OR_WaterPurifier.windows([1080,1380],[420,900],0.3)
OR_Iron = OR.Appliance(OR,1,1200,1,30,0.15,15, occasional_use=0.25)
OR_Iron.windows([900,1320],[0,0],0.3)
OR_MusicSystem = OR.Appliance(OR,1,200,1,60,0.15,15, occasional_use=0.25)
OR_MusicSystem.windows([1080,1380],[480,900],0.3)
OR_SetTopBox = OR.Appliance(OR,1,10,2,360,0.2,30)
OR_SetTopBox.windows([540,1400],[0,0],0.35)
OR_MosquitoRepellent = OR.Appliance(OR,1,7,2,480,0.15,30, occasional_use=0.5)
OR_MosquitoRepellent.windows([1200,1440],[0,360],0.35)
OR_MosquitoRepellent1 = OR.Appliance(OR,2,7,2,480,0.15,30, occasional_use=0.5)
OR_MosquitoRepellent1.windows([1080,1440],[0,0],0.35)
OR_BathroomGeyser = OR.Appliance(OR,1,2000,2,60,0.1,15, 'yes',1,occasional_use=0.75)
OR_BathroomGeyser.windows([420,900],[0,0],0.1)
OR_BathroomGeyser.specific_cycle_1(2000,10,10,5)
OR_BathroomGeyser.cycle_behaviour([420,900],[0,0])
OR_BathroomGeyser1 = OR.Appliance(OR,1,2000,2,60,0.1,15, 'yes',1,occasional_use=0.15)
OR_BathroomGeyser1.windows([420,900],[0,0],0.1)
OR_BathroomGeyser1.specific_cycle_1(2000,10,10,5)
OR_BathroomGeyser1.cycle_behaviour([420,900],[0,0])
