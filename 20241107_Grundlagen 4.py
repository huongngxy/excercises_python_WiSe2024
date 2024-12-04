# while-schleife
# Beispiel 1 
k = 3
while k > 0: 
    print(k)
    k -= 1 
print("Go!")

# Beispiel 2
k  = 0 
while k < 100:
    print(k, end = "")
    k += 1 

# Übung 





#Word = "Hallo,Berlin&/()"

#Alpha_list = list("Word")

def buchstaben_zählen(Word):
    Alpha_list = list(Word)
    count_alpha = []
    for i in Alpha_list: 
        check = i.isalpha()
        count_alpha.append(check)
        Count = count_alpha.count(True)
    return Count
        
        #count_alpha.append()
       


buchstaben_zählen("Hallo%&")

