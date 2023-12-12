class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        sorted_boxTypes = sorted(boxTypes, key=lambda x:x[1],reverse = True)
        boxes = 0
        for box, units in sorted_boxTypes:
            if truckSize > box:
                truckSize -= box
                boxes += box * units
            else:
                boxes += truckSize * units
                return boxes
        return boxes