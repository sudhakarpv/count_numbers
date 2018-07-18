# count_numbers
def main():
    pass
    n=input()
    l=list(n)
    o=[]
    for i in l:
     k=i.isdigit()
     if (k==True):
        o.append(i)
    print(len(o))

if __name__ == '__main__':
    main()
