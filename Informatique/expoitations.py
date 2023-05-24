import platform

print("Les systèmes d'exploitation disponibles en Python sont :")
operating_systems = platform.system_alias(platform.system(), platform.release(), platform.version())
i = 0
while i < len(operating_systems):
    os_name = operating_systems[i][0]
    if os_name not in ["", "unknown"] and os_name.lower() not in ["cygwin", "msys"]:
        print(f"- {os_name}")
    i += 1
