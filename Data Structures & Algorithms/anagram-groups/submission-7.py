class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict_count = {}
        for i in strs:
            count_ltrs = tuple(sorted(list(Counter(i).items())))
            if count_ltrs in dict_count:
                dict_count[count_ltrs].append(i)
            else:
                dict_count[count_ltrs] = [i]
        
        print(dict_count)
        return [j for i,j in dict_count.items()]