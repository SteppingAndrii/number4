class EvenNumbers:
  def __init__(self, quantity):
      self.quantity = quantity

  def __iter__(self):
      count = 0
      i = 0
      while count < self.quantity:
          if i % 2 == 0:
              yield i
              count += 1
          i += 1

evens = EvenNumbers(5)

for num in evens:
  print(num)
