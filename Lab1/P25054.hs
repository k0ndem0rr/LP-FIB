myLength :: [Int] -> Int 
myLength list 
    | null list = 0
    | otherwise = 1 + myLength (tail list)

myMaximum :: [Int] -> Int
myMaximum list 
    | null (tail list) = list !! 0
    | head list > last list = myMaximum(init list)
    | otherwise = myMaximum(tail list)

average :: [Int] -> Float
average list = fromIntegral (sum list) / fromIntegral (myLength list)

buildPalindrome :: [Int] -> [Int]
buildPalindrome list = reverse list ++ list 

remove :: [Int] -> [Int] -> [Int]
remove x y 
    | null y = x
    | otherwise = drop (head y) (remove x (tail y))
        where
            drop :: Int -> [Int] -> [Int]
            drop a b 
                | null b = b
                | head (b) == a = drop a (tail b) 
                | otherwise = [head (b)] ++ (drop a (tail b)) 

flatten :: [[Int]] -> [Int]
flatten list = if null list
    then []
    else head list ++ flatten (tail list)

oddsNevens :: [Int] -> ([Int],[Int])
oddsNevens list 
    | null list = ([],[])
    | even (head list) = (f1, [head list] ++ f2)
    | otherwise = ([head list] ++ f1, f2)
        where  
            (f1,f2) = oddsNevens (tail list)

primeDivisors :: Int -> [Int]
primeDivisors n = leaveDivisors (leavePrimes ([2]++[3,5..(div n 2)]))
    where 
        leaveDivisors list 
            | null list = []
            | mod n (head list) == 0 = [head (list)] ++ (leaveDivisors (tail list))
            | otherwise = leaveDivisors (tail list)
        leavePrimes list
            | null list = []
            | isPrime (head list) = [head (list)] ++ (leavePrimes (tail list))
            | otherwise = leavePrimes (tail list)
            where 
                isPrime x = aux 2
                        where 
                            aux d
                                | d >= x = True
                                | otherwise = (not ((mod x d) == 0) && (aux (d+1)))