
#One-Room Minimum Connected Load
#Create new user classes
OR = User("One room minimal",1,1)
User_list.append(OR)

#One-Room Minimum Connected Load
OR_indoor_LED = OR.Appliance(OR,1,55,2,420,0.15,15)
OR_indoor_LED.windows([1080,1440],[300,420],0.1)
OR_lavatory_LEDBulb = OR.Appliance(OR,1,5,1,90,0.2,5)
OR_lavatory_LEDBulb.windows([360,1440],[0,0],0.3)
OR_Phone_charger = OR.Appliance(OR,3,5,2,200,0.3,15)
OR_Phone_charger.windows([1082,1440],[480,1078],0.35)
OR_TV=OR.Appliance(OR,1,60,1,720,0.2,30)
OR_TV.windows([480,1440],[0,0],0.15)
OR_Fan = OR.Appliance(OR,1,70,1,1200,0.15,15)
OR_Fan.windows([0,1440],[0,0],0.2)
OR_SetTopBox = OR.Appliance(OR,1,10,1,720,0.15,15)
OR_SetTopBox.windows([480,1440],[0,0],0.35)
OR_MosquitoRepellent = OR.Appliance(OR,1,7,2,480,0.15,30)
OR_MosquitoRepellent.windows([1200,1440],[0,360],0.35)

