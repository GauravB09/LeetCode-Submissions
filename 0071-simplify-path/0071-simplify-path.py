class Solution:
    def simplifyPath(self, path: str) -> str:
        s = []
        path_arr = path.split('/')
        length = 0
        for i in path_arr:
            if i == '.' or i == '':
                continue
            elif i == '..':
                if length == 0:
                    continue
                else:
                    s.pop()
                    length -= 1
            else:
                s.append(i)
                length += 1
        return '/' + '/'.join(s)