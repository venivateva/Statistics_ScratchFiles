import numpy as np


growth_rate=np.exp(np.diff(np.log([222,333,555,6555]))-1)

#print(growth_rate)


def growth_rate(values):

    for i in range(1,len(values)):
        growth=((values[i]-values[i-1])/values[i-1])*100
    return growth

#print(growth_rate([222,333,555,655]))

# Differences between lists and NumPy Arrays
# An array's size is immutable.  You cannot append, insert or remove elements, like you can with a list.
# All of an array's elements must be of the same [data type]
# A NumPy array behaves in a Pythonic fashion.  You can `len(my_array)` just like you would assume.

GPA=[]
GPA=[4.0,3.8,3.286]
GPA.append(4.0)

gpas_array=np.array(GPA)
#print(gpas_array.size)

study_minutes=np.zeros(100,np.uint16)
study_minutes[0]=150
first_day_minutes=study_minutes[0]
study_minutes[1]=60
second_day_minutes=study_minutes[1]

#adding these values into indeces 2 to 6
study_minutes[2:6]=[80,60,30,90]

#two-dimensional array--matrix

students_gpas=np.array([[4.0,3.8,3.286,3.5],
                        [3.2,3.8,4.0,4.0],
                        [4.0,3.9,4.0,4.0]],np.float16)

orders = np.array([
                [2,0,0,0],
                [4,1,2,2],
                [0,1,0,1],
                [6,0,1,2] ])

totals = np.array([3,20.50,10,14.25])

prices = np.linalg.solve(orders,totals)

first, second=np.split(np.arange(1,11),2)
