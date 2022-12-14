#Script para enviar ficheiro local para servidor FTP

import ftplib

#Inserir IP de servidor FTP
ftp = ftplib.FTP("")

#Inserir credênciais de Login do servidor FTP
ftp.login("user", "password")

#Selecionar ficheiro local
localfile=''
remotefile=''
with open(localfile, "rb") as file:
    ftp.storbinary('STOR %s' % remotefile, file)



