using System;
using System.IO;
using System.Linq;
using System.Collections;
using System.Collections.Generic;

namespace daythree
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

            var paths = File.ReadAllText(path).Split('\n');
            var p1 = paths[0].Split(',').Select(m => new Move(m)).ToList();
            var p2 = paths[1].Split(',').Select(m => new Move(m)).ToList();

            var panel = new Panel(p1, p2);
            var pt1 = panel.FindClosestIntersectionByDistance();
            Console.WriteLine($"Closest intersection by distance: {pt1.Position} Distance: {pt1.Position.TaxiDistance()}");
            var pt2 = panel.FindClosestIntersectionBySteps();
            Console.WriteLine($"Closest intersection by steps: {pt2.Position} Steps {pt2.TotalSteps}");
            Console.Read();
        }
    }

    public class Point {
        public int X {get;set;}
        public int Y {get;set;}

        public Point(int x, int y)
        {
            X = x;
            Y = y;
        }

        public Point()
        {
            //Default to origin
            X = 0;
            Y = 0;
        }

        public int TaxiDistance() 
        {
            return Math.Abs(X) + Math.Abs(Y);
        }

        public override bool Equals(object obj)
        {
            if (obj == null || GetType() != obj.GetType())
            {
                return false;
            }
            
            var pt = (Point)obj;
            if(pt.X == X && pt.Y == Y) return true;
            return false;
        }
        
        public override int GetHashCode()
        {
            return X.GetHashCode() ^ Y.GetHashCode();
        }

        public override string ToString()
        {
            return $"({X},{Y})";
        }
    }

    public class WirePoint
    {
        //Num of wires touching
        public int NumWires {get;set;} = 1;
        //Sum of steps of all the wires
        public int TotalSteps {get;set;}
        //Position on Panel
        public Point Position {get;set;} = new Point();

        public WirePoint(Point p, int steps)
        {
            Position.X = p.X;
            Position.Y = p.Y;
            TotalSteps = steps;
        }
    }

    public class Panel
    {
        public Dictionary<Point, WirePoint> Grid {get;set;} = new Dictionary<Point, WirePoint>();
        public List<Move> PathOne {get;set;}
        public List<Move> PathTwo {get;set;}

        public Panel(List<Move> p1, List<Move> p2)
        {
            PathOne = p1;
            PathTwo = p2;
            InitializeGrid();
        }
        public Panel() { }

        public void ResetGrid()
        {
            Grid = new Dictionary<Point, WirePoint>();
        }

        public void InitializeGrid()
        {
            ResetGrid();
            RecordPath(PathOne);
            RecordPath(PathTwo);
        }
        public WirePoint FindClosestIntersectionByDistance()
        {
            return Grid.Values.Where(p => p.NumWires > 1).OrderBy(p => p.Position.TaxiDistance()).First();
        }

        public WirePoint FindClosestIntersectionBySteps()
        {
            return Grid.Values.Where(p => p.NumWires > 1).OrderBy(p => p.TotalSteps).First();
        }

        public void RecordPath(List<Move> moves)
        {
            //Point defaults to 0,0
            var curPos = new Point();
            var steps = 0;

            //To avoid counting self intersections keep track of current path points separately
            var pts = new Dictionary<Point, WirePoint>();

            foreach(var m in moves)
            {
                for (int i = m.Distance; i > 0; i--)
                {
                    switch(m.Direction)
                    {
                        case Direction.Up:
                            curPos.Y++;
                            break;
                        case Direction.Down:
                            curPos.Y--;
                            break;
                        case Direction.Right:
                            curPos.X++;
                            break;
                        case Direction.Left:
                            curPos.X--;
                            break;
                    }
                    steps++;
                    if(!pts.ContainsKey(curPos))
                        pts.Add(new Point(curPos.X, curPos.Y), new WirePoint(curPos, steps));
                }
            }

            //Mark points on main grid
            //Either increment numWires and TotalSteps or add new value object
            foreach(var p in pts.Values)
            {
                if (Grid.TryGetValue(p.Position, out WirePoint val))
                {
                    val.NumWires++;
                    val.TotalSteps += p.TotalSteps;
                }
                else
                {
                    Grid[new Point(p.Position.X, p.Position.Y)] = p;
                }
            }
        }
    }

    public class Move
    {
        public Direction Direction {get;set;}
        public int Distance {get;set;}

        public Move(string move)
        {
            Direction = ParseDirection(move.Substring(0,1));
            Distance = int.Parse(move.Substring(1));
        }

        Direction ParseDirection(string dir)
        {
            switch(dir.ToUpper())
            {
                case "U":
                    return Direction.Up;
                case "D":
                    return Direction.Down;
                case "R":
                    return Direction.Right;
                case "L":
                    return Direction.Left;
                default:
                    return Direction.Unknown;
            }
        }
    }

    public enum Direction
    {
        Unknown,
        Up,
        Down,
        Left,
        Right
    }
    
}
