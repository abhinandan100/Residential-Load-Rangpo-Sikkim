


#One-Room Minimum Connected Load
OR = User("One room minimal",1,1)
User_list.append(OR)

#One-Room Minimum Connected Load
OR_indoor_LEDBulb = OR.Appliance(OR,1,7,2,240,0.15,15)
OR_indoor_LEDBulb.windows([1080,1260],[360,420],0.1)
OR_indoor_LEDBulb1 = OR.Appliance(OR,1,7,2,240,0.15,15, occasional_use=0.5)
OR_indoor_LEDBulb1.windows([1080,1260],[360,420],0.1)
OR_lavatory_LEDBulb = OR.Appliance(OR,1,5,2,45,0.2,15)
OR_lavatory_LEDBulb.windows([360,1260],[0,0], 0.1)
OR_Phone_charger = OR.Appliance(OR,1,5,2,150,0.3,15)
OR_Phone_charger.windows([360,1260],[0,0],0.35)
OR_Fan = OR.Appliance(OR,1,70, 2, 780,0.15,15)
OR_Fan.windows([360,1260],[0,0],0.2)
OR_Fan1 = OR.Appliance(OR,1,70, 2, 780,0.15,15,occasional_use=0.5)
OR_Fan1.windows([360,1260],[0,0],0.2)
OR_TV=OR.Appliance(OR,1,60,2,180,0.25,30)
OR_TV.windows([840,1260],[0,0], 0.15)

