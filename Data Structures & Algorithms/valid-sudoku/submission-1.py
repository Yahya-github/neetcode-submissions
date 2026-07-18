class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        num_cls = {
    "s0": (), "s1": (), "s2": (), "s3": (), "s4": (), "s5": (), "s6": (), "s7": (), "s8": (),
    "c0": 0, "c1": 0, "c2": 0, "c3": 0, "c4": 0, "c5": 0, "c6": 0, "c7": 0, "c8": 0
}
        nums = [num_cls.copy() for _ in range(9)]

        for l in range(9):
            for c in range(9):
                num_obj = board[l][c]
                if not num_obj.isdigit():
                    continue
                if board[l].count(num_obj) > 1:
                    print("Same line !!!")
                    return False
                num_obj = int(num_obj)
                if nums[num_obj-1][f"c{c}"]:
                    print("Same column !!!")
                    print(f"Conflicting number {num_obj} on column {c}")
                    return False
                else:
                    nums[num_obj-1][f"c{c}"] = c
                if nums[num_obj-1][f"s{3*(l//3) + c//3}"]:
                    print(f"Square: {3*(l//3) + c//3}")
                    l0,c0 = nums[num_obj-1][f"s{3*(l//3) + (c//3)}"]
                    print("Same square !!!")
                    print(f"Conflicting number {num_obj} on {l0} - {c0} and {l} - {c}")
                    return False
                else:
                    print(f"Square: {3*(l//3) + c//3}")
                    nums[num_obj-1][f"s{3*(l//3) + (c//3)}"] = (l,c)
        return True