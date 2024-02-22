absValue :: Int -> Int
absValue n = if n > 0 
    then n 
    else n*(-1)

power :: Int -> Int -> Int 
power _ 0 = 1
power x p = x * power x (p-1)

isPrime :: Int -> Bool
isPrime x 
    |x == 0 = False
    |x == 1 = False
    |otherwise = aux 2
        where 
            aux d
                | d >= x = True
                | otherwise = (not ((mod x d) == 0) && (aux (d+1)))

slowFib :: Int -> Int 
slowFib n 
    | n == 0 = 0
    | n == 1 = 1
    | otherwise = slowFib (n-1) + slowFib (n-2)

quickFib :: Int -> Int
quickFib n = snd (fib n)
    where 
        fib 0 = (0,0)
        fib 1 = (0,1)
        fib i = (f1, f1+f2)
            where
                (f2,f1) = fib (i-1)