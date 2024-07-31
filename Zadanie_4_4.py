import logging
logging.basicConfig(level=logging.DEBUG)


def calculator(s, a, b):
    if s == "+":
        return float(a) + float(b)
    elif s == "-":
        return float(a) - float(b)
    elif s == "*":
        return float(a) * float(b)
    elif s == "/":
        return float(a) / float(b)
    

if __name__ == "__main__":
    while True:
        s = input("Podaj działanie, posługując się odpowiednim znakiem: Dodawanie: '+', Odejmowanie: '-', Mnożenie '*', Dzielenie '/': ")
        if s == "+":
            logging.debug("Wybrano dodawanie")
            break
        elif s == "-":
            logging.debug("Wybrano odejmowanie")
            break
        elif s == "*":
            logging.debug("Wybrano mnożenie")
            break
        elif s == "/":
            logging.debug("Wybrano dzielenie")
            break
    while True:
        a = input("Podaj składnik nr 1. Części dziesiętne oddzielaj znakiem: '.': ")
        try:
            if float(a):
                logging.debug(f"Składnik nr 1 = {a}")
                break
        except:
            continue
    while True:
        b = input("Podaj składnik nr 2. Części dziesiętne oddzielaj znakiem: '.': ")
        try:
            if float(a):
                logging.debug(f"Składnik nr 2 = {b}")
                break
        except:
            continue
    if s == "+":
        logging.debug(f"Dodaję {a} i {b}")
    elif s == "-":
        logging.debug(f"Od {a} odejmuję {b}")
    elif s == "*":
        logging.debug(f"Mnożę {a} i {b}")
    elif s == "/":
        logging.debug(f"Dzielę {a} przez {b}")
    logging.debug(f"Wynik wynosi = {calculator(s, a, b)}")


