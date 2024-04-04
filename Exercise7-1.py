#1.Password Criteria Checker

def password_validate(pwd):
    count=0
    if not (len(pwd)>=8 and len(pwd)<=16):
        return "Password length not met"
    if pwd!=pwd.upper(): #if lowercase
        count+=1
    if pwd!=pwd.lower(): #if uppercase
        count+=1
    for i in pwd:
        if i.isdigit():
            count+=1
            break
    for i in pwd:
        if not i.isalnum():
            count+=1
            break
    if count==4:
        return "Password Strength is Strong"
    elif count==2 or count==3:
        return "Password Strength is Medium"
    else:
        return "Password Strength is Poor"

x=input("Enter the Password: ")
print(password_validate(x))