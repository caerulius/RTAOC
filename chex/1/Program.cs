using System;
using System.IO;
using System.Linq;

namespace _1
{
    class Program
    {
        static void Main(string[] args)
        {
            int[] moduleMasses = File.ReadAllLines("input.txt")
                .Select(s => int.Parse(s))
                .ToArray();

            int fuelAmounts = moduleMasses
                .Select(s => (s / 3) - 2)
                .Sum();

            int part2FuelAmounts = moduleMasses
                .Select(s => GetFuelForMass(s))
                .Sum();

            Console.WriteLine($"Part 1 answer: {fuelAmounts}");
            Console.WriteLine($"Part 2 answer: {part2FuelAmounts}");
        }

        private static int GetFuelForMass(int mass)
        {
            int fuelToHaul = (mass / 3) - 2;
            int totalFuel = fuelToHaul;

            while (true)
            {
                int fuel = (fuelToHaul / 3) - 2;
                if (fuel <= 0)
                    break;

                totalFuel += fuel;
                fuelToHaul = fuel;
            }

            return totalFuel;
        }
    }
}
