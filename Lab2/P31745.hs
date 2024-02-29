flatten :: [[Int]] -> [Int]
flatten x = foldl (++) [] x

makeOne:: Char -> Int
makeOne x = 1

myLength :: String -> Int
myLength x = foldl (+) 0 (map (makeOne) x) 

myReverse :: [Int] -> [Int]
myReverse x = foldr (f) [] x
    where 
        f a b = b ++ [a] 

countIn :: [[Int]] -> Int -> [Int]
countIn list n = map (count) list
    where 
        count = length . (filter ((==) n))

firstWord :: String -> String
firstWord s = takeWhile ((/=) ' ') (dropWhile ((==) ' ') s)