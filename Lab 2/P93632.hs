eql :: [Int] -> [Int] -> Bool
eql x y = (length x == length y && and(zipWith (==) x y ))

