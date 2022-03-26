def main():   
    purpose = input('Confirm or search: ')
    if 'confirm' in purpose:
        confirm()
    elif 'search' in purpose:
        search()
    else:
        main()


def confirm():
    while True:
        number = input('Your number: ')
        if number.isdigit() == True:
            number = int(number)
            break
        else:
            continue
    not_prime = False 
    if number < 2:
        print('This is not prime number')
    if number > 1:
        for a in range(2,number-1):
            if number % a == 0:
                not_prime = True
                break
            if number % a != 0:
                not_prime = False
        if not_prime:
            print('This is not prime number')          
        if not_prime == False:
            print('This is prime number')    
    

def search():
    while True:
        number = input('Your number: ')
        if number.isdigit() == True:
            number = int(number)
            break
        else:
            continue  
    print('2')
    for i in range(2,number):
        not_prime = True
        for a in range(2, i):
            if i % a == 0:
                not_prime = True
                break
            if i % a != 0:
                not_prime = False    
        if not_prime == False:
            print(i)                


main()












