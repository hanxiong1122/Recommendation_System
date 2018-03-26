# Written by Hanxiong Wang on 10/1/2016

# This part is to define the class node for recording users
class NodeA(object):

    def __init__(self,ttype = '',averstar = -1 ,
                 id = '', name = '',review_count = -1,
                 review_list = {}, postvisit = -1, previsit = -1):
        self.ttype = ttype
        self.averstar = averstar
        self.id = id
        self.name = name
        self.review_count = review_count
        self.review_list = review_list
        self.postvisit = postvisit
        self.previsit = previsit
        
    def BuildNodeA(self, data_user):
        self.ttype = data_user['type']
        self.averstar = data_user['average_stars']
        self.id  = data_user['user_id']
        self.name = data_user['name']
        self.review_count = data_user['review_count']
        
    def FindReview_listA(self,data_review):
        self.review_list = {}
        count = 0
        for BssShop in data_review:
            if BssShop['user_id'] == self.id:
                if BssShop['business_id'] in self.review_list:
                    count+=1
                self.review_list[BssShop['business_id']] = BssShop['stars']
        return count


# This part is to define the class node for recording business unit
class NodeB(object):

    def __init__(self,ttype = '',stars = -1 ,
                 id = '', name = '',review_count = -1,
                 attributes ={}, categories ={},
                 review_list = {}, postvisit = -1, previsit = -1):
        self.ttype = ttype
        self.stars = stars
        self.id = id
        self.name = name
        self.review_count = review_count
        self.attributes = attributes
        self.categories = categories
        self.review_list = review_list
        self.postvisit = postvisit
        self.previsit = previsit
        
   
       
    def BuildNodeB(self,data_business):
        self.ttype = data_business['type']
        self.stars = data_business['stars']
        self.id  = data_business['business_id']
        self.name = data_business['name']
        self.review_count = data_business['review_count']
        self.attributes = data_business['attributes']
        self.categories = data_business['categories']
        
    def FindReview_listB(self,data_review):
        self.review_list = {}
        count = 0
        for BssShop in data_review:
            if BssShop['business_id'] == self.id:
                if BssShop['user_id'] in self.review_list:
                    count+=1
                self.review_list[BssShop['user_id']] = BssShop['review_id']
        return count


