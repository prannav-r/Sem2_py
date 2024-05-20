import re
'''email=input()
if re.match("^[a-z][a-z 0-9 ._-]*[@][a-z]*.com$",email):
    print("Valid Email")
else:
    print("Invalid Email")

def ok(x):
    if len(x)<3:
        return x
    else:
        if x[len(x)-3::]=="ing":
            x+="ly"
            return x
        else:
            x+="ing"
            return x

print(ok("readin"))

supermarket = {"milk": {"quantity": 20, "price": 25.00},
               "biscuits" : {"quantity": 32, "price": 20.00},
               "butter": {"quantity": 20, "price": 70.50},
               "cheese": {"quantity": 15, "price": 82.50},
               "bread": {"quantity": 15, "price": 45.00},
               "cookies": {"quantity": 20, "price": 52.80},
               "yogurt": {"quantity": 18, "price": 41.30},
               "apples": {"quantity": 35, "price": 120.40},
               "oranges": {"quantity": 40, "price": 60.50},
               "bananas": {"quantity": 23, "price": 50.00}} 
customers = ["Frank", "Mary", "Paul"] 
shopping = {"Frank" : [('milk', 5), ('apples', 5), ('butter', 1), ('cookies', 1)],
          "Mary": [('apples', 2), ('cheese', 4), ('bread', 2),
               ('pears', 3), ('bananas', 4), ('oranges', 1), ('cherries', 4)],
          "Paul": [('biscuits', 2), ('apples', 3), ('yogurt', 2),
               ('pears', 1), ('butter', 3), ('cheese', 1), ('milk', 1), ('cookies',4)]}

def available(supermarket,shopping):
    for i in shopping:
        for j in shopping[i]:
            if j[0] not in supermarket:
                print("Item Unavailable")
            if j[1]<=supermarket[j][0]["quantity"]:
                print("Stock Available")
            else:
                print("Stock unavailable")

available(supermarket,shopping)

def rev(x):                                      
    if x==0:
        return 1
    else:
        return x*rev(x-1)

print(rev(5))

x=[{"id":7,"name":"pr"},{"id":3,"name":"Ok"}]

asc=lambda l:sorted(l,key=lambda i:i['id'],reverse=True)
print(asc(x))

f=open("ok.txt",'r')
print(f.readlines(2))'''