class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        answers = {}

        for string in strs:
            key = "".join(sorted(string))

            if key not in answers:
                answers[key] = []
            answers[key].append(string)

        return list(answers.values())