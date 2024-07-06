class Solution:
    def heapify(self, meetings: List[List[int]], i: int, n: int):
        smallest = i
        
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n and meetings[left][0] < meetings[smallest][0]:
            smallest = left

        if right < n and meetings[right][0] < meetings[smallest][0]:
            smallest = right

        if smallest != i:
            meetings[smallest], meetings[i] = meetings[i], meetings[smallest]
            self.heapify(meetings, smallest, n)

    def getMin(self, meetings: List[List[int]]) -> int:
        if len(meetings) == 0:
            return None

        result = meetings[0]

        meetings[0] = meetings[-1]

        meetings.pop()

        self.heapify(meetings, 0, len(meetings))

        return result


    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:

        # n = 3, meetings = [[1,20],[2,10],[3,5],[4,9],[6,8]]
        # rooms = [-1, -1, -1]
        # room_count = [0, 0, 0]
        # curr_hour = 1
        # curr_meeting = [1, 20]

        rooms = n * [-1]
        room_count = n * [0]
            
        for i in range(len(meetings) // 2 - 1, -1, -1):
            self.heapify(meetings, i, len(meetings))
        
        curr_hour = 0
    
        min_ind = 0

        curr_meeting = self.getMin(meetings)
        while not curr_meeting is None:
            # rooms = [10, 10]
            check_room = True
            while curr_meeting != None and curr_meeting[0] <= curr_hour and check_room:
                check_room = False
                for j in range(len(rooms)):
                    if rooms[j] < 0 or rooms[j] <= curr_hour:
                        rooms[j] = curr_hour + (curr_meeting[1] - curr_meeting[0])                        
                        room_count[j] += 1
                        curr_meeting = self.getMin(meetings)
                        check_room = True
                        break

            curr_hour += 1