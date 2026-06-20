# Special Pythagorean Triplet

def is_pythagorean_triplet(a,b,c):

    if a ** 2 + b ** 2 == c ** 2:
        return True
    
    else:
        return False
    
for a in range(500):

    for b in range(500):
        
        for c in range(500):

            if a + b + c == 1000:

                if is_pythagorean_triplet(a,b,c):
                    
                    print("Encontrei")
                    print("A:", a)
                    print("B:", b)
                    print("C:", c)
                    print("O produto é", a*b*c)
                    break