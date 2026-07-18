test_dict = {"Codingal" : 2 , "is" : 2 , "the" : 2, "best" : 1}

print("Original dictionary : " + str(test_dict))

k = 2
results = 0

for key in test_dict:
    if test_dict[key] == k:
        results = results + 1

print("Frequency of k is: " + str(results))