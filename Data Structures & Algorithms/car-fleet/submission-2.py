class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        car = [(pos, speed) for pos, speed in zip(position, speed)]
        car.sort()
        time = [(target-pos)/speed for pos, speed in car]
        ans = []
        print(time)

        while time:
            if ans and ans[-1] - time[-1]>-1e-6:
                time.pop()
            elif time:
                ans.append(time[-1])
                time.pop()
        print(ans)

        return len(ans)