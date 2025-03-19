'''
Design Add and Search Word Data Structure
Solved 
Design a data structure that supports adding new words and searching for existing words.

Implement the WordDictionary class:

void addWord(word) Adds word to the data structure.
bool search(word) Returns true if there is any string in the data structure that matches word or false otherwise. word may contain dots '.' where dots can be matched with any letter.
Example 1:

Input:
["WordDictionary", "addWord", "day", "addWord", "bay", "addWord", "may", "search", "say", "search", "day", "search", ".ay", "search", "b.."]

Output:
[null, null, null, null, false, true, true, true]

Explanation:
WordDictionary wordDictionary = new WordDictionary();
wordDictionary.addWord("day");
wordDictionary.addWord("bay");
wordDictionary.addWord("may");
wordDictionary.search("say"); // return false
wordDictionary.search("day"); // return true
wordDictionary.search(".ay"); // return true
wordDictionary.search("b.."); // return true
Constraints:

1 <= word.length <= 20
word in addWord consists of lowercase English letters.
word in search consist of '.' or lowercase English letters.


'''

class TrieNode:
    def __init__(self, c: str):
        self.c = c
        self.children = {}
        self.is_word = False

    def __str__(self):
        children_str = ''
        for k in self.children.keys():
            children_str += "'%s': %s, " % (k, self.children[k].c)

        return "c=%s, children={%s}" % (self.c, children_str)


class WordDictionary:

    def __init__(self):
        self.trie_root = TrieNode('.')

    def addWord(self, word: str) -> None:
        curr_node = self.trie_root

        for i in range(len(word)):
            if not word[i] in curr_node.children.keys():
                curr_node.children[word[i]] = TrieNode(word[i])
            
            curr_node = curr_node.children[word[i]]
            
        curr_node.is_word = True

    '''
    def backtrack(self, word: str, curr_index: int, choices: List[TrieNode], solution: List[TrieNode]) -> bool:
        if curr_index > len(word):
            return True

        res = False
        for curr_node in choices:
            if curr_node.c == word[curr_index] or word[curr_index] == '.':
                solution.append(curr_node)
                res = self.backtrack(word, curr_index+1, [c for c in curr_node.children.values()], solution)
                solution.remove(curr_node)
                

        return res
    '''

    def search_dfs(self, node: TrieNode, word: str, index: int) -> bool:
        print('word[%d] = %s' % (index, word[index]))
        print('node: %s' % str(node))

        res = False

        if node.c == word[index] or word[index] == '.':
            if index == len(word)-1:
                if node.is_word: 
                    res = True
                else:
                    res = False

            elif word[index+1] != "." and not word[index+1] in node.children.keys():
                res = False
            
            else:
                for child in node.children.values():
                    res = res or self.search_dfs(child, word, index+1)


        '''
        if node.c == word[index]:
            if index == len(word)-1:
                res = True 
            else:

                if word[index+1] in node.children.keys():
                    res = self.search_dfs(node.children[word[index+1]], word, index+1)
                else:
                    if word[index+1] == '.':
                        for child in node.children.values():
                            res = res or self.search_dfs(child, word, index+1)            
        '''
                

        return res


    def search(self, word: str) -> bool:
        curr_node = self.trie_root


        print("word = %s" % word)

        res = False
        for c in curr_node.children.values():
            res = res or self.search_dfs(c, word, 0)

        print("result = %s" % str(res))

        print("----")

        return res
        
