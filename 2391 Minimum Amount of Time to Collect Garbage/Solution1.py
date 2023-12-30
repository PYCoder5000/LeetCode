class Solution:
    def cal(self, typer, garbage, travel):
        count = 0
        for house in garbage:
            for g in house:
                if g == typer:
                    count += 1
        time = 0
        last_house = 0
        for i in range(len(garbage)-1, -1, -1):
            if typer in garbage[i]:
                last_house = i
                break
        time += sum(travel[:i])
        return time + count
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        return self.cal("M", garbage, travel) + self.cal("P", garbage, travel) + self.cal("G", garbage, travel)
