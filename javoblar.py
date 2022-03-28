#son = float(input("Juft son kiriting: "))
#if son%2==0:
#    print("Rahmat!")
#else:
#    print("Bu son juft emas.")
#yosh = int(input("Yoshingiz nechida "))
#if yosh<= 4 or yosh>= 60:
#    narx = 0
#    print(f"Chipta {narx} so'm")
#elif yosh < 18:
#    narx = 1000
#    print(f"Chipta {narx} so'm")
#else:
#    narx = 20000
#    print(f"Chipta {narx} so'm")

users = ['alisher1983', 'aziza', 'umar', 'yasina']
login = input("Login kiriting: ")
if login in users:
    print("Login band, yangi login tanlang!")
else:
    print("Xush kelibsiz!")