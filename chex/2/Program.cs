using System;
using System.IO;
using System.Linq;

namespace _2
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine($"Part 1: {RunProgram(12, 2)}");

            for (int i = 0; i < 100; i++)
            for (int j = 0; j < 100; j++)
            {
                int result = RunProgram(i, j);
                if (result ==  19690720)
                {
                    Console.WriteLine($"Part 2: {100 * i + j}");
                    return;
                }
            }

            Console.WriteLine("no solution womp womp");
        }

        static int RunProgram(int noun, int verb)
        {
            int[] program = File.ReadAllLines("input.txt")
                .First()
                .Split(',')
                .Select(s => int.Parse(s))
                .ToArray();
            
            program[1] = noun;
            program[2] = verb;

            int idx = 0;
            bool halted = false;

            while (idx < program.Length && !halted)
            {
                int opCode = program[idx];
                switch(opCode)
                {
                    case 1:
                        program[program[idx+3]] = program[program[idx+1]] + program[program[idx+2]];
                        break;
                    case 2:
                        program[program[idx+3]] = program[program[idx+1]] * program[program[idx+2]];
                        break;
                    case 99:
                        halted = true;
                        break;
                }

                idx += 4;
            }

            return program[0];
        }
    }
}
