# most frequently occurring item in an Array

def most_frequent(given_list):
    max_count = 0
    max_item = None
    count = {}
    for i in given_list:
        if i not in count:
            count[i] = 1
        else:
            count[i] += 1
        if count[i] > max_count:
            max_count = count[i]
            max_item = i
    return max_item

list1 = [2, 2, 5, 77, 85, 4, 3, 2, 77, 9, 1, 13, 55, 2, 77, 8, 4]
print most_frequent(list1)
