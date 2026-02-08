# https://leetcode.com/problems/longest-common-prefix/

from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        # If first string is empty then stop program and return empty string
        if len(strs[0]) == 0:
            return ''

        # Store shortes word length for access while reading a result
        shortest_word_length = len(strs[0])

        # Prepare Trie
        # Feed Trie with the first word
        head = (strs[0][0], {})
        node = head
        for index in range(1, len(strs[0])):
            if strs[0][index] not in node[1]:
                node[1][strs[0][index]] = (strs[0][index], {})
            node = node[1][strs[0][index]]

        # For each next word add to trie
        for word_index in range(1, len(strs)):

            node = head
            word = strs[word_index]

            # If first string is empty then stop program and return empty string
            if len(word) == 0:
                return ''

            # If first letters of next word and head are different return empty string
            if node[0] != word[0]:
                return ''

            shortest_word_length = min(shortest_word_length, len(word))

            for letter_index in range(1, len(word)):
                if word[letter_index] not in node[1]:
                    node[1][word[letter_index]] = (word[letter_index], {})
                node = node[1][word[letter_index]]

        longest_common_prefix = ''
        node = head

        while True:

            longest_common_prefix += node[0]

            if len(node[1]) > 1 or len(node[1]) == 0:
                break

            node = node[1][list(node[1].keys())[0]]

        return longest_common_prefix[:shortest_word_length]
