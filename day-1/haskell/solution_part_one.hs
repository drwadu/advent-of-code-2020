main :: IO ()
main = do
   input <- lines <$> readFile "../input.txt"
   let xs = map read input :: [Int]
   print $ head [x*y*z | x<-xs, y<-xs, z<-xs, x+y+z==2020] 
