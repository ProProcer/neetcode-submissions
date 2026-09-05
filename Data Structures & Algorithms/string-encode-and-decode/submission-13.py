class Solution:

    def encode(self, strs: List[str]) -> str:
        sizes = [f'{len(s)},' for s in strs]
        
        return ''.join(sizes)  + '#' + ''.join(strs)

    def decode(self, s: str) -> List[str]:
        sizes = []
        i = 0
        print(s)
        sz = ''
        while s[i] != '#':
            if s[i] == ',':
                sizes.append(int(sz))
                sz =''
            else:
                sz += s[i]
            i += 1
        
        i += 1
        print(sizes)
        result = []
        for sz in sizes:
            result.append(s[i: i + sz])
            i = i + sz
        return result