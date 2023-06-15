import paramiko

def ssh_connect(hostname, username, password):
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        try:
            client.connect(hostname, username=username, password=password)
            print("Connexion établie avec succès!")

            while True:
                command = input("Entrez une commande à exécuter (q pour quitter) : ")

                if command.lower() == "q":
                    break

                stdin, stdout, stderr = client.exec_command(command)
                output = stdout.read().decode()
                error = stderr.read().decode()

                if output:
                    print(output)

                if error:
                    print(error)

            client.close()
            print("Connexion fermée.")
        except paramiko.AuthenticationException:
            print("Échec de l'authentification. Vérifiez vos identifiants.")
        except paramiko.SSHException as e:
            print("Erreur lors de l'établissement de la connexion SSH:", str(e))
        except paramiko.ssh_exception.NoValidConnectionsError as e:
            print("Échec de la connexion SSH:", str(e))

def main():
        print("=== Menu Principal ===")
        hostname = input("Entrez l'adresse IP du serveur SSH : ")
        username = input("Entrez le nom d'utilisateur : ")
        password = input("Entrez le mot de passe : ")

        ssh_connect(hostname, username, password)

if __name__ == "__main__":
        main()
