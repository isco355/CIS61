(define (composed f g)
  (lambda (x)
    (f (g x))
    )
)


(define (addN n) (+ n n))
(define (double n) (* n 2))

(composed addN double)


(define f (composed addN double))


(f 2)
