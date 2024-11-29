from typing import List


def meetingRooms(rooms:List[List[int]]):
    data = []

    for s,e in rooms:
        data.append((s, 1))
        data.append((e,-1))
    data.sort()

    cur = 0
    ans = 0
    for _, v in data:
        cur += v 
        ans = max(ans, cur)
    return ans
print(meetingRooms([[5,10],[15,20], [0,30]]))