class Solution:

    def encode(self, strs: List[str]) -> str:
        sizes = [str(len(s)) for s in strs]
        
        return ','.join(sizes) + '#&^' + ''.join(strs)

    def decode(self, s: str) -> List[str]:
        sizes, strs = s.split('#&^')
        result = []
        i = 0
        if not sizes:
            return result
        for s in sizes.split(','):
            result.append(strs[i : i + int(s)])
            i += int(s)
        return result