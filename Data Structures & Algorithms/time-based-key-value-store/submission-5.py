class TimeMap:

    def __init__(self):
        self.timemap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.timemap:
            self.timemap[key].append([value, timestamp])
        else:
            self.timemap[key] = [[value, timestamp]]
    def get(self, key: str, timestamp: int) -> str:
        
        if key not in self.timemap:
            return ""
        res = ""
        l, r = 0, len(self.timemap[key]) - 1
        while  l <= r:
            k = (l+r)//2
            if self.timemap[key][k][1] > timestamp:
                r = k - 1
            else:
                res = self.timemap[key][k][0]
                l = k + 1
        return res


            


        
