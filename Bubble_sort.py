class BubbleSorter:
    
    def __init__(self, data_list):
        self.data = list(data_list)
        self.original_data = list(data_list)
    
    def display(self, prefix="Current data:"):
        print(f"{prefix} {self.data}")

    def sort(self):
        n = len(self.data)
        for i in range(n - 1):
            swapped = False

            for j in range(0, n - i - 1):
                if self.data[j] > self.data[j + 1]:
                    self.data[j], self.data[j + 1] = self.data[j + 1], self.data[j]
                    swapped = True
            print(f"After round {i + 1}: {self.data}")
            break

if __name__ == "__main__":
    nums = [64, 34, 25, 12, 22, 11, 90]
    sorter = BubbleSorter(nums)
    print("Before sorting:")
    sorter.display()
    sorter.sort()
    print("\nAfter sorting:")
    sorter.display()
