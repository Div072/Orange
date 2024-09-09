# Orange
On current phase language interpreter can successfully evaluate arithmetic operations  

### Our CFG grammar looks like this currently ###
>program -> statements* EOF  
> statements -> Print || Expression  
> Print -> 'print' '(' expression ')'  
> Expression -> expression ';'
>expression ->equality  
>eqality -> comparision(("!=" || "==")comparision)*  
> comparision -> term((">" || "<" || ">=" || "<=" )term)*  
>term -> factor(("+" || "-")factor)*  
> factor -> unary(("*" || "/")unary)*  
> unary -> ("!" || "-")*unary || primary  
> primary -> NUMBER || STRING || IDENTIFIERS || Grouping  
> Grouping -> "("expression")"

### Supported Expression ###
> Currently Orange language only supports basic arithmetic operations 
> (-23*2)<=2 => false