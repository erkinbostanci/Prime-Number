def pri_number(number):
    if number == 1:
        return False
    if number == 2:
        return True
    else:
        for i in range(2,number):
            if number % i == 0:
                return False
        return True

while True:
    number = input("Enter the number: ")
    if number == 'q':
        break
    else:
        sayi = int(number)

        if (pri_number(sayi)):
            print(number,"is prime number")
        else:
            print(number,"not prime number")