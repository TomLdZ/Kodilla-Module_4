import logging
logging.basicConfig(level=logging.DEBUG)


def add(a, b):
    logging.debug("Wybrano dodawanie")
    logging.debug(f"Dodaję {a} i {b}")
    return a + b

def sub(a, b):
    logging.debug("Wybrano odejmowanie")
    logging.debug(f"Od {a} odejmuję {b}")
    return a - b

def multi(a, b):
    logging.debug("Wybrano mnożenie")
    logging.debug(f"Mnożę {a} i {b}")
    return a * b

def div(a, b):
    logging.debug("Wybrano dzielenie")
    logging.debug(f"Dzielę {a} przez {b}")
    return a / b

op_dict = {'+':add, '-':sub, '*':multi, '/':div}


if __name__ == "__main__":
    while True:
        a = input("Podaj składnik nr 1. Części dziesiętne oddzielaj znakiem: '.': ")
        try:
            if float(a):
                logging.debug(f"Składnik nr 1 = {a}")
                break
        except ValueError:
            continue
    while True:
        b = input("Podaj składnik nr 2. Części dziesiętne oddzielaj znakiem: '.': ")
        try:
            if float(b):
                logging.debug(f"Składnik nr 2 = {b}")
                break
        except ValueError:
            continue

    while True:
        s = input("Podaj działanie, posługując się odpowiednim znakiem: Dodawanie: '+', Odejmowanie: '-', Mnożenie '*', Dzielenie '/': ")
        if s in op_dict:
            value = op_dict[s](float(a), float(b))
            logging.debug(f"Wynik wynosi = {value}")
            break
    

    


