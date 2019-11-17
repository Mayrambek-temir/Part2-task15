age=int(input('Enter your age :'))

def even_numbers(age):
    if age % 2 == 0:
        for i in range(age):
            if i == 0:
                continue
            elif i % 2 == 0:
                print(i)
    elif age % 2 != 0:
        for i in range(age):
            if i == 0:
                continue
            elif i % 2 != 0:
                print(i)


even_numbers(age)
