spam=["apples","bananas","tofu","cats","deli","bulut","dana"]

def commaCode(givenList):
    for i in range(len(givenList)-1):
        print(givenList[i],end=", ")
    print("and " + givenList[len(givenList)-1]) 

commaCode(spam)
