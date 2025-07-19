
(define (filter-lst f lst)
  (cond
    ((null? lst) '()) 
    ((f (car lst))    
     (cons (car lst) (filter-lst f (cdr lst)))) 
    (else
     (filter-lst f (cdr lst))))) 
 
(define (flatten lst)
  (cond
    ((null? lst) lst)
    ((list? (car lst)) (append (flatten (car lst)) (flatten (cdr lst))))
    (else (cons (car lst) (flatten (cdr lst))))))


(define (ignore a)
  (define (ignorer b) 
      
      (not (= a b))
      )
    ignorer
)
(define (remove item lst)
    (define ignoredValue (ignore item))
    (filter-lst ignoredValue (flatten lst)) 
    
)

;;; Tests
(remove 3 nil)
; expect ()
(remove 3 '(1 3 5))
; expect (1 5)
(remove 5 '(5 3 5 5 1 4 5 4))
; expect (3 1 4 4)
