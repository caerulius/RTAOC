using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;

namespace AdventDay2
{
    class Part1
    {
        static void Main(string[] args)
        {

            List<int> IntcodeProgram = new List<int>();
            var instructionFile = File.ReadAllLines("C:\\Users\\justin.huang\\Documents\\GitHub\\RTAOC\\cas\\AdventDay2\\Day2Input.txt");
            string[] instructionFileArray = null;
            var instructionInputList = new List<string>();
            foreach (string line in instructionFile)
            {
                instructionFileArray = line.Split(',');
            }
            instructionInputList = instructionFileArray.ToList();
            IntcodeProgram = instructionInputList.ConvertAll(s => Int32.Parse(s));

            //Test Data
            //List<int> IntcodeProgram = new List<int>() { 1, 9, 10, 3, 2, 3, 11, 0, 99, 30, 40, 50 };

            //1202 Program
            IntcodeProgram[1] = 12;
            IntcodeProgram[2] = 2;

            int haltsignal = 0;
            int startpos = 0;

            while(haltsignal == 0)
            {
                (IntcodeProgram,haltsignal)=IntcodeProcess(IntcodeProgram, startpos);
                if (haltsignal == 0)
                {
                    startpos += 4;
                }
            }

            IntcodeProgram.ForEach(i => Console.Write("{0},", i));

        }

        public static (List<int> listout,int halt) IntcodeProcess (List<int> sequence,int startpos)
        {
            int opcode = sequence[startpos];
            int pos_in_1;
            int pos_in_2;
            int pos_out;
            int halt = 0;

            if (opcode == 99)
            {
                halt = 1;
            }
            else if (opcode == 1)
            {
                pos_in_1 = sequence[startpos + 1];
                pos_in_2 = sequence[startpos + 2];
                pos_out = sequence[startpos + 3];
                sequence[pos_out] = sequence[pos_in_1] + sequence[pos_in_2];
            }
            else if (opcode == 2)
            {
                pos_in_1 = sequence[startpos + 1];
                pos_in_2 = sequence[startpos + 2];
                pos_out = sequence[startpos + 3];
                sequence[pos_out] = sequence[pos_in_1] * sequence[pos_in_2];
            }
            else
            {
                Console.WriteLine("Opcode error in position"+startpos);
            }

            return (sequence,halt);
        }

    }
}
