while True:
        
        try:    
            number_students = int(input('Number Student> '))
            if 1 <= number_students <= 100:
            
                #? create empty list and dictionaries for save data stringletter
                sort_view = []
                sort_letter = {}
                #? method for show line added string letter 
                for _ in range(number_students):
                    string_letter = input('> ').strip().lower()
                    if (string_letter.isalpha() == False) or (1 >len(string_letter)> 100) :
                        raise TypeError('string input type error')
                    sort_view.append(string_letter)

                #? loop letter in string for sort letter
                for student in sort_view:
                    for letter in student:
                        sort_letter.setdefault(letter, 0)
                        sort_letter[letter] += 1

                #! create value found letter and value final for result view
                status_found = 0
                result_view = 0

                #? check and sort letter in subject view
                for letter in sort_letter.keys():
                    for string_letter in sort_view:
                        if letter in string_letter:
                            status_found += 1
                    if status_found == len(sort_view):
                        result_view += 1
                        status_found = 0

                #! return -1 if not found top view
                if result_view == 0:
                    result_view = -1

                #* show subject top view
                print(result_view)
                break
            else:
                raise ValueError()
        except ValueError : 
            print('Please enter integer between 1 and 100!')
        except TypeError:
            print(f'Please enter letter between 1 and 100  not( integer, symbols...etc)!\n{"-"*10}')

