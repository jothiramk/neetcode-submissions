class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        org_color = image[sr][sc]
        if org_color == color:
            return image

        def dfs (image, sr, sc):
            rows = len(image)
            cols = len(image[0])
            

            if sr < 0 or sc < 0 or sr == rows or sc == cols or image[sr][sc]!= org_color :
                return

            
            image[sr][sc] = color
            
            
            dfs(image, sr+1, sc)
            dfs(image, sr-1, sc)
            dfs(image, sr, sc+1)
            dfs(image, sr, sc-1)


        dfs(image, sr, sc)
        return image