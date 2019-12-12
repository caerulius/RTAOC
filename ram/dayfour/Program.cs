using System;

namespace dayfour
{
    class Program
    {
        static void Main(string[] args)
        {
            var min = 123257;
            var max = 647015;
            var count = CountValidPasswords(min, max);
            Console.WriteLine($"Valid passwords for range ({min}, {max}): {count}");
            Console.Read();
        }

        public static int CountValidPasswords(int min, int max)
        {
            var count = 0;
            for(int i = min; i <= max; i++)
                if(IsValid(i)) count++;
            return count;
        }

        public static bool IsValid(int val)
        {
            var str = val.ToString();
            if(str.Length != 6 || !HasValidDouble(str) || !NoDecrease(str)) return false;
            return true;
        }

        public static bool HasValidDouble(string val)
        {
            for(int i = 0; i < val.Length-1; i++)
            {
                if(val[i] == val[i+1]) 
                {
                    var res = true;
                    if(i != 0 && val[i-1] == val[i]) res = false;
                    if(i != val.Length-2 && val[i] == val[i+2]) res = false;
                    if(res) return true;
                }
            }
                
            return false;
        }

        public static bool NoDecrease(string val)
        {
            for(int i = 0; i < val.Length-1; i++) 
                if(val[i] > val[i+1]) return false;
            return true;
        }
    }
}
