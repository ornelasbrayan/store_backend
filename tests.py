
def say_hello():
    print("Hello")

def some_number():
    prices = [1.5, 2.5, 3.5, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0,
          11.0, 12.0, 13.0, 14.0, 15.0, 16.0, 17.0, 18.0, 19.0, 20.0]
    total = 0
    results = 0
    for num in prices:
        total += num 
        if num < 12:
            results += 1
    
    print("Total: " + str(total) + " Lower than 12: " + str(results))

def some_color():
    colors = ["red", "Green", "blue", "yellow", "green", "Orange", "Red", "BLUE", 
        "YELLOW", "blue", "purple", "Pink", "brown", "Black", "white", "GREY", "silver", 
        "Gold", "Cyan", "magenta", "BluE"]
    count = 0
    for color in colors:
        if color.lower() == "blue":
            count += 1

    results = []
    for color in colors:
        col = color.lower()
        if col not in results:
            results.append(col)
    
    print(results)       
    print(len(colors))
    print(str(count))
    
def some_ages():
    ages = [24, 35, 18, 46, 29, 51, 22, 33, 40, 27, 55, 19, 31, 37, 43, 25, 49, 20, 23, 26]
    count = 0
    repeat = 0
    for num in ages:
        if num > 30:
            count += 1
        if num >= 25 and num <= 35:
             repeat += 1

    print(f"There are {str(repeat)} numbers between 25 and 35")
    print(f"There are {str(count)} numbers over 30")



some_ages()
some_color()
some_number()
say_hello()