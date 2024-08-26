def kalkulator():
    print("Prosty kalkulator")
    print("Wybierz operację:")
    print("1. Dodawanie (+)")
    print("2. Odejmowanie (-)")
    print("3. Mnożenie (*)")
    print("4. Dzielenie (/)")

    # Pobierz wybór od użytkownika
    wybor = input("Wybierz operację (1/2/3/4): ")

    # Pobierz liczby od użytkownika
    liczba1 = float(input("Podaj pierwszą liczbę: "))
    liczba2 = float(input("Podaj drugą liczbę: "))

    # Wykonaj operację w zależności od wyboru
    if wybor == '1':
        wynik = liczba1 + liczba2
        print(f"Wynik: {liczba1} + {liczba2} = {wynik}")
    elif wybor == '2':
        wynik = liczba1 - liczba2
        print(f"Wynik: {liczba1} - {liczba2} = {wynik}")
    elif wybor == '3':
        wynik = liczba1 * liczba2
        print(f"Wynik: {liczba1} * {liczba2} = {wynik}")
    elif wybor == '4':
        if liczba2 != 0:
            wynik = liczba1 / liczba2
            print(f"Wynik: {liczba1} / {liczba2} = {wynik}")
        else:
            print("Błąd: Dzielenie przez zero!")
    else:
        print("Nieprawidłowy wybór operacji!")

# Uruchomienie kalkulatora
kalkulator()
