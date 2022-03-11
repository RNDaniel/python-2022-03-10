print("gondolj egy számra 1 es 10 között")
min =1
max =10
inp =  0
guess = (min+max)//2
while guess != "e":
    guess = (min+max)//2
    print("kisebb mint " + str(guess) +"? (k,n,e)")
    inp =  input()
    if inp == 'k':
        max=guess
        quess = (min+max)//2
    elif inp == 'n':
        min = guess
        guess = (min+max)//2
    elif inp=='e':
        print("A szám: " + str(guess))
        guess='e' 
    else:
        print("nem megfelelő szám")