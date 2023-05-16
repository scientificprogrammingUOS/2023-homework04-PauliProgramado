import numpy as np 

# implement your function to combine two numpy arrays 

def combination(arr1, arr2, a=0):
    arr1=np.squeeze(arr1)
    arr2=np.squeeze(arr2)
    if arr1.ndim==arr2.ndim:
        con = np.concatenate((arr1, arr2), axis=a)
        return con
    else:
        return("Combination not possible, check dimentions pls")


if __name__ == "__main__":
    # use this for your own testing!

    pass
