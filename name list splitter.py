exit=("No")
while exit != "y":
	
    Final_List_list= []
    Second_List_list= []
    Spaceless_list = []
    Spaceless_list_2 = []
    Counting_list = []
    Storage_list = []
	
    Full_List_string=input("List of Names: ")
    print("")
    Full_List_string= "".join([Full_List_string, ","])
    Full_List_string= Full_List_string.replace(" &",",")
    Full_List_string= Full_List_string.replace(";",",")
    Full_List_string= Full_List_string.replace("ORCID logo","")
    Full_List_string= Full_List_string.replace("ORCID","")
    Full_List_string= Full_List_string.replace("Irma","")
    Full_List_string= Full_List_string.replace(", and",",")
    Full_List_string= Full_List_string.replace(" and",",")
    Full_List_string= Full_List_string.replace(" †","")
    Full_List_string= Full_List_string.replace("†","")
    Full_List_string= Full_List_string.replace("‡","")
    Full_List_string= Full_List_string.replace("∗","")
    Full_List_string= Full_List_string.replace("¶","")
    Full_List_string= Full_List_string.replace("§","")
    Full_List_string= Full_List_string.replace("‖","")
    Full_List_string= Full_List_string.replace("*","")
    Full_List_string= Full_List_string.replace("#","")
    Full_List_string= Full_List_string.replace("corresponding author ","")
    Full_List_string= Full_List_string.replace("✉","")
    Full_List_string= Full_List_string.replace("∙",",")
    
    for i in range(0,10):
        Full_List_string=Full_List_string.replace(str(i),",")
        Full_List_string= Full_List_string.replace(",,",",")
    
    Full_List_string= Full_List_string.replace(" ,",",")
    Full_List_string= Full_List_string.replace("corresponding author ","")

    for i in range(1,4):
        Full_List_string= Full_List_string.replace(" a,",",")
        Full_List_string= Full_List_string.replace(" b,",",")
        Full_List_string= Full_List_string.replace(" c,",",")
        Full_List_string= Full_List_string.replace(" d,",",")
        Full_List_string= Full_List_string.replace(" e,",",")
        Full_List_string= Full_List_string.replace(" f,",",")
        Full_List_string= Full_List_string.replace(" g,",",")
        Full_List_string= Full_List_string.replace(" h,",",")
        Full_List_string= Full_List_string.replace(" i,",",")
        Full_List_string= Full_List_string.replace(" j,",",")
        Full_List_string= Full_List_string.replace(" k,",",")
        Full_List_string= Full_List_string.replace(" l,",",")
        Full_List_string= Full_List_string.replace(" m,",",")
        Full_List_string= Full_List_string.replace(" n,",",")
        Full_List_string= Full_List_string.replace(" o,",",")
        Full_List_string= Full_List_string.replace(" p,",",")
        Full_List_string= Full_List_string.replace(" q,",",")
        Full_List_string= Full_List_string.replace(" r,",",")
        Full_List_string= Full_List_string.replace(" s,",",")
        Full_List_string= Full_List_string.replace(" t,",",")
        Full_List_string= Full_List_string.replace(" u,",",")
        Full_List_string= Full_List_string.replace(" v,",",")
        Full_List_string= Full_List_string.replace(" w,",",")
        Full_List_string= Full_List_string.replace(" x,",",")
        Full_List_string= Full_List_string.replace(" y,",",")
        Full_List_string= Full_List_string.replace(" z,",",")
    print(Full_List_string)
    print("Space adder:")
    

	
    for i in range(0,10):
        Full_List_string= Full_List_string.replace(",,",",")
		
    if Full_List_string[len(Full_List_string)-1] == ",":
        Full_List_string= Full_List_string[:-1]

    if Full_List_string[Full_List_string.find(",")+1] != " ":
        Full_List_string= Full_List_string.replace(",",", ")
    else:
        Full_List_string=Full_List_string
    print(Full_List_string)
    print("")
    Full_List_string= Full_List_string.replace(", ,",",")
    Full_List_string= Full_List_string.replace(",,",",")
    Full_List_string= Full_List_string.replace(", ,",",")
    Full_List_string= Full_List_string.replace(",  ",", ")

    Full_List_list = Full_List_string.split(", ")
	
    for i in Full_List_list:
        if "http" in i:
            httpsless =i[:i.find("https")]
            Storage_list.append(httpsless)
        else:
            Storage_list.append(i)
			
    Full_List_list=Storage_list	
    print(Full_List_list)
    for i in Full_List_list:
        Counting_list.append(i.count(" "))
    for j in range(1,max(Counting_list)):
        Storage_list=[]
        for i in Full_List_list:
            if i[len(i)-1] == " ":
                space_less=i[:len(i)-1]
            else:
                space_less=i
            Storage_list.append(space_less)
        Full_List_list= Storage_list

    for i in Full_List_list:
        if "Jr." in i:
            space_replaced= i.replace(" ","-",i.count(" ")-2)
            point_removed= space_replaced.replace(".","",space_replaced.count(".")-1)
            Second_List_list.append(point_removed)
        else:
            space_replaced= i.replace(" ","-",i.count(" ")-1)
            point_removed= space_replaced.replace(".","")
            Second_List_list.append(point_removed)

    for i in Second_List_list:
        check = i.count("-")
        if check >3:
            print(i)
			
        elif check ==3:
            space_location=i.find(" ")
            minus_location=i.find("-")+1
            name_short1= i[:1]+i[minus_location:]
            minus_location = name_short1.find("-")+1
            name_short2= name_short1[:2]+name_short1[minus_location:] 
            minus_location = name_short2.find("-")+1
            name_short3= name_short2[:3]+name_short2[minus_location:]
            name_short4 = name_short3[:4]+ i[space_location:]
            Final_List_list.append(name_short4)
			
        elif check==2:
            space_location=i.find(" ")
            minus_location=i.find("-")+1
            name_short1= i[:1]+i[minus_location:]
            minus_location = name_short1.find("-")+1
            name_short2= name_short1[:2]+name_short1[minus_location:]
            name_short3 = name_short2[:3]+ i[space_location:]
            Final_List_list.append(name_short3)
			
        elif check ==1:
            space_location=i.find(" ")
            minus_location=i.find("-")+1
            name_short = i[:1]+i[minus_location:]
            name_short = name_short[:2] + i[space_location:] 	
            Final_List_list.append(name_short)
			
        else:
            space_location=i.find(" ")
            name_short = i[:1]+i[space_location:]
            Final_List_list.append(name_short)

    print(Final_List_list)
    Final_List_string= ", ".join(Final_List_list)
    print("")
    print("")
    print("Finale liste :")
    print(Final_List_string)