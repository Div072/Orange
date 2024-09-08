# Orange
On current phase language interpreter can successfully evaluate arithmetic operations  

### Our CFG grammar looks like this currently ###
>term -> factor(("+" || "-")factor)*  
> factor -> unary(("*" || "/")unary)*  
> unary -> ("!" || "-")*unary || primary  
> primary -> NUMBER || STRING || IDENTIFIERS

### Supported Expression ###
> Currently Orange language only supports basic arithmetic operations 
> -23+2*2 = -19