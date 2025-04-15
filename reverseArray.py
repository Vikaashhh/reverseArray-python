class Solution:
    def reverseArray(self, arr):
        # Do pointer use kar rahe hain: ek start se (left), ek end se (right)
        left, right = 0, len(arr) - 1  

        # Jab tak left pointer right se chhota hai tab tak loop chalega
        while left < right:
            # left aur right ke elements ko swap karo
            arr[left], arr[right] = arr[right], arr[left]
            
            # left ko aage badhao aur right ko peeche le jao
            left += 1
            right -= 1

# Driver Code
if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]  # Sample input array
    print("Original Array:", arr)

    sol = Solution()
    sol.reverseArray(arr)  # Function call to reverse array

    print("Reversed Array:", arr)  # Output reversed array
