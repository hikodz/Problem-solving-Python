def guess_password(password):
    letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    failed_attempts = 0
    #! user three for loop for three position in password
    for letter_first in letters:
        for letter_second in letters:
            for letter_third in letters:
                #! woed formation to check 
                attempt = letter_first + letter_second + letter_third
                failed_attempts += 1
                print(f'Trial [{failed_attempts}]: {attempt}')
                #! if found formation password
                if password == attempt:
                    print(f"Password is {password}\nFound After {failed_attempts} Trial(s)")
                    return
guess_password("AAF")
