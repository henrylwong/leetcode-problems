class Solution:
  def maxArea(self, height: list[int]) -> int:
    '''
    Solve via 2 pointers. Given two heights, keep the higher of the two heights.
    '''
    i, j = 0, len(height) - 1

    max_area = -1
    while j > i:
      width = j - i
      if height[i] > height[j]:
        min_height = height[j]
        j -= 1
      else:
        min_height = height[i]
        i += 1
      max_area = max(max_area, width * min_height)
      
    return max_area