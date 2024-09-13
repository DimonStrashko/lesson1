# test = [12, 3, 4, 10]
# test =[1]
# test = []
test = [12, 3, 4, 10, 8]

if len(test) > 1:
    element = test.pop()
    test.insert(0, element)
print(test)
