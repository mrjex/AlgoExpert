using System;

namespace SingleCycleCheck {
    class Program {
        static int startIdx = 0;

        static void Main(string[] args) {
            runTestCases();
        }

        private static bool HasSingleCycle(int[] array) {
            int currentIdx = startIdx;
            int visitedElements = 0;

            while (visitedElements < array.Length) {

                if (currentIdx == startIdx && visitedElements > 0) {
                    return false;
                }

                visitedElements++;
                currentIdx = GetNextIdx(array, currentIdx);
            }
            
            return currentIdx == startIdx;
        }

        private static int GetNextIdx(int[] array, int currentIdx) {
            int nextIdx = (currentIdx + array[currentIdx]) % array.Length;
            return nextIdx >= 0 ? nextIdx : array.Length + nextIdx;
        }

        private static void runTestCases() {

            // Define test arrays
            int[] test1 = {2, 3, 1, -4, -4, 2}; 
            int[] test2 = {1, 1, 1, 1, 1, 1};
            int[] test3 = {1, 1, 1, 0, 0, 0};
            int[] test4 = {0, 1, 1, 1, 1, 1};

            // Control output of executed test cases
            Console.WriteLine("");
            Console.WriteLine("OUTPUT TESTS:");

            Console.WriteLine("True = " + HasSingleCycle(test1)); // Expected output: True
            Console.WriteLine("True = " + HasSingleCycle(test2)); // Expected output: True
            Console.WriteLine("False = " + HasSingleCycle(test3)); // Expected output: False
            Console.WriteLine("False = " + HasSingleCycle(test4)); // Expected output: False
        }
    }
}
