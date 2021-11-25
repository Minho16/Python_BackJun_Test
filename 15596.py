def solve(a:list) -> int:
    result = 0
    for x in a:
        result = result + x
    return result


a = [1,2,3,4,5]

resultado = solve(a)
print(resultado)