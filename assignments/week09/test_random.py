import random

# สุ่มเลขระหว่าง 0 - 9
test_random = random.randint(1, 20)

print("-- เกมทายตัวเลข มาเดาใจคอมพิวเตอร์กันเถอะ --")
print("-- ทายเลขจำนวนเต็มตั้งแต่ 1 - 100 --")
print("-- คุณมีโอกาส 6 ครั้ง --")

i = 0

while True:

# รับค่าการทายเลขจากผู้ใช้
print(f"ความพยายามครั้งที่ {i+1}")
guess_number = int(input("What is your guess number (1-20)?: ")) 

# condition ==> if-elif-else
if test_random == guess_number:
    print("เก่งมาก มั่วถูกตั้งแต่ครั้งแรก เทพจริงๆ")
    break

elif guess_number < test_random:
    print("ผิดจร้า น้อยไปเนอะ")

elif guess_number > test_random:
    print("ผิดจร้า มากไปหน่อย")

    if i == 3:
        get_parity_hint(random_number)
    elif i == 5:
    elif i == 7:
    elif i == 10:

def test_random():
    random_number = random.randint(1, 100)
    print(random_number)
    
test_random()