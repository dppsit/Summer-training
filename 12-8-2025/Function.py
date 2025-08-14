'''def unique_elements(lst):
    seen = set()
    result = []
    for item in lst:
        if item not in seen:
            result.append(item)
            seen.add(item)
    return result
'''

# List Rotation
'''
def rotate_list(lst, k):
    if not lst:
        return lst  
    
    k = k % len(lst)
    return lst[-k:] + lst[:-k]

print(rotate_list([1, 2, 3, 4, 5], 2)) 

'''

def longest_word(sentence):
    words = sentence.split() 
    return max(words, key=len) 

print(longest_word("Python is an amazing programming language"))


    