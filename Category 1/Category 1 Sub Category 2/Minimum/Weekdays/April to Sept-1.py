#One-Room Minimum Connected Load
#Create new user classes
OR = User("One room minimal",1,1)
User_list.append(OR)

#One-Room Minimum Connected Load
OR_indoor_LEDlight1 = OR.Appliance(OR,1,7,2,420,0.15,15)
OR_indoor_LEDlight1.windows([1020,1320],[240,330],0.1)
OR_Fan = OR.Appliance(OR,2,70, 2, 720,0.15)
OR_Fan.windows([870,1440],[0,360],0.2)
OR_lavatory_LEDBulb = OR.Appliance(OR,1,5,1,60,0.2,15)
OR_lavatory_LEDBulb.windows([870,1440],[0,360],0.1)
OR_Phone_charger = OR.Appliance(OR,4,5,2,120,0.3,15)
OR_MosquitoRepellent = OR.Appliance(OR,1,7,2,480,0.15,30)
OR_MosquitoRepellent.windows([1200,1440],[0,360],0.35)

