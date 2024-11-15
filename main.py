def weather(temp):
    if temp>22:
        print("Today is a hot day.")

    else:
        print("Today is a cold day")

temp = int(input("Enter the temperature of today: "))

weather(temp)