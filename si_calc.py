def principal(interest,rate,time):
    result=interest/rate*time
    return result

def rate(principal,interest,time):
    result=interest/principal*time
    return result

def time(interest,principal,rate):
    result=interest/principal*rate
    return result

def simple_interest(principal,rate,time):
    result=principal*rate*time/100
    return result


f=open('explanations.txt')
print(f.read())