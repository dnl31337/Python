#################################################################
# crack2.py - Ferramenta automatizada para crackear /etc/shadow #
#                  danielcrvg@hotmail.com - 2014                #
#								#
#  Ferramenta com fins didaticos para auditoria do arquivo de   #
# senhas do sistemas linux, atraves do teste de forca bruta por #
# meio de dicionario ou wordlist. Feito em python 2.7.3		#
#								#
#  Qualquer duvida, critica ou sugestao: danielcrvg@hotmail.com #
#								#
#	     Espero que gostem, 1 abraco, daniel		#
#################################################################

import sys
import crypt
import os
import commands

def banner():
	os.system('clear')
	print '\n'+'*'*60
	print ' '*3+'GNU/Linux /etc/shadow Cr4ck3r - danielcrvg@hotmail.com'
	print '*'*60+'\n'

def uso():	
	print '\n'+'#'*22+' MODO DE USAR '+'#'*22
	print '# Unix-like /etc/shadow Cr4ck3r - danielcrvg@hotmail.com #'
	print '# $ python crack2.py <path_to_shadow> <path_word_list>   #'
	print '#    ! Leia o arquivo README para maiores detalhes !     #'
	print '#'*58+'\n'
	
def checarSenha(hashSenha, arqwlist):
	x = hashSenha.split('$')[1:3]
	salt = '$'+x[0]+'$'+x[1]
	wordList = open(arqwlist,'r')
	for senha in wordList.readlines():
		senha = senha.strip('\n')
		senhaCrip = crypt.crypt(senha,salt)
		if (senhaCrip == hashSenha):
			print '[+] Senha encontrada na wordlist: '+senha+'\n'
			return
	print '[-] Senha nao encontrada na wordlist \n'
		
def main():
	if len (sys.argv) != 3 :	
		uso()
		sys.exit(0)
	else:
		banner()
		arqwlist = sys.argv[2]
		try:
			arqShw = open(sys.argv[1])
			for linha in arqShw.readlines():
				if "$" in linha:
					user = linha.split(':')[0]
					hashSenha = linha.split(':')[1]
					print '[*] Crackeando senha para usuario: '+user
					checarSenha(hashSenha, arqwlist)
		except Exception, e:
			print '\n# Favor verificar a permissao OU caminho para o arquivo #'
			print e
			print '\n'
			uso()

if __name__ == '__main__':
	main()
