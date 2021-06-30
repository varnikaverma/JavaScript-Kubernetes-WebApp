#!/usr/bin/python3 

print("content-type: text/html")
print()

import cgi 
import subprocess

x=cgi.FieldStorage().getvalue("x")
y=cgi.FieldStorage().getvalue("y")
z=cgi.FieldStorage().getvalue("z")


if x == 'deploy':
    o=subprocess.getoutput("kubectl create deployment {} --image={} --kubeconfig admin.conf".format(y,z))

elif x == 'pod':
    o=subprocess.getoutput("kubectl run {} --image={} --kubeconfig admin.conf".format(y,z))

elif x == 'expose':
    o=subprocess.getoutput("kubectl expose deployment {} --port={} --type=NodePort --kubeconfig admin.conf".format(y,z))

elif x == 'replica':
    o=subprocess.getoutput("kubectl scale deployment {} --replicas={} --kubeconfig admin.conf".format(z,y))

elif x == 'display':
    o=subprocess.getoutput("kubectl get {} --kubeconfig admin.conf".format(y))

elif x == 'delete':
    o=subprocess.getoutput("kubectl delete deployment vvweb --kubeconfig admin.conf")
    #if y == 'deployment' or y == 'pod':
        #o=subprocess.getoutput("kubectl delete {y} {z} --kubeconfig admin.conf".format(y,z))
    #else:
        #o=subprocess.getoutput("kubectl delete all --all --kubeconfig admin.conf")

else:
    c = "{} --kubeconfig admin.conf".format(x)
    o=subprocess.getoutput(c)


print("<pre>")
print(o)
print("</pre>")
