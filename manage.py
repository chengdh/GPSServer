#coding=utf-8
import os,sys
command=None
PID=None
if(len(sys.argv)==2):
    ft=''
    f=open('./TCPServer/state.txt')
    try:
        ft=f.read()
    finally:
        f.close()

    command=sys.argv[1]
    if command=='help':
        print(' help \n startserver \n stopserver')
    elif command=='startserver':
        if ft!='start':
            os.chdir('TCPServer/')
            shellCommand ="nohup python setup.py &"
            os.system(shellCommand)
            f=open('state.txt','w')
            try:
                f.write('start')
            finally:
                f.close()
                
        
        else:
            print('server already Running!')
    
        
    elif command=='stopserver': 
        if ft!='stop':
            f=open('./TCPServer/state.txt','w')
            try:
                f.write('stop')
            finally:
                f.close()
        else:
            print('server is stopping!')
   
    else:
        print('command not found')

else:
    print('command not found')
#sys.exit()

