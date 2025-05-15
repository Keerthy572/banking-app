import os
from datetime import datetime
def admin():
    while True:
        a=input('Enter your admin username :')
        if a.strip()!="":
            break
        else:
            print("Username cannot be blank,Try again")
    while True:
        p=input('Enter your admin password :')
        if p.strip()!="" and 6<=len(p)<=12:
            break
        else:
            print('password should be minimum 6 characters or maximum 12 characters')
    with open('admin.txt','a') as file:
        file.write(f'{a}\t{p}')

# Getting customer's details
def customer_details():
    while True:
            name=input('Enter your name :')
            if name.strip()!="":
                break
            else:
                print("Name cannot be blank,Try again")
    username={}            
    if os.path.exists('customer.txt'):
        status = None
        with open('customer.txt','r') as file:
            for line in file:
                word=line.split()
                username[word[0]]=word[2]
        with open('admin.txt','r') as file:
            for line in file:
                word=line.split()
                username[word[1]]=word[0]
        while True:
            status='no'
            user=input('Enter your user name :')
            for userid in username:
                if username[userid]==user:
                    status = 'yes'
                    break
            if status=='yes':
                print('Username already exists, Try again')
                continue
            elif user.strip()=="":
                print("Username cannot be blank,Try again")
                continue
            else:
                break
    else:
        with open('admin.txt','r') as file:
            for line in file:
                word=line.split()
                username[word[1]]=word[0]
        while True:
            status='no'
            user=input('Enter your user name :')
            for userid in username:
                if username[userid]==user:
                    status = 'yes'
                    break
            if status=='yes':
                print('Username already exists, Try again')
                continue
            elif user.strip()=="":
                print("Username cannot be blank,Try again")
                continue
            else:
                break
    while True:
        phone = input("Enter your phone number (starting with 07 or 021 and 10 digits): ")
        if len(phone) == 10 and phone.isdigit() and (phone.startswith("07") or phone.startswith("021")):
            print("Phone number accepted.")
            break
        else:
            print("Invalid phone number. Please enter a valid 10-digit number starting with 07 or 021.")

    while True:
        password=input('Enter your password :')
        if password.strip()!="" and 6<=len(password)<=12:
            break
        else:
            print('password should be minimum 6 characters or maximum 12 characters and can not be blank')
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
            file.close()
    except FileNotFoundError:
        x=int(1000)
        # Here the number generation starts from 1000 and increases in order.
        # So it will be positive and a four digit number until 9999.
        file=open('account.txt','a')
        file.write(f"U{x}\tA{x}\t{info["password"]}\t{info["initial"]}\n")
        print(f'Your account number is :A{x}')
        file.close()     
        file=open('transaction.txt','a')
        file.write(f"A{x}\tinitial deposite\t{info['initial']}\t{info["time"]}\n")
        file.close()

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
            x=int(1000)
            file=open('customer.txt','a')
            file.write(f"U{x}\t{info['name']}\t{info['user']}\t{info['phone']}\n")
            file.close()
            account_registration(info)
            print('successfully created an account')


# depositing cash
def deposit():
    while True:        
        try:
            amount=float(input('Enter the amount you would like to deposit :'))
            if amount<=0:
                print('your amount should be greater than zero')                    
            else:
                print('Deposite successful')
                information={'amount':amount,'transaction_type':'deposit','time': datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
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
            if balance==0:
                print('Your account balance is zero')
                print("Can't do withdrawal")
                break
            elif amount<=0:
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
    with open('account.txt','r') as file:
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
def deposit_or_withdarw_registrstion(information):
    file=open('transaction.txt','a')
    file.write(f"{information['accountnum']}\t{information['transaction_type']}\t{information['amount']}\t{information['time']}\n")
    file.close()
    with open('account.txt','r') as filea:
        new_line=[]
        for line in filea:
            word=line.strip().split()
            if information['accountnum']==word[1] and information['transaction_type']=='deposit':
                word[3]=str(float(word[3])+information['amount'])
                line='\t'.join(word)+'\n'
                new_line.append(line)
            elif information['accountnum']==word[1] and information['transaction_type']=='withdrawal':
                word[3]=str(float(word[3])-information['amount'])
                line='\t'.join(word)+'\n'
                new_line.append(line)
            else:
                new_line.append(line)
    file=open('account.txt','w') 
    file.writelines(new_line)
    file.close() 


def accountnum_check():
    while True:
        global y 
        global a
        a=input('Enter the account number :')
        try:
            with open('account.txt','r')as file:
                for line in file:
                    word=line.split()
                    if word[1]==a:
                        y=1
                        break
        except FileNotFoundError:
            print('Not any accounts have been registered yet. First create an account')
            break
        if y==1:
            return y,a
        else:
            print('This account number does not exist,Try again')   
            try:
                print('1.Try again')
                print('2.Exit')
                z=int(input('Enter number 1 or 2 to choose :'))
                if z==1:
                    continue
                elif z==2:
                    break
                else:
                    print('Enter only number 1 or 2')
            except ValueError:
                print('Enter numbers only(1 or 2)')


def display_customer_list():
    customers={}
    try :
        with open('customer.txt','r') as file:
            lines=file.readlines()
            for line in lines:
                word=line.strip().split()   
                customers[word[0]]=[word[1]  ,]
            if customers=="":
                print('Not any customers found.')
            else:
                print(customers)
    except FileNotFoundError:
        print('customer file not found or customers have not been created yet')



def view_all_acc():
    try:
        with open('account.txt','r')as file:
            for line in file:
                print(line)   
    except FileNotFoundError:
        print('No accounts have been created yet') 

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
        print('             6. View all accounts')
        print('             7. Display customer list')
        print('             8. Exit')
        while True:
            try:
                x=float(input('Please enter number 1,2,3,4,5,6,7,8 in order to select the above services :'))
                break
            except ValueError:
                print('Enter a valid number')
        print('\n')
        y=None
        a=None
        if x==1:
            customer_registration()
        elif x==2:
            accountnum_check()
            if y==1:
                    information['accountnum']=a
                    information.update(deposit())
                    deposit_or_withdarw_registrstion(information)
        elif x==3:
            accountnum_check()
            if y==1:
                information['accountnum']=a
                information.update(withdraw(information))
                deposit_or_withdarw_registrstion(information)
        elif x==4:
            accountnum_check()
            if y==1:
                information['accountnum']=a
                balance(information)
        elif x==5:
            accountnum_check()
            if y==1:
                information['accountnum']=a
                transaction_history(a)
        elif x==6:
            view_all_acc()
        elif x==7:
            display_customer_list()
        elif x==8:
            print('THANK YOU')
            break
        else:
            print('Enter a number from 1 to 8')
            print('\n')           

# login into a personal account   
def login():
    u=input('Enter your user name :')
    p=input('Enter your password :')
    username={}
    password={}
    accountnum={}
    try:
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
    except FileNotFoundError:
        pass
    with open('admin.txt','r') as file:
        line=file.readline()
        word=line.split()
        admin_username=word[0]
        admin_password=word[1]
    login_successful=None
    for user_id in username:
        if username[user_id]==u and password[user_id]==p :
            login_successful='user'
            a=accountnum[user_id]
            break
    if admin_username==u and  admin_password==p:
        login_successful='admin'




    if login_successful=='user':
        print('login_successful')
        print('\n')
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
            while True:
                try:
                    x=float(input('Please enter number 1,2,3,4,5,6,7 in order to select the above services :'))
                    break
                except ValueError:
                    print('Enter a valid number')

            if x==1:
                    information.update(deposit())
                    deposit_or_withdarw_registrstion(information)
            elif x==2:
                    information.update(withdraw(information))
                    deposit_or_withdarw_registrstion(information)
            elif x==3:
                balance(information)
            elif x==4:
                transaction_history(a)
            elif x==5:
                print('THANK YOU')
                break
            else:
                print('Enter a number from 1 to 5')
                print('\n')

    elif login_successful=='admin':
        login_admin()
    else:
        print('Incorrect username or password or account number')

def login_again():
    while True:
        try:
            print('1.Login again')
            print('2.Exit')
            y=int(input('Enter number 1 or 2 to choose :'))
            if y==1:
                login()
            elif y==2:
                print('THANK YOU VERY MUCH FOR USING OUR BANKING SYSTEM. BYE...')
                break
            else:
                print('Enter only number 1 or 2')
        except ValueError:
            print('Enter numbers only(1 or 2)')

file='admin.txt'
if os.path.exists(file):
    login()
    login_again()
else:
    admin()
    login_admin()
    login_again()

