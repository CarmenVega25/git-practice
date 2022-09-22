# Taken From
# Iterating Over Data
# Problem-Set While Loops #11
def silly_sum():
    """ reads numbers from the user (use input_int) 
        summing as we go until either
        the user enters 0, or
        the sum reaches or exceeds 1000
    """
    input_int = 0
    num = input("Enter a number: ")
    while num != 0 and input_int < 999:
        input_int += int(num)
        print(input_int)
        num = input("Enter a number: ")

    return input_int

if __name__ == "__main__":
    print(f"Answer = {silly_sum()}")
