#CASE1
OR = User("Case1",2,1)
User_list.append(OR)
OR_indoor_Tubelight1 = OR.Appliance(OR,1,55,2,240,0.15,15)
OR_indoor_Tubelight1.windows([1050,1260],[360,420],0.1)
OR_indoor_Tubelight2 = OR.Appliance(OR,1,55,2,120,0.15,15,occasional_use = 0.5)
OR_indoor_Tubelight2.windows([1050,1260],[360,420],0.3)
OR_indoor_Tubelight3 = OR.Appliance(OR,1,55,2,240,0.15,15)
OR_indoor_Tubelight3.windows([1050,1260],[360,420],0.1)
OR_indoor_Tubelight4 = OR.Appliance(OR,1,55,2,120,0.15,15,occasional_use = 0.5)
OR_indoor_Tubelight4.windows([1050,1260],[0,0],0.3)
OR_lavatory_LEDBulb = OR.Appliance(OR,1,5,1,60,0.2,15)
OR_lavatory_LEDBulb.windows([360,1260],[0,0],0.1)
OR_Phone_charger = OR.Appliance(OR,1,5,1,150,0.3,15)
OR_Phone_charger.windows([360,1260],[0,0],0.35)
OR_TV=OR.Appliance(OR,1,60,1,180,0.25,30)
OR_TV.windows([840,1260],[0,0], 0.15)
OR_SetTopBox = OR.Appliance(OR,1,10,2,180,0.15,15)
OR_SetTopBox.windows([840,1260],[0,0],0.3)
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
OR_MixerGrinder = OR.Appliance(OR,1,500,2,60,0.15,15,occasional_use = 0.33)
OR_MixerGrinder.windows([720,900],[1080,1260],0.3)
OR_InductionCooktop = OR.Appliance(OR,1,2000,2,180,0.1,15, 'yes',1)
OR_InductionCooktop.windows([720,900],[1080,1200],0.15)
OR_InductionCooktop.specific_cycle_1(500,15,2000,5)
OR_InductionCooktop.cycle_behaviour([1080,1200],[750,900])
OR_Waterpurifier=OR.Appliance(OR,1,50,2,45,0.35, 15)
OR_Waterpurifier.windows([720,1260],[0,0], 0.35)
OR_Iron=OR.Appliance(OR,1,50,1,30,0.35, 15,occasional_use = 0.3)
OR_Iron.windows([900,1260],[0,0], 0.35)
OR_laptop = OR.Appliance(OR,1,50,2,60,0.15,30,occasional_use = 0.33)
OR_laptop.windows([720,1260],[0,0],0.1)
OR_hairtrimmercharger = OR.Appliance(OR,1,5,2,30,0.15,15,occasional_use = 0.2)
OR_hairtrimmercharger.windows([840,1260],[0,0],0.1)
OR_WashingMachine=OR.Appliance(OR,1,600,2,30,0.2,30, occasional_use=0.5)
OR_WashingMachine.windows([360,1260],[0,0], 0.15)
OR_VacuumCleaner=OR.Appliance(OR,1,1000,2,30,0.2,30, occasional_use=0.5)
OR_VacuumCleaner.windows([360,1260],[0,0], 0.15)
OR_MicroWaveOven=OR.Appliance(OR,1,1200,2,60,0.2,15, occasional_use=0.5)
OR_MicroWaveOven.windows([360,1260],[0,0], 0.15)
OR_MusicSystem = OR.Appliance(OR,1,200,1,60,0.15,15, occasional_use=0.25)
OR_MusicSystem.windows([720,1260],[0,0],0.3)
OR_WaterPump = OR.Appliance(OR,1,500,2,30,0.15,15, occasional_use=0.5)
OR_WaterPump.windows([360,540],[1080,1260],0.3)
OR_BathroomGeyser = OR.Appliance(OR,1,2000,2,60,0.1,15, 'yes',1)
OR_BathroomGeyser.windows([360,540],[720,900],0.1)
OR_BathroomGeyser.specific_cycle_1(2000,10,10,5)
OR_BathroomGeyser.cycle_behaviour([360,540],[720,900])
OR_RoomHeater = OR.Appliance(OR,1,2000,2,240,0.1,30, 'yes',1, occasional_use = 0.5)
OR_RoomHeater.windows([1080,1260],[0,0],0.1)
OR_RoomHeater.specific_cycle_1(20,20,2000,10)
OR_RoomHeater.cycle_behaviour([1080,1260],[0,0])

#CASE2
OR1 = User("Case2",4,1)
User_list.append(OR1)
OR1_indoor_LEDBulb = OR1.Appliance(OR1,1,7,2,240,0.15,15)
OR1_indoor_LEDBulb.windows([1080,1260],[360,420],0.1)
OR1_indoor_LEDBulb1 = OR1.Appliance(OR1,1,7,2,240,0.15,15, occasional_use=0.5)
OR1_indoor_LEDBulb1.windows([1080,1260],[360,420],0.1)
OR1_lavatory_LEDBulb = OR1.Appliance(OR1,1,5,2,45,0.2,15)
OR1_lavatory_LEDBulb.windows([360,1260],[0,0], 0.1)
OR1_Phone_charger = OR1.Appliance(OR1,1,5,2,150,0.3,15)
OR1_Phone_charger.windows([360,1260],[0,0],0.35)
OR1_TV=OR1.Appliance(OR1,1,60,2,180,0.25,30)
OR1_TV.windows([840,1260],[0,0], 0.15)
OR1_ImmersionHeater = OR1.Appliance(OR1,1,1000,2,45,0.3,15)
OR1_ImmersionHeater.windows([360,1260],[0,0],0.35)

#CASE3
OR2 = User("Case3",2,1)
User_list.append(OR2)
OR2_indoor_Tubelight1 = OR2.Appliance(OR2,1,55,2,240,0.15,15)
OR2_indoor_Tubelight1.windows([1050,1260],[360,420],0.1)
OR2_indoor_Tubelight2 = OR2.Appliance(OR2,1,55,2,120,0.15,15,occasional_use = 0.5)
OR2_indoor_Tubelight2.windows([1050,1260],[360,420],0.3)
OR2_indoor_Tubelight3 = OR2.Appliance(OR2,1,55,2,240,0.15,15)
OR2_indoor_Tubelight3.windows([1050,1260],[360,420],0.1)
OR2_indoor_Tubelight4 = OR2.Appliance(OR2,1,55,2,120,0.15,15,occasional_use = 0.5)
OR2_indoor_Tubelight4.windows([1050,1260],[0,0],0.3)
OR2_lavatory_LEDBulb = OR2.Appliance(OR2,1,5,1,60,0.2,15)
OR2_lavatory_LEDBulb.windows([360,1260],[0,0],0.1)
OR2_Phone_charger = OR2.Appliance(OR2,1,5,1,150,0.3,15)
OR2_Phone_charger.windows([360,1260],[0,0],0.35)
OR2_TV=OR2.Appliance(OR2,1,60,1,180,0.25,30)
OR2_TV.windows([840,1260],[0,0], 0.15)
OR2_SetTopBox = OR2.Appliance(OR2,1,10,2,180,0.15,15)
OR2_SetTopBox.windows([840,1260],[0,0],0.3)
OR2_KitchenTubelight=OR2.Appliance(OR2,1,40,2,240,0.15,15)
OR2_KitchenTubelight.windows([1050,1230],[720,900],0.2)
OR2_KitchenExhaustFan=OR2.Appliance(OR2,1,40,2,240,0.15,15)
OR2_KitchenExhaustFan.windows([1050,1230],[720,900],0.2)
OR2_balcony_LED = OR2.Appliance(OR2,1,9,1,30,0.15,5)
OR2_balcony_LED.windows([1080,1230],[0,0],0.1)
OR2_Fridge = OR2.Appliance(OR2,1,200,1,1440,0,45, 'yes',1)
OR2_Fridge.windows([0,1440],[0,0])
OR2_Fridge.specific_cycle_1(5,45,200,45)
OR2_Fridge.cycle_behaviour([0,1440],[0,0])
OR2_MixerGrinder = OR2.Appliance(OR2,1,500,2,60,0.15,15,occasional_use = 0.33)
OR2_MixerGrinder.windows([720,900],[1080,1260],0.3)
OR2_Waterpurifier=OR2.Appliance(OR2,1,50,2,45,0.35, 15)
OR2_Waterpurifier.windows([720,1260],[0,0], 0.35)
OR2_Iron=OR2.Appliance(OR2,1,50,1,30,0.35, 15,occasional_use = 0.3)
OR2_Iron.windows([900,1260],[0,0], 0.35)
OR2_laptop = OR2.Appliance(OR2,1,50,2,60,0.15,30)
OR2_laptop.windows([720,1260],[0,0],0.1)
OR2_hairtrimmercharger = OR2.Appliance(OR2,1,5,2,30,0.15,15,occasional_use = 0.2)
OR2_hairtrimmercharger.windows([840,1260],[0,0],0.1)
OR2_WashingMachine=OR2.Appliance(OR2,1,600,2,30,0.2,30, occasional_use=0.5)
OR2_WashingMachine.windows([360,1260],[0,0], 0.15)
OR2_MicroWaveOven=OR2.Appliance(OR2,1,1200,2,60,0.2,15, occasional_use=0.5)
OR2_MicroWaveOven.windows([360,1260],[0,0], 0.15)
OR2_WaterPump = OR2.Appliance(OR2,1,500,2,30,0.15,15, occasional_use=0.5)
OR2_WaterPump.windows([360,540],[1080,1260],0.3)
OR2_BathroomGeyser = OR2.Appliance(OR2,1,2000,2,60,0.1,15, 'yes',1)
OR2_BathroomGeyser.windows([360,540],[720,900],0.1)
OR2_BathroomGeyser.specific_cycle_1(2000,10,10,5)
OR2_BathroomGeyser.cycle_behaviour([360,540],[720,900])

#CASE4
OR3 = User("Case4",1,1)
User_list.append(OR3)
OR3_indoor_Tubelight1 = OR3.Appliance(OR3,1,55,2,240,0.15,15)
OR3_indoor_Tubelight1.windows([1050,1260],[360,420],0.1)
OR3_indoor_Tubelight2 = OR3.Appliance(OR3,1,55,2,120,0.15,15,occasional_use = 0.5)
OR3_indoor_Tubelight2.windows([1050,1260],[360,420],0.3)
OR3_indoor_Tubelight3 = OR3.Appliance(OR3,1,55,2,240,0.15,15)
OR3_indoor_Tubelight3.windows([1050,1260],[360,420],0.1)
OR3_indoor_Tubelight4 = OR3.Appliance(OR3,1,55,2,120,0.15,15,occasional_use = 0.5)
OR3_indoor_Tubelight4.windows([1050,1260],[0,0],0.3)
OR3_lavatory_LEDBulb = OR3.Appliance(OR3,1,5,1,60,0.2,15)
OR3_lavatory_LEDBulb.windows([360,1260],[0,0],0.1)
OR3_Phone_charger = OR3.Appliance(OR3,2,5,1,150,0.3,15)
OR3_Phone_charger.windows([360,1260],[0,0],0.35)
OR3_TV=OR2.Appliance(OR3,1,60,1,180,0.25,30)
OR3_TV.windows([840,1260],[0,0], 0.15)
OR3_SetTopBox = OR3.Appliance(OR3,1,10,2,180,0.15,15)
OR3_SetTopBox.windows([840,1260],[0,0],0.3)
OR3_KitchenTubelight=OR3.Appliance(OR3,1,40,2,240,0.15,15)
OR3_KitchenTubelight.windows([1050,1230],[720,900],0.2)
OR3_KitchenExhaustFan=OR3.Appliance(OR3,1,40,2,240,0.15,15)
OR3_KitchenExhaustFan.windows([1050,1230],[720,900],0.2)
OR3_balcony_LED = OR3.Appliance(OR3,1,9,1,30,0.15,5)
OR3_balcony_LED.windows([1080,1230],[0,0],0.1)
OR3_Fridge = OR3.Appliance(OR3,1,200,1,1440,0,45, 'yes',1)
OR3_Fridge.windows([0,1440],[0,0])
OR3_Fridge.specific_cycle_1(5,45,200,45)
OR3_Fridge.cycle_behaviour([0,1440],[0,0])
OR3_MixerGrinder = OR3.Appliance(OR3,1,500,2,60,0.15,15,occasional_use = 0.33)
OR3_MixerGrinder.windows([720,900],[1080,1260],0.3)
OR3_Waterpurifier=OR3.Appliance(OR3,1,50,2,45,0.35, 15)
OR3_Waterpurifier.windows([720,1260],[0,0], 0.35)
OR3_Iron=OR3.Appliance(OR3,1,50,1,30,0.35, 15,occasional_use = 0.3)
OR3_Iron.windows([900,1260],[0,0], 0.35)
OR3_RoomHeater = OR3.Appliance(OR3,1,2000,2,240,0.1,30, 'yes',1, occasional_use = 0.5)
OR3_RoomHeater.windows([1080,1260],[0,0],0.1)
OR3_RoomHeater.specific_cycle_1(20,20,2000,10)
OR3_RoomHeater.cycle_behaviour([1080,1260],[0,0])
OR3_BathroomGeyser = OR3.Appliance(OR3,1,2000,2,60,0.1,15, 'yes',1)
OR3_BathroomGeyser.windows([360,540],[720,900],0.1)
OR3_BathroomGeyser.specific_cycle_1(2000,10,10,5)
OR3_BathroomGeyser.cycle_behaviour([360,540],[720,900])

#CASE5
OR4 = User("Case5",2,1)
User_list.append(OR4)
OR4_indoor_Tubelight1 = OR4.Appliance(OR4,1,55,2,240,0.15,15)
OR4_indoor_Tubelight1.windows([1050,1260],[360,420],0.1)
OR4_indoor_Tubelight2 = OR4.Appliance(OR4,1,55,2,120,0.15,15,occasional_use = 0.5)
OR4_indoor_Tubelight2.windows([1050,1260],[360,420],0.3)
OR4_lavatory_LEDBulb = OR4.Appliance(OR4,1,5,1,60,0.2,15)
OR4_lavatory_LEDBulb.windows([360,1260],[0,0],0.1)
OR4_Phone_charger = OR4.Appliance(OR4,1,5,1,150,0.3,15)
OR4_Phone_charger.windows([360,1260],[0,0],0.35)
OR4_TV=OR4.Appliance(OR4,1,60,1,180,0.25,30)
OR4_TV.windows([840,1260],[0,0], 0.15)
OR4_SetTopBox = OR4.Appliance(OR4,1,10,2,180,0.15,15)
OR4_SetTopBox.windows([840,1260],[0,0],0.3)
OR4_KitchenTubelight=OR4.Appliance(OR4,1,40,2,240,0.15,15, occasional_use=0.5)
OR4_KitchenTubelight.windows([1050,1230],[720,900],0.2)
OR4_KitchenExhaustFan=OR4.Appliance(OR4,1,40,2,240,0.15,15, occasional_use=0.5)
OR4_KitchenExhaustFan.windows([1050,1230],[720,900],0.2)
OR4_Fridge = OR4.Appliance(OR4,1,200,1,1440,0,45, 'yes',1)
OR4_Fridge.windows([0,1440],[0,0])
OR4_Fridge.specific_cycle_1(5,45,200,45)
OR4_Fridge.cycle_behaviour([0,1440],[0,0])
OR4_Waterpurifier=OR4.Appliance(OR4,1,50,2,45,0.35, 15)
OR4_Waterpurifier.windows([720,1260],[0,0], 0.35)
OR4_BathroomGeyser = OR4.Appliance(OR4,1,2000,2,60,0.1,15, 'yes',1)
OR4_BathroomGeyser.windows([360,540],[720,900],0.1)
OR4_BathroomGeyser.specific_cycle_1(2000,10,10,5)
OR4_BathroomGeyser.cycle_behaviour([360,540],[720,900])

#CASE6
OR5 = User("Case6",1,1)
User_list.append(OR5)
OR5_indoor_Tubelight1 = OR5.Appliance(OR5,1,55,2,240,0.15,15)
OR5_indoor_Tubelight1.windows([1050,1260],[360,420],0.1)
OR5_indoor_Tubelight2 = OR5.Appliance(OR5,1,55,2,120,0.15,15,occasional_use = 0.5)
OR5_indoor_Tubelight2.windows([1050,1260],[360,420],0.3)
OR5_indoor_Tubelight3 = OR5.Appliance(OR5,1,55,2,240,0.15,15)
OR5_indoor_Tubelight3.windows([1050,1260],[360,420],0.1)
OR5_indoor_Tubelight4 = OR5.Appliance(OR5,1,55,2,120,0.15,15,occasional_use = 0.5)
OR5_indoor_Tubelight4.windows([1050,1260],[0,0],0.3)
OR5_lavatory_LEDBulb = OR5.Appliance(OR5,1,5,1,60,0.2,15)
OR5_lavatory_LEDBulb.windows([360,1260],[0,0],0.1)
OR5_Phone_charger = OR5.Appliance(OR5,2,5,1,150,0.3,15)
OR5_Phone_charger.windows([360,1260],[0,0],0.35)
OR5_TV=OR5.Appliance(OR5,1,60,1,180,0.25,30)
OR5_TV.windows([840,1260],[0,0], 0.15)
OR5_SetTopBox = OR5.Appliance(OR5,1,10,2,180,0.15,15)
OR5_SetTopBox.windows([840,1260],[0,0],0.3)
OR5_KitchenTubelight=OR5.Appliance(OR5,1,40,2,240,0.15,15)
OR5_KitchenTubelight.windows([1050,1230],[720,900],0.2)
OR5_KitchenExhaustFan=OR5.Appliance(OR5,1,40,2,240,0.15,15)
OR5_KitchenExhaustFan.windows([1050,1230],[720,900],0.2)
OR5_balcony_LED = OR5.Appliance(OR5,1,9,1,30,0.15,5)
OR5_balcony_LED.windows([1080,1230],[0,0],0.1)
OR5_Fridge = OR5.Appliance(OR5,1,200,1,1440,0,45, 'yes',1)
OR5_Fridge.windows([0,1440],[0,0])
OR5_Fridge.specific_cycle_1(5,45,200,45)
OR5_Fridge.cycle_behaviour([0,1440],[0,0])
OR5_MixerGrinder = OR5.Appliance(OR5,1,500,2,60,0.15,15,occasional_use = 0.33)
OR5_MixerGrinder.windows([720,900],[1080,1260],0.3)
OR5_Waterpurifier=OR5.Appliance(OR5,1,50,2,45,0.35, 15)
OR5_Waterpurifier.windows([720,1260],[0,0], 0.35)
OR5_Iron=OR5.Appliance(OR5,1,50,1,30,0.35, 15,occasional_use = 0.3)
OR5_Iron.windows([900,1260],[0,0], 0.35)
OR5_BathroomGeyser = OR5.Appliance(OR5,1,2000,2,60,0.1,15, 'yes',1)
OR5_BathroomGeyser.windows([360,540],[720,900],0.1)
OR5_BathroomGeyser.specific_cycle_1(2000,10,10,5)
OR5_BathroomGeyser.cycle_behaviour([360,540],[720,900])
