using System;

namespace _4
{
    class Program
    {
        const int minVal = 136818;
        const int maxVal = 685979;

        static void Main(string[] args)
        {
            int validPart1Count = 0;
            int validPart2Count = 0;

            for (int i = minVal; i < maxVal; i++)
            {
                if (IsValidPasswordPart1(i))
                    validPart1Count++;
                if (IsValidPasswordPart2(i))
                    validPart2Count++;
            }

            Console.WriteLine($"Part 1: {validPart1Count}");
            Console.WriteLine($"Part 2: {validPart2Count}");
        }

        private static bool IsValidPasswordPart1(int i)
        {
            var pwString = i.ToString();
            bool hasDouble = false;

            for (int j = 0; j < pwString.Length - 1; j++)
            {
                int x = (int)pwString[j];
                int y = (int)pwString[j+1];

                if (y < x)
                    return false;

                if (y == x)
                    hasDouble = true;
            }

            return hasDouble;
        }

        private static bool IsValidPasswordPart2(int i)
        {
            var pwString = i.ToString();
            bool hasDouble = false;

            for (int j = 0; j < pwString.Length - 1; j++)
            {
                int x = (int)pwString[j];
                int y = (int)pwString[j+1];

                if (y < x)
                    return false;

                if (y == x)
                {
                    if (j > 0)
                    {
                        int w = (int)pwString[j-1];
                        if (w == x)
                            continue;
                    }

                    if (j < pwString.Length - 2)
                    {
                        int z = (int)pwString[j+2];
                        if (z == y)
                            continue;
                    }

                    hasDouble = true;
                }
            }

            return hasDouble;
        }
    }
}
