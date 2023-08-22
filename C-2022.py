while True:
    try:    
        amount =  int(input('> '))
        if  2 <= amount <= (10**12)  :
            #? create list in order to keep the possibilities possible
            lst_possibilities = []
            #? loop for check all possibilities in range amount
            for i in range(amount):
                if amount % (i+1) == 0 :
                    lst_possibilities.append(i)
            break
        else:
            print('Please enter amount between (2 and 10^12)!')
            continue
    except ValueError:
        print('Please enter integer!')

#! show line possibilities after dump list possibilities:
print(*lst_possibilities, sep=' ')