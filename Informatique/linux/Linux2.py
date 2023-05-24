import os

def afficher_commandes_linux():
    commandes = [
        "ls",
        "pwd",
        "cd",
        "mkdir",
        "rm",
        "cp",
        "mv",
        "touch",
        "cat",
        "grep",
        "chmod",
        "chown",
        "ps",
        "top",
        "kill",
        "ifconfig",
        "ip addr",
        "ping",
        "ssh",
        "wget",
        "curl"
    ]

    for commande in commandes:
        print(f"Commande Linux : {commande}")
        os.system(f"man {commande}")

afficher_commandes_linux()
