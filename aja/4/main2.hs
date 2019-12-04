import Data.List.Split

digits :: Int -> [Int]
digits 0 = []
digits x = digits (x `div` 10) ++ [x `mod` 10]

validatePassword :: ([Int], Bool, Bool, Bool) -> Bool
validatePassword ([digit], foundSeq, twoSeq, _) = foundSeq || twoSeq
validatePassword (list@(digit:tail), foundSeq, twoSeq, inSeq)
    | digit < head tail && twoSeq = validatePassword (tail,True,False,False)
    | digit < head tail = validatePassword (tail,foundSeq,False,False)
    | digit == head tail = validatePassword (tail,foundSeq,not inSeq,True)
    | otherwise = False

checkPasswords :: [Int] -> [Int]
checkPasswords [password] = if validatePassword (digits password, False, False, False)
                            then [password]
                            else []
checkPasswords list@(password:tail) = if validatePassword (digits password, False, False, False)
                                      then password:checkPasswords tail
                                      else checkPasswords tail

doTheThing :: String -> [Int]
doTheThing input = checkPasswords [read (head (splitOn "-" input)) :: Int .. read (last (splitOn "-" input)) :: Int]

countTheThing :: String -> Int
countTheThing input = length (doTheThing input)