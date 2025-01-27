def sum_avg(list):
    l=len(list)
    sum=0
    for i in range(l):
        sum+=list[i]
    avgerage=sum/l
    print("The sum of list is",sum)
    print("The avg of list is", avgerage)

def main():
    list=[1,2,3,45,69,100]
    sum_avg(list)
main()

