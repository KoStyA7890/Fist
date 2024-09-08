a = input("ведіть свое імя:")
print("Привіт", a, ",раді бачити вас!")
while True:
   if not a:
    print("Ви нічого не ввели")
   else:
    print("Привіт", a, ",раді бачити вас!")
    break

while True:
   b = int(input("Введіть свій вік:"))
   if not b:
    print("Ви нічого не ввели")
   else:
    print(a)
    if b >= 18:
        print("Ви  повнолітній")
    else:
        print("ви не повнолітній")
    break

