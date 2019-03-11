The Apriori1.py contains the actual implementation of apriori algorithm..

makepairs() - this is used to make pairs to generate rules
ex [(a,b,c,d)]
then (a->b,c,d),(b->a,c,d),(c->a,b,d),(d->a,b,c) ,((a,b)->(c,d)),,,(taken 2 at a time at LHS)...(a,b,c->d),(b,c,d->a),,,(taken 3 at a time
it will run n-1 times
i.e we have length 4 in our case , so lhs can max be 3 items and 1 items shd be in RHS to form rules

