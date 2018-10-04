import numpy
mat=numpy.full((3,3),"_")
lif=[]
def matrix():
    for x in range(3):
        for i in range(3):
            print(mat[x,i],end=" ")
        print()
    return
matrix()
p1=input(" Select your symbol player 1 ")
p2=input(" Select your symbol player 2 ")
p1l=numpy.array([p1,p1,p1])
p2l=numpy.array([p2,p2,p2])
def game(p):
    c=p
    ar=list(map(int,input().split()))
    if lif==[]:
       mat[ar[0],ar[1]]=p
       lif.append(ar)
    elif ar not in lif:
         mat[ar[0],ar[1]]=p
         lif.append(ar)
    else:
        print("wrong index")
        game(c)
def play():
    while True:
          print("player 1 your turn ",p1)
          game(p1)
          if (mat[0]==p1l).all() or (mat[1]==p1l).all() or (mat[2]==p1l).all() or (mat[:,0]==p1l).all()or (mat[:,1]==p1l).all() or (mat[:,2]==p1l).all() or (mat.diagonal()==p1l).all() or (numpy.diagonal(numpy.fliplr(mat))==p1l).all():
             matrix()
             print("player 1 you won ") 
             break
          if (mat!=numpy.full((3,3),"_")).all():
             matrix()
             print("DRAW")
             break
          matrix()
          print("player 2 your turn ",p2)
          game(p2)
          if (mat[0]==p2l).all() or (mat[1]==p2l).all() or (mat[2]==p2l).all() or (mat[:,0]==p2l).all()or (mat[:,1]==p2l).all() or (mat[:,2]==p2l).all() or (mat.diagonal()==p2l).all() or (numpy.diagonal(numpy.fliplr(mat))==p1l).all():
             matrix()
             print("player2 won")
             break
          if (mat!=numpy.full((3,3),"_")).all():
             matrix()
             print("DRAW")
             break
          matrix()
play()
    
