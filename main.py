#TEST DATA - AREA OF A CIRCLE
def area_circle (pi, r):
    area= pi * r**2
    return round(area,2)

print(area_circle(3.1416, 10))

#TEST DATA - TAXES
def taxes (money, tax):
    t_due = money + (money * (tax/100))
    return t_due

print(taxes(68, 8))

#TEST DATA - TEMPERATURE

def temperature(fahrenheit):
    celcius = (fahrenheit - 32) * (5/9)
    return round(celcius, 4)

print (temperature(32))