class Solution(object):
    def helperFunc(self, formula, i, n):
        # print(i, n)
        helper_dict = defaultdict(int)
        num = ""
        elem = ""
        while i < n:
            # print(formula[i], num, helper_dict)
            if formula[i].isdigit():
                # print("Numeric Case:", formula[i], num, elem)
                num += formula[i]
            elif formula[i].isupper():
                # print("New Element Case:", formula[i], num, helper_dict, elem)
                if elem != "":
                    helper_dict[elem] += 1 if num == "" else int(num)
                num = ""
                elem = formula[i]
            elif formula[i].islower():
                # print("Old Element Case:", formula[i], num, helper_dict, elem)
                elem += formula[i]
            elif formula[i] == "(":
                if elem != "":
                    helper_dict[elem] += 1 if num == "" else int(num)
                elem = ""
                # print("Recursive Call Start:", num, helper_dict, elem)
                (new_dict, i) = self.helperFunc(formula, i + 1, n)
                # print("Recursive Call Result:", num, new_dict, elem, i)
                for key in new_dict:
                    helper_dict[key] += new_dict[key]
            else:
                if elem != "":
                    helper_dict[elem] += 1 if num == "" else int(num)
                num = ""
                i += 1
                while i < n and formula[i].isdigit():
                    num += formula[i]
                    i += 1
                # print("Recursive Call Number of Times1:", num, helper_dict, elem)
                for key in helper_dict:
                    helper_dict[key] *= 1 if num == "" else int(num)
                # print("Recursive Call Number of Times2:", num, helper_dict, elem)
                num = ""
                return (helper_dict, i-1)
            i += 1
        # print("End of String", i, num, helper_dict, elem)
        if elem != "":
            helper_dict[elem] += 1 if num == "" else int(num)
        return (helper_dict, i)

    def countOfAtoms(self, formula):
        """
        :type formula: str
        :rtype: str
        """
        n = len(formula)
        (result_dict, _) = self.helperFunc(formula, 0, n)
        # print(result_dict, _)
        sorted_keys = sorted(result_dict.keys())
        s = ""
        for key in sorted_keys:
            s += key
            if result_dict[key] > 1:
                s += str(result_dict[key])
        return s