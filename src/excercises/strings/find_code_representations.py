class Solution:
    """
    Considering a code where a=1, b=2... z=26
    Given a string with numberic values, print the possible representations of those numbers and return the amount of combinations
    """
    def _find_code_repr(self, s, num_dict, i=0):
        s_len = len(s)
        if i >= s_len:
            return ['']

        combinations = []
        for length in range(s_len - i):
            num = int(s[i:i + length + 1])
            if num in num_dict:
                c = num_dict[num]
                rest = self._find_code_repr(s, num_dict, i + length + 1)
                for suffix in rest:
                    combinations.append(c + suffix)
        return combinations

    def get_dict(self):
        num_dict = {}
        base = ord('a')
        for i in range(26):
            num_dict[i + 1] = chr(base + i)
        return num_dict

    def print_code_repr(self, s):
        num_dict = self.get_dict()
        combinations = self._find_code_repr(s, num_dict)
        print("\n".join(combinations))
        return len(combinations)
