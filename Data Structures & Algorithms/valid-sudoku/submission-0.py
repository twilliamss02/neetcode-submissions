class Solution:
    def check(self,bunch_of_numbers : list) -> bool:
        for x in range(10):

            if bunch_of_numbers.count(str(x)) > 1:
                print(bunch_of_numbers)
                return False
        return True
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        location_dict = {
            (1,1):1,
            (1,2):4,
            (1,3):7,
            (2,1):2,
            (2,2):5,
            (2,3):8,
            (3,1):3,
            (3,2):6,
            (3,3):9
        }
        thr_by_thr = [
            [],
            [],
            [],
            [],
            [],
            [],
            [],
            [],
            [],
        ]
        columns = [
            [],
            [],
            [],
            [],
            [],
            [],
            [],
            [],
            [],
        ]
        for row_num, row_elements in enumerate(board):
            if not self.check(row_elements):
                return False
            for col_num, cell_value in enumerate(row_elements):
                columns[col_num].append(cell_value)
                coordinates = (math.ceil((col_num + 1) / 3), math.ceil((row_num + 1) / 3))
                print(coordinates)
                thr_by_thr[location_dict[coordinates] - 1].append(cell_value)
        for col_num, col_elements in enumerate(columns):
            if not self.check(col_elements):
                return False
        for thr_by_thr_num, thr_by_thr_elements in enumerate(thr_by_thr):
            if not self.check(thr_by_thr_elements):
                return False
        

        return True
        