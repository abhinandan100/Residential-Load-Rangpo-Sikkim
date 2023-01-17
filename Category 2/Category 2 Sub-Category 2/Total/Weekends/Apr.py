#CASE1
OR = User("Case1",2,1)
User_list.append(OR)
OR_indoor_Tubelight1 = OR.Appliance(OR,1,55,2,420,0.15,15, occasional_use = 0.5)
OR_indoor_Tubelight1.windows([1080,1440],[300,420],0.1)
OR_indoor_Tubelight2 = OR.Appliance(OR,1,55,2,120,0.15,15, occasional_use = 0.15)
OR_indoor_Tubelight2.windows([1080,1440],[300,420],0.3)
OR_indoor_Tubelight3 = OR.Appliance(OR,1,55,2,420,0.15,15, occasional_use = 0.5)
OR_indoor_Tubelight3.windows([1080,1440],[300,420],0.1)
OR_indoor_Tubelight4 = OR.Appliance(OR,1,55,2,120,0.15,15, occasional_use = 0.1)
OR_indoor_Tubelight4.windows([1080,1440],[300,420],0.3)
OR_lavatory_LEDBulb = OR.Appliance(OR,1,5,2,45,0.2,5,occasional_use = 0.5)
OR_lavatory_LEDBulb.windows([0,1440],[0,0],0.1)
OR_lavatory_LEDBulb1 = OR.Appliance(OR,1,5,2,30,0.2,5,occasional_use = 0.5)
OR_lavatory_LEDBulb1.windows([0,1440],[0,0],0.1)
OR_Phone_charger = OR.Appliance(OR,1,5,1,180,0.3,15, occasional_use = 0.5)
OR_Phone_charger.windows([0,1440],[0,0],0.35)
OR_Fan = OR.Appliance(OR,1,70, 2, 720,0.15, occasional_use=0.5)
OR_Fan.windows([480,1440],[0,0],0.2)
OR_Fan1 = OR.Appliance(OR,1,70, 2, 720,0.15,15,occasional_use=0.25)
OR_Fan1.windows([0,1440],[0,0],0.2)
OR_TV=OR.Appliance(OR,1,60,2,360,0.2,30,occasional_use = 0.5)
OR_TV.windows([540,1440],[0,0], 0.35)
OR_SetTopBox = OR.Appliance(OR,1,10,2,360,0.2,30,occasional_use=0.5)
OR_SetTopBox.windows([540,1400],[0,0],0.35)
OR_KitchenTubelight=OR.Appliance(OR,1,40,3,300,0.15,15,occasional_use = 0.5)
OR_KitchenTubelight.windows([1140,1380],[420,600],0.25,[720,900])
OR_KitchenExhaustFan=OR.Appliance(OR,1,40,2,180,0.15,15,occasional_use = 0.5)
OR_KitchenExhaustFan.windows([1140,1380],[420,600],0.2,[720,900])
OR_balcony_LED = OR.Appliance(OR,1,9,2,30,0.15,5, occasional_use = 0.5)
OR_balcony_LED.windows([1080,1159],[1201,1440],0.1)
OR_laptop = OR.Appliance(OR,1,50,1,240,0.15,30,occasional_use = 0.15)
OR_laptop.windows([540,1440],[0,0],0.1)
OR_hairtrimmercharger = OR.Appliance(OR,1,5,2,30,0.15,15,occasional_use = 0.1)
OR_hairtrimmercharger.windows([300,480],[0,0],0.1)
OR_Fridge = OR.Appliance(OR,1,200,1,1440,0,45, 'yes',1)
OR_Fridge.windows([0,1440],[0,0])
OR_Fridge.specific_cycle_1(5,45,200,45)
OR_Fridge.cycle_behaviour([0,1440],[0,0])
OR_WashingMachine=OR.Appliance(OR,1,600,2,120,0.2,30, occasional_use=0.5)
OR_WashingMachine.windows([480,720],[0,0],0.25)
OR_VacuumCleaner=OR.Appliance(OR,1,1000,2,30,0.2,30, occasional_use=0.5)
OR_VacuumCleaner.windows([480,720],[0,0], 0.15)
OR_MicroWaveOven=OR.Appliance(OR,1,1200,3,60,0.2,15, occasional_use=0.5)
OR_MicroWaveOven.windows([1080,1320],[420,600], 0.15, [720,900])
OR_MixerGrinder = OR.Appliance(OR,1,500,2,60,0.15,15,occasional_use = 0.33)
OR_MixerGrinder.windows([1080,1320],[420,600],0.3, [720,900])
OR_WaterPurifier = OR.Appliance(OR,1,60,2,60,0.15,15)
OR_WaterPurifier.windows([1080,1380],[420,900],0.3)
OR_Iron = OR.Appliance(OR,1,1200,1,30,0.15,15, occasional_use=0.5)
OR_Iron.windows([900,1320],[0,0],0.3)
OR_MusicSystem = OR.Appliance(OR,1,200,1,60,0.15,15, occasional_use=0.25)
OR_MusicSystem.windows([1080,1380],[480,900],0.3)
OR_WaterPump = OR.Appliance(OR,1,500,2,45,0.15,15,occasional_use=0.5)
OR_WaterPump.windows([360,540],[1080,1140],0.3, [720,900])
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

#CASE2
OR1 = User("Case2",4,1)
User_list.append(OR1)
OR1_indoor_LEDBulb = OR1.Appliance(OR1,1,7,2,480,0.35,15,occasional_use = 0.5)
OR1_indoor_LEDBulb.windows([1080,1440],[300,420],0.3)
OR1_indoor_LEDBulb1 = OR1.Appliance(OR1,1,7,2,480,0.35,15,occasional_use = 0.5)
OR1_indoor_LEDBulb1.windows([1080,1440],[300,420],0.3)
OR1_lavatory_LEDBulb = OR1.Appliance(OR1,1,5,2,60,0.35,5,occasional_use = 0.5)
OR1_lavatory_LEDBulb.windows([360,1440],[0,120], 0.35)
OR1_Phone_charger = OR1.Appliance(OR1,1,5,2,180,0.35,15,occasional_use = 0.5)
OR1_Phone_charger.windows([0,1440],[0,0],0.35)
OR1_Fan = OR1.Appliance(OR1,1,70, 2, 1260,0.35,15,occasional_use = 0.5)
OR1_Fan.windows([360,1440],[0,0],0.35)
OR1_Fan1 = OR1.Appliance(OR1,1,70, 2, 900,0.35,15,occasional_use = 0.5)
OR1_Fan1.windows([0,1440],[0,0],0.35)
OR1_TV=OR1.Appliance(OR1,1,60,2,180,0.25,30)
OR1_TV.windows([360,1440],[0,0], 0.15)


#CASE3
OR2 = User("Case3",2,1)
User_list.append(OR2)
OR2_indoor_Tubelight1 = OR2.Appliance(OR2,1,55,2,420,0.15,15, occasional_use = 0.5)
OR2_indoor_Tubelight1.windows([1080,1440],[300,420],0.1)
OR2_indoor_Tubelight2 = OR2.Appliance(OR2,1,55,2,120,0.15,15, occasional_use = 0.15)
OR2_indoor_Tubelight2.windows([1080,1440],[300,420],0.3)
OR2_indoor_Tubelight3 = OR2.Appliance(OR2,1,55,2,420,0.15,15, occasional_use = 0.5)
OR2_indoor_Tubelight3.windows([1080,1440],[300,420],0.1)
OR2_indoor_Tubelight4 = OR2.Appliance(OR2,1,55,2,120,0.15,15, occasional_use = 0.1)
OR2_indoor_Tubelight4.windows([1080,1440],[300,420],0.3)
OR2_lavatory_LEDBulb = OR2.Appliance(OR2,1,5,2,45,0.2,5,occasional_use = 0.5)
OR2_lavatory_LEDBulb.windows([0,1440],[0,0],0.1)
OR2_lavatory_LEDBulb1 = OR2.Appliance(OR2,1,5,2,30,0.2,5,occasional_use = 0.5)
OR2_lavatory_LEDBulb1.windows([0,1440],[0,0],0.1)
OR2_Phone_charger = OR2.Appliance(OR2,1,5,1,180,0.3,15, occasional_use = 0.5)
OR2_Phone_charger.windows([0,1440],[0,0],0.35)
OR2_Fan = OR2.Appliance(OR2,1,70, 2, 720,0.15, occasional_use=0.5)
OR2_Fan.windows([480,1440],[0,0],0.2)
OR2_Fan1 = OR2.Appliance(OR2,1,70, 2, 720,0.15,15,occasional_use=0.25)
OR2_Fan1.windows([0,1440],[0,0],0.2)
OR2_TV=OR2.Appliance(OR2,1,60,2,360,0.2,30,occasional_use = 0.5)
OR2_TV.windows([540,1440],[0,0], 0.35)
OR2_SetTopBox = OR2.Appliance(OR2,1,10,2,360,0.2,30,occasional_use=0.5)
OR2_SetTopBox.windows([540,1400],[0,0],0.35)
OR2_KitchenTubelight=OR2.Appliance(OR2,1,40,3,300,0.15,15,occasional_use = 0.5)
OR2_KitchenTubelight.windows([1140,1380],[420,600],0.25,[720,900])
OR2_KitchenExhaustFan=OR2.Appliance(OR2,1,40,2,180,0.15,15,occasional_use = 0.5)
OR2_KitchenExhaustFan.windows([1140,1380],[420,600],0.2,[720,900])
OR2_balcony_LED = OR2.Appliance(OR2,1,9,2,30,0.15,5, occasional_use = 0.5)
OR2_balcony_LED.windows([1080,1159],[1201,1440],0.1)
OR2_Fridge = OR2.Appliance(OR2,1,200,1,1440,0,45, 'yes',1)
OR2_Fridge.windows([0,1440],[0,0])
OR2_Fridge.specific_cycle_1(5,45,200,45)
OR2_Fridge.cycle_behaviour([0,1440],[0,0])
OR2_MixerGrinder = OR2.Appliance(OR2,1,500,2,60,0.15,15,occasional_use = 0.5)
OR2_MixerGrinder.windows([1080,1320],[420,600],0.3, [720,900])
OR2_WaterPurifier = OR2.Appliance(OR2,1,60,2,60,0.15,15)
OR2_WaterPurifier.windows([1080,1380],[420,900],0.3)
OR2_Iron = OR2.Appliance(OR2,1,1200,1,30,0.15,15, occasional_use=0.5)
OR2_Iron.windows([900,1320],[0,0],0.3)
OR2_laptop = OR2.Appliance(OR2,1,50,1,240,0.15,30,occasional_use = 0.15)
OR2_laptop.windows([540,1440],[0,0],0.1)
OR2_hairtrimmercharger = OR2.Appliance(OR2,1,5,2,30,0.15,15,occasional_use = 0.1)
OR2_hairtrimmercharger.windows([300,900],[0,0],0.1)
OR2_WashingMachine=OR2.Appliance(OR2,1,600,2,120,0.2,30, occasional_use=0.5)
OR2_WashingMachine.windows([480,720],[0,0],0.25)
OR2_MicroWaveOven=OR2.Appliance(OR2,1,1200,3,60,0.2,15, occasional_use=0.5)
OR2_MicroWaveOven.windows([1080,1320],[420,600], 0.15, [720,900])
OR2_WaterPump = OR2.Appliance(OR2,1,500,2,45,0.15,15,occasional_use=0.5)
OR2_WaterPump.windows([360,540],[1080,1140],0.3, [720,900])
OR2_BathroomGeyser = OR2.Appliance(OR2,1,2000,2,60,0.1,15, 'yes',1,occasional_use=0.5)
OR2_BathroomGeyser.windows([420,900],[0,0],0.1)
OR2_BathroomGeyser.specific_cycle_1(2000,10,10,5)
OR2_BathroomGeyser.cycle_behaviour([420,900],[0,0])

#CASE4
OR3 = User("Case4",2,1)
User_list.append(OR3)
OR3_indoor_Tubelight1 = OR3.Appliance(OR3,1,55,2,420,0.15,15, occasional_use = 0.5)
OR3_indoor_Tubelight1.windows([1080,1440],[300,420],0.1)
OR3_indoor_Tubelight2 = OR3.Appliance(OR3,1,55,2,120,0.15,15, occasional_use = 0.15)
OR3_indoor_Tubelight2.windows([1080,1440],[300,420],0.3)
OR3_indoor_Tubelight3 = OR3.Appliance(OR3,1,55,2,420,0.15,15, occasional_use = 0.5)
OR3_indoor_Tubelight3.windows([1080,1440],[300,420],0.1)
OR3_indoor_Tubelight4 = OR3.Appliance(OR3,1,55,2,120,0.15,15, occasional_use = 0.1)
OR3_indoor_Tubelight4.windows([1080,1440],[300,420],0.3)
OR3_Fan = OR3.Appliance(OR3,1,70, 2, 720,0.15, occasional_use=0.5)
OR3_Fan.windows([480,1440],[0,0],0.2)
OR3_Fan1 = OR3.Appliance(OR3,1,70, 2, 720,0.15,15,occasional_use=0.25)
OR3_Fan1.windows([0,1440],[0,0],0.2)
OR3_lavatory_LEDBulb = OR3.Appliance(OR3,1,5,2,45,0.2,5,occasional_use = 0.5)
OR3_lavatory_LEDBulb.windows([0,1440],[0,0],0.1)
OR3_Phone_charger = OR3.Appliance(OR3,1,5,1,180,0.3,15, occasional_use = 0.5)
OR3_Phone_charger.windows([0,1440],[0,0],0.35)
OR3_TV=OR3.Appliance(OR3,1,60,2,360,0.2,30,occasional_use = 0.5)
OR3_TV.windows([540,1440],[0,0], 0.35)
OR3_SetTopBox = OR3.Appliance(OR3,1,10,2,360,0.2,30,occasional_use=0.5)
OR3_SetTopBox.windows([540,1400],[0,0],0.35)
OR3_KitchenTubelight=OR3.Appliance(OR3,1,40,3,300,0.15,15,occasional_use = 0.5)
OR3_KitchenTubelight.windows([1140,1380],[420,600],0.25,[720,900])
OR3_KitchenExhaustFan=OR3.Appliance(OR3,1,40,2,180,0.15,15,occasional_use = 0.5)
OR3_KitchenExhaustFan.windows([1140,1380],[420,600],0.2,[720,900])
OR3_balcony_LED = OR3.Appliance(OR3,1,9,2,30,0.15,5, occasional_use = 0.5)
OR3_balcony_LED.windows([1080,1159],[1201,1440],0.1)
OR3_Fridge = OR3.Appliance(OR3,1,200,1,1440,0,45, 'yes',1)
OR3_Fridge.windows([0,1440],[0,0])
OR3_Fridge.specific_cycle_1(5,45,200,45)
OR3_Fridge.cycle_behaviour([0,1440],[0,0])
OR3_MixerGrinder = OR3.Appliance(OR3,1,500,2,60,0.15,15,occasional_use = 0.5)
OR3_MixerGrinder.windows([1080,1320],[420,600],0.3, [720,900])
OR3_WaterPurifier = OR3.Appliance(OR3,1,60,2,60,0.15,15)
OR3_WaterPurifier.windows([1080,1380],[420,900],0.3)
OR3_Iron = OR3.Appliance(OR3,1,1200,1,30,0.15,15, occasional_use=0.5)
OR3_Iron.windows([900,1320],[0,0],0.3)

#CASE5
OR4 = User("Case5",2,1)
OR4_indoor_Tubelight1 = OR4.Appliance(OR4,1,55,2,420,0.15,15, occasional_use = 0.5)
OR4_indoor_Tubelight1.windows([1080,1440],[300,420],0.1)
OR4_indoor_Tubelight2 = OR4.Appliance(OR4,1,55,2,120,0.15,15, occasional_use = 0.15)
OR4_indoor_Tubelight2.windows([1080,1440],[300,420],0.3)
OR4_indoor_Tubelight3 = OR4.Appliance(OR4,1,55,2,420,0.15,15, occasional_use = 0.5)
OR4_indoor_Tubelight3.windows([1080,1440],[300,420],0.1)
OR4_indoor_Tubelight4 = OR4.Appliance(OR4,1,55,2,120,0.15,15, occasional_use = 0.1)
OR4_indoor_Tubelight4.windows([1080,1440],[300,420],0.3)
OR4_Fan = OR4.Appliance(OR4,1,70, 2, 720,0.15, occasional_use=0.5)
OR4_Fan.windows([480,1440],[0,0],0.2)
OR4_Fan1 = OR4.Appliance(OR4,1,70, 2, 720,0.15,15,occasional_use=0.25)
OR4_Fan1.windows([0,1440],[0,0],0.2)
OR4_lavatory_LEDBulb = OR4.Appliance(OR4,1,5,2,45,0.2,5,occasional_use = 0.5)
OR4_lavatory_LEDBulb.windows([0,1440],[0,0],0.1)
OR4_Phone_charger = OR4.Appliance(OR4,1,5,1,180,0.3,15, occasional_use = 0.5)
OR4_Phone_charger.windows([0,1440],[0,0],0.35)
OR4_TV=OR4.Appliance(OR4,1,60,2,360,0.2,30,occasional_use = 0.5)
OR4_TV.windows([540,1440],[0,0], 0.35)
OR4_SetTopBox = OR4.Appliance(OR4,1,10,2,360,0.2,30,occasional_use=0.5)
OR4_SetTopBox.windows([540,1400],[0,0],0.35)
OR4_KitchenTubelight=OR4.Appliance(OR4,1,40,3,300,0.15,15,occasional_use = 0.5)
OR4_KitchenTubelight.windows([1140,1380],[420,600],0.25,[720,900])
OR4_KitchenExhaustFan=OR4.Appliance(OR4,1,40,2,180,0.15,15,occasional_use = 0.5)
OR4_KitchenExhaustFan.windows([1140,1380],[420,600],0.2,[720,900])
OR4_WaterPurifier = OR4.Appliance(OR4,1,60,2,60,0.15,15)
OR4_WaterPurifier.windows([1080,1380],[420,900],0.3)