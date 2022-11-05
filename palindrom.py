# palindrom  string read the same when read forward or backwards

# example: Madam, Mum

# Given thet n is the length of the palindrom string and k the number of unique 
# elements,  create a function that returns  a palindrom string

# if n =10, the maximum number of unique elements can be calculated as
#     if n <= 2 then the max unique element is 1
#     if  n is even, and the two middle elements must be same hence max = (n-2)/2 +1 
#     if n is odd, the max number of elements  is (n +1)/2

import string
import sys

class Palindrom:
    def __init(self):
        pass



    def create_palindrom(self, k, n):
        """
        :param k: The number of umique elements
        :param n: the length of the parindrom string
        :return: a parindrom string
        """
        start, rem_char_count = "", 0
        # let m be max unique  elements a palindrom string of length n can have
        # for example n = 2, aa, bb, dd can make a palindrom
        # a single letter is considered a palindrom
        #  The number of required unique letter cannot exceed the max  unique
        #  letters in a palindrom. 

        rem_char_count, m = self.unique_count(n)
        print(rem_char_count, m)

        if k > m:
            return None
        
        alp = string.ascii_lowercase

        # start by initializing the middle letter(s) of the palindrom string 
        if n % 2 ==0:
            start = alp[0] + alp[0]  # even length has 2 same letters in middle
        else:
            start = alp[0]

        unique_chars =  alp[1:k]
        # You can also include the middle element for selection 
        unique_chars += alp[0]

        count = 0
        while rem_char_count > 0:
            cnext = unique_chars[count % k]
            start = cnext + start + cnext
            count += 1
            rem_char_count -= 2
        return start
    

    def unique_count(self, n):
        if n <= 2:
            m = 1
        elif  n > 2 and n % 2 == 0:
            m = (n - 2) // 2 + 1
            rem_char_count = n - 2
        else:
            m = (n + 1) // 2
            rem_char_count = n -1

        return (rem_char_count, m)


if __name__ == "__main__":
    uniq_elements, length  = int(sys.argv[1]), int(sys.argv[2])
    p = Palindrom()
    print(p.create_palindrom(uniq_elements, length))






