(define (substitute s old new)
  (cond
    ((null? s) '()) 
    ((pair? s)      
     (cons (substitute (car s) old new) (substitute (cdr s) old new)))
    ((equal? s old) new) 
    (else s)))           



(define (sub-all s olds news)
  (if (null? olds)
      s
      (sub-all (substitute s (car olds) (car news))
               (cdr olds)
               (cdr news))))



(sub-all `(h e l l o) '(e  l)  '(a p))

