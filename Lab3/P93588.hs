myMap :: (a -> b) -> [a] -> [b] 
myMap f list = [f x | x <- list]

myFilter :: (a -> Bool) -> [a] -> [a]
myFilter f list = [x | x <- list, f x]

myZipWith :: (a -> b -> c) -> [a] -> [b] -> [c]
myZipWith f a b = [f x y | (x, y) <- zip a b]

thingify :: [Int] -> [Int] -> [(Int, Int)]
thingify n d = [(a, b) | a <- n, b <- d, mod a b == 0 ]

factors :: Int -> [Int]
factors n = [x | x <- [1..n], mod n x == 0]