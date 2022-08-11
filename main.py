import random

def ibanGenerator():
    a = str(random.randint(10, 99))
    b = str(random.randint(35000000000, 40000000000))
    IBAN = "GB" + a + "BARC200" + b
    print(IBAN)


ibanGenerator()