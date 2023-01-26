import datetime
print(datetime.date.today())
print("Введите имя")
data = str(input())
print("Введите возраст")
age = int(input())
def Smoke(data):
    if(age >= 18):
        print(f"{data} Ты можешь курить")
    else:
        print(f"{data} Ты не можешь курить")

Smoke(data)