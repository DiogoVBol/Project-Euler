# Smallest Multiple

divisores = (4,6,8,10,12,14,16,18,20)

for i in range(2520,1000000000, 20):

    if i % 2 == 0:

        if i % 3 == 0:

            if i % 5 == 0:

                if i % 7 == 0:

                    if i % 9 == 0:

                        if i % 13 == 0:

                            if i % 11 == 0:

                                if i % 15 == 0:

                                    if i % 17 == 0:

                                        if i % 19 == 0:

                                            if all(i % d == 0 for d in divisores):

                                                print("Divisível por todos")
                                                print(i)
                                                break