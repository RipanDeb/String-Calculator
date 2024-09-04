def add(numbers: str) -> int:

    if numbers == "":
        return 0
    
    if numbers.startswith('//'):
        end = numbers.find('\n')
        divider = numbers[2:end]
        numbers = numbers[end + 1:]
        mylist = list(map(int, numbers.split(divider)))
    else:
        mylist = list(map(int, numbers.replace('\n', ',').split(',')))
    
    negative_numbers = [i for i in mylist if i < 0]

    if negative_numbers:
        raise ValueError(f"negative numbers not allowed {', '.join(map(str, negative_numbers))}")

    return sum(mylist)


print(add(""))
print(add("5"))
print(add("1,9"))
print(add("1\n3,5"))
print(add("//;\n1;7"))
#print(add("1,2,-10"))