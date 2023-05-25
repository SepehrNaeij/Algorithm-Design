def Succus(number):
    if number == 0:
        return False
    else:
        return True
        
def Monopouli(text):
    check = True
    succus_test = True
    moves = ""
    result = []
    main_result = ""
    
    moves = text.split(",")
        
    count = -1 
    index = 0   
    while check:
        count = count + 1
        if ( count == 0 ):
            result.append(moves[0])
        else:
            #max_index = largest(index, index+int(moves[index]), moves)
            index = index + int(moves[index])
            if index < len(moves):
                 result.append(moves[index])
                 succus_test = Succus(int(moves[index]))
                 if succus_test == False:
                     check = False
            else:
                if count != len(moves):
                    result.append(moves[-1])
                    check = False
                    
    if succus_test == True:            
        moves_count = len(result) - 1  
    else:
        moves_count = "Unreachable!"
                      
    print(moves_count) 
    
    for i in range(0,len(result)):
        if i == len(result) - 1:
            main_result += str(result[i])
        else:
            main_result += str(result[i]) + "-"          
    
    return main_result            
    
text = input()
awnser = (Monopouli(text))
print(awnser)
    
                   

        
            
