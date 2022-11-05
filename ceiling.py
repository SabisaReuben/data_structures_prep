# Find the ceiling of number n in a sorted  array A. The ceiling of a number n is
# minimum number in the array that is greater or equal to n. 
# For example:
#    A = [2, 6, 9, 12, 17, 23] and n = 7, then the ceiling(n) should return 9

class Ceiling:
    def __init__(self):
        pass

    def ceiling(self, A, n):
        """
        The method apply binary search to find the ceiling 
        :A: Sorted array of integers
        :n: integer value
        :return: The ceiling of integer n
        """

        length  = len(A)
        if n > A[length -1]:
            raise ValueError(" value {} is greater than the max element".format(n))
        index = self.binary_search(A, n, 0, length-1)
        if index == -1:
            return 0
        else:
            return A[index]

    def binary_search(self, A, n, start_index, end_index):
        if start_index > end_index:
            return -1
        mid = start_index + (end_index - start_index)//2
        if A[mid] == n:
            return mid
        if A[mid] < n:
            if A[mid+1] > n:
                return mid+1
            return self.binary_search(A, n, mid+1, end_index)
        return self.binary_search(A, n, start_index, mid-1)



if __name__ == "__main__":
    ceil = Ceiling()

    print(ceil.ceiling([2,4,5,7,8,34,56],35))



