using System;
using System.Collections.Generic;
using System.IO;



namespace AdventDay1
{
    class Program
    {
        static void Main(string[] args)
        {
            var massFile = File.ReadAllLines("C:\\Users\\justin.huang\\Documents\\GitHub\\RTAOC\\cas\\AdventDay1\\Day1Input.txt");
            var massInputList = new List<string>(massFile);
            List<int> massList = massInputList.ConvertAll(s => Int32.Parse(s));

            //Test Data
            //List<int> massList = new List<int>() { 12, 14, 1969, 100756 };

            int fuelTotal = 0;
            int fuelStage = 0;
            int fuelStageTotal;

            List<int> fuelList = new List<int>();
            foreach (int mass in massList)
            {
                fuelStageTotal = Convert.ToInt32(Math.Floor(Convert.ToDecimal(mass / 3))) - 2;
                fuelStage = Convert.ToInt32(Math.Floor(Convert.ToDecimal(mass / 3))) - 2;
                while (fuelStage > 0)
                {
                    fuelStage = Convert.ToInt32(Math.Floor(Convert.ToDecimal(fuelStage / 3))) - 2;
                    if (fuelStage < 0)
                        fuelStage = 0;
                    fuelStageTotal += fuelStage;
                }
                fuelList.Add(fuelStageTotal);
            }

            foreach (int fuel in fuelList)
            {
                fuelTotal += fuel;
                //Console.WriteLine(fuel);
            }

            Console.WriteLine(fuelTotal);
        }
    }
}
