

def linear_search(list,target):

     for i in range(len(list)):
         if list[i]==target:
             return i
         else:
             None

def linear_search_2(list,target):

    for index,value in enumerate(list):
        if value==target:
            return index
        else:
            None


def binary_search(list,target):

    first=0
    last=len(list)-1

    while first<=last:

          midpoint=first+last // 2

          if list[midpoint]==target:
              return midpoint
          elif list[midpoint]<target:
                first=midpoint+1
          else:
                first=midpoint-1
    return -1



mylist=[3,4,5,6,7,8,9]
target=8

binary_search([3,4,5,6,7,8,9],8)