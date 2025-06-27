# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None

# class LinkedList:
#     def __init__(self):
#         self.head = None 
    
#     def append(self, data):
#         new_node = Node(data)
#         if not self.head:
#             self.head = new_node
#             return 
#         curr = self.head
#         while curr.next:
#             curr = curr.next
#         curr.next = new_node

#     def reverse(self):
#         prev = None
#         curr = self.head
#         while curr:
#             nxt = curr.next
#             curr.next = prev
#             prev = curr
#             curr = nxt
#         return prev

#     def print_list(self):
#         curr = self.head
#         while curr:
#             print(curr.data, end="->")
#             curr = curr.next
#         print("None")


# arr_list = LinkedList()
# arr_list.append(5)
# arr_list.reverse()
# arr_list.append(6)
# arr_list.reverse()
# arr_list.append(7)
# arr_list.reverse()
# arr_list.append(9)
# arr_list.reverse()
# arr_list.print_list()
# # arr_list.reverse()
# # arr_list.print_list()

# def numDecodings(s: str) -> int:
#         dp = {len(s): 1}
#         for i in range(len(s) - 1, -1, -1):
#             if s[i] == "0":
#                 dp[i] = 0
#             else:
#                 dp[i] = dp[i + 1]

#             if i + 1 < len(s) and (s[i] == "1" or
#                s[i] == "2" and s[i + 1] in "0123456"
#             ):
#                 dp[i] += dp[i + 2]
#         return dp[0]

# print(numDecodings("226"))


# """
# return max product a * b
# [1,2,3,4] 
# - 1 * 2 = 2
# - 1 * 3 = 3
# - 1 * 4 = 4
# - 3 * 4 = 12

# for loop where [i] * [j] = max
# max_prod = curr_prod
# """
# def max_product(arr: list) -> int:
#     max_prod = 1
#     for i in range(len(arr)):
#         for j in range(i + 1, len(arr)):
#             prod = arr[i] * arr[j]
#             max_prod = max(max_prod, prod)
#     return max_prod

# print(max_product([-100, -2, 1,5,4,4]))

# """
# max([1,2,3,4]) = 4
# del 4
# [1,2,3]
# max([1,2,3]) = 3
# 3 * 4 = 12
# """

# def max_prod_op(arr:list) -> int:
#     max_val1 = max(arr)
#     arr.remove(max_val1)
#     max_val2 = max(arr)
#     return max_val1 * max_val2

# print(max_prod_op([-100, -2, 1,5,4,4]))

# def trap(height: list) -> int:
#     if not height:
#         return 0
#     left, right = 0, len(height) - 1
#     left_max, right_max = height[left], height[right]
#     water_count = 0
#     while left < right:
#         if left_max <= right_max:
#             left += 1
#             left_max = max(left_max, height[left])
#             water_count += max(0, left_max - height[left])
#         else:
#             right -= 1
#             right_max = max(right_max, height[right])
#             water_count += max(0, right_max - height[right])
#     return water_count

# print(trap([0,1,0,2,1,0,1,3,2,1,2,1]))


