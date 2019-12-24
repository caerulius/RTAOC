using System;
using System.Collections.Generic;


namespace AdventDay4
{
    class Day4p1
    {
        static void Main(string[] args)
        {
            List<int> puzzlerange = new List<int>();
            //for (int i = 254032; i <= 789860; i++)
            //{
            //    puzzlerange.Add(i);
            //}
            puzzlerange.Add(111111); //no
            puzzlerange.Add(223450); //no
            puzzlerange.Add(123789); //no
            puzzlerange.Add(112233); //yes
            puzzlerange.Add(123444); //no
            puzzlerange.Add(111122); //yes
            puzzlerange.Add(223333); //yes


            bool doublesFlag = false;
            bool increasingFlag = false;
            bool largegroupFlag = false;
            string password;
            int numOfPass = 0;

            foreach (int num in puzzlerange)
            {
                password = num.ToString();
                for (int j = 0; j < password.Length - 1; j++)
                {
                    if (j < password.Length - 2)
                    {
                        if ((password[j] == password[j + 1]))
                        {
                            doublesFlag = true;
                            break;
                        }
                        else
                            doublesFlag = false;
                    }
                }

                if (doublesFlag == true)
                {
                    for (int j = 0; j < 4; j++)
                    {
                       // largegroupFlag = false;
                        if (password[j] == password[j + 1] && password[j] != password[j + 2])
                        {
                            largegroupFlag = true;
                            //break;
                        }
                        //else if (password[j + 1] == password[j + 2] && (password[j + 1] == password[j + 2] && password[j] == password[j + 2]))
                        //{
                        //    largegroupFlag = true;
                        //    break;
                        //}
                       // Console.WriteLine("{0},{1},{2} - {3}", password[j], password[j + 1], password[j + 2], acceptableFlag);

                    }
                }

                
                if (doublesFlag == true && largegroupFlag == true)
                {
                    for (int k = 0; k < password.Length - 1; k++)
                    {
                        if (Convert.ToInt32(password[k]) <= Convert.ToInt32(password[k + 1]))
                        {
                            increasingFlag = true;
                        }
                        else
                        {
                            increasingFlag = false;
                            break;
                        }
                    }
                }

                //Console.WriteLine("{0} - {1}", password, acceptableFlag);

                if (increasingFlag == true)
                {
                    //if (doublesFlag == true && largegroupFlag == false && )
                    Console.WriteLine("{0}", num);
                    numOfPass++;
                }
            }

            Console.WriteLine("{0}", numOfPass);
        }
    }
}
