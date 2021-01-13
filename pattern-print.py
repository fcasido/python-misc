class Solution:
    def hollowTriangle(self):
        for row in range(5):
            for col in range(5):
                if col == 0 or row == 4 or col-row == 0:
                    print ("*", end="")
                else:
                    print (' ', end='')
            print()
    def Triangle(self):
        for row in range(6):
            for star in range(row):
                    print ("*",end="")
            print()
    
Solution().hollowTriangle()
Solution().Triangle()
