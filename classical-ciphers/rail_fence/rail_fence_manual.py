def encrypt_fence(text, key) :
    rail = [['\n' for i in range(len(text))] for j in range (key)]
    dir_down = False
    row, col = 0, 0
    for i in range(len(text)):
        if(row == 0) or (row == key-1):
            dir_down = not dir_down
        #filling tge corrsponding alphabet
        rail[row][col] = text[i]
        col+=1
        
        if dir_down :
            row+=1
        else:
            row-=1
    #Now constructing the cipher using the ril matrix
    result = []
    for i in range(key):
        for j in range(len(text)):
            if(rail[i][j] != '\n'):
                result.append(rail[i][j])
    return ("".join(result))


def decrypt_fence(cipher, key):
    rail = [['\n' for i in range(len(cipher))] for j in range(key)]
    result = []
    dir_down = None
    row, col = 0, 0
    
    #Initially marking the places with the - using the encryption logic
    for i in range(len(cipher)):
        
        if(row == 0) or (row == key-1):
            dir_down = not dir_down
        
        rail[row][col] = '-'
        col+=1
        if(dir_down):
            row += 1
        else:
            row -= 1
    #Now let's fill the rail matrix by iteratively traversing the matrix
    index = 0
    for i in range(key):
        for j in range(len(cipher)):
            if ((rail[i][j] == '-') and (index < len(cipher))) :
                rail[i][j] = cipher[index]
                index +=1
    
    #Now with the help of the enc logic , help to collect the alphabets
    row, col = 0, 0
    dir_down = False
    for i in range(len(cipher)) : 
        if(row  == 0 ) or (row == key-1):
            dir_down = not dir_down
        if(rail[row][col] != '-') : 
            result.append(rail[row][col])
            col+=1
        
        if(dir_down) : 
            row += 1
        else:
            row -= 1
    return("".join(result))

#main code
if __name__ == "__main__":
    print(encrypt_fence("GEEKS FOR GEEKS", 3))
    print(decrypt_fence("GSREEK O EKEFGS", 3))