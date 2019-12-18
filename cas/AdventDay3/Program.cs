using System;
using System.IO;
using System.Collections.Generic;
using System.Linq;


namespace AdventDay3
{
    class Program
    {
        static void Main(string[] args)
        {
            var wireFile = File.ReadAllLines("C:\\Users\\justin.huang\\Documents\\GitHub\\RTAOC\\cas\\AdventDay3\\Day3Input.txt");


            Wirepoint wire1 = new Wirepoint(0, 0,0);
            Wirepoint wire2 = new Wirepoint(0, 0,0);
            Wirepoint quickestpoint = new Wirepoint(0, 0, 0);

            int totallength = 0;
            int shortestlength = 0;
            int wire1length = 0;
            int wire2length = 0;

            List<Wirepoint> wirePath1 = new List<Wirepoint>() { wire1 };
            List<Wirepoint> wirePath2 = new List<Wirepoint>() { wire2 };

            //Test Data
            //string path1 = "R8,U5,L5,D3";
            //string path2 = "U7,R6,D4,L4";
            //string path1 = "R75,D30,R83,U83,L12,D49,R71,U7,L72";
            //string path2 = "U62,R66,U55,R34,D71,R55,D58,R83";
            //string path1 = "R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51";
            //string path2 = "U98,R91,D20,R16,D67,R40,U7,R15,U6,R7";

            //Actual Data
            string path1 = wireFile[0];
            string path2 = wireFile[1];

            string[] pathArray1 = path1.Split(",");
            string[] pathArray2 = path2.Split(",");
            List<string> pathList1 = new List<string>();
            List<string> pathList2 = new List<string>();
            pathList1 = pathArray1.ToList();
            pathList2 = pathArray2.ToList();

            wirePath1 = AddMovementPath(wirePath1, pathList1);
            wirePath2 = AddMovementPath(wirePath2, pathList2);


            IEnumerable<Wirepoint> bothwires = wirePath1.Intersect(wirePath2);
            quickestpoint = bothwires.ElementAt(1);
            foreach (Wirepoint wire in bothwires)
            {
                if (!(wire.X_cord == 0 && wire.Y_cord == 0))
                {
                    totallength = Math.Abs(wire.X_cord) + Math.Abs(wire.Y_cord);
                    if (shortestlength == 0)
                        shortestlength = totallength;
                    else if (shortestlength > totallength)
                        shortestlength = totallength;
                }
                Console.WriteLine(
                    "{0},{1} - {2}",
                    wire.X_cord,
                    wire.Y_cord,
                    totallength);
            }
            Console.WriteLine("\n");
            Console.WriteLine(shortestlength);
            Console.WriteLine("{0},{1}",quickestpoint.X_cord, quickestpoint.Y_cord);

            wire1length = wirePath1.Find(x => x.X_cord == quickestpoint.X_cord && x.Y_cord == quickestpoint.Y_cord).Distancetraveled;
            wire2length = wirePath2.Find(x => x.X_cord == quickestpoint.X_cord && x.Y_cord == quickestpoint.Y_cord).Distancetraveled;

            Console.WriteLine("{0}", wire1length);
            Console.WriteLine("{0}", wire2length);
            Console.WriteLine("\n");
            Console.WriteLine("Answer: {0}", (wire1length + wire2length));
        }

        public static List<Wirepoint> AddMovementPath (List<Wirepoint> Wirepoints, List<string> path)
        {
            char direction;
            int length;
            //List<Wirepoint> rangeadd;
            foreach (string line in path)
            {
                direction = line[0];
                length = Convert.ToInt32(line.Substring(1));
                switch (direction)
                {
                    case 'U':
                        MoveUp(Wirepoints, length);
                        break;
                    case 'R':
                        MoveRight(Wirepoints, length);
                        break;
                    case 'D':
                        MoveDown(Wirepoints, length);
                        break;
                    case 'L':
                        MoveLeft(Wirepoints, length);
                        break;
                }
            }
            return Wirepoints;
        }

        public class Wirepoint : IEquatable<Wirepoint>
        {
            public int X_cord { get; set; }
            public int Y_cord { get; set; }
            public int Distancetraveled { get; set; }
            public Wirepoint (int x_cord,int y_cord, int distancetraveled)
            {
                X_cord = x_cord;
                Y_cord = y_cord;
                Distancetraveled = distancetraveled;
            }

            public bool Equals(Wirepoint other)
            {
                if (other is null)
                    return false;

                return this.X_cord == other.X_cord && this.Y_cord == other.Y_cord;
            }

            public override bool Equals(object obj) => Equals(obj as Wirepoint);
            public override int GetHashCode() => (X_cord, Y_cord).GetHashCode();
            
        }

        

        public static List<Wirepoint> MoveUp(List<Wirepoint> Wirepoints, int movement)
         {
            for(int i = 0; i<movement; i++)
            {
                Wirepoints.Add(new Wirepoint(Wirepoints.Last().X_cord+1,Wirepoints.Last().Y_cord,Wirepoints.Last().Distancetraveled+ 1));
            }
            return Wirepoints;
         }

        public static List<Wirepoint> MoveDown(List<Wirepoint> Wirepoints, int movement)
         {
            for (int i = 0; i < movement; i++)
            {
                Wirepoints.Add(new Wirepoint(Wirepoints.Last().X_cord - 1, Wirepoints.Last().Y_cord, Wirepoints.Last().Distancetraveled + 1));
            }
            return Wirepoints;
         }

        public static List<Wirepoint> MoveLeft(List<Wirepoint> Wirepoints, int movement)
         {
            for (int i = 0; i < movement; i++)
            {
                Wirepoints.Add(new Wirepoint(Wirepoints.Last().X_cord, Wirepoints.Last().Y_cord - 1, Wirepoints.Last().Distancetraveled + 1));
            }
            return Wirepoints;
         }

        public static List<Wirepoint> MoveRight(List<Wirepoint> Wirepoints, int movement)
         {
            for (int i = 0; i < movement; i++)
            {
                Wirepoints.Add(new Wirepoint(Wirepoints.Last().X_cord, Wirepoints.Last().Y_cord + 1, Wirepoints.Last().Distancetraveled + 1));
            }
            return Wirepoints;
         }
    }
}
