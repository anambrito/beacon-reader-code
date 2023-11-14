import ScanUtility
import bluetooth._bluetooth as bluez
import time
import arrow 
from bluepy import btle
from bluepy.btle import Scanner

class BLELS: #classe que busca dispositivos BLE
    SCAN_TIMEOUT = 20
    def __init__(self):
        self.scanner = Scanner()
    
    def scan(self, duration=SCAN_TIMEOUT):
        return self.scanner.scan(duration)

def main():
    dev_id = 0
    try:
        sock = bluez.hci_open_dev(dev_id)
        print("\n *** Procurando por Beacons BLE ***")
        print(" *** Pressione CTRL-C para cancelar ***\n")
    except:
        print("Erro ao acessar o Bluetooth")

    ScanUtility.hci_enable_le_scan(sock) #ativa biblioteca que busca dispositivos com protocolos compativeis com o Beacon

    start_time = time.time()
    end_time = start_time + 60 * 10 #limite de tempo de execução

    blels = BLELS() #instancia a classe BLELS que busca dispositivos BLE

    #declaração das variaveis
    devices = []
    item= []
    devname=""
    now=""
    item=""
    dev=""
    i=0
    j=0

    
    dispositivos_salvos = set() # Defina um conjunto para rastrear os endereços MAC dos dispositivos salvos
    with open("beacon_data.txt", "a") as file:
        while time.time() < end_time:
            item = ScanUtility.parse_events(sock, 20) #busca dispositivos com protocolos compativeis com o Beacon
            devices = blels.scan() #busca dispositivos BLE
            if item: #item nao é vazio
                for dev in devices:
                    if dev.addr not in dispositivos_salvos and dev.addr == item[0]["macAddress"]: #Se o dispositivo não está em dispositivos_salvos e tem o mesmo endereço MAC
                        dispositivos_salvos.add(dev.addr) #salva o mac na lista de dispositivos identificados
                        devname = dev.getValueText(btle.ScanEntry.COMPLETE_LOCAL_NAME) or dev.getValueText(btle.ScanEntry.SHORT_LOCAL_NAME) #pega o SSID
                        print(f"SSID: {devname}")
                        print(f"MAC: {item[0]['macAddress']}")
                        print(f"UUID: {item[0]['uuid']}")
                        now = arrow.now()
                        print("Data e Hora:", now.format("DD-MM-YYYY HH:mm:ss")) 
                        print(f"---------------------------------------") 

                        #salva todas as informações coletadas no arquivo
                        file.write(f"SSID: {devname}\n")
                        file.write(f"MacAddr: {item[0]['macAddress']}\n")
                        file.write(f"UUID: {item[0]['uuid']}\n")
                        file.write(f"Data e Hora: {now.format('DD-MM-YYYY HH:mm:ss')}\n") #salva a data e horario
                        file.write(f"--------------------------------------------\n") #separador
                        
                        # Esvaziar as listas no final do loop
                        returnedList = {}
                        devices = {}
                        break


if __name__ == "__main__":
    main()
