# Author: Chetan Mitra czm5805@psu.edu


def run():
  number = int(input("Enter an int: "))
  sum = digit_sum(number)
  print(f"sum of digits of {number} is {sum}.")
 

def digit_sum(n):
  if n<1:
    return 0
  else:
    return n%10 + digit_sum(n//10)


if __name__ == "__main__":
  run()