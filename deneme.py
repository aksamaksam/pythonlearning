def collatz(number):
    if number%2==0:
            number=number//2
    elif number%2==1:
            number=3*number+1
    return number


            

print("Enter a number:")

while True:
    try:
        i=int(input())
    
        while i!=1:
            i=collatz(i)
            print(i)
        if i==1:
            break

    except ValueError:
        print("Please enter a NUMBER")
        continue
    

    
