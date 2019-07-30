fizzBuzz_dict = {}

def add_Value():
    keyword, diviValue = input("""Enter a keyword, followed by a integer value that you wish to test (seperate with a space).
    If you wish to stop adding values, type 'STOP 0' """).split()

    if keyword.upper() == 'STOP' and diviValue == '0':
        quit
    else:
        keyword = keyword.strip()
        diviValue = diviValue.strip()
        fizzBuzz_dict[keyword] = diviValue

    return keyword, diviValue

maxvalue = int(input("Please print the maximum value we'll count up to: "))
keyword, diviValue = add_Value()

while keyword.upper() != 'STOP' and diviValue != '0':
    keyword, diviValue = add_Value()

print(fizzBuzz_dict)
# Above assembles the dictionary of values and their keywords
# Below, we want to know for which values in the range one, two, or all three divide a value

#Does just one of the values divide values in the range?
for x in range(1, (maxvalue+1)): 
    print('\n')
    total = 0
    for k, v in fizzBuzz_dict.items():
        v = int(v)
        if (x%v) != 0:
            total += 1
        else:
            print(k, end = ' ')
    if total == len(fizzBuzz_dict):
        print('\n', x)
    else:
        continue





