print("Hello world")

for x in range(1,101):
    if (x%3) == 0 and (x%5) == 0:
        print("fizzbuzz {}".format(x))
    elif (x%5) == 0:
        print("buzz {}".format(x))
    elif (x%3) == 0:
        print("fizz {}".format(x))
    else:
        continue
