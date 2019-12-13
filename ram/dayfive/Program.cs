using System;
using System.IO;
using System.Linq;

namespace dayfive
{
    class Program
    {
        static void Main(string[] args)
        {
            var path = "input.txt";
            if (args.Length != 0) 
            {
                path = args[0];   
            }

            if(!File.Exists(path)) 
            {
                Console.WriteLine($"File: {path} does not exist");
                Console.ReadLine();
                return;
            }

            int[] prog = File.ReadAllText(path).Split(',').Select(s => int.Parse(s)).ToArray();
            var comp = new IntComputer(prog);
            comp.RunProgram();

            var outputText = String.Join(',', comp.WorkingMemory);
            File.WriteAllText("output.txt", outputText);
        }
    }

    public class IntComputer
    {
        public int[] InitialMemory {get;set;}
        public int[] WorkingMemory {get;set;}
        public int WorkingPointer {get;set;} = 0;

        public IntComputer(int[] prog)
        {
            SetInitMemory(prog);
        }

        public void SetInitMemory(int[] prog)
        {
            InitialMemory = (int[])prog.Clone();
            ResetWorkingMemory();
            WorkingPointer = 0;
        }

        public void ResetWorkingMemory() 
        {
            WorkingMemory = (int[])InitialMemory.Clone();
            WorkingPointer = 0;
        }

        public void RunProgram()
        {
            WorkingPointer = 0;
            var curOp = DecodeOp(WorkingMemory[WorkingPointer]);
            while(curOp.OpCode != 99)
            {
                try
                {
                    switch(curOp.OpCode)
                    {
                        case 1:
                            AdditionOp(curOp);
                            break;
                        case 2:
                            MultiplicationOp(curOp);
                            break;
                        case 3:
                            InputOp(curOp);
                            break;
                        case 4:
                            OutputOp(curOp);
                            break;
                        case 5:
                            JumpTrueOp(curOp);
                            break;
                        case 6:
                            JumpFalseOp(curOp);
                            break;
                        case 7:
                            LessThanOp(curOp);
                            break;
                        case 8:
                            EqualsOp(curOp);
                            break;
                        default:
                            throw new Exception($"bad op code: {curOp.OpCode}");
                    }
                }
                catch (Exception e)
                {
                    Console.WriteLine($"Error occured at position: {curOp.Pos}");
                    Console.WriteLine($"Error op: {WorkingMemory[curOp.Pos]}");
                    for(int i = 0; i < curOp.NumParams; i++) 
                    {
                        Console.WriteLine($"Param {i+1}: {WorkingMemory[curOp.Pos+i+1]}");
                    }

                    //Dump mem at error time
                    var outputText = String.Join(',', WorkingMemory);
                    File.WriteAllText("output.txt", outputText);

                    throw;
                }
                
                curOp = DecodeOp(WorkingMemory[WorkingPointer]);
            }
        }

        void AdditionOp(Operator op)
        {
            var p1 = op.ParamModes[0] == 0 ? WorkingMemory[op.Pos+1] : op.Pos+1;
            var p2 = op.ParamModes[1] == 0 ? WorkingMemory[op.Pos+2] : op.Pos+2;
            var p3 = op.ParamModes[2] == 0 ? WorkingMemory[op.Pos+3] : op.Pos+3;

            var input1 = WorkingMemory[p1];
            var input2 = WorkingMemory[p2];
            WorkingMemory[p3] = input1 + input2;

            WorkingPointer += op.NumParams+1;
        }

        void MultiplicationOp(Operator op)
        {
            var p1 = op.ParamModes[0] == 0 ? WorkingMemory[op.Pos+1] : op.Pos+1;
            var p2 = op.ParamModes[1] == 0 ? WorkingMemory[op.Pos+2] : op.Pos+2;
            var p3 = op.ParamModes[2] == 0 ? WorkingMemory[op.Pos+3] : op.Pos+3;

            var input1 = WorkingMemory[p1];
            var input2 = WorkingMemory[p2];
            WorkingMemory[p3] = input1 * input2;

            WorkingPointer += op.NumParams+1;
        }

        void InputOp(Operator op)
        {
            Console.Write($"({op.Pos}) User input required:");
            var input = Console.ReadLine();
            var i = 0;
            while(!int.TryParse(input, out i))
            {
                Console.Write($"Invalid input. Please type in an integer:");
                Console.ReadLine();
            }

            var savePos = op.ParamModes[0] == 0 ? WorkingMemory[op.Pos+1] : op.Pos+1;
            WorkingMemory[savePos] = i;

            WorkingPointer += op.NumParams+1;
        }

        void OutputOp(Operator op)
        {
            var output = WorkingMemory[WorkingMemory[op.Pos+1]];
            Console.WriteLine($"({op.Pos}) Output: {output}");

            WorkingPointer += op.NumParams+1;
        }

        void JumpTrueOp(Operator op)
        {
            var p1 = op.ParamModes[0] == 0 ? WorkingMemory[op.Pos+1] : op.Pos+1;
            var p2 = op.ParamModes[1] == 0 ? WorkingMemory[op.Pos+2] : op.Pos+2;

            var val1 = WorkingMemory[p1];
            if(val1 != 0)
                WorkingPointer = WorkingMemory[p2];
            else
                WorkingPointer += op.NumParams+1;
        }

        void JumpFalseOp(Operator op)
        {
            var p1 = op.ParamModes[0] == 0 ? WorkingMemory[op.Pos+1] : op.Pos+1;
            var p2 = op.ParamModes[1] == 0 ? WorkingMemory[op.Pos+2] : op.Pos+2;

            var val1 = WorkingMemory[p1];
            if(val1 == 0)
                WorkingPointer = WorkingMemory[p2];
            else
                WorkingPointer += op.NumParams+1;
        }

        void LessThanOp(Operator op)
        {
            var p1 = op.ParamModes[0] == 0 ? WorkingMemory[op.Pos+1] : op.Pos+1;
            var p2 = op.ParamModes[1] == 0 ? WorkingMemory[op.Pos+2] : op.Pos+2;
            var p3 = op.ParamModes[2] == 0 ? WorkingMemory[op.Pos+3] : op.Pos+3;

            var val1 = WorkingMemory[p1];
            var val2 = WorkingMemory[p2];
            if(val1 < val2)
                WorkingMemory[p3] = 1;
            else
                WorkingMemory[p3] = 0;

            WorkingPointer += op.NumParams+1;
        }

        void EqualsOp(Operator op)
        {
            var p1 = op.ParamModes[0] == 0 ? WorkingMemory[op.Pos+1] : op.Pos+1;
            var p2 = op.ParamModes[1] == 0 ? WorkingMemory[op.Pos+2] : op.Pos+2;
            var p3 = op.ParamModes[2] == 0 ? WorkingMemory[op.Pos+3] : op.Pos+3;

            var val1 = WorkingMemory[p1];
            var val2 = WorkingMemory[p2];
            if(val1 == val2)
                WorkingMemory[p3] = 1;
            else
                WorkingMemory[p3] = 0;

            WorkingPointer += op.NumParams+1;
        }

        public Operator DecodeOp(int op)
        {
            var digits = GetDigits(op);
            var code = digits[0];
            var modes = digits.Skip(1).Take(digits.Length - 1).ToArray();

            switch(code)
            {
                case 1:
                case 2:
                case 7:
                case 8:
                    return new Operator(code, WorkingPointer, 3, modes);
                case 3:
                case 4:
                    return new Operator(code, WorkingPointer, 1, modes);
                case 5:
                case 6:
                    return new Operator(code, WorkingPointer, 2, modes);
                case 99:
                    return new Operator(code, WorkingPointer, 0, modes);
                default:
                    throw new Exception($"bad op code: {code}");
            }
        }

        public int[] GetDigits(int code)
        {
            var res = new int[4];
            res[0] = code % 100;
            code = code / 100;
            for(int i = 1; i < 4; i++)
            {
                res[i] = code % 10;
                code = code / 10;
            }

            return res;
        }

        public struct Operator
        {
            public int OpCode {get;}
            public int Pos {get;}
            public int NumParams {get;}
            public int[] ParamModes {get;}

            public Operator(int op, int pos, int num, int[] modes)
            {
                OpCode = op;
                Pos = pos;
                NumParams = num;
                ParamModes = (int[])modes.Clone();
            }
        }
    }
}
