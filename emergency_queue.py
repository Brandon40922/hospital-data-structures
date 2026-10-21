
class Patient:
    def __init__(self, name, urgency):
        if not isinstance(urgency, int) or isinstance(urgency, bool):
            raise ValueError("Urgency must be an integer from 1 to 10.")

        if urgency < 1 or urgency > 10:
            raise ValueError("Urgency must be between 1 and 10.")

        self.name = name
        self.urgency = urgency


class MinHeap:
    def __init__(self):
        self.data = []

    def heapify_up(self, index):
        while index > 0:
            parent_index = (index - 1) // 2

            if self.data[index].urgency < self.data[parent_index].urgency:
                self.data[index], self.data[parent_index] = (
                    self.data[parent_index],
                    self.data[index]
                )
                index = parent_index
            else:
                break

    def heapify_down(self, index):
        size = len(self.data)

        while True:
            left = 2 * index + 1
            right = 2 * index + 2
            smallest = index

            if (
                left < size
                and self.data[left].urgency < self.data[smallest].urgency
            ):
                smallest = left

            if (
                right < size
                and self.data[right].urgency < self.data[smallest].urgency
            ):
                smallest = right

            if smallest == index:
                break

            self.data[index], self.data[smallest] = (
                self.data[smallest],
                self.data[index]
            )

            index = smallest

    def insert(self, patient):
        self.data.append(patient)
        self.heapify_up(len(self.data) - 1)

    def print_heap(self):
        print("Current Queue:")

        if not self.data:
            print("Queue is empty.")
            return

        for patient in self.data:
            print(f"- {patient.name} ({patient.urgency})")

    def peek(self):
        if not self.data:
            return None

        return self.data[0]

    def remove_min(self):
        if not self.data:
            return None

        if len(self.data) == 1:
            return self.data.pop()

        min_patient = self.data[0]
        self.data[0] = self.data.pop()

        self.heapify_down(0)

        return min_patient


def main():
    heap = MinHeap()

    print("--- Emergency Priority Queue ---")

    heap.insert(Patient("Jordan", 3))
    heap.insert(Patient("Taylor", 1))
    heap.insert(Patient("Avery", 5))

    print("\nInitial Patient Queue:")
    heap.print_heap()

    next_up = heap.peek()
    print(f"\nNext Patient: {next_up.name} ({next_up.urgency})")

    served = heap.remove_min()
    print(f"\nPatient Served: {served.name}")

    print("\nUpdated Patient Queue:")
    heap.print_heap()

    print("\n--- Additional Tests ---")

    heap.insert(Patient("Riley", 2))
    heap.insert(Patient("Morgan", 4))
    heap.insert(Patient("Casey", 1))

    heap.print_heap()

    print("\nServing Patients by Priority:")

    served_urgencies = []

    while heap.peek() is not None:
        patient = heap.remove_min()
        served_urgencies.append(patient.urgency)
        print(f"Serving {patient.name} (Urgency: {patient.urgency})")

    assert served_urgencies == sorted(served_urgencies)

    print("\nTesting Empty Queue:")
    heap.print_heap()

    assert heap.peek() is None
    assert heap.remove_min() is None

    print("\nTesting Invalid Urgency:")

    try:
        Patient("Invalid Patient", 11)
    except ValueError as error:
        print("Error:", error)

    print("\nAll emergency queue tests passed!")


if __name__ == "__main__":
    main()
