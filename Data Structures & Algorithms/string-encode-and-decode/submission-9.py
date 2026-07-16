class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs: return "None"
        encoded_string = "hehehehexd".join(strs)
        return encoded_string

    def decode(self, s: str) -> List[str]:
        if s == "None": return []
        return s.split("hehehehexd")

