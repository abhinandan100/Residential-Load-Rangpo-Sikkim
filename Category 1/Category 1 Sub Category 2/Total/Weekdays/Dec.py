

#Case1
#Case1
OR = User("Case1",2,1)
User_list.append(OR)
OR_indoor_Tubelight1 = OR.Appliance(OR,1,55,2,240,0.15,15)
OR_indoor_Tubelight1.windows([1050,1260],[360,420],0.1)
OR_indoor_Tubelight2 = OR.Appliance(OR,1,55,2,120,0.15,15,occasional_use = 0.33)
OR_indoor_Tubelight2.windows([1050,1260],[330,390],0.3)
OR_lavatory_LEDBulb = OR.Appliance(OR,1,5,1,60,0.2,15)
OR_lavatory_LEDBulb.windows([360,1260],[0,0],0.1)
OR_Phone_charger = OR.Appliance(OR,1,5,1,150,0.3,15)
OR_Phone_charger.windows([360,1260],[0,0],0.35)
OR_TV=OR.Appliance(OR,1,60,1,180,0.25,30)
OR_TV.windows([840,1260],[0,0], 0.15)
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
OR_MixerGrinder = OR.Appliance(OR,1,500,2,60,0.15,15,occasional_use = 0.33 )
OR_MixerGrinder.windows([750,900],[1080,1200],0.3)
OR_SetTopBox = OR.Appliance(OR,1,10,2,180,0.15,15)
OR_SetTopBox.windows([840,1230],[0,0],0.3)
OR_InductionCooktop = OR.Appliance(OR,1,2000,2,180,0.1,15, 'yes',1)
OR_InductionCooktop.windows([720,900],[1080,1200],0.15)
OR_InductionCooktop.specific_cycle_1(500,15,2000,5)
OR_InductionCooktop.cycle_behaviour([1080,1200],[750,900])
OR_Waterpurifier=OR.Appliance(OR,1,50,2,45,0.35, 15)
OR_Waterpurifier.windows([720,1230],[0,0], 0.35)
OR_Iron=OR.Appliance(OR,1,50,1,30,0.35, 15,occasional_use = 0.3)
OR_Iron.windows([900,1230],[0,0], 0.35)
OR_BathroomGeyser = OR.Appliance(OR,1,2000,2,60,0.1,15, 'yes',1)
OR_BathroomGeyser.windows([720,900],[300,360],0.1)
OR_BathroomGeyser.specific_cycle_1(2000,10,100,20)
OR_BathroomGeyser.cycle_behaviour([720,900],[300,360])

#Case2
OR1 = User("Case2",4,1)
User_list.append(OR1)

OR1_indoor_Tubelight1 = OR1.Appliance(OR1,1,55,2,240,0.15,15)
OR1_indoor_Tubelight1.windows([1050,1260],[360,420],0.1)
OR1_indoor_Tubelight2 = OR1.Appliance(OR1,1,55,2,120,0.15,15,occasional_use = 0.33)
OR1_indoor_Tubelight2.windows([1050,1260],[330,390],0.3)
OR1_lavatory_LEDBulb = OR1.Appliance(OR1,1,5,1,60,0.2,15)
OR1_lavatory_LEDBulb.windows([360,1260],[0,0],0.1)
OR1_Phone_charger = OR1.Appliance(OR1,1,5,1,150,0.3,15)
OR1_Phone_charger.windows([360,1260],[0,0],0.35)
OR1_TV=OR1.Appliance(OR1,1,60,1,180,0.25,30)
OR1_TV.windows([840,1260],[0,0], 0.15)
OR1_KitchenTubelight=OR1.Appliance(OR1,1,40,2,240,0.15,15)
OR1_KitchenTubelight.windows([1050,1230],[720,900],0.2)
OR1_KitchenExhaustFan=OR1.Appliance(OR1,1,40,2,240,0.15,15)
OR1_KitchenExhaustFan.windows([1050,1230],[720,900],0.2)
OR1_balcony_LED = OR1.Appliance(OR1,1,9,1,30,0.15,5,occasional_use = 0.75 )
OR1_balcony_LED.windows([1080,1230],[0,0],0.1)
OR1_Fridge = OR1.Appliance(OR1,1,200,1,1440,0,45, 'yes',1)
OR1_Fridge.windows([0,1440],[0,0])
OR1_Fridge.specific_cycle_1(5,45,200,45)
OR1_Fridge.cycle_behaviour([0,720],[721,1440])
OR1_MixerGrinder = OR1.Appliance(OR1,1,500,2,60,0.15,15,occasional_use = 0.33 )
OR1_MixerGrinder.windows([750,900],[1080,1200],0.3)
OR1_SetTopBox = OR1.Appliance(OR1,1,10,2,180,0.15,15)
OR1_SetTopBox.windows([840,1230],[0,0],0.3)
OR1_Waterpurifier=OR1.Appliance(OR1,1,50,2,45,0.35, 15)
OR1_Waterpurifier.windows([720,1230],[0,0], 0.35)
OR1_Iron=OR1.Appliance(OR1,1,50,1,30,0.35, 15,occasional_use = 0.3)
OR1_Iron.windows([900,1230],[0,0], 0.35)
OR1_BathroomGeyser = OR1.Appliance(OR1,1,2000,2,60,0.1,15, 'yes',1)
OR1_BathroomGeyser.windows([720,900],[300,360],0.1)
OR1_BathroomGeyser.specific_cycle_1(2000,10,100,20)
OR1_BathroomGeyser.cycle_behaviour([720,900],[300,360])

#Case3
OR2 = User("Case3",3,1)
User_list.append(OR2)

OR2_indoor_Tubelight1 = OR2.Appliance(OR2,1,55,2,240,0.15,15)
OR2_indoor_Tubelight1.windows([1050,1260],[360,420],0.1)
OR2_lavatory_LEDBulb = OR2.Appliance(OR2,1,5,1,60,0.2,15)
OR2_lavatory_LEDBulb.windows([360,1260],[0,0],0.1)
OR2_Phone_charger = OR2.Appliance(OR2,1,5,1,150,0.3,15)
OR2_Phone_charger.windows([360,1260],[0,0],0.35)
OR2_Laptop=OR2.Appliance(OR2,1,50,1,180,0.25,30)
OR2_Laptop.windows([840,1260],[0,0], 0.15)
OR2_SetTopBox = OR2.Appliance(OR2,1,10,2,180,0.15,15)
OR2_SetTopBox.windows([840,1230],[0,0],0.3)
OR2_Waterpurifier=OR2.Appliance(OR2,1,50,2,45,0.35, 15)
OR2_Waterpurifier.windows([720,1230],[0,0], 0.35)
OR2_Iron=OR2.Appliance(OR2,1,50,1,30,0.35, 15,occasional_use = 0.15)
OR2_Iron.windows([900,1230],[0,0], 0.35)
OR2_outdoor_LED = OR2.Appliance(OR2,1,9,1,30,0.15,5,occasional_use = 0.75 )
OR2_outdoor_LED.windows([1080,1230],[0,0],0.1)
OR2_BathroomGeyser = OR2.Appliance(OR2,1,2000,2,60,0.1,15, 'yes',1)
OR2_BathroomGeyser.windows([720,900],[300,360],0.1)
OR2_BathroomGeyser.specific_cycle_1(2000,10,100,20)
OR2_BathroomGeyser.cycle_behaviour([720,900],[300,360])

#Case4
OR3 = User("Case4",3,1)
User_list.append(OR3)

OR3_indoor_LEDBulb = OR3.Appliance(OR3,1,9,2,240,0.15,15)
OR3_indoor_LEDBulb.windows([1050,1260],[360,420],0.1)
OR3_lavatory_LEDBulb = OR3.Appliance(OR3,1,9,1,60,0.2,15)
OR3_lavatory_LEDBulb.windows([360,1260],[0,0],0.1)
OR3_Phone_charger = OR3.Appliance(OR3,1,5,1,150,0.3,15)
OR3_Phone_charger.windows([360,1260],[0,0],0.35)
OR3_TV=OR3.Appliance(OR3,1,60,1,180,0.25,30)
OR3_TV.windows([840,1260],[0,0], 0.15)
OR3_SetTopBox = OR3.Appliance(OR3,1,10,2,180,0.15,15)
OR3_SetTopBox.windows([840,1230],[0,0],0.3)
OR3_ImmersonRod = OR3.Appliance(OR3,1,1000,2,60,0.1,15)
OR3_ImmersonRod.windows([720,900],[300,360],0.1)

#Case5
OR4 = User("Case5",2,1)
User_list.append(OR4)

OR4_indoor_LEDBulb = OR4.Appliance(OR4,1,9,2,240,0.15,15)
OR4_indoor_LEDBulb.windows([1050,1260],[360,420],0.1)
OR4_lavatory_LEDBulb = OR4.Appliance(OR4,1,9,1,60,0.2,15)
OR4_lavatory_LEDBulb.windows([360,1260],[0,0],0.1)
OR4_Phone_charger = OR4.Appliance(OR4,1,5,1,150,0.3,15)
OR4_Phone_charger.windows([360,1260],[0,0],0.35)
OR4_InductionCooktop = OR4.Appliance(OR4,1,1500,2,240,0.1,15)
OR4_InductionCooktop.windows([720,900],[1080,1200],0.15)
OR4_ImmersonRod = OR4.Appliance(OR4,1,1000,2,60,0.1,15)
OR4_ImmersonRod.windows([720,900],[300,360],0.1)

#Case6
OR5 = User("Case6",3,1)
User_list.append(OR5)
OR5_indoor_LEDBulb = OR5.Appliance(OR5,1,7,2,240,0.15,15)
OR5_indoor_LEDBulb.windows([1080,1260],[360,420],0.1)
OR5_lavatory_LEDBulb = OR5.Appliance(OR5,1,5,2,45,0.2,15)
OR5_lavatory_LEDBulb.windows([360,1260],[0,0],0.1)
OR5_Phone_charger = OR5.Appliance(OR5,1,5,1,150,0.3,15)
OR5_Phone_charger.windows([360,900],[901,1230],0.35)

