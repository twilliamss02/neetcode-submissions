class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_strs = [sorted(x) for x in strs]

        output_dict = {
            #sorted : [diff anagrams]
        }
        output_list = []
        
        for i, word in enumerate(strs):

            temp = "".join(sorted(word))
            if output_dict.get(temp):
                output_dict[temp].append(word)
            elif not output_dict.get(temp):
                output_dict[temp] = [word]

        
        return list(output_dict.values())