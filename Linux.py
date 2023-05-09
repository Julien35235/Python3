import subprocess

result = subprocess.run(['ls'], stdout=subprocess.PIPE)
print(result.stdout.decode('utf-8'))
