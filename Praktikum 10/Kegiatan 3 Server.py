import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("", 50002))
s.listen(5)
print "Server siap"
perintah =''
a=0
t=0
Tp=0
while perintah != 'keluar':
    komm, addr = s.accept()
    while perintah != 'keluar':
        item = komm.recv(1024).lower().split("=")
        perintah = item [0]
        if perintah == 'keluar':
            komm.send('done')
            s.close()
            break
        print "pesan:",perintah
        if len(item)==2:
            if perintah =='alas':
                a=int(item[1])
                komm.send('alas disimpan')
            elif perintah =='tinggi':
                t=int(item[1])
                komm.send('tinggi disimpan')
            elif perintah =='tinggi prisma ':
                Tp=int(item[1])
                komm.send('tinggi prisma disimpan')
            else:
                komm.send('Pesan tidak diketahui')
        elif perintah == 'hitung':
            L=float((1/2*a*t)*Tp)
            response ='Luas Prisma dengan alas {} tinggi {} dan Tinggi prisma {} adalah {}'.format(a,t,Tp,L)
            komm.send(response)
        else:
            komm.send('Pesan tidak diketahui')
