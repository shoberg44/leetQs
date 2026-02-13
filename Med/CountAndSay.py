class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        # base case
        if (n == 1):
            return '1'
        # recursive case
        else:
            prevRLE = self.countAndSay(n - 1)
            ret = ''

            currentRunCount = 1 # the number of similar chars in this run
            currentRunChar = prevRLE[0] # the char being tracked in the run
            
            # construct the RLE
            for i in range(0, len(prevRLE)):
                # RLE is constructed
                if i == len(prevRLE) - 1:
                    ret = ret + str(currentRunCount) + currentRunChar
                    return ret
                # current run is over
                elif currentRunChar != prevRLE[i + 1]:
                    # append run results
                    ret = ret + str(currentRunCount) + currentRunChar
                    # reset run for next
                    currentRunChar = prevRLE[i+1]
                    currentRunCount = 1
                else:
                    currentRunCount += 1



main = Solution()
for i in range (1,30):
    print(main.countAndSay(i))