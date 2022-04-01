"""Lists sorting and selection exercise"""


class ListStats:
    """ListStats allows selecting items from a list"""

    def __init__(self, item_list: list):
        self._item_list = item_list

    def between(self, value_1: int, value_2: int) -> None:
        """Prints elements between items criteria"""
        start = self._item_list.index(value_1)
        end = self._item_list.index(value_2)
        print(self._item_list[start : end + 1])

    def greater(self, value: int) -> None:
        """Prints greater elements than a criteria"""
        index = self._item_list.index(value)
        print(self._item_list.__getitem__(slice(index, -1)))

    def less(self, value: int) -> None:
        """Prints lower elements than a criteria"""
        index = self._item_list.index(value)
        print(self._item_list.__getitem__(slice(0, index)))


class DataCapture:
    """DataCapture creates a list and sort it"""

    def __init__(self):
        self._data_capture_list: list = []

    def add(self, value: int) -> None:
        """Adds an item into a list"""
        self._data_capture_list.append(value)

    def sort_list(self) -> None:
        """Sorts the list by Insertion's' Sort Algorithm"""
        for step in range(1, len(self._data_capture_list)):
            key = self._data_capture_list[step]
            j = step - 1

            while j >= 0 and key < self._data_capture_list[j]:
                self._data_capture_list[j + 1] = self._data_capture_list[j]
                j = j - 1

            self._data_capture_list[j + 1] = key

    def buildstats(self) -> ListStats:
        """Returns ListStats object"""
        self.sort_list()
        return ListStats(self._data_capture_list)


if __name__ == "__main__":
    capture = DataCapture()
    capture.add(3)
    capture.add(9)
    capture.add(3)
    capture.add(4)
    capture.add(6)
    stats = capture.buildstats()
    stats.between(3, 6)
    stats.greater(4)
    stats.less(6)
