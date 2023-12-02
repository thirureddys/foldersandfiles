import os
folders=[]
files=[]
with open("C:/Python27/body_scanner.py") as fh:
    cl=0
    de=0
    l=fh.readlines()
    for i in range(len(l)): #line in fh.readlines():
        w=l[i].rstrip().split(' ')
        if w[0]=='class':
            print ' '.join(w)
            i=i+1
            
            #print ' '.join(w)
            cl+=1
            for j in range(i,len(l)):
                #print j
                ch=l[j].split(' ')
                #print ch
                #print ch
                if ch[0]=='':
                    if len(ch) > 4 and ch[4]=='def':
                        print ' '.join(ch).rstrip()
                    #pass
                elif ch[0]=='class':
                    #exit
                    break
                #elif ch[0]=='def':
                    #pass
                #    print ' '.join(ch)
                j+=1
                    

            i=i+j
            #exit
            #break

        elif w[0]=='def':
            print ' '.join(w)
            de+=1
            i+=1
            #print i
       # print i
    print cl
    print de
