def front_ok(front):
    year=int(front[:2])
    month=int(front[2:4])
    day=int(front[4:])

    
    #윤년인 경우
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        if month==2:
            #윤년에 2월
            if 1<=day and day<=29:
                return True
            else :
                return False
        elif month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12:
            if 1<=day and day<=31:
                return True
            else:
                return False
        elif month==4 or month==6 or month==9 or month==11:
            if 1<=day and day<=30:
                return True
            else:
                False
        else :
            return False
        
    #평년인 경우
    else :
        if month==2:
            #평년에 2월
            if 1<=day and day<=28:
                return True
            else:
                return False
        elif month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12:
            if  1<=day and day<=31:
                return True
            else :
                return False
        elif month==4 or month==6 or month==9 or month==11:
            if 1<=day and day<=30:
                return True
            else :
                return False
        else :
            return False


def check(a,b,c,d,e,f,g,h,i,j,k,l):  
    if 11 - ((2*a+3*b+4*c+5*d+6*e+7*f+8*g+9*h+2*i+3*j+4*k+5*l) % 11)<10:
        return 11 - ((2*a+3*b+4*c+5*d+6*e+7*f+8*g+9*h+2*i+3*j+4*k+5*l) % 11)
    else :
        return 11 - ((2*a+3*b+4*c+5*d+6*e+7*f+8*g+9*h+2*i+3*j+4*k+5*l) % 11) -10

def back_ok(s):
    (front, mid, back) = s.partition("-")
    
    sex=int(back[0])
    town=int(back[1:5])
    turn=int(back[5])
    test=int(back[6])
    
    a=int(front[0])
    b=int(front[1])
    c=int(front[2])
    d=int(front[3])
    e=int(front[4])
    f=int(front[5])
    
    g=int(back[0])
    h=int(back[1])
    i=int(back[2])
    j=int(back[3])
    k=int(back[4])
    l=int(back[5])
    m=int(back[6])

    
    if m==check(a,b,c,d,e,f,g,h,i,j,k,l):
        return True
    else:
        return False
       
def isRRN(s):
    (front, mid, back) = s.partition("-")    
    return front_ok(front) and mid == "-" and back_ok(s)
