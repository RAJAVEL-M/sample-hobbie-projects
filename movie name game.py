import random


print("movie name guessing game")

movies=['avengers','ironman','batman','dark knight']
details={'avengers':'marvel,super heroes','ironman':'marvel,god of marvel','batman':'dc,Gotham city','dark knight':'dc nolan\'s hit'}

gu=[]
movie=random.choice(movies)
print(details[movie])
l=len(movie)
print("the movie contains",l,"letters including spaces")
print('-'*l)

    
for i in range(4):
    print('\n')
    n=input("enter guess")
    if(n in movie):
        gu.append(n)
        for j in movie:
            if(j in gu):
                print(j,end="")
            else:
                print('-',end="")
        print('\n')
        c=input("can you guess it")
        if(c==movie):
            print("success  you guessed correctly")
            break
        else:
            print("wrong guess. try another one")
            continue
    else:
        print(n,"is not present in this movie name ")
print("the movie name is",movie)
                    
      

