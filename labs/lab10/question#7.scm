(define (filter-lst f lst)

  (cond
    ((null? lst) '()) 
    ((f (car lst))    
     (cons (car lst) (filter-lst f (cdr lst)))) 
    (else
     (filter-lst f (cdr lst))))) 

(define (ignore a)
  (define (ignorer b) 
      
      (not (= a b))
      )
    ignorer
)

 (define (no-repeats s)
  (if (null? s)
      '()
      (cons (car s)
            (no-repeats (filter (ignore (car s)) (cdr s) )))))


;;; Tests 
(no-repeats (list 5 4 5 4 2 2))
; expect (5 4 2)
