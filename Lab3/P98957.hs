ones :: [Integer]
ones = [1,1..]

nats :: [Integer]
nats = iterate (+1) 0

ints :: [Integer]
ints = [0] ++ concat [[p,p*(-1)] | p <- [1..]]

triangulars :: [Integer]
triangulars = scanl (+) 0 [1..]

factorials :: [Integer]
factorials = scanl (*) 1 [1..]

fibs :: [Integer]
fibs = [0, 1] ++ [fibs !! x + fibs !! (x-1) | x <- [1..]]

primes :: [Integer]
{-primes = filterPrime ([2] ++ [3,5.. 70])
    where 
        filterPrime list = [head list] ++ (filterPrime (filter (divisible (head list)) (tail list)))
            where 
                divisible x y = ((mod y x) == 0)-}

primes = garbell [2..]
    where
        garbell (p : xs) = p : garbell [x | x <- xs, x `mod` p /= 0]

hammings :: [Integer]
hammings = (mult [1])
    where
        mult  n = merge n (mult (concat [[x*2,x*3,x*5] | x <- n, x < 10]))
            where
                merge (x:xs) (y:ys)
                    | x < y               = x : merge xs (y:ys)
                    | x == y              = x : merge xs ys
                    | otherwise           = y : merge (x:xs) ys


{-hammings = hammings' [] [1..]
    where
        hammings' a b
            | checkHamming (head b) = [head b] ++ hammings' (a++[head b]) (tail b)
            | otherwise = hammings' a (tail b)
            where 
                checkHamming x
                    | (x == 1 ) = True
                    | mod x 5 == 0 = checkHamming (div x 5)
                    | mod x 3 == 0 = checkHamming (div x 3)
                    | mod x 2 == 0 = checkHamming (div x 2)
                    | otherwise = False-}



lookNsay :: [Integer]
lookNsay = iterate (read . say . show) 1
    where
        say [] = [] 
        say s = show(count (tail s)) ++ [head s] ++ say (difftail s)
            where
                count s'
                    | null s' = 1
                    | head s' == (head s) = 1 + count (tail s')
                    | otherwise = 1
                difftail s' 
                    | null s' = []
                    | head s' == (head s) = difftail (tail s')
                    | otherwise = s'

tartaglia :: [[Integer]]
tartaglia = iterate (say) [1]
    where
        say s
            | null s = []
            | null (tail s) = [head s] ++ [head s]
            | otherwise = [head s] ++ [head s + (head (say (tail s)))] ++ tail (say (tail s))