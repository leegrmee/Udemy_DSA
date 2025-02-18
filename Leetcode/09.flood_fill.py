"""
You are given an image represented by an m x n grid of integers image, where image[i][j] represents the pixel value of the image. You are also given three integers sr, sc, and color. Your task is to perform a flood fill on the image starting from the pixel image[sr][sc].

To perform a flood fill:

Begin with the starting pixel and change its color to color.
Perform the same process for each pixel that is directly adjacent (pixels that share a side with the original pixel, either horizontally or vertically) and shares the same color as the starting pixel.
Keep repeating this process by checking neighboring pixels of the updated pixels and modifying their color if it matches the original color of the starting pixel.
The process stops when there are no more adjacent pixels of the original color to update.
Return the modified image after performing the flood fill.
"""


class Solution(object):
    def floodFill(self, image, sr, sc, color):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type color: int
        :rtype: List[List[int]]
        """
        if image[sr][sc] == color:
            return image

        # Get the original color and dimensions
        original_color = image[sr][sc]
        rows = len(image)
        cols = len(image[0])

        def dfs(r, c):
            # Check if current position is valid and has the original color
            if (
                r < 0
                or r >= rows
                or c < 0
                or c >= cols
                or image[r][c] != original_color
            ):
                return

            image[r][c] = color

            # Recursively fill all 4 adjacent pixels
            dfs(r + 1, c)  # down
            dfs(r - 1, c)  # up
            dfs(r, c + 1)  # right
            dfs(r, c - 1)  # left

        # Start DFS from the given starting position
        dfs(sr, sc)
        return image
