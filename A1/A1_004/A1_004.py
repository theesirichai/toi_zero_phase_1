ex_s = float(input("ป้อนคะแนนแบบฝึกหัด (เต็ม 10): "))
mid_s = float(input("ป้อนคะแนนกลางภาค (เต็ม 40): "))
fin_s = float(input("ป้อนคะแนนปลายภาค (เต็ม 50): "))

exs_percent = (ex_s / 10) * 100
mids_percent = (mid_s / 40) * 100
fins_percent = (fin_s / 50) * 100

if exs_percent >= 50 and mids_percent >= 50 and fins_percent >= 50:
    print("pass")
else:
    print("fail")