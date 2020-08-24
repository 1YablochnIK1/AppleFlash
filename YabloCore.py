def applerun():
	import os
	import wget
	os.system("Title Apple]~[Flash запущен при помощи YabloCore")
	os.system("cls")
	print(banner)
	i=input("Действие: ")
	os.system("cls")
	if i =="1":
		wget.download("https://github.com/topjohnwu/Magisk/releases/download/v20.4/Magisk-v20.4.zip")
		os.system("adb sideload Magisk-v20.4.zip")
	elif i =="2":
		print(banner6)
		y=input("Раздел: ")
		os.system("fastboot earse " + y)
	elif i =="3":
		h=input("Ведите имя или путь к Zip: ")
		os.system("adb sideload " + h)
	elif i =="4":
		print(banner3)
		y=input("Способ: ")
		if y =="1":
			wget.download("https://github.com/topjohnwu/Magisk/releases/download/v20.4/Magisk-v20.4.zip")
			os.system("adb sideload Magisk-v20.4.zip")
			print("Перезагрузка через 5 секунд...")
			time.sleep(1)
			print("Перезагрузка через 4 секунды...")
			time.sleep(1)
			print("Перезагрузка через 3 секунды...")
			time.sleep(1)
			print("Перезагрузка через 2 секунды...")
			time.sleep(1)
			print("Перезагрузка через 1 секунду...")
			time.sleep(1)
			print("Перезагрузка через 0 секунд...")
			os.system("adb reboot")
			input("При включении устройства и режима ADB Sideload нажмите пробел... ")
			wget.download("https://github.com/RikkaApps/Riru/releases/download/v21.3/magisk-riru-v21.3.zip")
			os.system("adb sidelaod magisk-riru-v21.3.zip")
			wget.download("https://github.com/ElderDrivers/EdXposed/releases/download/v0.4.6.2/EdXposed-SandHook-v0.4.6.2.4529.-release.zip")
			os.system("adb sideload EdXposed-SandHook-v0.4.6.2.4529.-release.zip")
		elif y =="2":
			wget.download("https://github.com/ElderDrivers/EdXposed/releases/download/v0.4.6.2/EdXposed-SandHook-v0.4.6.2.4529.-release.zip")
			os.system("adb sideload EdXposed-SandHook-v0.4.6.2.4529.-release.zip")
	elif i =="5":
		os.system("adb shell")
	elif i =="6":
		os.system("adb root")
		os.system("adb shell su -")
	elif i =="7":
		print(banner5)
		y=input("Раздел: ")
		h=input("Образ раздела: ")
		os.system("fastboot flash " + y + "" + h)
	elif i =="8":
		print(banner7)
		y=input("Перезагружаем в: ")
		print(banner8)
		h=input("Способ: ")
		if h =="2":
			if y =="1":
				os.system("adb reboot")
			elif y =="2":
				os.system("adb reboot to recovery")
			elif y =="3":
				os.system("adb reboot to botloader")
		if h =="1":
			if y =="1":
				os.system("fastboot reboot")
			elif y =="2":
				os.system("fastboot reboot to recovery")
			elif y =="3":
				os.system("fastboot reboot to botloader")
	else:
		pass

banner="""
{======|Главное Меню|======} {===|Apple]~[Flash by BIO_YablochniK|===}
[============================================================================]
[ 1 - Получить Root с помощью Magisk 20.04 {ADB Only}
[ 2 - Форматировать... {FASTBOOT Only}
[ 3 - Прошить Zip... {ADB Only}
[ 4 - Установить Xposed Framework #SandHook# (Зависимости: Magisk 19.0+, Riru - Core v19+) {ADB Only}
[ 5 - Терминал {ADB Only}
[ 6 - Терминал (Root) {ADB Only}
[ 7 - Прошить раздел... {FASTBOOT Only}
[ 8 - Перезагрузка... {FASTBOOT/ADB}
[============================================================================]
"""

banner2="""
{======|Получение Root|======}
[================================]
[ 1 - Magisk 20.04 (Рекомендуется)
[================================]
"""

banner3="""
{======| Установка EdXposed Framework|======}
[=================================================================]
[ 1 - Обычная установка (Riru - Core, EdXposed Framework #SandHook#, Magisk
[ 2 - Установить только EdXposed Framework #SandHook#
[=================================================================]
"""

banner4="""
{======|Прошить Zip|======}
[==========================]
[ Прошивание zip только через
[ ADB Sideload!
[==========================]
"""

bannermod="""
{======|Модификации|======}
[===================================]
[ Apple]~[Flash
[===================================]
"""
banner5="""
{======|Прошить раздел|======}
[===========================]
[ Ведите имя раздела и образ ниже.
[ Часто: system, recovery, boot
[===========================]
"""

banner6="""
{======|Форматировать раздел|======}
[===========================]
[ Ведите имя раздела ниже.
[ Часто: system, data, userdata
[===========================]
"""

banner7="""
{======|Перезагрузка|======}
[===========================]
[ 1 - System
[ 2 - Recovery
[ 3 - botloader
[===========================]
"""

banner8="""
{======|Способ|======}
[==========================]
[ 1 - FastBoot
[ 2 - ADB
[==========================]
"""


if __name__ == '__main__':
	print(bannermod)
	input()
