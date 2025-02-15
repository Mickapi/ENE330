from typing import Optional

# Define the ListNode class
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Define the Solution class
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummyHead = ListNode(0)
        tail = dummyHead
        carry = 0

        while l1 is not None or l2 is not None or carry != 0:
            digit1 = l1.val if l1 is not None else 0
            digit2 = l2.val if l2 is not None else 0

            sum_value = digit1 + digit2 + carry
            digit = sum_value % 10
            carry = sum_value // 10

            newNode = ListNode(digit)
            tail.next = newNode
            tail = tail.next

            l1 = l1.next if l1 is not None else None
            l2 = l2.next if l2 is not None else None

        return dummyHead.next  # Return head of result list


# Helper function to convert a list to a ListNode
def create_linked_list(numbers):
    dummy = ListNode()
    current = dummy
    for num in numbers:
        current.next = ListNode(num)
        current = current.next
    return dummy.next  # Return head of linked list

# Helper function to print a ListNode
def print_linked_list(node):
    values = []
    while node:
        values.append(str(node.val))
        node = node.next
    print(" -> ".join(values))

# Test Case 1: 342 + 465 = 807
l1 = create_linked_list([2, 4, 3])  # Represents 342
l2 = create_linked_list([5, 6, 4])  # Represents 465

solution = Solution()
result = solution.addTwoNumbers(l1, l2)

# Output the result
print("Output Linked List:")
print_linked_list(result)  # Expected Output: 7 -> 0 -> 8
