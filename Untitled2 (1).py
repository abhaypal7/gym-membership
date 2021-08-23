#!/usr/bin/env python
# coding: utf-8

# In[27]:


class GymManager:
    regimen={}
    customers = dict()
    def __init__(self,s_id,s_name):
        self.s_id = s_id
        self.s_name = s_name
        
    @classmethod
    def addCustomer(cls,customer):
        GymManager.customers[customer.getphone_no()]=customer
        
obj =GymManager('s_1','john')


class Customer:
    
    def __init__(self,name='',age='',gender='',phone_no='',bmi='',duration='',email=''):
        self.__name = name
        self.__phone_no = phone_no
        self.__age = age
        self.__gender = gender
        self.__email = email
        self.__bmi = bmi
        self.__duration = duration
        
    def setname(self,name):
        self.__name = name
    def getname(self):
        return self.__name
    
    def setage(self,age):
        self.__age=age
    def getage(self):
        return self.__age
    
    def setgender(self,gender):
        self.__gender = gender
    def getgender(self):
        return self.__gender
    
    def setphone_no(self,phone_no):
        self.__phone_no=phone_no
    def getphone_no(self):
        return self.__phone_no
    
    def setemail(self,email):
        self.__email=email
    def getemail(self):
        return self.__email
    
    def setBmi(self,bmi):
        self.__bmi=bmi
    def getBmi(self):
        return self.__bmi
    
    def setduration(self,duration):
        self.__duration = duration
    def getduration(self):
        return self.__duration
    
    def __str__(self):
        return self.getname()+' '+self.getphone_no()+' '+self.getduration()+' '+self.getage()+' '+self.getgender()+' '+self.getemail +' '+self.getBmi

print('Welcome')
print('Enter your Choice')


def menu():
    print('1.create member')
    print('2.View Member')
    print('3.Delete Member')
    print('4.Update Member')
    print('5.Create Regimen')
    print('6.View Regimen')
    print('7.Delete Regimen')
    print('8.Update Regimen')
    print('0.Exit')
    print('\n Enter your choice')
    
menu()

while(True):
    option = int(input())
    if option == 1:
        name = str(input('Enter your name- '))
        age = str(input('enter your age: '))
        gender = str(input('enter your gender- '))
        phone_no = str(input('enter your phone number: '))
        email = str(input('enter your email address-'))
        bmi = str(input('enter your BMI- '))
        if bmi < '18.5':
            r = {'Mon':'Chest','Tue':'Biceps','Wed':'Rest','Thu': 'Back','Fri': 'Triceps','Sat': 'Rest','Sun': 'Rest'}
        
        elif bmi < '25':
            r = {'Mon':'Chest','Tue':'Biceps','Wed':'Cardio/abs','Thu': 'Back','Fri': 'Triceps','Sat': 'Rest','Sun': 'Rest'}
        
        elif bmi < '30':
            r = {'Mon':'Chest','Tue':'Biceps','Wed':'Cardio/abs','Thu': 'Back','Fri': 'Triceps','Sat': 'legs','Sun': 'Cardio'}
        
        else:
            r = {'Mon':'Chest','Tue':'Biceps','Wed':'Cardio/abs','Thu': 'Back','Fri': 'Triceps','Sat': 'legs','Sun': 'Cardio'}
        
        duration = input('Enter Duration in months- ')
        customer  = Customer(name, age, gender, phone_no,email, bmi, duration)
        GymManager.regimen[phone_no] = r
        GymManager.addCustomer(customer)
        
        
    elif option == 2:
        check_phn = input('Enter phone number ')
        print('name\tage\tgender\tphone_no\temail\tBMI\tduration')
        for cusId in GymManager.customers.keys():
            if cusId == check_phn:
                customer= GymManager.customers[cusId]
                name = customer.getname()
                age = customer.getage()
                gender = customer.getgender()
                phone_no = customer.getphone_no()
                email = customer.getemail()
                bmi = customer.getBmi()
                duration = customer.getduration()
                print(name+' \t '+age+'\t'+gender+'\t'+phone_no+'\t'+email+'\t'+bmi+'\t'+duration)
        print('\n')
            
    elif option==3:
        check_phn=input("Enter the phone number you want to delete: ")
        try:
            for cusId in GymManager.customer.keys():
                if cudId == check_phn:
                    print('Member deleted')
            GymManager.customers.pop(check_phn)
        except:
             print("Number doesn't exist\n")
                
    elif option==4:
        check = input("Enter phone number: ")
        exr = input("Enter if you want to extend or revoke: ")
        if exr =='extend':
            for cusId in GymManager.customers.keys():
                customer = GymManager.customers[cusId]
                if cusId==check:
                    dur = customer.getduration()
                    s=int(dur)+int(input('Enter how many months of extension you want- '))
                    res=str(s)
                    customer.setduration(res)
                    
        elif exr=='revoke':
            for cusId in GymManager.customers.keys():
                customer = GymManager.customers[cusId]
                if cusId == check:
                    customer.setduration('0')
                    print('Membership revoked')
    elif option==5:
        phn=input('enter phone number')
        for i in GymManager.regimen:
            if i ==phn:
                for j in GymManager.regimen[i]:
                    GymManager.regimen[i][j]=input(j+':')
    elif option ==6:
        check_phn=input('enter phone number:')
        for i in GymManager.regimen:
            if i ==check_phn:
                for key,val in GymManager.regimen[i].item():
                    print(key,':',val)
        print('\n')
        
    elif option==7:
        check_phn=input('enter phone number')
        for i in GymManager.regimen:
            if i ==check_phn:
                print('workout regimen deleted!!')
        GymManager.regimen.pop(check_phn)
        print('\n')
    
    elif option==8:
        check_phn = input('enter phone number:')
        for i in GymManager.regimen:
            if i==check_phn:
                d=input('Enter day: ')
                for j in GymManager.regimen[i]:
                    if j==d:
                        GymManager.regimen[i][j]=input('Enter workout:')
                        print('updated successfully')
        print('\n')
        
    elif option==0:
        break
        
    else:
        print('Enter a valid number')
        
        
    menu()

def memenu():
    print('\n***your Profile***\n')
    print('1.My Regimen')
    print('2.My Profile')
    print('3.Exit')
    print('\nEnter your choice: ')
    
memenu()
while(True):
    option=int(input())
    if option == 1:
        p=input('Enter your phone number: ')
        print('--your Regimen based on your BMI--')
        for i in GymManager.regimen:
            if i==p:
                for key,val in GymManager.regimen[i].item():
                    print(key,':',val)
        print('\n')
    
    elif option==2:
        p=input('Enter your phone number: ')
        try:
            for cusId in GymManager.customer.keys():
                if cusId == p:
                    customer = GymManager.customer[cusId]
                    name = customer.getname()
                    age=customer.getage()
                    gender=customer.getgender()
                    phone_no=customer.getphone_no()
                    email=customer.getemail()
                    BMI=customer.getBMI()
                    duration=customer.getduration()
                    print('Your Profile')
                    print('name:',name,'\nAge',age,'\nGender',gender,'\nphone number')
        except:
            print('check phone number')
            
    elif option ==3:
        break
        
    else:
        print('enter a valid number')
        


# In[ ]:





# In[ ]:




