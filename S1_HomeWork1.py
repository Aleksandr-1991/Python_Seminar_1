print("\033[H\033[J", end="")

n, res = 789, 0
while n > 0:
    res += n%10
    n //= 10
# print(res)