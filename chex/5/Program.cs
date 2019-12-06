using System;
using System.IO;
using System.Linq;

namespace _5
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine($"Part 1 solution: {RunProgram(1)}");
            Console.WriteLine($"Part 2 solution: {RunProgram(5)}");
        }

        static int RunProgram(int input)
        {
            int[] program = File.ReadAllLines("input.txt")
                .First()
                .Split(',')
                .Select(s => int.Parse(s))
                .ToArray();

            int idx = 0;
            bool halted = false;

            while (idx < program.Length && !halted)
            {
                var instruction = new Instruction(program[idx].ToString());
                Console.WriteLine(instruction);

                if (instruction.OpCode == 31)
                    halted = true;

                switch (instruction.OpCode)
                {
                    case 1:
                        program[program[idx + 3]] = GetValue(instruction.Parameter1Mode, program, idx + 1) + GetValue(instruction.Parameter2Mode, program, idx + 2);
                        idx += 4;
                        break;
                    case 2:
                        program[program[idx + 3]] = GetValue(instruction.Parameter1Mode, program, idx + 1) * GetValue(instruction.Parameter2Mode, program, idx + 2);
                        idx += 4;
                        break;
                    case 3:
                        program[program[idx + 1]] = input;
                        idx += 2;
                        break;
                    case 4:
                        Console.WriteLine($"Output: {GetValue(instruction.Parameter1Mode, program, idx + 1)}");
                        idx += 2;
                        break;
                    case 5:
                        if (GetValue(instruction.Parameter1Mode, program, idx + 1) != 0)
                            idx = GetValue(instruction.Parameter2Mode, program, idx + 2);
                        else
                            idx += 3;
                        break;
                    case 6:
                        if (GetValue(instruction.Parameter1Mode, program, idx + 1) == 0)
                            idx = GetValue(instruction.Parameter2Mode, program, idx + 2);
                        else
                            idx += 3;
                        break;
                    case 7:
                        if (GetValue(instruction.Parameter1Mode, program, idx + 1) < GetValue(instruction.Parameter2Mode, program, idx + 2))
                            program[program[idx + 3]] = 1;
                        else
                            program[program[idx + 3]] = 0;
                        idx += 4;
                        break;
                    case 8:
                        if (GetValue(instruction.Parameter1Mode, program, idx + 1) == GetValue(instruction.Parameter2Mode, program, idx + 2))
                            program[program[idx + 3]] = 1;
                        else
                            program[program[idx + 3]] = 0;
                        idx += 4;
                        break;
                    case 99:
                        halted = true;
                        break;
                }
            }

            return program[0];
        }

        private static int GetValue(ParameterMode mode, int[] program, int idx)
        {
            switch(mode)
            {
                case ParameterMode.Immediate:
                    return program[idx];
                case ParameterMode.Position:
                default:
                    return program[program[idx]];
            }
        }

        public class Instruction
        {
            private string _paddedString;

            public Instruction(string operation)
            {
                string paddedString = operation.PadLeft(5, '0');
                _paddedString = paddedString;

                Parameter3Mode = (ParameterMode)Char.GetNumericValue(paddedString[0]);
                Parameter2Mode = (ParameterMode)Char.GetNumericValue(paddedString[1]);
                Parameter1Mode = (ParameterMode)Char.GetNumericValue(paddedString[2]);
                OpCode = int.Parse(paddedString.Substring(3));
            }

            public ParameterMode Parameter1Mode { get; set; }
            public ParameterMode Parameter2Mode { get; set; }
            public ParameterMode Parameter3Mode { get; set; }
            public int OpCode { get; set; }

            public override string ToString() => $"Instruction: {_paddedString}, OpCode: {OpCode}, Parameter 1 Mode: {Parameter1Mode}, Parameter 2 Mode: {Parameter2Mode}, Parameter 3 Mode: {Parameter3Mode}";
        }

        public enum ParameterMode
        {
            Position = 0,
            Immediate = 1,
        }
    }
}
