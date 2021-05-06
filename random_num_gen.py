import secrets

nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

def random_number(digits):
    res = [secrets.choice(nums) for _ in range(digits)]
    return int(''.join(str(a) for a in res))





print(random_number(4))
print(random_number(5))
print(random_number(6))
print(random_number(7))
print(random_number(8))
print(random_number(9))
print(random_number(10))
