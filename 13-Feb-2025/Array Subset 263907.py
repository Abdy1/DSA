# Problem: Array Subset - https://practice.geeksforgeeks.org/problems/array-subset-of-another-array2317/1?utm_source=geeksforgeeks&utm_medium=article_practice_tab&utm_campaign=article_practice_tab

from collections import Counter

def is_subset(a, b):
    # Count the frequency of each element in both arrays
    a_count = Counter(a)
    b_count = Counter(b)
    
    # Check if for every element in b[], it appears in a[] with at least the same frequency
    for key in b_count:
        if b_count[key] > a_count.get(key, 0):
            return False
    
    return True
