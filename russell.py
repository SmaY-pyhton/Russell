import colorama
from colorama import *
import socket
import os
import sys
import webbrowser

sock = socket.socket()
os.system ("cls")
os.system ("color f0")
opt1 = "Escaner de Puertos"
opt2 = "Escaner de Subdominios"
opt3 = "ForceOP"
opt4 = "Conseguir IP"
opt5 = "Rango de IP"
opt6 = "Lista de Servers"
opt7 = "Nmap tracker"
opt8 = "Ayudante de Comandos"
opt9 = "Cambiar a Ingles"
opt10 = "Salir"
opt11 = "Escaneando... Esto puede llevar un rato..."
opt12 = "Pon la IP Aqui >> "
opt13 = "Escanear Rango Corto"
opt14 = "Escanear Rango Medio"
opt15 = "Escanear Rango Grande"
opt16 = "Setea Tu Opcion"




userlogin = input (Fore.RED+"Porfavor pon tu "+Fore.BLACK+"usuario : "+Fore.YELLOW+"")
if userlogin == "smay":
	password = input (Fore.RED+"Porfavor pon tu "+Fore.BLACK+"contraseña : "+Fore.YELLOW+"")
	if password == "god":


		while True:
			input()
			os.system ("cls")
			print ()
			print (Fore.RED+"***"+Fore.RED+"**********************************"+Fore.CYAN+"           S")
			print (Fore.RED+"***"+Fore.BLUE+"  Hola "+Fore.YELLOW+""+(userlogin)+"                    "+Fore.RED+"***"+Fore.CYAN+"           M")
			print (Fore.RED+"***"+Fore.GREEN+"  Setea tu opcion              "+Fore.RED+"***"+Fore.CYAN+"           A")
			print (Fore.RED+"***"+Fore.RED+"**********************************"+Fore.CYAN+"           Y")
			print (Fore.RED+"***"+Fore.BLUE+"  1) "+(opt1)+"        "+Fore.RED+"***")
			print (Fore.RED+"***"+Fore.BLUE+"  2) "+(opt2)+"    "+Fore.RED+"***"+Fore.CYAN+"           T")
			print (Fore.RED+"***"+Fore.BLUE+"  3) "+(opt3)+"                   "+Fore.RED+"***"+Fore.CYAN+"           O")
			print (Fore.RED+"***"+Fore.BLUE+"  4) "+(opt4)+"              "+Fore.RED+"***"+Fore.CYAN+"           O")
			print (Fore.RED+"***"+Fore.BLUE+"  5) "+(opt5)+"               "+Fore.RED+"***"+Fore.CYAN+"           L")
			print (Fore.RED+"***"+Fore.BLUE+"  6) "+(opt6)+"          "+Fore.RED+"***")
			print (Fore.RED+"***"+Fore.BLUE+"  7) "+(opt7)+"              "+Fore.RED+"***")
			print (Fore.RED+"***"+Fore.BLUE+"  8) "+(opt8)+"      "+Fore.RED+"***")
			print (Fore.RED+"***"+Fore.BLUE+"  9) "+(opt9)+"          "+Fore.RED+"***")
			print (Fore.RED+"***"+Fore.BLUE+"  10) "+(opt10)+"                    "+Fore.RED+"***")
			print (Fore.RED+"***"+Fore.RED+"**********************************")
			x = input (Fore.BLACK+""+(opt16)+" [1/10] >> "+Fore.RED+"")
			
			
			if x == "10":
				exit()
			elif x == "1":
				ipvic = input (Fore.RED+""+opt12+""+Fore.GREEN+"")
				print (Fore.YELLOW+"1) "+opt13+" '1-80' ")
				print (Fore.YELLOW+"2) "+opt14+" '25500-25600' ")
				print (Fore.YELLOW+"3) "+opt15+" '65500-65535' ")
				ranz = input (Fore.RED+"Selecciona tu opcion de escaneo >> "+Fore.GREEN+"")
				if ranz == "1":
					rka = range(1,80)        
				elif ranz == "2":
					rka = range(25500,35000) 
				elif ranz == "3":
					rka = range(65530,65535) 
				print (opt11)
				for puertos in (rka):
					try:
						socka = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
						resultadofinal = socka.connect_ex((ipvic, puertos))
						if resultadofinal == 0:
							print (Fore.BLUE+str(ipvic)+":"+str(puertos))
						socka.close()
					except:
						pass
			elif x == "3":
				subdomains = ["build", "play"]
				victima = input (Fore.RED+""+(opt12)+""+Fore.GREEN+"")
				print (opt11)
				for ejecutar in subdomains:
					try:
						hosts = str(ejecutar) + "." + str(victima)
						iphost = socket.gethostbyname(str(hosts))
						try:
							for port in range(25560,25575):
								sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
								result = sock.connect_ex((iphost, port))
								if result == 0:
									print (Fore.BLUE+str(iphost)+":"+str(port))
								sock.close()
						except:
							pass
					except:
						pass
			elif x == "2":
				os.system ("cls")     
				subdomains0 = ["www", "build", "web", "dev", "staff", "mc", "play", "sys", "node1", "node2", "node3", "builder", "developer", "test", "test1", "forum", "bans", "baneos", "ts", "ts3", "sys1", "sys2", "mods", "bungee", "bungeecord", "array", "spawn", "server", "help", "client", "api", "smtp", "s1", "s2", "s3", "s4", "server1", "server2", "jugar", "test", "mysql", "phpmyadmin", "demo", "na", "eu", "us", "es", "fr", "it", "ru", "support", "developing", "discord", "backup", "buy", "buycraft", "go", "dedicado1", "dedi", "dedi1", "dedi2", "dedi3", "minecraft", "prueba", "pruebas", "ping", "register", "cdn", "stats", "store", "serie", "buildteam", "info", "host", "jogar", "proxy", "vps", "ovh", "partner", "partners", "appeals", "appeal", "store-assets", "BungStore"]
				victima0 = input (opt12+""+Fore.GREEN+"")
				for ejecutar0 in subdomains0:
					try:
						ipserver0 = str(ejecutar0)+"."+str(victima0)
						iphost0 = socket.gethostbyname(str(ipserver0))
						print (Fore.MAGENTA+"SmayTool>> "+Fore.CYAN+""+str(ejecutar0)+"."+str(victima0)+" >> "+Fore.BLACK+""+str(iphost0))
					except:
						pass
			elif x == "4":
				os.system ("cls")
				asd = input (Fore.RED+""+(opt12)+Fore.GREEN+"")
				dsa = socket.gethostbyname(str(asd))
				print (Fore.BLUE+(dsa))
			elif x == "7":
				os.system ("cls")
				print (Fore.RED+""+opt12)
				a = input (Fore.YELLOW+"Set your first IP [1/4] (127) >> ")
				b = input (Fore.YELLOW+"Set your first IP [2/4] (0) >> ")
				c = input (Fore.YELLOW+"Set your first IP [3/4] (0) >> ")
				x = input (Fore.YELLOW+"Set your first IP [4/4] (1) >> ")
				y = int(1)
				z = int(x) - int(y)
				r = int(x) + int(y)
				ipresul = str(a)+"."+str(b)+"."+str(c)+"."+str(z)+"-"+str(r)
				print (Fore.MAGENTA+"")
				os.system ("nmap -p 1-12,1000-1010,20000-20005,25500-25600,28010-28015,30000-30005,40000-40010,65500-65535 -T5 -v -A -Pn "+ipresul)
			elif x == "5":
				from socket import *
				open_ports = []
				stty = input (opt12+""+Fore.GREEN+"")
				print (Fore.MAGENTA+""+opt11)
				for la in range(0, 255):
					try:
						rangeIP = stty+str(la)
						socky = socket(AF_INET, SOCK_STREAM)
						resulta3 = socky.connect_ex((rangeIP, 25565))
						if resulta3 == 0:
							open_ports.append(str(rangeIP)+":25565")
						socky.close()
					except KeyboardInterrupt:
						pass
				for resulta4 in open_ports:
					print (Fore.BLUE+(resulta4))
			elif x == "9":    
				opt1 = "Port Scanner      "
				opt2 = "Subdomain Scanner     "
				opt3 = "ForceOP"
				opt4 = "Get IP      "
				opt5 = "IP Range   "
				opt6 = "Server List     "
				opt7 = "Nmap tracker"
				opt8 = "Command Helper      "
				opt9 = "Restart         "
				opt10 = "Exit "
				opt11 = "Scaning... This may take a while..."
				opt12 = "Put Your IP Here >> "
				opt13 = "Scan Short Range"
				opt14 = "Scan Medium Range"
				opt15 = "Scan Long Range"
				opt16 = "Set Your Option"
				opt17 = "Music "
				
			elif x == "6":
				from random import seed
				from random import randint
				for _ in range(1):
					value = randint(1, 150)
				if value == 1:
					print ("hub.mcs.gg")
				if value == 2:
					print ("play.becto.net")
				if value == 3:
					print ("PLAY.ROYALLEGACY.NET")
				if value == 4:
					print ("pvp.desteria.com")
				if value == 5:
					print ("play.manacube.net")
				if value == 6:
					print ("play.extremecraft.net")
				if value == 7:
					print ("mc-central.net")
				if value == 8:
					print ("pixel.mc-complex.com")
				if value == 9:
					print ("mineheroes.net")
				if value == 10:
					print ("mc.snapcraft.net")
				if value == 11:
					print ("MC.Performium.net")
				if value == 12:
					print ("play.applecraft.org")
				if value == 13:
					print ("play.jartexnetwork.com")
				if value == 14:
					print ("play.thedestinymc.com")
				if value == 15:
					print ("play.vexedmc.com")
				if value == 16:
					print ("earthmc.net")
				if value == 17:
					print ("play.pixelmonrealms.com")
				if value == 18:
					print ("mc-gtm.net")
				if value == 19:
					print ("FadeCloud.com")
				if value == 20:
					print ("FadeCloud.com")
				if value == 21:
					print ("pvp.desteria.com")
				if value == 22:
					print ("pixel.rc-gamers.com")
				if value == 23:
					print ("eu.sonoyuncu.network")
				if value == 24:
					print ("PlayPokeNinjas.com")
				if value == 25:
					print ("DIRTCRAFT.GG")
				if value == 26:
					print ("jogar.gearfriends.net")
				if value == 27:
					print ("play.strongcraft.org")
				if value == 28:
					print ("play.pika-network.net")
				if value == 29:
					print ("mc.ecuacraft.com")
				if value == 30:
					print ("play.ggmc.me")
				if value == 31:
					print ("play.castiamc.com")
				if value == 32:
					print ("play.projectwonder.net")
				if value == 33:
					print ("play.mineville.org")
				if value == 34:
					print ("pixel.mc-blaze.com")
				if value == 35:
					print ("play.MuxMC.net")
				if value == 36:
					print ("jogar.rocketmc.com.br")
				if value == 37:
					print ("play.omegacraft.cl")
				if value == 38:
					print ("oyna.provanas.com")
				if value == 39:
					print ("play.uniocraft.com")
				if value == 40:
					print ("mineverse.com")
				if value == 41:
					print ("mc.minebox.es")
				if value == 42:
					print ("mc.ventureland.net")
				if value == 43:
					print ("Pokecentral.org")
				if value == 44:
					print ("play.azertumc.com")
				if value == 45:
					print ("mc.momentonetwork.net")
				if value == 46:
					print ("play.wildercraft.net")
				if value == 47:
					print ("play.mc-complex.com")
				if value == 48:
					print ("Play.Betacraft.Org")
				if value == 49:
					print ("play.wheelcraft-id.net")
				if value == 50:
					print ("smp.hometownmc.com")
				if value == 51:
					print ("mc.safesurvival.net")
				if value == 52:
					print ("play.cultivatemc.com")
				if value == 53:
					print ("play.alttd.com")
				if value == 54:
					print ("play.limitlessmc.net")
				if value == 55:
					print ("mc.clubobsidian.com")
				if value == 56:
					print ("play.pokeverse.org")
				if value == 57:
					print ("play.bulbacraft.com")
				if value == 58:
					print ("Play.Minecraft-Romania.Ro")
				if value == 59:
					print ("fun.multyplay.ro")
				if value == 60:
					print ("miningdead.com")
				if value == 61:
					print ("play.primemc.org")
				if value == 62:
					print ("jogar.luthcraft.com")
				if value == 63:
					print ("minelife.dk")
				if value == 64:
					print ("play.pokemayhem.com")
				if value == 65:
					print ("play.skyblocknetwork.com")
				if value == 66:
					print ("mc.PokeSmash.co")
				if value == 67:
					print ("play.ajgaming.net")
				if value == 68:
					print ("play.guildcraft.org")
				if value == 69:
					print ("mc.soulplex.net")
				if value == 70:
					print ("play.mineway.org")
				if value == 71:
					print ("mc.playdreamcraft.com.br")
				if value == 72:
					print ("mc.myftb.de")
				if value == 73:
					print ("mc.akarcraft.es")
				if value == 74:
					print ("jogar.pokelandia.com")
				if value == 75:
					print ("arefy.net")
				if value == 76:
					print ("mcm.datblock.com")
				if value == 77:
					print ("play.apeironmc.com")
				if value == 78:
					print ("mc.kingnw.com")
				if value == 79:
					print ("play.battleasya.com")
				if value == 80:
					print ("play.onlymc.net")
				if value == 81:
					print ("servicraft.org")
				if value == 82:
					print ("DBC.ApolloNetworkMC.net")
				if value == 83:
					print ("play.primemc.org")
				if value == 84:
					print ("mc.megaplanet.net")
				if value == 85:
					print ("play.skyblocknetwork.com")
				if value == 86:
					print ("mc.PokeSmash.co")
				if value == 87:
					print ("mc.akarcraft.es")
				if value == 88:
					print ("play.PrismForge.com")
				if value == 89:
					print ("mc.survival.pw")
				if value == 90:
					print ("play.potterworldmc.com")
				if value == 91:
					print ("play.journeygaming.com")
				if value == 92:
					print ("pixel.un-linked.com")
				if value == 93:
					print ("mc.kriptonpvp.com")
				if value == 94:
					print ("play.peacefulfarms.net")
				if value == 95:
					print ("tekkit.mc-complex.com")
				if value == 96:
					print ("mcmp.AspiriaMc.com")
				if value == 97:
					print ("play.breachpvp.com")
				if value == 98:
					print ("Pixelmon.HappyCloudMC.com")
				if value == 99:
					print ("play.minewonderland.net")
				if value == 100:
					print ("my.mineland.net")
				if value == 101:
					print ("mc.kgb-minecraft.info")
				if value == 102:
					print ("play.pokedash.org")
				if value == 103:
					print ("Play.DipCraft.Ro")
				if value == 151:
					print ("play.breakdowncraft.com")
				if value == 104:
					print ("play.pixelmonadventures.com")
				if value == 105:
					print ("play.mineswift.net")
				if value == 105:
					print ("omegarealm.com")
				if value == 106:
					print ("play.skybattle.net")
				if value == 106:
					print ("mc.ultranetwork.me")
				if value == 107:
					print ("jogar.craftsgp.net")
				if value == 108:
					print ("geoblock.es")
				if value == 109:
					print ("play.pixelmonharmony.com")
				if value == 110:
					print ("play.xenolithnetwork.com")
				if value == 111:
					print ("play.conspiracycraft.net")
				if value == 112:
					print ("play.creativefun.net")
				if value == 113:
					print ("play.phanaticmc.com")
				if value == 114:
					print ("tinetwork.net")
				if value == 115:
					print ("play.decimatepvp.com")
				if value == 116:
					print ("play.YomNetwork.ca")
				if value == 117:
					print ("play.silkycraft.net")
				if value == 118:
					print ("play.nytro.network")
				if value == 119:
					print ("mc.aminearserver.es")
				if value == 120:
					print ("play.lunarrisingmc.com")
				if value == 121:
					print ("InfinityCubedMC.com")
				if value == 122:
					print ("play.minelink.net")
				if value == 123:
					print ("SB-Central.com")
				if value == 124:
					print ("play.voidrealms.net")
				if value == 125:
					print ("play.ickcraft.nl")
				if value == 126:
					print ("play.hallowedfantasy.com")
				if value == 127:
					print ("mc.lotc.co")
				if value == 128:
					print ("play.poke-brawl.com")
				if value == 129:
					print ("play.feroxmc.net")
				if value == 130:
					print ("mc.pvpbulgaria.eu")
				if value == 131:
					print ("jogar.backmc.com.br")
				if value == 132:
					print ("play-pokecraft.com")
				if value == 133:
					print ("play.eminentmc.com")
				if value == 134:
					print ("play.dawnhaven.net")
				if value == 135:
					print ("massivecraft.com")
				if value == 136:
					print ("mc.divictusgaming.com")
				if value == 137:
					print ("play.acornmc.org")
				if value == 138:
					print ("vnlla.net")
				if value == 139:
					print ("play.shadownode.ca")
				if value == 140:
					print ("mc.calderaminecraft.com")
				if value == 141:
					print ("play.ghiblicraft.com")
				if value == 142:
					print ("diamond.voxmc.com")
				if value == 143:
					print ("server.proyecto40.es")
				if value == 144:
					print ("play.cursedcraft.com")
				if value == 145:
					print ("play.harvestmc.net")
				if value == 146:
					print ("play.harvestmc.net")
				if value == 147:
					print ("DangCap.Ga")
				if value == 148:
					print ("twerion.net")
				if value == 149:
					print ("play.poke-saga.com")
				if value == 150:
					print ("mc.feargames.it")
			elif x == "8":
				os.system ("cls")
				print (Fore.RED+" 1) Spam Commands ")
				print (Fore.RED+" 2) Destruction Commands ")
				print (Fore.RED+" 3) Troll Commands ")
				print (Fore.RED+" 4) AutoOP Commands ")
				print (Fore.RED+" 5) Permission PL  ")
				pregun = input (Fore.GREEN+"Setea tu opcion >> "+Fore.BLUE+"")
				os.system ("cls")
				if pregun == "1":
					esset = input (Fore.GREEN+"El Server tiene essentials? [YES/NO] >>>> "+Fore.BLUE+"")
					if esset == "NO":
						execut3 = "/minecraft:say"
					elif esset == "YES":
						execut3 = "/ept ebc"
					else:
						print ("error :/")
					essen1 = input (Fore.GREEN+"Is a Spanish Server? [YES/NO] >>> "+Fore.BLUE+"")
					if essen1 == "YES":
						print (Fore.RED+"1) Spam YT/TG  ")
						print (Fore.RED+"2) Usuario / Squad Spam")
						print (Fore.RED+"3) User + Squad + YT/TG")
						prag = input (Fore.GREEN+"Setea tu Opcion >> "+Fore.BLUE+"")
						os.system ("cls")
						if prag == "1":
							ytchan = input (Fore.GREEN+"Pon la URL >>>  "+Fore.BLUE+"")
							os.system ("cls")
							print (Fore.MAGENTA+(execut3)+" &5El Server Esta Siendo &4&lHACKEADO &6por "+(ytchan)+" &2Suscribanse para tener &aOP!!")
						if prag == "2":
							user1 = input (Fore.GREEN+"Pon tu Username >>>  "+Fore.BLUE+"")
							os.system ("cls")
							print (Fore.MAGENTA+(execut3)+" &4&kasdf &dServidor &6Grifeado &bPor: &9&l"+(user1))
						if prag == "3":
							chan2 = input ("Pon tu YT Channel >>>  ")
							sqad2 = input ("Pon tu Squad Name >>>  ")
							os.system ("cls")
							print (Fore.MAGENTA+(execut3)+" &aServer Atacado por &4"+(sqad2)+" &6Suscribete a &2"+(chan2))
					
					if essen1 == "NO":
						print (Fore.RED+"1) YT/TG Channel Spam ")
						print (Fore.RED+"2) User /// Squad Spam")
						print (Fore.RED+"3) User + Squad + YT/TG")
						prag = input (Fore.GREEN+"Put Your Option >> "+Fore.BLUE+"")
						os.system ("cls")
						if prag == "1":
							ytchan = input (Fore.GREEN+"Put The URL >>> "+Fore.BLUE+"")
							os.system ("cls")
							print (Fore.MAGENTA+(execut3)+" &5The Server have been by &4&lHACKED "+(ytchan)+" &2Suscribe for get &aOP!!")
						if prag == "2":
							user1 = input (Fore.GREEN+"Put The Username >>> "+Fore.BLUE+"")
							os.system ("cls")
							print (Fore.MAGENTA+(execut3)+" &4&kasdf &dServer &6Griefed &bBy: &9&l"+(user1))
						if prag == "3":
							chan2 = input (Fore.GREEN+"Put The YT Channel >>> "+Fore.BLUE+"")
							sqad2 = input (Fore.GREEN+"Put The Squad Name >>>  "+Fore.BLUE+"")
							os.system ("cls")
							print (Fore.MAGENTA+(execut3)+" &aThe Server have been attacked &4"+(sqad2)+" &Suscribe to &2"+(chan2))
					
				elif pregun == "2":
					pregwe = input (Fore.GREEN+"Have The Server World Edit Plugin??? [YES/NO] >>>  "+Fore.BLUE+"")
					if pregwe == "YES":
						preges = input (Fore.GREEN+"Have The Server Essentials Plugin??? [YES/NO] >>> "+Fore.BLUE+"")
						if preges == "YES":
							os.system ("cls")
							print (Fore.MAGENTA+"/ept /sphere 0 10")
							print (Fore.MAGENTA+"/ept /cyl lava 5")
						if preges == "NO":
							os.system ("cls")
							print (Fore.MAGENTA+"/br sphere 0 5")
							print (Fore.MAGENTA+"/sp area 5")
					if pregwe == "NO":
						os.system ("cls")
						print (Fore.MAGENTA+"/fill ~-10 ~-2 ~-10 ~10 ~2 ~10 air")
						print (Fore.MAGENTA+"/fill ~-5 ~-5 ~-5 ~5 ~5 ~5 lava")
						print (Fore.MAGENTA+"/minecraft:summon PrimedTnt")
						
				elif pregun == "3":
					os.system ("cls")
					print (Fore.MAGENTA+"/effect 1 255 255")
					print (Fore.MAGENTA+"/minecraft:tp @a @p")
					print (Fore.MAGENTA+"/fill ~0 ~30 ~0 ~0 ~30 ~0 anvil")
					
				elif pregun == "4":
					pregop = input (Fore.GREEN+"El servidor tiene el plugin [YES/NO] >>> "+Fore.BLUE+"")
					if pregop == "YES":
						os.system ("cls")
						print (Fore.MAGENTA+"/epowertool minecraft:op [USER]")
					if pregop == "NO":
						os.system ("cls")
						print (Fore.MAGENTA+"/minecraft:execute 0 0 0 @p minecraft:op @p")

				elif pregun == "5":
					os.system ("cls")
					usrknow = input (Fore.GREEN+"Pon tu nick >>>  "+Fore.BLUE+"")
					os.system ("cls")
					print (Fore.MAGENTA+"1) PermissionEx ")
					print (Fore.MAGENTA+"2) LuckyPerms ")
					print (Fore.MAGENTA+"3) PowerFulPerms ")
					print (Fore.MAGENTA+"4) UltraPermissions ")
					print (Fore.MAGENTA+"5) GroupManager ")
					print (Fore.MAGENTA+"6) zPermissions  ")
					print (Fore.MAGENTA+"7) Sin plugins ")
					print ()
					pregperms = input (Fore.GREEN+"Set Your Option [1-7] >>>  "+Fore.BLUE+"")
					if pregperms == "1":
						os.system ("cls")
						print (Fore.MAGENTA+"/pex user "+(usrknow)+" add *")
					elif pregperms == "2":
						os.system ("cls")
						print (Fore.MAGENTA+"/lp user "+(usrknow)+" set *")
					elif pregperms == "3":
						os.system ("cls")
						print (Fore.MAGENTA+"/pp "+(usrknow)+" add *")
					elif pregperms == "4":
						os.system ("cls")
						print (Fore.MAGENTA+"/ups addpermission "+(usrknow)+" *")
					elif pregperms == "5":
						os.system ("cls")
						print (Fore.MAGENTA+"/manuaddp "+(usrknow)+" *")
					elif pregperms == "6":
						os.system ("cls")
						print (Fore.MAGENTA+"/permissions player "+(usrknow)+" set *")
					elif pregperms == "7":
						os.system ("cls")
						print (Fore.MAGENTA+"/minecraft:op "+(usrknow))
					else:
						os.system ("cls")
						print ("Opcion sin respuesta")
else:
	exit()


    ##################################
	#								 #
	# LoveRussel                     #
	# Terminated At 08/09/2020 18:08 #
	#                                #
	##################################