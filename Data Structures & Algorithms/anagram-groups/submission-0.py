class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = []
        indices = {}
        for s in strs:
            sorted_s = ''.join(sorted(s))
            if sorted_s in indices:
                groups[indices[sorted_s]].append(s)
            else:
                indices[sorted_s] = len(groups)
                groups.append([s])
        return groups