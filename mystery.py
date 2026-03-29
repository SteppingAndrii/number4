# my_list = [1, 2, 3, 4]
# iterator = iter(my_list)
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))


# class Counter:
#     def __init__(self, max_number):
#         self.i = 0
#         return self

#     def __iter__(self):
#         self.i = 0
#         return self

#     def __next__(self):
#         self.i += 1
#         if self.i > self.max_number:
#             raise StopIteration
#         return self.i
# count = Counter(5)

# try:
#     print(count.__next__)
#     print(count.__iter__)

#     print(next(count))
#     print(iter(count))
#     print(next(count))
# except StopIteration:
#     print("Counter has reached her limit")


# def raise_to_the_degrees(number, max_number):
#     i = 0
#     # while True:
#     #     yield number **i
#     #     i += 1
    
#     for _ in range(max_number):
#         yield number ** i
#         i += 1
# res = raise_to_the_degrees(10,10)
# print(res)
# for _ in res:
#     print(_)


# def helper(work):
#     work_in_memory = work
#     def helper(work):
#         return f"i will help you with your {work_in_memory}. afterwards i will help you with {work}"
#     return helper

# helper = helper("homework")
# print(helper("cleaning"))
# print(helper("driving"))


def generate_even_numbers(quantity):
    even_numbers = []
    i = 0

    while (len(even_numbers) < quantity):
        if i % 2 == 0:
            even_numbers.append(i)
        i += 1
    return even_numbers

for i in generate_even_numbers(5):
    print(i)