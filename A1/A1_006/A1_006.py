num1 = int(input("ตัวเลขที่ 1 : "))
num2 = int(input("ตัวเลขที่ 2 : "))

if num2 != 0:
    if num1 % num2 == 0:
        print("yes")
    else:
        print("no")
else:
    print("หารด้วยศูนย์ไม่ได้")