to_be_checked = "abc"

def is_unique(to_be_checked):
    hashmap = [0] * 255
    if(to_be_checked is None):
        return False
    for i in to_be_checked:
        hashmap[ord(i)] += 1
        if(hashmap[ord(i)] == 2):
            return False
    return True

def is_unique_without_data_structure(to_be_checked):
    sorted_string = sorted(to_be_checked)
    compare = None
    for i in sorted_string:
        if compare == i:
            return False
        compare = i
    return True

if (is_unique(to_be_checked)):
    print("All are unique")
else:
    print("There are repetitions")

if (is_unique_without_data_structure(to_be_checked)):
    print("Without Data Structure: All are unique")
else:
    print("Without Data Structure: There are repetitions")