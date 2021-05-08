import secrets
import argparse

nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
class RNG:

    def generate_random_number(self, digits):
        res = [secrets.choice(nums) for _ in range(digits)]
        return int(''.join(str(a) for a in res))


if __name__ == '__main__':
    rng = RNG()
    parser = argparse.ArgumentParser()
    parser.add_argument("digits", help="Number of digits random number will have.", type=int)
    args = parser.parse_args()

    print(rng.generate_random_number(args.digits))






# print(random_number(4))
# print(random_number(5))
# print(random_number(6))
# print(random_number(7))
# print(random_number(8))
# print(random_number(9))
# print(random_number(10))
