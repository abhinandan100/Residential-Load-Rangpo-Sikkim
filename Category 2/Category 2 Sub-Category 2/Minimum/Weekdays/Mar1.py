#One-Room Minimum Connected Load
#Create new user classes
OR = User("One room minimal",1,1)
User_list.append(OR)

#One-Room Minimum Connected Load
OR_indoor_LEDBulb1 = OR.Appliance(OR,1,55,2,420,0.15,15)
OR_indoor_LEDBulb1.windows([1020,1320],[240,330],0.1)
OR_indoor_LEDBulb2 = OR.Appliance(OR,1,55,2,360,0.15,15, occasional_use = 0.5)
OR_indoor_LEDBulb2.windows([1020,1320],[240,360],0.3)
OR_lavatory_LEDBulb = OR.Appliance(OR,1,5,1,60,0.2,15)
OR_lavatory_LEDBulb.windows([870,1440],[0,360],0.1)
OR_Phone_charger = OR.Appliance(OR,4,5,2,120,0.3,15)
OR_Phone_charger.windows([870,1320],[240,360],0.35)
OR_TV=OR.Appliance(OR,1,60,2,180,0.2,30)
OR_TV.windows([900,1199],[1201,1320], 0.15)
OR_SetTopBox = OR.Appliance(OR,1,10,2,210,0.15,15)
OR_SetTopBox.windows([900,1199],[1201,1320],0.3)
OR_MosquitoRepellent = OR.Appliance(OR,1,7,2,480,0.15,30)
OR_MosquitoRepellent.windows([1200,1440],[0,360],0.35)
