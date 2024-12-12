import math

def show_menu():
    print("\nماشین حساب پیشرفته")
    print("1. جمع (+)")
    print("2. تفریق (-)")
    print("3. ضرب (*)")
    print("4. تقسیم (/)")
    print("5. توان (^)")
    print("6. جذر (√)")
    print("7. سینوس (sin)")
    print("8. کسینوس (cos)")
    print("9. تانژانت (tan)")
    print("10. لگاریتم (log)")
    print("11. خروج")

def get_two_numbers():
    num1 = float(input("عدد اول: "))
    num2 = float(input("عدد دوم: "))
    return num1, num2

def main():
    while True:
        show_menu()
        choice = input("\nیک گزینه انتخاب کنید (1-11): ")

        if choice == '1':  # جمع
            num1, num2 = get_two_numbers()
            print("نتیجه:", num1 + num2)

        elif choice == '2':  # تفریق
            num1, num2 = get_two_numbers()
            print("نتیجه:", num1 - num2)

        elif choice == '3':  # ضرب
            num1, num2 = get_two_numbers()
            print("نتیجه:", num1 * num2)

        elif choice == '4':  # تقسیم
            num1, num2 = get_two_numbers()
            if num2 != 0:
                print("نتیجه:", num1 / num2)
            else:
                print("خطا: تقسیم بر صفر ممکن نیست!")

        elif choice == '5':  # توان
            num1, num2 = get_two_numbers()
            print("نتیجه:", num1 ** num2)

        elif choice == '6':  # جذر
            num = float(input("عدد: "))
            if num >= 0:
                print("نتیجه:", math.sqrt(num))
            else:
                print("خطا: عدد منفی جذر ندارد!")

        elif choice == '7':  # سینوس
            num = float(input("عدد (به درجه): "))
            print("نتیجه:", math.sin(math.radians(num)))

        elif choice == '8':  # کسینوس
            num = float(input("عدد (به درجه): "))
            print("نتیجه:", math.cos(math.radians(num)))

        elif choice == '9':  # تانژانت
            num = float(input("عدد (به درجه): "))
            print("نتیجه:", math.tan(math.radians(num)))

        elif choice == '10':  # لگاریتم
            num = float(input("عدد: "))
            if num > 0:
                print("نتیجه:", math.log(num))
            else:
                print("خطا: لگاریتم اعداد غیرمثبت تعریف نشده است!")

        elif choice == '11':  # خروج
            print("خدانگهدار!")
            break

        else:
            print("گزینه نامعتبر است. لطفاً دوباره تلاش کنید.")

if __name__ == "__main__":
    main()