import colorama

colorama.init()

pinguin = '''
   .--.
  |o_o |
  |:_/ |
 //   \ \\
(|     | )
/'\_   _/`\\
\___)=(___/
'''

colored_pinguin = colorama.Fore.CYAN + pinguin

print(colored_pinguin)

colorama.deinit()
