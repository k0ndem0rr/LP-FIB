t7 = Node 7 Empty Empty
t6 = Node 6 Empty Empty
t5 = Node 5 Empty Empty
t4 = Node 4 Empty Empty
t3 = Node 3 t6 t7
t2 = Node 2 t4 t5
t1 = Node 1 t2 t3
t1' = Node 1 t3 t2

   

data Tree a = Node a (Tree a) (Tree a) | Empty deriving (Show)

size :: Tree a -> Int
size (Empty) = 0
size (Node a left right) = 1 + (size left) + (size right)

height :: Tree a -> Int
height (Empty) = 0
height (Node a left right) = 1 + (max (height left) (height right))

equal :: Eq a => Tree a -> Tree a -> Bool
equal (Empty) (Empty) = True
equal (Empty) _ = False
equal _ (Empty) = False
equal (Node x xleft xright) (Node y yleft yright) = ((x == y) && (equal xleft yleft) && (equal xright yright))

isomorphic :: Eq a => Tree a -> Tree a -> Bool
isomorphic (Node x xleft xright) (Node y yleft yright) = 
    ((x == y) && 
     (((equal xleft yleft) && (equal xright yright)) ||
        ((equal xleft yright) && (equal xright yleft))))
isomorphic a b = (equal a b)

preOrder :: Tree a -> [a] 
preOrder Empty = []
preOrder (Node x left right) = [x] ++ (preOrder left) ++ (preOrder right)

postOrder :: Tree a -> [a] 
postOrder Empty = []
postOrder (Node x left right) = (postOrder left) ++ (postOrder right) ++ [x]

inOrder :: Tree a -> [a] 
inOrder Empty = []
inOrder (Node x left right) = (inOrder left) ++ [x] ++ (inOrder right)

breadthFirst :: Tree a -> [a]
breadthFirst t = (breadthFirst' [t])
    where
        breadthFirst' [] = []
        breadthFirst' (Empty:xt) = breadthFirst' xt
        breadthFirst' ((Node x left right):xt) = [x] ++ (breadthFirst' (xt ++ [left] ++ [right]))

build :: Eq a => [a] -> [a] -> Tree a
build x y = justTree (build' (take 0 [x]) [])
    where 
        justTree (a, b, c) = a
        build' :: Eq a => [a] -> [a] -> (Tree a, [a], [a])
        build' [] _ = (Empty, [], [])
        build' (a:at) (b:bt)
            | a == b = (Empty, x, [])
            | otherwise = (Empty , y,x)