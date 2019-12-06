using System;
using System.IO;
using System.Linq;

namespace daytwo
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
            int[] init = (int[])prog.Clone();

            int n = 0; //Input 1 aka Noun 
            int v = 0; //Input 2 aka Verb
            int o = prog[0]; //Output
            int goal = 19690720;
            var found = false;
            for(n = 0; n < 100; n++)
            {
                for(v = 0; v < 100; v++)
                {
                    prog = (int[])init.Clone();
                    prog[1] = n;
                    prog[2] = v;
                    RunProg(prog);
                    o = prog[0];
                    if(o == goal)
                    {
                        found = true;
                        break;
                    }
                }
                if(found) break;
            }

            if(found)
            {
                Console.WriteLine($"Desired Output:{o} found with Noun:{n} and Verb:{v}");
            } 
            else
            {
                Console.WriteLine($"Could not find desired output: {o}");
            }

            // var outputText = String.Join(',', prog);
            // File.WriteAllText("output.txt", outputText);
        }

        static void RunProg(int[] prog) 
        {
            var curPos = 0;
            var curOp = prog[curPos];
            CheckOp(curOp);

            while(curOp != 99) 
            {
                var p1 = prog[curPos+1];
                var p2 = prog[curPos+2];
                var p3 = prog[curPos+3];
                if(curOp == 1) 
                {
                    prog[p3] = prog[p1] + prog[p2];
                }
                if(curOp == 2) 
                {
                    prog[p3] = prog[p1] * prog[p2];
                }

                curPos += 4;
                curOp = prog[curPos];
                CheckOp(curOp);
            }
        }

        static void CheckOp(int op) 
        {
            if(op != 1 && op != 2 && op != 99) 
            {
                Console.WriteLine($"Invalid Op encountered: {op}");
                Console.Read();
                Environment.Exit(0);
            }
        }
    }
}
