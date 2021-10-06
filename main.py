#Create a function called countA() that returns the number of "a"s in a given word w
def countA(w):
    
    total = 0
    
    for i in range(0, len(w)):
        if w[i] == "a":
            total = total + 1

    return total

print(countA("cat"))