# 動かないコード

class Solution:
    def isValid(self, s: str) -> bool:
        while s:
            if "(" in s:
                s.pop("(")
                s.pop(")")
            elif "[" in s:
                s.pop("[")
                s.pop("]")
            elif "{" in s:
                s.pop("{")
                s.pop("}")
        
        return True

class Solution:
    def isValid(self, s: str) -> bool:
        while s:
            if "()" in s:
                s = s.replace("()", "")
            elif "[]" in s:
                s = s.replace("[]", "")
            elif "{}" in s:
                s = s.replace("{}", "")
        
        if s: return True
        else: return False
