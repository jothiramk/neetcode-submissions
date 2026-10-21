class TimeMap:

    def __init__(self):
        self.key_value = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.key_value[key].append((timestamp,value))
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.key_value:
            return ""
        
        values_list = self.key_value[key]
        result = ""
        greater_prev = -math.inf
        l = 0
        h = len(values_list)-1
        while l <=h :
            m = (l+h)//2
            prev_timestamp = values_list[m][0]
            if  prev_timestamp == timestamp:
                return values_list[m][1]
            elif prev_timestamp < timestamp:
                result = values_list[m][1]
                l = m + 1             
            else:
                h = m - 1
        return result

        # for value,timestamp_set in values_list:
        #     if timestamp == timestamp_set:
        #         return value
        #     elif timestamp_set < timestamp:
        #         result = value
        #     elif timestamp_set > timestamp:
        #         break
        
        # return result
        
