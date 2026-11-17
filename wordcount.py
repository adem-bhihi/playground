import sys
if len(sys.argv)==2:
    n=sys.argv[1]
    try:
        with open(n) as x:
            a=x.read()
            lines=len(a.splitlines())
            words=len(a.split())
            crt=len(a)
        print("lines=",lines)
        print("caracters=",crt)
        print("words=",words)
    except FileNotFoundError:
        print("fichier pas trouvé")
else:
    print("UTILISATION ............")
