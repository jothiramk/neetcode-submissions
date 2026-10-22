class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        counter_judge = defaultdict(int)
        counter_nonjudge = defaultdict(int)
        judge = -1
        for trust_pairs in trust:
            #people who trust the judge
            counter_nonjudge[trust_pairs[0]]+=1
            #candidates for the judge
            counter_judge[trust_pairs[1]]+=1
        
        # print(counter_nonjudge)
        # print(counter_judge)
        for key,value in counter_judge.items():
            # print(f'key is {key} and {value}')
            if value == n - 1 and key not in counter_nonjudge:
                judge = key   

        return judge
