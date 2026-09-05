class Solution:

    def encode(self, strs: List[str]) -> str:
        if strs == []:
            return '^%(*Y)'
        if strs == ['']:
            return '$@!$%'
        return '*&^%'.join(strs)
    def decode(self, s: str) -> List[str]:
        if s == '^%(*Y)':
            return []
        elif s == '$@!$%':
            return ['']
        return s.split('*&^%')
