from typing import List
from collections import deque
class Solution:
    def countMentions(self, numberOfUsers: int, events: List[List[str]]) -> List[int]:
        events = sorted(events, key=lambda x: (int(x[1]), 0 if x[0] == "OFFLINE" else 1))
        ans = [0] * numberOfUsers
        online = set()
        for i in range(numberOfUsers):
            online.add(i)
        waiting = deque()
        for [event_type, timestamp, quantifier] in events:
            timestamp = int(timestamp)
            # handle update online/offline ppl before handling updates
            if waiting:
                while waiting:
                    id, back_timestamp = waiting[0]
                    if back_timestamp <= timestamp:
                        online.add(id)
                        waiting.popleft()
                    else:
                        break
            
            if event_type == "MESSAGE":
                if quantifier == "ALL":
                    for i in range(numberOfUsers):
                        ans[i] += 1
                elif quantifier == "HERE":
                    # for each online person with id, do ans[id] += 1
                    for i in online:
                        ans[i] += 1
                else:
                    ids_mentioned = [int(w[2:]) for w in quantifier.split()]
                    for i in ids_mentioned:
                        ans[i] += 1
            else:
                quantifier = int(quantifier)
                online.remove(quantifier)
                waiting.append((quantifier, timestamp + 60))

        return ans
sol = Solution()
numberOfUsers = 2
events = [["MESSAGE","10","id1 id0"],["OFFLINE","11","0"],["MESSAGE","71","HERE"]]
print(sol.countMentions(numberOfUsers, events))
# main problem: how to hold and update data structure with all online users
# just hold a list of indices [1,3,5] meaning 1,3,5 are online, if numberOfUsers = 6 then 0,2,4 are offline
# but then the OFFLINE event would cause issues
# also need to keep track of those that become online in 60 time units
# can have list of those that are waiting to become online again and then just proceed an index through the list from left to right 
# indicating the current one that needs to be online soon-ish