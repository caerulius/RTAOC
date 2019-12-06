using System;
using System.IO;

namespace dayone
{
    class Program
    {
        static void Main(string[] args)
        {
            if (args.Length == 0) 
            {
                ConsoleInputLoop();
                return;
            }

            var path = args[0];

            if(!File.Exists(path)) 
            {
                Console.WriteLine($"File: {path} does not exist");
                Console.ReadLine();
                return;
            }

            string[] lines = File.ReadAllLines(path);
            var total = 0;
            foreach(var l in lines) total += CalcTotalFuel(int.Parse(l));

            Console.WriteLine($"Total fuel needed: {total}");
            Console.ReadLine();
        }

        static void ConsoleInputLoop() 
        {
            Console.WriteLine("Enter each module's mass (end to stop and show end result): ");

            var total = 0;
            var val = Console.ReadLine();
            while(val != "end") 
            {
                if(Int32.TryParse(val, out int i)) 
                {
                    var fuel = CalcFuel(i);
                    Console.WriteLine($"Fuel required for module of mass({i}) = {fuel}");
                    total += fuel;
                    Console.WriteLine($"Running total: {total}");
                } else 
                {
                    Console.WriteLine($"Invalid input: {val}");
                }
                
                Console.WriteLine("Please enter another value or \"end\" to stop: ");
                val = Console.ReadLine();
            }
            Console.WriteLine($"Total fuel required: {total}");
            Console.WriteLine("Press any key to end");
            Console.ReadLine();
        }

        static int CalcTotalFuel(int mass) 
        {
            var init = CalcFuel(mass);
            var add = CalcFuel(init);
            var total = init + (add > 0 ? add : 0);
            while (add > 0) {
                add = CalcFuel(add);
                if(add > 0) total += add;
            }
            return total;
        }
        static int CalcFuel(int mass)
        {
            return (int)Math.Floor(mass/3m) - 2;
        }
    }
}
