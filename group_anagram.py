"""
Given an array of strings strs, group the anagrams together. You can return 
the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a 
different word or phrase, typically using all the original letters exactly 
once.

 

Example 1:
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Example 2:
Input: strs = [""]
Output: [[""]]

Example 3:
Input: strs = ["a"]
Output: [["a"]]
"""

from valid_anagram import isAnagram


def groupAnagrams(strs: list[str]) -> list[list[str]]:
    anagram_groups = []
    while strs:
        group = [strs.pop(0)]
        i = len(strs) - 1
        while i >= 0:
            if isAnagram(group[0], strs[i]):
                group.append(strs.pop(i))
            i -= 1
        anagram_groups.append(group)
    return anagram_groups


test1 = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(groupAnagrams(test1))
assert groupAnagrams(test1) == [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]

test2 = [""]
assert groupAnagrams(test2) == [[""]]

test3 = ["a"]
assert groupAnagrams(test3) == [["a"]]
