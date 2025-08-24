from collections import defaultdict

def string_group_anagrams(strs):
    groups = defaultdict(list)          
    for s in strs:
        key = ''.join(sorted(s))        
        groups[key].append(s)           
    return list(groups.values())      



strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(string_group_anagrams(strs))

