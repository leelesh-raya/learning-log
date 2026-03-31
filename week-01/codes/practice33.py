


spam='abcabcdabbc'



def longestUniqueSubstring(s):
    char_set = set()
    left = 0
    max_length = 0

    for right in range(len(s)):
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1

        char_set.add(s[right])
        max_length = max(max_length, right - left + 1)

    return max_length
print(longestUniqueSubstring(spam))



#Corrections: My program using if statements didnt work when the substring comes at the end of 
# input string. Understood what a sliding window is and why a while loop and set() is used. 