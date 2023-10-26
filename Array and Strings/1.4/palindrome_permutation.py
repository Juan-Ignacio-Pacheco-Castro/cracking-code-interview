input = "Tact Cateee"

def palindrome_permutation(sentence):
    result_array = [0]*26 
    for i in sentence:
        if i != " ":
            result_array[ord(i.lower()) - ord('a')] += 1
    only_one_odd = False
    for i in result_array:
        if i % 2 == 1:
            if (only_one_odd):
                return False
            only_one_odd = True
    return True

if palindrome_permutation(input):
    print("Its a palindrome permutation")
else:
    print("Its NOT a palindrome permutation")