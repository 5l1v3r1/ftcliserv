#!/usr/bin/env python
#
# Usage: python ftserver.py 1234 
#
import os,os.path,sys,socket
from socket import error as SocketError
if len(sys.argv) < 2:
    sys.stderr.write('Usage: python ftserver.py 1234\n')
    sys.exit(1)
c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
c.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
c.bind(('0.0.0.0', int(sys.argv[1])))
c.listen(5)
print '[*]', 'Listening on 0.0.0.0:'+sys.argv[1],'...'
try:
    while True:
        try:
            s, a = c.accept()
            print
            print '[ ]', 'Connection from', a[0]+':'+str(a[1]), '...'
            s.sendall('h')
            n = s.recv(1024)
            while n.startswith('/'):
                n = n[1:]
            n = 'loot/' + n
            if '..' in n:
                print '[!]', 'Ignoring filename', n
                continue
            if '/' in n:
                dir = os.path.dirname(n)
                try:
                    os.stat(dir)
                except:
                    print '[ ]', 'Creating directory', dir
                    os.makedirs(dir)
            if os.path.exists(n):
                if os.path.isdir(n):
                    print '[!]', 'Destination file is directory, ignoring...'
                    continue
                else:
                    print '[ ]', 'Overwriting file', n
            else:
                print '[ ]', 'Creating file', n
            f = open(n, 'wb')
            while True:
                print '    ',
                s.sendall('b')
                while True:
                    data = s.recv(1024)
                    sys.stdout.write('.')
                    if not data: 
                        break
                    #recvd += data
                    f.write(data)
                    #print len(recvd)
                print
                break
            print '[*]', n, 'received.'
            s.close()
            f.close()
        except SocketError as e:
            pass
except:
    pass
    #import traceback
    #traceback.print_exc()
c.close()
