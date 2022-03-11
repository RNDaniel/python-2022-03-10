number = 200
if number<100:
    print("A szám kisebb mint száz")
print("end") 

number = 5
if number<0:
    print("Negatív")
elif number ==0:
    print("Nulla")
else:
    print("Pozitív")

number =int(input("szám"))
if(number%2)==0:
    print("paros")
else:
    print("paratlan")

l = [5,2,-5,3,-6,1]
sum = 0
for i in l:
    if i>0:
        sum +=i
print(sum)

i = 0
while i!=10:
    i+=1
    print(i)

n=1
while n!=0:
    print("nem nulla") 
    n=int(input())

while int(input())!=0:
    print("nem nulla") 

print("gondolj egy számra 1 es 10 között")
min =1
max =10
while guess != "e":
    guess = (min+max)/2
    print("kisebb mint " + str(guess) +"? (k,n,e)")
    inp =  input()
    if inp == 'k':
        max=guess
    elif inp == 'n':
        min = guess
    elif inp=='e':
        print("A szám: " + str(guess)) 
    else:
        print("nem megfelelő szám")

    
    


