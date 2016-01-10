import re

def check(email):
    delim = (email.lower()).split("@")
    name = delim[0]
    domen = delim[1]
    quo = '"'
    k = 0
    dot = '..'
    d = name.find(dot)
    for c in name:
        if(c == quo):
            k+=1
    if (re.match(r'(?:[^\-][a-z\d\_\-]+[^\-\Z]\.)+[^\-][a-z\d\_\-]+', domen) and (domen[len(domen)-1:]!= "-") and (len(domen) < 256)) :
        if(re.match(r'([a-z\d"]([-a-z\d"]{1,128}[a-z\d])+\.?)', name) and (k % 2 == 0) and (d < 0) and (len(name) < 128)):
            if(re.search(r'["][\!\,\:]*["]', name) or (k == 0)):
                print(email, '- successfully')
            else:
                print(email, '-mistake')
        else:
            print(email, '-mistake')
    else:
        print(email, '-mistake')
