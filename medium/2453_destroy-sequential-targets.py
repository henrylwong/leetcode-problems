class Solution(object):
    def destroyTargets(self, nums, space):
        """
        :type nums: List[int]
        :type space: int
        :rtype: int
        """

        modulos = dict()
        min_val, max_targets = None, -1

        for i in nums:
            modulo = i % space

            if modulo not in modulos:
                modulos[modulo] = list()
            modulos[modulo].append(i)

        for modulo, targets in modulos.items():
            num_targets = len(targets)
            if num_targets > max_targets:
                max_targets = num_targets
                min_val = min(targets)
            elif num_targets == max_targets:
                min_val = min(min_val, min(targets))
            
        return min_val