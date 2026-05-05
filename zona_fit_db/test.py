create_phone_number =[1, 2, 3, 4, 5, 6, 7, 8, 9, 0] # => returns "(123) 456-7890"

def create_contact(n):
    tel = ''
    for x in n:
        tel = tel + str(x)


    return f'({tel[:3]}) {tel[3:6]}-{tel[6:10]}' # => returns "(123) 456-7890"


print(create_contact(create_phone_number))