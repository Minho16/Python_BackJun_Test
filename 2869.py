A,B,V = map(int,input().split())

day = (((V-A)/(A-B))+1)
day = int(-(-day //1))

print(day)