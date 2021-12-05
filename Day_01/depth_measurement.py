
def simple_measurements():
    data = open("depth_measurements.txt", "r")

    incr, decr = 0, 0
    all_measurements = list()

    for measurement in data:
        measurement = int(measurement)
        if len(all_measurements)==0:
            all_measurements.append(measurement)
            continue

        incr += (measurement > all_measurements[-1])
        decr += (measurement < all_measurements[-1])
        print(f"{measurement:04} (increased: {(measurement > all_measurements[-1])}) ") 
        all_measurements.append(measurement)

    print(f"Increments: {incr}")
    print(f"Decrements: {decr}")





def triple_measurements():
    data = open("depth_measurements.txt", "r")

    incr, decr = 0, 0
    all_measurements = list()

    triple = list()

    for m in data:
        m = int(m)
        all_measurements.append(m)

        if len(all_measurements) < 4:
            continue
        
        A = sum(all_measurements[-4:-1])
        B = sum(all_measurements[-3:])

        incr += (B > A)
        decr += (B < A)

        print(f"A={A}, B={B} (increased: {B>A})")




    print(f"Increments: {incr}")
    print(f"Decrements: {decr}")


if __name__ == "__main__":


    triple_measurements()



