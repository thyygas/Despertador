import subprocess
import time





# Função para exibir a hora no formato HH:MM:SS
def exibir_hora():
    hora_atual = time.localtime()
    hora = hora_atual.tm_hour
    minuto = hora_atual.tm_min
    segundo = hora_atual.tm_sec
    print(f"{hora:02d}:{minuto:02d}:{segundo:02d}")

# Função para disparar o alarme
def disparar_alarme():
    # Use o comando echo para enviar o caractere 'A' para a porta serial do Arduino
    subprocess.run(['echo', 'A', '>', 'COM3'], shell=True)  # Substitua 'COM3' pela porta serial correta


def parar_alarme():
    # Use o comando echo para enviar o caractere 'A' para a porta serial do Arduino
    subprocess.run(['echo', 'P', '>', 'COM3'], shell=True)  # Substitua 'COM3' pela porta serial correta


# Função para definir o alarme
def definir_alarme(hora_alarme, minuto_alarme, segundo_alarme):
    while True:
        hora_atual = time.localtime()
        if hora_atual.tm_hour == hora_alarme and hora_atual.tm_min == minuto_alarme and hora_atual.tm_sec == segundo_alarme:
            print("ALARME DISPARADO!")
            disparar_alarme()  # Chama a função para disparar o alarme
            break
        time.sleep(1)  # Aguarda 1 segundo antes de verificar novamente


# Pede ao usuário para definir a hora, o minuto e o segundo do alarme
hora_alarme = int(input("Digite a hora do alarme (0-23): "))
minuto_alarme = int(input("Digite o minuto do alarme (0-59): "))
segundo_alarme = int(input("Digite o segundo do alarme (0-59): "))

# Chama a função para definir o alarme
definir_alarme(hora_alarme, minuto_alarme, segundo_alarme)


while True:
    if input("Pressione 'P' para parar o alarme: ").upper() == "P":
        parar_alarme()
        break