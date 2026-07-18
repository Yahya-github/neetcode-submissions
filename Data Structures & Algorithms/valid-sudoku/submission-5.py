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
                    return False
                num_obj = int(num_obj)
                if nums[num_obj-1][f"c{c}"]:
                    return False
                else:
                    nums[num_obj-1][f"c{c}"] = 1
                if nums[num_obj-1][f"s{3*(l//3) + c//3}"]:
                    return False
                else:
                    nums[num_obj-1][f"s{3*(l//3) + (c//3)}"] = 1
        return True