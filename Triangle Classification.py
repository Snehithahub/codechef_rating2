import math

def triangle_type(f, g, h):
    # Determine if the triangle is isosceles or scalene
    if (f == g and f != h) or (g == h and g != f) or (f == h and f != g):
        triangle_base = "Isosceles"
    else:
        triangle_base = "Scalene"

    # Sort the sides for easier angle checking
    sides = sorted([f, g, h])
    a, b, c = sides[0], sides[1], sides[2]

    # Use the Pythagorean theorem to classify the angles
    if math.isclose(c**2, a**2 + b**2):
        triangle_angle = "right"
    elif c**2 < a**2 + b**2:
        triangle_angle = "acute"
    else:
        triangle_angle = "obtuse"

    return f"{triangle_base} {triangle_angle} triangle"

# Main function to read input and process triangles
for f in range(int(input())):
    c = int(input())
    for _ in range(c):
        x1, y1, x2, y2, x3, y3 = map(int, input().split())
        f = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)  # Side 1
        g = math.sqrt((x2 - x3) ** 2 + (y2 - y3) ** 2)  # Side 2
        h = math.sqrt((x1 - x3) ** 2 + (y1 - y3) ** 2)  # Side 3
        if f==2:
            print(triangle_type(f, g, h))
        else:
            if (f == g and f != h) or (g == h and g != f) or (f == h and f != g):
                print("Isosceles triangle")
            else:
                print("Scalene triangle")
