# Orange
Currently we have done with parsing and generating AST for interpreter
Still some need to include sopport some operators

### Our CFG grammar looks like this currently ###
>term -> factor(("+" || "-")factor)*  
> factor -> unary(("*" || "/")unary)*  
> unary -> ("!" || "-")*unary || primary  
> primary -> NUMBER || STRING || IDENTIFIERS
