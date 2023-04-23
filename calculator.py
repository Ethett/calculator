# funkcja dodająca ułamki
def add_frac(num1, den1, num2, den2):
    den3 = gcd(den1, den2)
    den3 = (den1*den2) / den3
    num3 = (num1)*(den3/den1) + (num2)*(den3/den2)
    common_factor = gcd(num3, den3)
    den3 = int(den3/common_factor)
    num3 = int(num3/common_factor)
    return num3, den3

# funkcja odejmująca ułamki
def sub_frac(num1, den1, num2, den2):
    den3 = gcd(den1, den2)
    den3 = (den1*den2) / den3
    num3 = (num1)*(den3/den1) - (num2)*(den3/den2)
    common_factor = gcd(num3, den3)
    den3 = int(den3/common_factor)
    num3 = int(num3/common_factor)
    return num3, den3

# funkcja mnożąca ułamki
def mul_frac(num1, den1, num2, den2):
    num3 = num1 * num2
    den3 = den1 * den2
    common_factor = gcd(num3, den3)
    den3 = int(den3/common_factor)
    num3 = int(num3/common_factor)
    return num3, den3

# funkcja dzieląca ułamki
def div_frac(num1, den1, num2, den2):
    num3 = num1 * den2
    den3 = den1 * num2
    common_factor = gcd(num3, den3)
    den3 = int(den3/common_factor)
    num3 = int(num3/common_factor)
    return num3, den3

# funkcja znajdująca największy wspólny dzielnik
def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

# pobranie ułamka od użytkownika
def get_frac():
    num = int(input("Podaj licznik ułamka: "))
    den = int(input("Podaj mianownik ułamka: "))
    return num, den

# wyświetlanie wyniku
def display_result(num, den):
    if den == 1:
        print(num)
    else:
        print("{}/{}".format(num, den))

# menu
def main():
    print("Witaj w kalkulatorze ułamków!")
    while True:
        print("Wybierz działanie:")
        print("1. Dodawanie")
        print("2. Odejmowanie")
        print("3. Mnożenie")
        print("4. Dzielenie")
        print("5. Wyjście")
        choice = int(input("Wybierz opcję (1-5): "))
        if choice == 1:
            num1, den1 = get_frac()
            num2, den2 = get_frac()
            num3, den3 = add_frac(num1, den1, num2, den2)
            display_result(num3, den3)
        elif choice == 2:
            num1, den1 = get_frac()
            num2, den2 = get_frac()
            num3,

