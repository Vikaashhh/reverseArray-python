# 🚀 Day-3 DSA Challenge – Reverse Array

This repository contains the solution for the **"Reverse Array"** problem, implemented using the efficient **two-pointer approach** in Python.

---

## 🧠 Problem Statement

Given an array, reverse its elements in-place so that the first element becomes the last, the second becomes second last, and so on.

### ✅ Example:

**Input:**
[1, 2, 3, 4, 5]

**Output:**
[5, 4, 3, 2, 1]

---

## 🔍 Approach

We utilize the **two-pointer technique**:

- One pointer starts from the beginning (`left`) and the other from the end (`right`).
- Swap the elements at `left` and `right`.
- Increment `left` and decrement `right` after each swap.
- Stop the loop once `left >= right`.

This technique allows us to reverse the array **in O(n) time and O(1) space**.

---

## 🧾 Code Explanation

```python
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

```
## Output
Original Array: [1, 2, 3, 4, 5]

Reversed Array: [5, 4, 3, 2, 1]

## 📦 How to Run:
1. Clone the repository:
git clone https://github.com/your-username/day3-reverse-array.git

cd day3-reverse-array

2. Run the Python script: python reverseArray.py

## 📌 Tags
#python #dsa #array #reverse-array #twopointer #100daysofcode #leetcode #beginnerfriendly

## 🙌 Author
Vikash Joshi

Front-End Developer | UI/UX Enthusiast | DSA Explorer
- LinkedIn:- https://www.linkedin.com/in/itaintvi/

## ⭐️ Let's Grow Together
If you found this solution helpful, kindly ⭐️ the repository and share it with others. 
Let’s learn and grow together! 💡
