def trap(height):
    left, right = 0, len(height) - 1
    leftMax = rightMax = 0
    water = 0
    while left < right:
        if height[left] < height[right]:
            leftMax = max(leftMax, height[left])
            water += leftMax - height[left]
            left += 1
        else:
            rightMax = max(rightMax, height[right])
            water += rightMax - height[right]
            right -= 1
    return water
def main():
        height = [0,1,0,2,1,0,1,3,2,1,2,1]
        print(trap(height))
if __name__ == '__main__':
    main()