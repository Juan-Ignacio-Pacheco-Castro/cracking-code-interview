to_be_checked = "abcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()"

def is_unique(to_be_checked):
    hashmap = [0] * 255
    if(to_be_checked is None):
        return False
    for i in to_be_checked:
        hashmap[ord(i)] += 1
        if(hashmap[ord(i)] == 2):
            print(i)
            return False
    return True

if (is_unique(to_be_checked)):
    print("All are unique")
else:
    print("There are repetitions")