###code to check if a number is prime:

def is_prime(num):
    checking = 2

    while checking <= num:
        if num % checking == 0:
            if checking != 1 and checking != num:
                return False
            else:
                return True
        checking += 1