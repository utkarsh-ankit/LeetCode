class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        k=image[sr][sc]
        col=len(image[0])
        row=len(image)

        if k==color:
            return image
        
        def f(im,a,b,c):
            if a<0 or b<0 or a>=row or b>=col:
                return
            if im[a][b]!=k:
                return
            im[a][b]=c

            f(im,a-1,b,c)
            f(im,a,b-1,c)
            f(im,a+1,b,c)
            f(im,a,b+1,c)

        f(image, sr, sc, color)
        return image
            
        

        