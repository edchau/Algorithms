"""
Given an array of events where events[i] = [startDayi, endDayi]. 
Every event i starts at startDayi and ends at endDayi.

You can attend an event i at any day d where startTimei <= d <= 
endTimei. Notice that you can only attend one event at any time d.

Return the maximum number of events you can attend.
"""
import heapq as hq
class Solution(object):
    def maxEvents(self, events):
        """
        :type events: List[List[int]]
        :rtype: int
        """
        pq = []
        
        events.sort(reverse=1)
        count = 0
        day = 0
        
        # each day, add the event that starts soonest to queue
        while len(events) > 0 or len(pq) > 0:
            if len(pq) == 0:
                day = events[-1][0]
        
            while len(events) > 0 and events[-1][0] <= day:
                hq.heappush(pq, events.pop()[1])
            
            # pop off first event that we can attend
            hq.heappop(pq)
            count += 1
            day += 1
            
            # if the queue has end dates less than the current date,
            # then we pop them off
            while len(pq) > 0 and pq[0] < day:
                hq.heappop(pq)
        
        return count