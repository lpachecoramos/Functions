#TEST DATA - AREA OF A CIRCLE
def area_circle (pi, r):
    area= pi * r**2
    return round(area,2)

#TEST DATA - TAXES
def taxes (money, tax):
    t_due = money + (money * (tax/100))
    return round(t_due,2)

#TEST DATA - TEMPERATURE

def temperature(fahrenheit):
    celcius = (fahrenheit - 32) * (5/9)
    return round(celcius, 4)

# INPUTS
r = float(input("insert radius: "))
print(area_circle(3.1416, r))

money = float(input("insert your money: "))
tax = float(input("insert tax: "))
print(taxes(money, tax))

fahrenheit = float(input("insert your fahrenheit: "))
print(temperature(fahrenheit))