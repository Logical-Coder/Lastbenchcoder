def password_check(_password):
    length=len(_password)
    Capalpha=''
    num=''
    Lowalpha=''
    symbol=''
    pswd=''
    count=dict()
    cnt=0
    password=""
    bol=True
    #This Function Returns the Password Combnation Not Achievd
    def re_callback(strr):
        if strr.islower():
            print("• At least need 1 Lower Charecter [a-z]")
        elif strr.isupper():
            print("• At least need 1 Upper Charecter [A-Z]")
        elif strr.isnumeric():
            print("• At least need 1 number  [0-9]")
        else:
            print("• At least need 1 Symbol [$#@]")
  #Dividing Passwords        
    for i in _password:
        if i.isalnum():
            if i.isupper():
                Capalpha+=i
                count[cnt]=i
                cnt+=1
            if i.islower():
                Lowalpha+=i
                count[cnt]=i
                cnt+=1
            if i.isnumeric():
                num+=i
                count[cnt]=i
                cnt+=1 
        else:
            symbol+=i
            count[cnt]=i
            cnt+=1
    #Checking Length of strings
    if len(Lowalpha)>=1:
        pswd+=Lowalpha
    if len(Lowalpha)<1:
        re_callback("abc")
        bol=False
    if len(num)>=1:
        pswd+=num
    if len(num)<1:
        re_callback("123")
        bol=False
    if len(Capalpha)>=1:
        pswd+=Capalpha
    if len(Capalpha)<1:
        re_callback("ABC")
        bol=False
    if len(symbol)>=1:
        pswd+=symbol
    if len(symbol)<1:
        re_callback("###")
        bol=False
    if bol==False:
        #Checking Total Length of string
        if length<6:
            print("• Error:Your password length is",length,"Minimun Passoword Length is 6")
        elif length>12:
            print("• Error:Your password length is",length,"Maximum Password Length is 12")
        return "• Password is Not Valid to Sign up"
    else:
        #Reverting password from dictionary
        if len(pswd)>=6 and len(pswd)<=12:
            for i in count.values():
                password+=str(i)
            return password

i=5
lss=''
f = open ('password.csv','a')
k = open ('password.csv','r')
for j in k:
    lss+=j
print('''•	At least 1 letter between [a-z]
•	At least 1 number between [0-9]
•	At least 1 letter between [A-Z]
•	At least 1 character from [$#@]
•	Minimum length of transaction password: 6
•	Maximum length of transaction password: 12''')
while True:
    passoword=input("Enter PASSWORD:")
    pswd=password_check(passoword)
    i-=1
    if passoword==pswd:
        print("Password Check Passed")
        print(pswd,"is Valid")
        print("If You want to Save passord with Your Name: Type Y/N:")
        en_inp=input().lower()
        if en_inp=="y":
                if not(lss.startswith("N")):
                    f.write("Name"+','+"Password \n".capitalize())
                    name=input("Enter Your Name:")
                    f.write(name+','+pswd+'\n')
                    f.close()
                else:
                    name=input("Enter Your Name:")
                    f.write(name+','+pswd+'\n')
                    f.close()
                    print("Password is saved successfully")
                    print("••••••••••••••••••")
                    break
        else:
            print("OK Password will be Not Saved:")
            print("••••••••••••••••••")
        break
    else:
        if i>0:
            print("Please Enter Correct Password: You have %d attempts left"%(i)) 
        else:
            print("You have 0 attempts left Try again later")
            break
    