
#Listar os ficheiros remotos no servidor FTP

import ftplib

#Inserir IP de servidor FTP
ftp = ftplib.FTP("")

#Inserir credênciais de Login do servidor FTP
ftp.login("user", "password")

print("Diretoria: {}".format(ftp.pwd()))
ftp.retrlines("LIST")
ftp.quit()
