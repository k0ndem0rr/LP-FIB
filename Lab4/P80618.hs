data Queue a = Queue [a] [a]
    deriving (Show)
 
create :: Queue a
create = Queue [] []

push :: a -> Queue a -> Queue a
push x (Queue front back) = Queue front (x:back)  

pop :: Queue a -> Queue a
pop (Queue [] back) =  pop (Queue (reverse back) [])
pop (Queue (x:xs) back) = Queue xs back

top :: Queue a -> a
top (Queue [] back) = last back
top (Queue front _) = head front

empty :: Queue a -> Bool
empty (Queue [] []) = True
empty q = False

instance Eq a => Eq (Queue a)
     where
        (Queue a1 b1) == (Queue a2 b2) = (a1++(reverse b1) == (a2 ++ (reverse b2)))

