# Written by Hanxiong Wang on 10/18/2016
#!/usr/bin/python
from BuildClass import *
from NodeClassFun import *
from PlotObjGraph import *
from FormRecList import *
from tkinter import *
import pickle
import copy
import time
import tkinter.messagebox as messagebox


data_user = pickle.load(open("data_user_PA.dat",'rb'))
data_review = pickle.load(open("data_review_PA.dat",'rb'))
data_business = pickle.load(open("data_business_PA.dat",'rb'))



class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def datainput(self, data_user, data_business, data_review):
        self.data_user = data_user
        self.data_business = data_business
        self.data_review = data_review

    def createWidgets(self):
        self.helloLabel = Label(self, text='Input the user\'s number to test:')
        self.helloLabel.pack()
        self.nameInput = Entry(self)
        self.nameInput.pack()
        self.alertButton = Button(self, text='Search', command=self.hello)
        self.alertButton.pack()
        self.quitButton = Button(self, text='Quit', command=self.quit)
        self.quitButton.pack()

    def hello(self):
        name = self.nameInput.get()
        num_user=int(name)
        prefer_set = set()
        dislike_set = set()
        Top10_list = []
        List_For_Rec = ''

        Temp = NodeA()
        Temp.BuildNodeA(data_user[num_user])
        Temp.FindReview_listA(data_review)

        for item in Temp.review_list.keys():
            if Temp.review_list[item]>Temp.averstar:
                prefer_set.add(Findinfo(item, data_business)['name'])
            else:
                dislike_set.add(Findinfo(item, data_business)['name'])

        viewlen = len(prefer_set)
        if  viewlen<3 or viewlen>50:
            messagebox.showinfo('Answer', 'This user %d is not eligible to provide the recommendation list.' %num_user)
            return
        else:
            (Graph_list,Node_list,NumF,NumS)=PlotObjGraph(num_user,self.data_user, self.data_review, self.data_business)
            (Rec_Node_list, Rec_list,Graph_list,Node_list)=FindRecList(num_user,self.data_user,self.data_review,self.data_business,Graph_list, Node_list, NumF, NumS)
            count = 0
            for item in Rec_Node_list:
                if item[1] in prefer_set or item[1] in dislike_set:
                    continue
                else:
                    if count == 10:
                        for s in Top10_list:
                            List_For_Rec += s+'\n'
                        messagebox.showinfo('Answer', 'User %d\'s recommendation list is:\n %s' %(num_user,List_For_Rec))
                        return
                    else:
                        count +=1
                        Top10_list.append(item[1])

app = Application()
app.datainput(data_user,data_business,data_review)
# set the title:
app.master.title('CS512 Recommendation System Demo')
# mainloop:
app.mainloop()
