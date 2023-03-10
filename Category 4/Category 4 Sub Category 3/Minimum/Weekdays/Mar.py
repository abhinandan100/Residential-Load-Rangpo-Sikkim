#One-Room Minimum Connected Load
#Create new user classes
OR = User("One room minimal",1,1)
User_list.append(OR)

#One-Room Minimum Connected Load
OR_indoor_LED1 = OR.Appliance(OR,2,9,2,360,0.15,15)
OR_indoor_LED1.windows([1080,1440],[0,60],0.15)
OR_indoor_Tubelights2 = OR.Appliance(OR,2,55,2,120,0.15,15,occasional_use = 0.5)
OR_indoor_Tubelights2.windows([1080,1440],[0,0],0.3)
OR_lavatory_LED = OR.Appliance(OR,2,9,2,60,0.2,5)
OR_lavatory_LED.windows([360,1440],[0,120],0.1)
OR_Phone_charger = OR.Appliance(OR,3,5,2,180,0.3,15)
OR_Phone_charger.windows([0,1440],[0,0],0.35)
OR_TV=OR.Appliance(OR,1,60,2,420,0.2,30)
OR_TV.windows([420,1410],[0,0], 0.35)
OR_SetTopBox = OR.Appliance(OR,1,10,2,420,0.2,30)
OR_SetTopBox.windows([420,1410],[0,0],0.35)
OR_KitchenTubelight=OR.Appliance(OR,1,40,2,240,0.15,15,occasional_use = 0.2 )
OR_KitchenTubelight.windows([1140,1380],[0,0],0.25)
OR_KitchenLED=OR.Appliance(OR,1,7,2,240,0.15,15)
OR_KitchenLED.windows([1080,1380],[0,0],0.25)
OR_KitchenExhaustFan=OR.Appliance(OR,1,40,2,240,0.15,15)
OR_KitchenExhaustFan.windows([1140,1380],[360,600],0.2,[720,900])
OR_balcony_LED = OR.Appliance(OR,1,9,2,30,0.15,5)
OR_balcony_LED.windows([1080,1320],[0,0],0.1)
OR_Fridge = OR.Appliance(OR,1,200,1,1440,0,45, 'yes',1)
OR_Fridge.windows([0,1440],[0,0])
OR_Fridge.specific_cycle_1(5,45,200,45)
OR_Fridge.cycle_behaviour([0,1440],[0,0])
OR_WashingMachine=OR.Appliance(OR,1,600,2,120,0.2,30, occasional_use=0.75)
OR_WashingMachine.windows([420,840],[0,0],0.25)
OR_MixerGrinder = OR.Appliance(OR,1,500,2,60,0.15,15,occasional_use = 0.33)
OR_MixerGrinder.windows([1080,1320],[420,600],0.3, [720,900])
OR_Iron = OR.Appliance(OR,1,1200,1,30,0.15,15, occasional_use=0.5)
OR_Iron.windows([900,1320],[0,0],0.3)
OR_MosquitoRepellent = OR.Appliance(OR,2,7,2,480,0.15,30, occasional_use=0.5)
OR_MosquitoRepellent.windows([1080,1440],[0,360],0.35)



