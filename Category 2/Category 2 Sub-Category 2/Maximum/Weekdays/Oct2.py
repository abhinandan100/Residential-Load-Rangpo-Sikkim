#One-Room Minimum Connected Load
#Create new user classes
OR = User("One room minimal",1,1)
User_list.append(OR)

#One-Room Minimum Connected Load
OR_indoor_Tubelight1 = OR.Appliance(OR,1,55,2,420,0.15,15)
OR_indoor_Tubelight1.windows([1290,1440],[0,120],0.1)
OR_indoor_Tubelight2 = OR.Appliance(OR,1,55,2,120,0.15,15, occasional_use = 0.5)
OR_indoor_Tubelight2.windows([1290,1440],[0,120],0.3)
OR_indoor_Tubelight3 = OR.Appliance(OR,1,55,2,420,0.15,1)
OR_indoor_Tubelight3.windows([1290,1440],[0,120],0.1)
OR_indoor_Tubelight4 = OR.Appliance(OR,1,55,2,120,0.15,15, occasional_use = 0.5)
OR_indoor_Tubelight4.windows([1290,1440],[0,120],0.3)
OR_lavatory_LEDBulb = OR.Appliance(OR,1,5,2,60,0.2,15)
OR_lavatory_LEDBulb.windows([1290,1440],[300,840],0.1,[0,299])
OR_Phone_charger = OR.Appliance(OR,4,5,2,120,0.3,15)
OR_Phone_charger.windows([1290,1440],[420,840],0.35)
OR_TV=OR.Appliance(OR,2,60,2,300,0.2,30)
OR_TV.windows([1290,1440],[480,840], 0.15)
OR_SetTopBox = OR.Appliance(OR,1,10,2,300,0.2,30)
OR_SetTopBox.windows([1290,1440],[480,840],0.15)
OR_KitchenTubelight=OR.Appliance(OR,1,40,2,180,0.15,15)
OR_KitchenTubelight.windows([1320,1440],[0,120],0.2)
OR_KitchenExhaustFan=OR.Appliance(OR,1,40,3,180,0.15,15)
OR_KitchenExhaustFan.windows([1320,1440],[480,540],0.2,[720,840])
OR_balcony_LED = OR.Appliance(OR,1,9,2,30,0.15,5)
OR_balcony_LED.windows([1320,1440],[0,0],0.1)
OR_Fridge = OR.Appliance(OR,1,200,1,1440,0,45, 'yes',1)
OR_Fridge.windows([0,1440],[0,0])
OR_Fridge.specific_cycle_1(5,45,200,45)
OR_Fridge.cycle_behaviour([0,1440],[0,0])
OR_MixerGrinder = OR.Appliance(OR,1,500,2,60,0.15,15,occasional_use = 0.33)
OR_MixerGrinder.windows([1320,1440],[480,840],0.3)
OR_InductionCooktop = OR.Appliance(OR,1,2000,3,150,0.1,15, 'yes',1)
OR_InductionCooktop.windows([1320,1440],[480,540],0.15, [720,840])
OR_InductionCooktop.specific_cycle_1(500,15,2000,15)
OR_InductionCooktop.cycle_behaviour([1320,1440],[720,840])
OR_WaterPurifier = OR.Appliance(OR,1,50,2,60,0.15,15)
OR_WaterPurifier.windows([1320,1380],[360,540],0.3)
OR_Iron = OR.Appliance(OR,1,1200,2,30,0.15,15, occasional_use=0.5)
OR_Iron.windows([480,780],[0,0],0.3)
OR_laptop = OR.Appliance(OR,1,50,2,60,0.15,30,occasional_use = 0.33)
OR_laptop.windows([480,840],[0,0],0.1)
OR_hairtrimmercharger = OR.Appliance(OR,1,5,2,30,0.15,15,occasional_use = 0.2)
OR_hairtrimmercharger.windows([480,780],[0,0],0.1)
OR_WashingMachine=OR.Appliance(OR,1,600,2,30,0.2,30, occasional_use=0.5)
OR_WashingMachine.windows([480,780],[0,0], 0.15)
OR_VacuumCleaner=OR.Appliance(OR,1,1000,2,30,0.2,30, occasional_use=0.5)
OR_VacuumCleaner.windows([420,600],[0,0], 0.15)
OR_MicroWaveOven=OR.Appliance(OR,1,1200,2,60,0.2,15, occasional_use=0.5)
OR_MicroWaveOven.windows([480,780],[0,0], 0.15)
OR_MusicSystem = OR.Appliance(OR,1,200,1,60,0.15,15, occasional_use=0.25)
OR_MusicSystem.windows([480,840],[0,0],0.3)
OR_BathroomGeyser = OR.Appliance(OR,1,2000,2,60,0.1,15, 'yes',1, occasional_use=.5)
OR_BathroomGeyser.windows([480,780],[1290,1350],0.1)
OR_BathroomGeyser.specific_cycle_1(2000,10,10,5)
OR_BathroomGeyser.cycle_behaviour([480,780],[1290,1350])
OR_MosquitoRepellent = OR.Appliance(OR,2,7,2,480,0.15,30)
OR_MosquitoRepellent.windows([480,780],[1290,1350],0.35)

