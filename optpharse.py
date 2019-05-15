import optparse

#print dir(optparse)

tghost="10.10.10.10"
tgport=12

par = optparse.OptionParser('usage %prog -H' + '<target host> -P <target port>')

par.add_option('-H', dest='tghost', type='string', help='Enter the target host')

par.add_option('-P', dest='tgport', type='int', help='Enter the port numbers')

(options,args) = par.parse_args()

tghost == options.tghost

tgport == options.tgport

if (tghost==None) | (tgport==None):
    print par.usage
    exit(0)



