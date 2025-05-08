def admin():
    a=input('Enter your admin username :')
    p=input('Enter your admin password :')
    with open('admin.txt','a') as file:
        file.write(f'{a}\t{p}')


from datetime import datetime
# Getting customer's details
def customer_details():
    name=input('Enter your name :')
    user=input('Enter your user name :')
    phone=input('Enter your phone number :')
    password=input('Enter your password :')
    while True:        
        
            try:
                initial=float(input('Enter the initial amount you would like to deposit :'))
                if initial<=0:
                    print('your amount should be greater than zero')                    
                else:                                        
                    info = {'name':name,'user':user,'phone':phone,'initial':initial,'password':password,'time': datetime.now().strftime("%Y-%m-%d %H:%M:%S")}   
                    return info           
            except ValueError:
                print('Enter number only')
    
# Saving account details in txt file
def account_registration(info):
    try:
        with open('account.txt','r') as file:
            lines=file.readlines()
            last_line=lines[-1]
            words=last_line.split()

            file=open('account.txt','a')
            file.write(f"U{int(words[0][1:])+1}\tA{int(words[0][1:])+1}\t{info["password"]}\t{info["initial"]}\n")
            print(f'Your account number is :A{int(words[0][1:])+1}')
            file.close()
            file=open('transaction.txt','a')
            file.write(f"A{int(words[0][1:])+1}\tinitial deposite\t{info['initial']}\t{info["time"]}\n")
            file.close
    except FileNotFoundError:
        x=int(1)
        file=open('account.txt','a')
        file.write(f"U{x}\tA{x}\t{info["password"]}\t{info["initial"]}\n")
        print(f'Your account number is :A{x}')
        file.close()     
        file=open('transaction.txt','a')
        file.write(f"A{x}\tinitial deposite\t{info['initial']}\t{info["time"]}\n")
        file.close

# Saving customer details in txt file
def customer_registration():
    try:
        info = customer_details()
        with open('customer.txt','r') as file:
            lines=file.readlines()
            last_line=lines[-1]
            words=last_line.split()

            file=open('customer.txt','a')
            file.write(f"U{int(words[0][1:])+1}\t{info["name"]}\t{info["user"]}\t{info["phone"]}\n")
            file.close()
            account_registration(info)
            print('successfully created an account')
    except FileNotFoundError:
            x=int(1)
            file=open('customer.txt','a')
            file.write(f"U{x}\t{info['name']}\t{info['user']}\t{info['phone']}\n")
            file.close()
            account_registration(info)
            print('successfully created an account')

# customer_registration()


# depositing cash
def deposite():
    while True:        
        try:
            amount=float(input('Enter the amount you would like to deposit :'))
            if amount<=0:
                print('your amount should be greater than zero')                    
            else:
                print('Deposite successful')
                information={'amount':amount,'transaction_type':'deposite','time': datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
                return information
        except ValueError:
            print('Enter number only')


# withdrawing cash
def withdraw(information):
    filea=open('account.txt','r')
    for line in filea:
        word=line.strip().split()
        if information['accountnum']==word[1]:
            balance=float(word[3])
            break
    while True:        
        try:
            amount=float(input('Enter the withdrawal amount :'))
            if amount<=0:
                print('your amount should be greater than zero')   
            elif amount > balance:
                print('Your withdrawal amount is greater than your balance')
                print('your balance is :',balance)                 
            else:
                print('withdrawal successful')
                information={'amount':amount,'transaction_type':'withdrawal','time': datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
                return information
        except ValueError:
            print('Enter number only')


def balance(information):
    file=open('account.txt','r')
    for line in file:
        word=line.strip().split()
        if information['accountnum']==word[1]:
            print(f"Your account balance is :{float(word[3])}")


def transaction_history(a):
    with open('transaction.txt','r') as file:
        for line in file:
            word=line.split()
            if word[0]==a:
                print(line)

# saving deposite or withdrawal details in transaction text file
def deposite_or_withdarw_registrstion(information):
    file=open('transaction.txt','a')
    file.write(f"{information['accountnum']}\t{information['transaction_type']}\t{information['amount']}\t{information['time']}\n")
    file.close
    filea=open('account.txt','r')
    new_line=[]
    for line in filea:
        word=line.strip().split()
        if information['accountnum']==word[1] and information['transaction_type']=='deposite':
            word[3]=str(float(word[3])+information['amount'])
            line='\t'.join(word)+'\n'
            new_line.append(line)
            file.close()
        elif information['accountnum']==word[1] and information['transaction_type']=='withdrawal':
            word[3]=str(float(word[3])-information['amount'])
            line='\t'.join(word)+'\n'
            new_line.append(line)
            file.close()
        else:
            new_line.append(line)
    file=open('account.txt','w') 
    file.writelines(new_line)
    file.close() 

def login_admin():
    print('login_successful')
    information={}
    print('========ADMIN MENU==========')
    while True:
        print('             1. Account creation')
        print('             2. Deposit Money')
        print('             3. Withdraw Money')
        print('             4. Check Balance')
        print('             5. Transaction History')
        print('             6. Exit')
        print('\n')
        x=int(input('Please enter number 1,2,3,4,5, in order to select the above services :'))
        print('\n')

        if x==1:
            customer_registration()
        if x==2:
            a=input('Enter the account number :')
            information['accountnum']=a
            information.update(deposite())
            deposite_or_withdarw_registrstion(information)
        elif x==3:
            a=input('Enter the account number :')
            information['accountnum']=a
            information.update(withdraw(information))
            deposite_or_withdarw_registrstion(information)
        elif x==4:
            a=input('Enter the account number :')
            information['accountnum']=a
            balance(information)
        elif x==5:
            a=input('Enter the account number :')
            information['accountnum']=a
            transaction_history(a)
        elif x==6:
            print('THANK YOU VERY MUCH FOR USING OUR BANKING SYSTEM. BYE...')
            break
        else:
            print('Enter a number from 1 to 5')
            print('\n')           


# login into a personal account   
def login():
    u=input('Enter your user name :')
    p=input('Enter your password :')
    username={}
    password={}
    accountnum={}
    file=open('customer.txt','r')
    for line in file:
        word=line.split()
        username[word[0]]=word[2]
    file.close()
    file=open('account.txt','r')
    for line in file:
        word=line.split()
        password[word[0]]=word[2]
        accountnum[word[0]]=word[1]
    file.close()
    with open('admin.txt','r') as file:
        line=file.readline()
        word=line.split()
        admin_username=word[0]
        admin_password=word[1]

    for user_id in username:
        if username[user_id]==u and password[user_id]==p :
            login_successful='user'
            a=accountnum[user_id]
            break
    if admin_username==u and  admin_password==p:
        login_successful='admin'




    if login_successful=='user':
        print('login_successful')
        information={}
        information['accountnum']=a
        print('========WELCOME TO OUR BANKING SERVICE==========')
        while True:
            print('     OUR SERVICES')
            print('             1. Deposit Money')
            print('             2. Withdraw Money')
            print('             3. Check Balance')
            print('             4. Transaction History')
            print('             5. Exit')
            print('\n')
            x=int(input('Please enter number 1,2,3,4,5, in order to select the above services :'))
            print('\n')

            if x==1:
                    information.update(deposite())
                    deposite_or_withdarw_registrstion(information)
            elif x==2:
                    information.update(withdraw(information))
                    deposite_or_withdarw_registrstion(information)
            elif x==3:
                balance(information)
            elif x==4:
                transaction_history(a)
            elif x==5:
                print('THANK YOU VERY MUCH FOR USING OUR BANKING SYSTEM. BYE...')
                break
            else:
                print('Enter a number from 1 to 5')
                print('\n')

    elif login_successful=='admin':
        login_admin()
    else:
        print('Incorrect username or password or account number')

import os
file='admin.txt'
if os.path.exists(file):
    login()
else:
    admin()
    login_admin()

# x=int(input('Number :'))
# information=login()
# deposite_or_withdarw_registrstion()

