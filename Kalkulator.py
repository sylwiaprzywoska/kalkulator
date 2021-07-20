import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(message)s')

def dodawanie(liczba1, liczba2):
  logging.debug("Dodaję %.2f i %.2f" %(liczba1, liczba2))
  return(liczba1 + liczba2)
def odejmowanie(liczba1, liczba2):
  logging.debug("Odejmuję %.2f i %.2f" %(liczba1, liczba2))
  return(liczba1 -liczba2)
def mnozenie(liczba1, liczba2):
  logging.debug("Mnożę %.2f i %.2f" %(liczba1, liczba2))
  return(liczba1 * liczba2)
def dzielenie(liczba1, liczba2):
  logging.debug("Dzielę %.2f i %.2f" %(liczba1, liczba2))
  return(liczba1 / liczba2)

if __name__ == "__main__":
  dzialanie = int(input("Podaj działanie, posługując się odpowiednią liczbą:\n 1 Dodawanie,\n 2 Odejmowanie,\n 3 Mnożenie,\n 4 Dzielenie: "))
  liczba1 = float(input("Podaj składnik 1. "))
  liczba2 = float(input("Podaj składnik 2. "))
  if dzialanie == 1:
    print(f"Wynik to: {dodawanie(liczba1, liczba2)}")
  if dzialanie == 2:
    print(f"Wynik to: {odejmowanie(liczba1, liczba2)}")
  if dzialanie == 3:
    print(f"Wynik to: {mnozenie(liczba1, liczba2)}")
  if dzialanie == 4:
    print(f"Wynik to: {dzielenie(liczba1, liczba2)}")
  if dzialanie > 4 or dzialanie < 1:
    logging.error("Nie ma takiego działania")
