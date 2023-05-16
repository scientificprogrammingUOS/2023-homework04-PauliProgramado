import numpy as np

# implement the function gaussian_analysis

def gaussian_analysis(loc, scale, lower_bound, upper_bound):
    parameters= {loc,scale,lower_bound,upper_bound}
    if all([isinstance(item, int) for item in parameters]) or all([isinstance(item, float) for item in parameters]):
        if lower_bound>=upper_bound:
            raise ValueError("pls make sure lower and upper bound are in order")
        else:
            array=np.random.normal(loc, scale, size=100)
            array=np.array([x for x in array if x<=upper_bound])
            array=np.array([x for x in array if x>=lower_bound])
            mean=np.mean(array)
            std=np.std(array)
            return((mean, std))
        
    else:
        raise ValueError("pls only give me int or float")


if __name__ == "__main__":
    # use this for your own testing!

    pass
