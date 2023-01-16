
OR = User("Case1",2,1)
User_list.append(OR)
OR_indoor_Tubelight1 = OR.Appliance(OR,1,55,2,420,0.15,15,occasional_use = 0.75)
OR_indoor_Tubelight1.windows([1080,1440],[300,420],0.1)
OR_indoor_Tubelight2 = OR.Appliance(OR,1,55,2,180,0.15,15, occasional_use = 0.165)
OR_indoor_Tubelight2.windows([1080,1440],[300,420],0.3)
OR_lavatory_LEDBulb = OR.Appliance(OR,1,5,1,90,0.2,5,occasional_use = 0.75)
OR_lavatory_LEDBulb.windows([360,1440],[0,0],0.3)
OR_Phone_charger = OR.Appliance(OR,1,5,2,200,0.3,15,occasional_use = 0.75)
OR_Phone_charger.windows([1082,1440],[480,1078],0.35)
OR_TV=OR.Appliance(OR,1,60,1,720,0.2,30,occasional_use = 0.75)
OR_TV.windows([480,1440],[0,0],0.15)
OR_KitchenTubelight=OR.Appliance(OR,1,40,2,300,0.15,15, occasional_use = 0.75)
OR_KitchenTubelight.windows([1140,1380],[360,540],0.2)
OR_KitchenExhaustFan=OR.Appliance(OR,1,40,3,240,0.15,15, occasional_use = 0.75)
OR_KitchenExhaustFan.windows([720,900],[1140,1380],0.2,[420,600])
OR_balcony_LED = OR.Appliance(OR,1,9,1,30,0.15,5, occasional_use = 0.75)
OR_balcony_LED.windows([1080,1440],[0,0],0.1)
OR_Fridge = OR.Appliance(OR,1,200,1,1440,0,45, 'yes',1 )
OR_Fridge.windows([0,1440],[0,0])
OR_Fridge.specific_cycle_1(5,45,200,45)
OR_Fridge.cycle_behaviour([0,1440],[0,0])
OR_MixerGrinder = OR.Appliance(OR,1,500,2,90,0.15,15, occasional_use = 0.165)
OR_MixerGrinder.windows([720,900],[1080,1380],0.35)
OR_SetTopBox = OR.Appliance(OR,1,10,1,720,0.15,15, occasional_use = 0.75)
OR_SetTopBox.windows([480,1440],[0,0],0.35)
OR_MosquitoRepellent = OR.Appliance(OR,1,7,2,480,0.15,30, occasional_use = 0.5)
OR_MosquitoRepellent.windows([1200,1440],[0,360],0.35)
OR_InductionCooktop = OR.Appliance(OR,1,2000,3,300,0.1,15, 'yes',1, occasional_use = 0.75)
OR_InductionCooktop.windows([720,900],[1110,1350],0.15,[480,540])
OR_InductionCooktop.specific_cycle_1(500,15,2000,15)
OR_InductionCooktop.cycle_behaviour([1110,1350],[480,900])
OR_Waterpurifier=OR.Appliance(OR,1,50,2,45,0.35, 15, occasional_use = 0.75)
OR_Waterpurifier.windows([720,1320],[0,0], 0.35)
OR_Iron=OR.Appliance(OR,1,50,1,30,0.35, 15,occasional_use = 0.15)
OR_Iron.windows([360,1230],[0,0], 0.35)
OR_BathroomGeyser = OR.Appliance(OR,1,2000,2,60,0.1,15, 'yes',1)
OR_BathroomGeyser.windows([720,900],[300,360],0.1)
OR_BathroomGeyser.specific_cycle_1(2000,10,100,20)
OR_BathroomGeyser.cycle_behaviour([720,900],[300,360])

#Case2
OR1 = User("Case2",4,1)
User_list.append(OR1)
OR1_indoor_Tubelight1 = OR1.Appliance(OR1,1,55,2,420,0.15,15,occasional_use = 0.75)
OR1_indoor_Tubelight1.windows([1080,1440],[300,420],0.1)
OR1_indoor_Tubelight2 = OR1.Appliance(OR1,1,55,2,180,0.15,15, occasional_use = 0.165)
OR1_indoor_Tubelight2.windows([1080,1440],[300,420],0.3)
OR1_lavatory_LEDBulb = OR1.Appliance(OR1,1,5,1,90,0.2,5,occasional_use = 0.75)
OR1_lavatory_LEDBulb.windows([360,1440],[0,0],0.3)
OR1_Phone_charger = OR1.Appliance(OR1,1,5,2,200,0.3,15,occasional_use = 0.75)
OR1_Phone_charger.windows([1082,1440],[480,1078],0.35)
OR1_TV=OR1.Appliance(OR1,1,60,1,720,0.2,30,occasional_use = 0.75)
OR1_TV.windows([480,1440],[0,0],0.15)
OR1_KitchenTubelight=OR1.Appliance(OR1,1,40,2,300,0.15,15, occasional_use = 0.75)
OR1_KitchenTubelight.windows([1140,1380],[360,540],0.2)
OR1_KitchenExhaustFan=OR1.Appliance(OR1,1,40,3,240,0.15,15, occasional_use = 0.75)
OR1_KitchenExhaustFan.windows([720,900],[1140,1380],0.2,[420,600])
OR1_balcony_LED = OR1.Appliance(OR1,1,9,1,30,0.15,5, occasional_use = 0.75)
OR1_balcony_LED.windows([1080,1440],[0,0],0.1)
OR1_Fridge = OR1.Appliance(OR1,1,200,1,1440,0,45, 'yes',1 )
OR1_Fridge.windows([0,1440],[0,0])
OR1_Fridge.specific_cycle_1(5,45,200,45)
OR1_Fridge.cycle_behaviour([0,1440],[0,0])
OR1_MixerGrinder = OR1.Appliance(OR1,1,500,2,90,0.15,15, occasional_use = 0.165)
OR1_MixerGrinder.windows([720,900],[1080,1380],0.35)
OR1_SetTopBox = OR1.Appliance(OR1,1,10,1,720,0.15,15, occasional_use = 0.75)
OR1_SetTopBox.windows([480,1440],[0,0],0.35)
OR1_Waterpurifier=OR1.Appliance(OR1,1,50,2,45,0.35, 15, occasional_use = 0.75)
OR1_Waterpurifier.windows([720,1320],[0,0], 0.35)
OR1_Iron=OR1.Appliance(OR1,1,50,1,30,0.35, 15,occasional_use = 0.15)
OR1_Iron.windows([360,1260],[0,0], 0.35)
OR1_BathroomGeyser = OR1.Appliance(OR1,1,2000,1,60,0.1,15, 'yes',1)
OR1_BathroomGeyser.windows([420,900],[0,0],0.1)
OR1_BathroomGeyser.specific_cycle_1(2000,10,100,30)
OR1_BathroomGeyser.cycle_behaviour([720,900],[300,360])


#Case3
OR2 = User("Case3",3,1)
User_list.append(OR2)
OR2_indoor_Tubelight1 = OR2.Appliance(OR2,1,55,2,420,0.15,15,occasional_use = 0.75)
OR2_indoor_Tubelight1.windows([1080,1440],[300,420],0.1)
OR2_lavatory_LEDBulb = OR2.Appliance(OR2,1,5,1,90,0.2,5,occasional_use = 0.75)
OR2_lavatory_LEDBulb.windows([360,1440],[0,0],0.3)
OR2_Phone_charger = OR2.Appliance(OR2,1,5,2,200,0.3,15,occasional_use = 0.75)
OR2_Phone_charger.windows([1082,1440],[480,1078],0.35)
OR2_Laptop=OR2.Appliance(OR2,1,50,1,180,0.25,30)
OR2_Laptop.windows([840,1260],[0,0], 0.15)
OR2_Waterpurifier=OR2.Appliance(OR2,1,50,2,45,0.35, 15, occasional_use = 0.75)
OR2_Waterpurifier.windows([720,1320],[0,0], 0.35)
OR2_Iron=OR2.Appliance(OR2,1,50,1,30,0.35, 15,occasional_use = 0.15)
OR2_Iron.windows([360,1260],[0,0], 0.35)
OR2_outdoor_LED = OR2.Appliance(OR2,1,9,1,30,0.15,5,occasional_use = 0.75 )
OR2_outdoor_LED.windows([1080,1230],[0,0],0.1)
OR2_BathroomGeyser = OR2.Appliance(OR2,1,2000,1,60,0.1,15, 'yes',1)
OR2_BathroomGeyser.windows([420,900],[0,0],0.1)
OR2_BathroomGeyser.specific_cycle_1(2000,10,100,20)
OR2_BathroomGeyser.cycle_behaviour([720,900],[300,360])

#Case4
OR3 = User("Case4",3,1)
User_list.append(OR3)
OR3_indoor_LEDBulb = OR3.Appliance(OR3,1,9,2,420,0.15,15,occasional_use = 0.75)
OR3_indoor_LEDBulb.windows([1080,1440],[300,420],0.1)
OR3_lavatory_LEDBulb = OR3.Appliance(OR3,1,5,1,90,0.2,5,occasional_use = 0.75)
OR3_lavatory_LEDBulb.windows([360,1440],[0,0],0.3)
OR3_Phone_charger = OR3.Appliance(OR3,1,5,2,200,0.3,15,occasional_use = 0.75)
OR3_Phone_charger.windows([1082,1440],[480,1078],0.35)
OR3_TV=OR3.Appliance(OR3,1,60,1,720,0.2,30,occasional_use = 0.75)
OR3_TV.windows([480,1440],[0,0],0.15)
OR3_SetTopBox = OR3.Appliance(OR3,1,10,1,720,0.15,15, occasional_use = 0.75)
OR3_SetTopBox.windows([480,1440],[0,0],0.35)
OR3_ImmersonRod = OR3.Appliance(OR3,1,1000,1,60,0.1,15)
OR3_ImmersonRod.windows([420,900],[0,0],0.1)

#Case5
OR4 = User("Case5",2,1)
User_list.append(OR4)
OR4_indoor_LEDBulb = OR4.Appliance(OR4,1,9,2,420,0.15,15,occasional_use = 0.75)
OR4_indoor_LEDBulb.windows([1080,1440],[300,420],0.1)
OR4_lavatory_LEDBulb = OR4.Appliance(OR4,1,5,1,90,0.2,5,occasional_use = 0.75)
OR4_lavatory_LEDBulb.windows([360,1440],[0,0],0.3)
OR4_Phone_charger = OR4.Appliance(OR4,1,5,2,200,0.3,15,occasional_use = 0.75)
OR4_Phone_charger.windows([1082,1440],[480,1078],0.35)
OR4_InductionCooktop = OR4.Appliance(OR4,1,1500,3,240,0.1,15)
OR4_InductionCooktop.windows([720,900],[1110,1350],0.15, [420,600])
OR4_ImmersonRod = OR4.Appliance(OR4,1,1000,2,60,0.1,15)
OR4_ImmersonRod.windows([480,900],[0,0],0.1)

#Case6
OR5 = User("Case6",3,1)
User_list.append(OR5)
OR5_indoor_LEDBulb = OR5.Appliance(OR5,1,9,2,420,0.15,15,occasional_use = 0.5)
OR5_indoor_LEDBulb.windows([1080,1440],[300,420],0.1)
OR5_lavatory_LEDBulb = OR5.Appliance(OR5,1,5,1,90,0.2,5,occasional_use = 0.5)
OR5_lavatory_LEDBulb.windows([360,1440],[0,0],0.3)
OR5_Phone_charger = OR5.Appliance(OR5,1,5,2,200,0.3,15,occasional_use = 0.5)
OR5_Phone_charger.windows([1082,1440],[480,1078],0.35)


