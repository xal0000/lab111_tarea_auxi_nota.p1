#la contraseña es "torcos" pero cifrado seria "snqbnr" recorremos -1 en el abecedario
# los datos de la contraseña se deve ingresar en minuscula 
import string
alfabeto=list(string.ascii_lowercase)
def cifrado_cesar(alfabeto,n,texto):
    texto_cifrado =""
    for letra in texto:
        if letra in alfabeto:
            indice_actual=alfabeto.index(letra)
            indice_cesar=indice_actual+n
            if (indice_cesar>25):
                indice_cesar-=25
            texto_cifrado += alfabeto[indice_cesar]
        else:
            texto_cifrado += letra
    return texto_cifrado
frase="torcos"                                          
frase_cifrada = cifrado_cesar(alfabeto,-1,frase)
print("esta es la contraseña cifrada>>>>>>          ",frase_cifrada)
contraseña=""
while (contraseña != frase_cifrada):
    print("introdusca la contraseña")
    contraseña=str(input())
print("contraseña correcta")
c5=""
while(c5!=5):
    print("1.division de dos numeros")
    print("2.divisores de un numero ingresado")
    print("3.numeros capicuas")
    print("4.cambio de base")
    print("5.salir")
    c5=int(input("ingrese una opcion"))
    if(c5==1):
        a=int(input("ingrese el numerador para realizar la division: "))
        b=int(input("ingrese el denominador de la division: "))
        cociente=0
        if (b!=0):
            while(b<=a):
                a=a-b
                cociente=cociente+1
            print("el resto es: ",a," , el cociente es:",cociente)
        else:
            print("no se puede realizar la division entre cero finalizo el programa")
    if(c5==2):
        n=int(input("ingrese un numero para verificar los numeros que dividen a ese numero: "))
        cn=n
        for i in range(1,n+1):
            while(i<=cn):
                cn=cn-i
            if(cn==0):
                print(i,"divide a :",n)
            cn=n
    if(c5==3):
        a=int(input("ingrese un numero para verificar numeros capicuas cada 3 digitos: "))
        ca=a;b=10;c2=0;c3=0;cn=1;suma=0;suma2=0;cn1=2;s3=0;s1=0;c9=0;b1=0;c8=0;g1=0;cc=0;capi=0
        while(c2<=ca):
            c1=0
            while(b<=ca):
                ca=ca-b
                c1=c1+1
            if(c3<3):
                suma=suma+ca*10**c3
                c3=c3+1
            c4=c1
            if(c1>0):
                c9=0
                s3=0
                while(c9<=a):
                    s1=0
                    while(b<=c4):
                        c4=c4-b
                        s1=s1+1
                    if(s3<3):
                        suma2=suma2+c4*10**s3
                        s3=s3+1
                    c4=s1
                    c9=c9+1
                cdsuma=suma2
                d=cdsuma
                cc=2
                capi=0
                cccapi=0
                copisuma=0
                f2=2
                while(cccapi<3):
                    g2=0
                    while(b<=d):
                        d=d-b
                        g2=g2+1
                    if(g2>0):
                        capi=capi+d*10**cc
                        cc=cc-1
                    else:
                        capi=capi+d*10**cc
                    d=g2
                    cccapi=cccapi+1
                if(capi==suma2):
                    print(cdsuma,"es capicua")
                suma2=0
            ca=c1
            c2=c2+1
            cn=cn+1
        copisuma=suma
        ccapi=0
        f1=2
        resto=0
        while(ccapi<3):
            g1=0
            while(b<=copisuma):
                copisuma=copisuma-b
                g1=g1+1
            if(g1>0):
                resto=resto+copisuma*10**f1
                f1=f1-1
            else:
                resto=resto+copisuma*10**f1
            copisuma=g1
            ccapi=ccapi+1
            if(suma==resto):
                print(suma,"es capicuaaaaa")
    if(c5==4):
        n=int(input("ingrese un numero en base decimal: "))
        x=int(input("ingrese la base a la que decea llevar el numero: "))
        cn=n
        s=0
        i=0
        c1=0;suma=0
        while(i<=n):
            s=0
            while(x<=cn):
                cn=cn-x
                s=s+1

            if(cn>=0):
                suma=suma+cn*10**c1
                c1=c1+1
            cn=s
            i=i+1
        print(suma)
    print("la operacion finalizo ,ingrese un numero para realizar la operacion")
print("el programa a finalizado")



