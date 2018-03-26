# Written by Hanxiong Wang on 10/1/2016
# This part of code is used to define some useful functions to help the generate the objective graph


from BuildClass import *

# find the index of the objective node list
def FindIndex(keyword, Objlist):
    Index = len(Objlist)
    for i in range(len(Objlist)):
        if Objlist[i].id == keyword:
            Index = i
    return Index

# find the informatino list of the objective node list    
def Findinfo(keyword, Data):
    for info in Data:
        if info['type'] == 'user':
            if info['user_id'] == keyword:
                return info
        if info['type'] == 'business':
            if info['business_id'] == keyword:
                return info
        if info['type'] == 'review':
            if info['review_id'] == keyword:
                return info
    return 'not found'

# find the categories distribution for the root user's
def CateDisCal(ObjNode_ele,Data_business):
    cateDis = {}
    sumnum = 0
    for key in ObjNode_ele.review_list.keys():
        info = Findinfo(key,Data_business)
        for cate in info['categories']:
            if cate in cateDis:
                cateDis[cate] +=1
                sumnum += 1
            else:
                cateDis[cate] = 1
                sumnum += 1
    for cate in cateDis:
        cateDis[cate] = cateDis[cate]/sumnum
    return cateDis

# Calculate the modified edge by categories distribution
def ModCateEdge(bussinfo,cateDis):
    MCEdge = 0
    for key in bussinfo.categories:
        if key in cateDis:
            MCEdge += cateDis[key]
    return MCEdge

# Calculate the modified edge by Attributes           
def ModAttrEdge(bussinfo,ObjNode_list):
    attrDis = {}
    sumnum = 0
    MAEdge = 0
    lista = bussinfo.categories
    for item in ObjNode_list:
        listb = item.categories
        if len(list(set(lista).intersection(set(listb))))!=0:
            if 'Price Range' in item.attributes and item.attributes['Price Range']==1:
                if 'Price Range:1' in attrDis:
                    attrDis['Price Range:1']+=1
                else:
                    attrDis['Price Range:1'] =1
            elif 'Price Range' in item.attributes and item.attributes['Price Range']==2:
                if 'Price Range:2' in attrDis:
                    attrDis['Price Range:2']+=1
                else:
                    attrDis['Price Range:2'] =1
            elif 'Price Range' in item.attributes and item.attributes['Price Range']==3:
                if 'Price Range:3' in attrDis:
                    attrDis['Price Range:3']+=1
                else:
                    attrDis['Price Range:3'] =1
            elif 'Price Range' in item.attributes and item.attributes['Price Range']==4:
                if 'Price Range:4' in attrDis:
                    attrDis['Price Range:4']+=1
                else:
                    attrDis['Price Range:4'] =1
            if 'Alcohol' in item.attributes and item.attributes['Alcohol']=='full_bar':
                if 'Alcohol: full_bar' in attrDis:
                    attrDis['Alcohol: full_bar']+=1
                else:
                    attrDis['Alcohol: full_bar'] =1
            elif 'Alcohol' in item.attributes and item.attributes['Alcohol']=='beer_and_wine':
                if 'Alcohol: beer_and_wine' in attrDis:
                    attrDis['Alcohol: beer_and_wine']+=1
                else:
                    attrDis['Alcohol: beer_and_wine'] =1
            elif 'Alcohol' in item.attributes and item.attributes['Alcohol']=='none':
                if 'Alcohol: none' in attrDis:
                    attrDis['Alcohol: none']+=1
                else:
                    attrDis['Alcohol: none'] =1
            if 'Accepts Credit Cards' in item.attributes and item.attributes['Accepts Credit Cards']==True:
                if 'Accepts Credit Cards: True' in attrDis:
                    attrDis['Accepts Credit Cards: True']+=1
                else:
                    attrDis['Accepts Credit Cards: True'] =1
            if 'Wi-Fi' in item.attributes and item.attributes['Wi-Fi']=='free':
                if 'Wi-Fi: free' in attrDis:
                    attrDis['Wi-Fi: free']+=1
                else:
                    attrDis['Wi-Fi: free'] =1
            if 'Good For Groups' in item.attributes and item.attributes['Good For Groups']==True:
                if 'Good For Groups' in attrDis:
                    attrDis['Good For Groups: True']+=1
                else:
                    attrDis['Good For Groups: True'] =1
            if 'Good For Kids' in item.attributes and item.attributes['Good For Kids']==True:
                if 'Good For Kids' in attrDis:
                    attrDis['Good For Kids: True']+=1
                else:
                    attrDis['Good For Kids: True'] =1
            if 'By Appointment Only' in item.attributes and item.attributes['By Appointment Only']==False:
                if 'By Appointment Only' in attrDis:
                    attrDis['By Appointment Only: False']+=1
                else:
                    attrDis['By Appointment Only: False'] =1
            if 'Takes Reservations' in item.attributes and item.attributes['Takes Reservations']==True:
                if 'Takes Reservations' in attrDis:
                    attrDis['Takes Reservations: True']+=1
                else:
                    attrDis['Takes Reservations: True'] =1
            if 'Wheelchair Accessible' in item.attributes and item.attributes['Wheelchair Accessible']==True:
                if 'Wheelchair Accessible' in attrDis:
                    attrDis['Wheelchair Accessible: True']+=1
                else:
                    attrDis['Wheelchair Accessible: True'] =1
            if 'Outdoor Seating' in item.attributes and item.attributes['Outdoor Seating']==True:
                if 'Outdoor Seating' in attrDis:
                    attrDis['Outdoor Seating: True']+=1
                else:
                    attrDis['Outdoor Seating: True'] =1
            if 'Delivery' in item.attributes and item.attributes['Delivery']==True:
                if 'Delivery' in attrDis:
                    attrDis['Delivery: True']+=1
                else:
                    attrDis['Delivery: True'] =1
    for attr in attrDis:
        sumnum += attrDis[attr]
    for attr in attrDis:
        attrDis[attr] = attrDis[attr]/sumnum

###########################################
    if attrDis !={}:
        if 'Price Range' in bussinfo.attributes and bussinfo.attributes['Price Range']==1 and 'Price Range:1' in attrDis:
            MAEdge += attrDis['Price Range:1']
        if 'Price Range' in bussinfo.attributes and bussinfo.attributes['Price Range']==2 and 'Price Range:2' in attrDis:
            MAEdge += attrDis['Price Range:2']
        if 'Price Range' in bussinfo.attributes and bussinfo.attributes['Price Range']==3 and 'Price Range:3' in attrDis:
            MAEdge += attrDis['Price Range:3']
        if 'Price Range' in bussinfo.attributes and bussinfo.attributes['Price Range']==4 and 'Price Range:4' in attrDis:
            MAEdge += attrDis['Price Range:4']
        if 'Alcohol' in bussinfo.attributes and bussinfo.attributes['Alcohol']=='full_bar' and 'Alcohol: full_bar' in attrDis:
            MAEdge += attrDis['Alcohol: full_bar']
        if 'Alcohol' in bussinfo.attributes and bussinfo.attributes['Alcohol']=='beer_and_wine' and 'Alcohol: beer_and_wine' in attrDis:
            MAEdge += attrDis['Alcohol: beer_and_wine']
        if 'Alcohol' in bussinfo.attributes and bussinfo.attributes['Alcohol']=='none' and 'Alcohol: none' in attrDis:
            MAEdge += attrDis['Alcohol: none']
        if 'Accepts Credit Cards' in bussinfo.attributes and bussinfo.attributes['Accepts Credit Cards']==True and 'Accepts Credit Cards: True' in attrDis:
            MAEdge += attrDis['Accepts Credit Cards: True']
        if 'Wi-Fi' in bussinfo.attributes and bussinfo.attributes['Wi-Fi']=='free' and 'Wi-Fi: free' in attrDis:
            MAEdge += attrDis['Wi-Fi: free']
        if 'Good For Group' in bussinfo.attributes and bussinfo.attributes['Good For Group']==True and 'Good For Groups: True' in attrDis:
            MAEdge += attrDis['Good For Groups: True']
        if 'Good For Kids' in bussinfo.attributes and bussinfo.attributes['Good For Kids']==True and 'Good For Kids: True' in attrDis:
            MAEdge += attrDis['Good For Kids: True']
        if 'By Appointment Only' in bussinfo.attributes and bussinfo.attributes['By Appointment Only']==False and 'By Appointment Only: False' in attrDis:
            MAEdge += attrDis['By Appointment Only: False']
        if 'Takes Reservations' in bussinfo.attributes and bussinfo.attributes['Takes Reservations']==True and 'Takes Reservations: True' in attrDis:
            MAEdge += attrDis['Takes Reservations: True']
        if 'Wheelchair Accessible' in bussinfo.attributes and bussinfo.attributes['Wheelchair Accessible']==True and 'Wheelchair Accessible: True' in attrDis:
            MAEdge += attrDis['Wheelchair Accessible: True']
        if 'Outdoor Seating' in bussinfo.attributes and bussinfo.attributes['Outdoor Seating']==True and 'Outdoor Seating: True' in attrDis:
            MAEdge += attrDis['Outdoor Seating: True']
        if 'Delivery' in bussinfo.attributes and bussinfo.attributes['Delivery']==True and 'Delivery: True' in attrDis:
            MAEdge += attrDis['Delivery: True']   
    return MAEdge

            
