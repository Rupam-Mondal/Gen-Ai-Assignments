#1Consistency:

"""Immutable keys ensure that once a key is created,it cannot 
change. This makes  it reliable to use keys to look up values"""

""" Strings
    Numbers
    Tuples  """

#ex-->
dict = {
    "name": "Alice",
    42: "age",
    (1, 2): "coordinates"
}
print(dict)

# d = {
#     "name": "Alice",
#     42: "age",
#     [1, 2]: "coordinates" --- This will throw error
# }
# print(d)