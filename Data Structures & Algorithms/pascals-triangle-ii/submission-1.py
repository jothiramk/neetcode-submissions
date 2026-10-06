class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        row = [1]

        for _ in range(rowIndex):
            next_row = [1]
            # Add sums of adjacent elements from the previous row
            for j in range(1, len(row)):
                next_row.append(row[j - 1] + row[j])
            next_row.append(1)
            row = next_row

        return row