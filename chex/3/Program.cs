using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;

namespace _3
{
    class Program
    {
        static void Main(string[] args)
        {
            List<string> lines = File.ReadAllLines("input.txt").ToList();

            var line1Points = WalkPath(lines[0]);
            var line2Points = WalkPath(lines[1]);

            var intersectedPoints = line1Points
                .Intersect(line2Points)
                .Where(s => s.X != 0 && s.Y != 0)
                .ToList();

            var manhattanDistance = intersectedPoints
                .Select(s => s.ManhattanDistance())
                .Min();

            var nearestIntersection = intersectedPoints
                .Select(s =>
                {
                    var firstPoint = line1Points.Single(l => l.X == s.X && l.Y == s.Y);
                    var secondPoint = line2Points.Single(l => l.X == s.X && l.Y == s.Y);

                    Console.WriteLine($"Point 1: {firstPoint}");
                    Console.WriteLine($"Point 2: {secondPoint}");

                    return firstPoint.Weight + secondPoint.Weight;
                }).Min();

            Console.WriteLine($"Part 1 Manhattan distance: {manhattanDistance}");
            Console.WriteLine($"Part 2 nearest intersection: {nearestIntersection}");
        }

        public static HashSet<Point> WalkPath(string path)
        {
            Instruction[] steps = path.Split(',')
                .Select(s => new Instruction(s.Substring(0, 1)[0], int.Parse(s.Substring(1))))
                .ToArray();

            var currentPos = new Point(0, 0, 0);
            var points = new HashSet<Point>();
            var stepCounter = 0;

            for (var i = 0; i < steps.Length; i++)
            {
                var step = steps[i];
                switch (step.Direction)
                {
                    case 'D':
                        for (int j = currentPos.Y; j > currentPos.Y - step.Magnitude; j--)
                        {
                            var point = new Point(currentPos.X, j, stepCounter++);
                            points.Add(point);
                        }

                        currentPos = new Point(currentPos.X, currentPos.Y - step.Magnitude, stepCounter);
                        break;
                    case 'U':
                        for (int j = currentPos.Y; j < currentPos.Y + step.Magnitude; j++)
                        {
                            var point = new Point(currentPos.X, j, stepCounter++);
                            points.Add(point);
                        }

                        currentPos = new Point(currentPos.X, currentPos.Y + step.Magnitude, stepCounter);
                        break;
                    case 'L':
                        for (int j = currentPos.X; j > currentPos.X - step.Magnitude; j--)
                        {
                            var point = new Point(j, currentPos.Y, stepCounter++);
                            points.Add(point);
                        }

                        currentPos = new Point(currentPos.X - step.Magnitude, currentPos.Y, stepCounter);
                        break;
                    case 'R':
                        for (int j = currentPos.X; j < currentPos.X + step.Magnitude; j++)
                        {
                            var point = new Point(j, currentPos.Y, stepCounter++);
                            points.Add(point);
                        }

                        currentPos = new Point(currentPos.X + step.Magnitude, currentPos.Y, stepCounter);
                        break;
                }
            }

            return points;
        }
    }

    public struct Instruction
    {
        public char Direction { get; }
        public int Magnitude { get; }

        public Instruction(char direction, int magnitude)
        {
            Direction = direction;
            Magnitude = magnitude;
        }
    }

    public struct Point
    {
        public int X { get; }
        public int Y { get; }
        public int Weight { get; }

        public Point(int x, int y)
        {
            X = x;
            Y = y;
            Weight = 0;
        }

        public Point(int x, int y, int weight)
        {
            X = x;
            Y = y;
            Weight = weight;
        }

        public int ManhattanDistance()
        {
            return Math.Abs(X) + Math.Abs(Y);
        }

        public override string ToString()
        {
            return $"({X}, {Y}, {Weight})";
        }

        public override bool Equals(object other)
        {
            var otherPoint = (Point)other;
            return X == otherPoint.X && Y == otherPoint.Y;
        }

        public override int GetHashCode()
        {
            return X.GetHashCode() + Y.GetHashCode();
        }
    }
}
