import numpy as np

# implement the function strange pattern

def strange_pattern(tup):
    m = tup[0]
    n = tup[1]
    counter=0
    array = np.full(tup, False)
    for row in range(m):
        if counter == 0:
            line=array[row]
            line[::3] = True
            array[row]=line
            counter+=1
        elif counter == 1:
            line=array[row]
            line[2::3] = True
            array[row]=line
            counter+=1
        else:
            line=array[row]
            line[1::3] = True
            array[row]=line
            counter=0

    return array




if __name__ == "__main__":
    # use this for your own testing!

    pass
