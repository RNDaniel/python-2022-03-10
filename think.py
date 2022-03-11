#print("gondolj egy számra 1 es 10 között")
#min =1
#max =10
#inp =  0
#guess = (min+max)//2
#while guess != "e":
#    guess = (min+max)//2
#    print("kisebb mint " + str(guess) +"? (k,n,e)")
#    inp =  input()
#    if inp == 'k':
#        max=guess
#        quess = (min+max)//2
#    elif inp == 'n':
#        min = guess
#        guess = (min+max)//2
#    elif inp=='e':
#        print("A szám: " + str(guess))
#        guess='e' 
#    else:
#        print("nem megfelelő szám")

    
min =1
max =100

print(f"gondolj egy számra {min} es {max} között")


answer = "x"
prev_guess = -1
guess=-2
while answer != "e":
    prev_guess=guess
    guess = (min+max)//2
    if guess == prev_guess:
        print("ne szórakozz")
        answer="e"
    else:        
        print(f"""Aszám amire gondoltam: {guess}
        Válassz kérlek!
        e-egyenlő
        k-kisebb
        n-nagyobb
        """)
        answer = input("Mi a válaszod?")
        if answer =="k":
            max=guess
        elif answer =="n":
            min=guess
        elif answer =="e":
            print(f"Eltaláltam a szám a {guess}")
        else:
            print("Ez nem válasz!")
    