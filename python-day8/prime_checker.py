def prime_checker(number):
  is_prime = True
  if (number <= 1):
    print("It's not a prime number.")
  else:
    for i in range(2, number):
      if (number % i == 0):
        is_prime = False
        break
      
  if (is_prime):
    print("It's a prime number.")
  else:
    print("It's not a prime number.")

prime_checker(11)