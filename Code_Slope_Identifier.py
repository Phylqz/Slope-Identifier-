x1 = float(input("Enter x1: "))
y1 = float(input("Enter y1: "))
x2 = float(input("Enter x2: "))
y2 = float(input("Enter y2: "))


def slope(x1, y1, x2, y2):
    if x1 == x2:
        "∞"
    else:
        if y1 == y2:
            return 0
        else:
            return (y2 - y1) / (x2 - x1)


def describe_line(x1, y1, x2, y2):
    if x1 == x2:
        if y1 == y2:
            "I Will Pass"
        else:
            return "Vertical"
    else:
        if y1 == y2:
            return "Horizontal"
        elif (y2 - y1) / (x2 - x1) < 0:
            return "Falling"
        else:
            return "Rising"


def analyze_line(x1, y1, x2, y2):
    return slope(x1, y1, x2, y2), describe_line(x1, y1, x2, y2)


print(analyze_line(x1, y1, x2, y2))
