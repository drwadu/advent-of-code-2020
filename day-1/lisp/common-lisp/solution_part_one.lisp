(require "asdf")

(defvar ints
  (remove-duplicates
   (mapcar 'parse-integer (uiop:read-file-lines "../../input.txt"))))
(print (reduce '* (remove-if-not (lambda (x)
			    (some (lambda (y) (= 2020 (+ x y))) ints))
			  ints)))

