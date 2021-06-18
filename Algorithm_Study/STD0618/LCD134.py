from typing import List

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        diff = [ ]
        for i in range(len(gas)) :
            diff.append(gas[i] - cost[i])
        if sum(diff) < 0 :
            return -1
        for i in range(len(gas)) :
            if diff[i] < 0 :
                continue
            cnt = 0 
            tmp = i
            gas_state = diff[tmp]
            flag = True
            while cnt < len(gas) :
                if gas_state < 0 :
                    flag = False
                    break
                cnt += 1
                tmp += 1
                if tmp >= len(gas) :
                    tmp = 0
                gas_state += diff[tmp]
            if flag :
                return i


solution = Solution()
gas = [1,2,3,4,5]
cost = [3,4,5,1,2]
print(solution.canCompleteCircuit(gas,cost))
gas = [2,3,4]
cost = [3,4,3]
print(solution.canCompleteCircuit(gas,cost))
