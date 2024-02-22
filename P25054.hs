--uncurry (+) (2,3) -> 5 

average :: [Int] -> Float 
average l = uncurry g $ average' l
    where 
        g :: Int -> Int -> Float 
        g x y = (fromIntegral x:: Float) / (fromIntegral y:: Float) 
        average' :: [Int] -> (Int, Int) 
        average' [x] = (x, 1) 
        average' (x:xs) = f x $ average' xs 
            where 
                f :: Int -> (Int, Int) -> (Int, Int)
                f x t = (x + fst t, 1 + snd t)