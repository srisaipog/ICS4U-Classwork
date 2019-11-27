
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
'''
messages = []

def sum_up_to_show(n: int) -> int:
    messages.append(f"sum_up_to_show({n})")
    if n == 1:
        messages[-1] += " -- Return 1"
        return 1
    else:
        return n + sum_up_to_show(n-1)


print(sum_up_to_show(5))

messages.reverse()
print(messages)
for mess in messages:
    print(mess)
'''

# base case (n = 1)
# recursive case

def factorial(n):
    if n == 1:
        return 1


def main():
    count_down(69)



if __name__ == "__main__":
    pass
    # main()