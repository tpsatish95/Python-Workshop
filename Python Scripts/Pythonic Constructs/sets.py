# list of participants in events A and B
a = set(["Jake", "John", "Eric"])
b = set(["John", "Jill"])

# To find out which members attended both events
a.intersection(b)  # set(['John'])
b.intersection(a)  # set(['John'])

# To find out which members attended only one of the events
a.symmetric_difference(b)  # set(['Jill', 'Jake', 'Eric'])
b.symmetric_difference(a)  # set(['Jill', 'Jake', 'Eric'])

# To find out which members attended only one event and not the other
a.difference(b)  # set(['Jake', 'Eric'])
b.difference(a)  # set(['Jill'])

# To receive a list of all participants
a.union(b)  # set(['Jill', 'Jake', 'John', 'Eric'])
