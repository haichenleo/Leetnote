class NextGreatElement:
    def nextGreaterElement(self, nums1, nums2):
        next_great_pairs = dict()
        stack = list()
        res = []

        for n in nums2:
            while stack and n > stack[-1]:
                next_great_pairs[stack.pop()] = n
            stack.append(n)
        while stack:
            next_great_pairs[stack.pop()] = -1
        for n in nums1:
            res.append(next_great_pairs[n])
        return res

print(NextGreatElement().nextGreaterElement([1,2],[0,2,1]))