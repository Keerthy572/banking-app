# Getting customer's details
def account_creation():
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
                    info = {'name':name,'user':user,'phone':phone,'initial':initial,'password':password}   
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
            file.close()
            file=open('transaction.txt','a')
            file.write(f"A{int(words[0][1:])+1}\tinitial deposite\t{info['initial']}\n")
            file.close
    except FileNotFoundError:
        x=int(1)
        file=open('account.txt','a')
        file.write(f"U{x}\tA{x}\t{info["password"]}\t{info["initial"]}\n")
        file.close()     
        file=open('transaction.txt','a')
        file.write(f"A{x}\tinitial deposite\t{info['initial']}\n")
        file.close

# Saving customer details in txt file
def customer_registration():
    try:
        info = account_creation()
        with open('customer.txt','r') as file:
            lines=file.readlines()
            last_line=lines[-1]
            words=last_line.split()

            file=open('customer.txt','a')
            file.write(f"U{int(words[0][1:])+1}\t{info["name"]}\t{info["user"]}\t{info["phone"]}\n")
            file.close()
            print('successfully created account')
            account_registration(info)
    except FileNotFoundError:
            x=int(1)
            file=open('customer.txt','a')
            file.write(f"u{x}\t{info['name']}\t{info['user']}\t{info['phone']}\n")
            file.close()
            print('successfully created account')
            account_registration(info)

# customer_registration()


# depositing cash
def deposite():
    while True:        
        try:
            amount=float(input('Enter the amount you would like to deposit :'))
            if amount<=0:
                print('your amount should be greater than zero')                    
            else:
                print('withdrawal successful')
                information={'amount':amount,'transaction_type':'deposite'}
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
                information['amount']=amount
                information['transaction_type']='withdrawal'
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
        if x==1:
            information.update(deposite())
            return information
        elif x==2:
            information.update(withdraw(information))
            return information
        elif x==3:
            balance(information)
        elif x==4:
            transaction_history(a)
    else:
        print('Incorrect username or password or account number')



# saving deposite or withdrawal details in transaction text file
def deposite_or_withdarw_registrstion():
    file=open('transaction.txt','a')
    file.write(f"{information['accountnum']}\t{information['transaction_type']}\t{information['amount']}\n")
    file.close
    filea=open('account.txt','r')
    new_line=[]
    for line in filea:
        word=line.strip().split()
        if information['accountnum']==word[1] and information['transaction type']=='deposite':
            word[3]=str(float(word[3])+information['amount'])
            line='\t'.join(word)+'\n'
            new_line.append(line)
            file.close()
        elif information['accountnum']==word[1] and information['transaction type']=='withdrawal':
            word[3]=str(float(word[3])-information['amount'])
            line='\t'.join(word)+'\n'
            new_line.append(line)
            file.close()
        else:
            new_line.append(line)
    file=open('account.txt','w') 
    file.writelines(new_line)
    file.close() 

x=int(input('Number :'))
information=login()
# deposite_or_withdarw_registrstion()

