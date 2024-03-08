data Tree a = Node a (Tree a) (Tree a) | Empty deriving (Show)

size :: Tree a -> Int
size (Empty) = 0
size (Node a left right) = 1 + (size left) + (size right)