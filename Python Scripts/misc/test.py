# from __future__ import division
# from datetime import (datetime, timedelta)
#
#
# now = datetime.now()
#
# out = []
# for i in range(1, 1001):
#     temp = {"timestamp": str(now + timedelta(seconds=i)), "progress_percentage": (i / 1000) * 100}
#     out.append(temp)
# b = open("download.log", "w").writelines("\n".join(list(set([str(o) for o in out]))))
# print(out)

# read from file
logs = open("download_1.log").readlines()

# sorting logs based on time
sorted_logs = sorted(logs, key=lambda x: x["timestamp"])

# conveting string to variables
import ast
log_str = '''{"timestamp": "2017-02-24 01:12:03.234892", "progress_percentage": 10}'''
log_dict = ast.literal_eval(log_str)
print(log_dict["progress_percentage"])  # 10

# converting string date time datetime object
from datetime import datetime
time1 = datetime.strptime("2017-02-24 01:12:03.234892", "%Y-%m-%d %H:%M:%S.%f")
time2 = datetime.strptime("2017-02-25 01:12:03.234892", "%Y-%m-%d %H:%M:%S.%f")
print(time1 < time2)    # True

input_word = "pokemon"
output_word_list = list()
for i in range(1, len(input_word)):
    output_word_list.extend([input_word[:i], input_word[i:]])

print(output_word_list)
#
#
# def func1(val):
#     val += 'bar'
#
# x = 'foo'
# x
# func1(x)
# x
#
#
# def func2(val):
#     val += [3, 2, 1]
#
# x = [1, 2, 3]
# x
# func2(x)
# x
#
#
# from functools import wraps
#
#
# def authorize(func):
#     @wraps(func)
#     def check_credentials(*args, **kwargs):
#         # check the login credentials
#         return func(*args, **kwargs)
#     return check_credentials
#
#
# @authorize
# def apiCall(username, password):
#     # do operation
#     pass
#
#
# def foo(a, *args):
#     print(a, args)
#
# foo(1, 2, 3, 4)
#
# foo(1, *[2, 3, 4])
#
#
# def bar(a, **kwargs):
#     print(a, kwargs)
#
# bar(1, b=2, c=3, d=4)
#
#
# def foo_bar(a, *args, **kwargs):
#     print(a, args, kwargs)
#
# foo_bar(1, 2, 3, 4, b=5, c=6, d=7)
#
#
#
#
# # 'is' compares object level identity
# # '==' compares value level identity
#
# a = [1, 2, 3]
# b = a
# a
# b
#
#
# a is b
# a == b
#
#
# a = [1, 2, 3]
# b = list(a)
# a
# b
#
# a is b
# a == b
#
#
#
# a = ["one", "two", "three"]
# a.append("four")
# a
#
#
# a = ["one", "two", "three"]
# a.append(["four", "five"])
# a
#
#
# a = ["one", "two", "three"]
# a.extend(["four", "five"])
# a
#
#
# a = ["one", "two", "three"]
# print(a.index("two"))
#
#
# a = ["one", "two", "three"]
# a.remove("one")
# a
#
#
# a = [5, -1, 10]
# a.sort()
# a
#
#
# a = ["one", "two", "three"]
# a.reverse()
# a
#
#
# a = ["one", "two", "three"]
# a.pop(2)
#
#
# a = ["one", "two", "three"]
# a.insert(1, "four")
# a
#
#
#
# # This prints out: 'First Value-Second Value'
# '{0}-{1}'.format('First Value', 'Second Value')
#
# # This prints out: 'My name is Chris. I like Machine Learning'
# 'My name is {name}. I like {interest}'.format(name='Chris', interest="Machine Learning")
#
#
# "\n Harry Potter ".strip()
#
# "Harry Potter".lower()
# "Harry Potter".upper()
#
#
# "abc".isalpha()
# "abc ".isalpha()
#
#
# "123".isdigit()
# "123a".isdigit()
#
#
# " \t\n".isspace()
# " 1\t\n".isspace()
#
#
# "Star Wars".startswith("S")
# "Star Wars".startswith("s")
#
#
# "Star Wars".find("Wars")
# "Star Wars".find("wars")
#
#
# "Star Wars".replace("Wars", "Battle")
#
#
# "Star Wars".split(" ")
#
#
# "||".join(["Monty", "Python's", "Circus"])
#
# # def pow2s():
# #     yield 1
# #     for i in map((lambda x: 2 * x), pow2s()):
# #         yield i
# #
# #
# # def mymap(func, iteration):
# #     for i in iteration:
# #         yield func(i)
# #
# #
# # def read_in_chunks(file_object, chunk_size=1024):
# #     """Lazy function (generator) to read a file piece by piece.
# #     Default chunk size: 1k."""
# #     while True:
# #         data = file_object.read(chunk_size)
# #         if not data:
# #             break
# #         yield data
# #
# #
# # f = open('really_big_file.dat')
# # for piece in read_in_chunks(f):
# #     process_data(piece)
# #
# #
# # def process_data():
# #     pass
