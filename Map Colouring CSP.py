variables = ['WA','NT','SA','Q','NSW','V','T']
colors = ['r','g','b']
constraints = [
    ('WA','NT'), ('WA','SA'), ('NT','SA'), ('NT','Q'),
    ('SA','Q'), ('SA','NSW'), ('SA','V'), ('Q','NSW'), ('NSW','V')
]
def is_safe(assign, var, color):
    for (v1,v2) in constraints:
        if (var==v1 and assign.get(v2)==color) or (var==v2 and assign.get(v1)==color):
            return False
    return True
def backtrack(assign={}):
    if len(assign) == len(variables):
        return assign
    var = [v for v in variables if v not in assign][0]
    for color in colors:
        if is_safe(assign,var,color):
            assign[var] = color
            result = backtrack(assign)
            if result:
                return result
            assign.pop(var)
    return None
solution = backtrack()
print(solution)
