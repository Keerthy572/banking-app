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
            


# login into a personal account   
def login():
    u=input('Enter your user name :')
    p=input('Enter your password :')
    a=input('Enter your account number :')
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
    

    login_successful=False
    for user_id in username:
        if username[user_id]==u and password[user_id]==p and accountnum[user_id]==a:
            login_successful=True
            break

    if login_successful:
        print('login_successful')
        information={}
        information['accountnum']=a
        if x==2:
            information.update(deposite())
            deposite_or_withdarw_registrstion(information)
        elif x==3:
            information.update(withdraw(information))
            deposite_or_withdarw_registrstion(information)
        elif x==4:
            balance(information)
        elif x==5:
            transaction_history(a)
    else:
        print('Incorrect username or password or account number')



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

# x=int(input('Number :'))
# information=login()
# deposite_or_withdarw_registrstion()

print('========WELCOME TO OUR BANKING SERVICE==========')
while True:
    print('     OUR SERVICES')
    print('             1.Create Account')
    print('             2. Deposit Money')
    print('             3. Withdraw Money')
    print('             4. Check Balance')
    print('             5. Transaction History')
    print('             6. Exit')
    print('\n')
    x=int(input('Please enter number 1,2,3,4,5,6 in order to select the above services :'))
    print('\n')

    if x==1:
        customer_registration()
        print('\n')
    elif x==2 or x==3 or x==4 or x==5:
        login()
        print('\n')
    elif x==6:
        print('THANK YOU VERY MUCH FOR USING OUR BANKING SYSTEM. BYE...')
        break
    else:
        print('Enter a number from 1 to 6')
        print('\n')