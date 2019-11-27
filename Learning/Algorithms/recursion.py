
# Recursion

def count_down(n):
    print(n)

    if n == 0:
        return

    count_down(n-1)
    # implicit return at the end of the function


def sum_up_to(n: int) -> int:
    if n == 1:
        return 1
    else:
        return n + sum_up_to(n-1)


print(sum_up_to(5))


def main():
    count_down(69)



if __name__ == "__main__":
    pass
    # main()