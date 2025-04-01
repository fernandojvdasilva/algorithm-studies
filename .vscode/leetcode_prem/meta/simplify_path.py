'''
71. Simplify Path
Solved
Medium
Topics
Companies
You are given an absolute path for a Unix-style file system, which always begins with a slash '/'. Your task is to transform this absolute path into its simplified canonical path.

The rules of a Unix-style file system are as follows:

A single period '.' represents the current directory.
A double period '..' represents the previous/parent directory.
Multiple consecutive slashes such as '//' and '///' are treated as a single slash '/'.
Any sequence of periods that does not match the rules above should be treated as a valid directory or file name. For example, '...' and '....' are valid directory or file names.
The simplified canonical path should follow these rules:

The path must start with a single slash '/'.
Directories within the path must be separated by exactly one slash '/'.
The path must not end with a slash '/', unless it is the root directory.
The path must not have any single or double periods ('.' and '..') used to denote current or parent directories.
Return the simplified canonical path.

 

Example 1:

Input: path = "/home/"

Output: "/home"

Explanation:

The trailing slash should be removed.

Example 2:

Input: path = "/home//foo/"

Output: "/home/foo"

Explanation:

Multiple consecutive slashes are replaced by a single one.

Example 3:

Input: path = "/home/user/Documents/../Pictures"

Output: "/home/user/Pictures"

Explanation:

A double period ".." refers to the directory up a level (the parent directory).

Example 4:

Input: path = "/../"

Output: "/"

Explanation:

Going one level up from the root directory is not possible.

Example 5:

Input: path = "/.../a/../b/c/../d/./"

Output: "/.../b/d"

Explanation:

"..." is a valid name for a directory in this problem.

 

Constraints:

1 <= path.length <= 3000
path consists of English letters, digits, period '.', slash '/' or '_'.
path is a valid absolute Unix path.
'''

class PathNode:

        def __init__(self, text: str, lastNode):
            self.text = text
            self.next = None
            self.last = lastNode


class Solution:

    

    def simplifyPath(self, path: str) -> str:
        '''

        /home/user/Documents/../Pictures


        /
            home
                user
                    Documents
                            ..


        '''

        curr_word = ''
        curr_node = PathNode(None, None)
        first_node = curr_node

        for i in range(len(path)):
            if path[i] == '/':
                if len(curr_word) > 0:
                    if curr_word == '..':
                        if curr_node.last != None:
                            curr_node = curr_node.last
                            if curr_node != None:
                                curr_node.text = None
                    elif curr_word != '.':
                        curr_node.text = curr_word
                        curr_node.next = PathNode(None, curr_node)
                        curr_node = curr_node.next

                    curr_word = ''
            else:
                curr_word += path[i]

        if len(curr_word) > 0:
            if curr_word == '..':
                if curr_node != None:
                    curr_node = curr_node.last
                    if curr_node != None:
                        curr_node.next = None
                        curr_node.text = None
            elif curr_word != '.':
                if curr_node != None:
                    curr_node.text = curr_word


        curr_node = first_node
        res = ''
        while curr_node != None:
            if curr_node.text != None:
                res += '/%s' % curr_node.text

            curr_node = curr_node.next

        if len(res) == 0:
            res = '/'

        return res
