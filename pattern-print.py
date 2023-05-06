#leetcode solution
#*    
#**   
#* *  
#*  * 
#*****
#
#*
#**
#***
#****
#*****
#    *   
#   * *  
#  *   * 
#********

class Solution:
    def rightTriangle(self):
        for row in range(5):
            for col in range(5):
                if col == 0 or row == 4 or col-row == 0:
                    print ("*", end="")
                else:
                    print (' ', end='')
            print()
            
    def hollowRightTriangle(self):
        for row in range(6):
            for star in range(row):
                    print ("*",end="")
            print()
            
    def hollowTriangle(self):
        for row in range(4):
            for col in range(8):
                if col+row == 4 or col-row == 4 or row == 3:
                    print ("*",end="")
                else:
                    print (' ', end='')
            print()
    
x = Solution()
x.rightTriangle()
x.hollowRightTriangle()
x.hollowTriangle()
