def operation(a, b) -> int:
    if (a == None) or (b == None):
        return None
    return a + b

def calculate(a,b,oper)->int:
    if oper=='+':
        return a+b
    elif oper=='-':
        return a-b
    elif oper=='*':
        return a*b
    elif oper=='/':
        return a/b if b!=0 else 'Divide zero error'