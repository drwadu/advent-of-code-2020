(require "asdf")

(defvar *ints*
   (mapcar 'parse-integer (uiop:read-file-lines "../../input.txt")))
(print (reduce '* (remove-if-not (lambda (x)
				   (some (lambda (y) (and (= 2020 (+ x y)) (/= x y))) *ints*))
				 *ints*)))
