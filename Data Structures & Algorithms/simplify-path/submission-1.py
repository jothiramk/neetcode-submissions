class Solution:
    def simplifyPath(self, path: str) -> str:
        result = ""
        paths = path.split("/")
        
        
        stack = []
        for path in paths:
            # print(path)
            if path == ".." and stack:
                stack.pop()
            elif path == "" or path == ".." or path == ".":
                continue
            else:
                stack.append(path)
        
        
        result = "/"+"/".join(stack)
        return result

