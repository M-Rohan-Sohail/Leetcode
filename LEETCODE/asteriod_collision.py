def ac(asteriods):

    result = []
    final_result = []

    for num in asteriods:
        result.append(num)

    for numx in result:

        if len(final_result) == 0:
            final_result.append(numx)

        else:

            top = final_result[-1]

            if numx < 0 and top < 0:
                final_result.append(numx)

            elif top > 0 and numx < 0:

                destroyed = False

                while final_result and final_result[-1] > 0 and numx < 0:

                    if abs(final_result[-1]) < abs(numx):
                        final_result.pop(-1)

                    elif abs(numx) == abs(final_result[-1]):
                        final_result.pop(-1)
                        destroyed = True
                        break

                    else:
                        destroyed = True
                        break

                if not destroyed:
                    final_result.append(numx)

            else:
                final_result.append(numx)

    return final_result

asteroids = [-2,2,1,-2]

print(ac(asteroids))


            