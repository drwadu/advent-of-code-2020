main :: IO ()
main = do
   input <- lines <$> readFile "../input.txt"
   let xs = map read input :: [Int]
   print $ head [x*x'*x'' | x<-xs, x'<-xs, x''<-xs, x+x'+x''==2020] 