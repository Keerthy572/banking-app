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
    except FileNotFoundError:
        x=int(1)
        file=open('account.txt','a')
        file.write(f"U{x}\tA{x}\t{info["password"]}\t{info["initial"]}\n")
        file.close()     


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
    

    login_successful=False
    for user_id in username:
        if username[user_id]==u and password[user_id]==p:
            login_successful=True
            a=accountnum[user_id]
            break

    if login_successful:
        print('login_successful')
        information=deposite()
        information['accountnum']=a
        return information
    else:
        print('Incorrect username or password')



# saving deposite details in transaction text file
def deposite_registrstion():
    file=open('transaction.txt','a')
    file.write(f"{information['accountnum']}\t{information['transaction_type']}\t{information['amount']}\n")
    file.close
    filea=open('account.txt','r')
    new_line=[]
    for line in filea:
        word=line.strip().split()
        if information['accountnum']==word[1]:
            word[3]=str(float(word[3])+information['amount'])
            line='\t'.join(word)+'\n'
            new_line.append(line)
            file.close()
        else:
            new_line.append(line)
    file=open('account.txt','w') 
    file.writelines(new_line)
    file.close() 


information=login()
deposite_registrstion()




