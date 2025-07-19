(define (make-adder num)
  (define (adder rest) 
      (+ rest num))
    adder
)

;;; Tests
(define adder (make-adder 5))
(adder 8) 
; expect 13

