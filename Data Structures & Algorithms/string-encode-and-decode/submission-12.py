class Solution:

    def encode(self, strs: List[str]) -> str:

        returning_string = str()
        if strs == []:
            return returning_string
        elif strs == [""]:
            return ";"

        for i,unencoded_string in enumerate(strs):
            bytes_list = list(bytes(unencoded_string, "ascii"))
            returning_string += ";".join([str(int(x)+1) for x in bytes_list])
            if i+1 == len(strs):
                return returning_string
            returning_string += " "





    def decode(self, s: str) -> List[str]:
        returning_list = []

        if s == "":
            return []
        elif s == ";":
            return [""]

        stripped_string = s.split(" ")
        stripped_string = [x.split(";") for x in stripped_string]
        for encoded_word_list in stripped_string:
            encoded_word_list = [x for x in encoded_word_list if x != ""]
            returning_list.append("".join([chr(int(x)-1) for x in encoded_word_list]))
        
        return returning_list
            
            
        
