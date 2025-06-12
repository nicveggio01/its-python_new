
def merge_intervals(intervals:list[list[int]])-> list[list[int]]:

    new_intervals=[]

    if not intervals:
        return []
        
    elif len(intervals)==1:
        return intervals
    else:
        intervals= sorted(intervals, key=lambda x:x[0])
        for intervallo in intervals:

            end= intervallo[1]
            start= intervallo[0]

            if not new_intervals:
                new_intervals.append(intervallo)
            else:
                last_end = new_intervals[-1][1]
                if start <= last_end:
                    new_intervals[-1][1] = max(last_end, end)
                else:
                    new_intervals.append(intervallo)
    
        return new_intervals

intervals = [[1, 3], [2, 6], [8, 10], [7, 18]] 
print(merge_intervals(intervals))



       
       


        
    




     