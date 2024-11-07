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


Word2 = "gALLLO"
List = list(Word2)
List[1].isalpha()

for i in List: 
    Ab = i.isalpha()
   