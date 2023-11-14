#Beacon reader

O código beacon-reader.py é relativo ao Trabalho de Conclusão de Curso do curso de Graduação de Engenharia de Computação do CEFET-MG/BH da aluna Ana Maria Mendes de Brito. 

Os códigos a seguir estão disponíveis para consulta e verificação. Foi utilizado a biblioteca ScanUtility do autor bowdentheo disponível em: https://github.com/bowdentheo/BLE-Beacon-Scanner

Atenção, o autor da biblioteca ScanUtility alerta que este código foi desenvolvido para ser usando no Raspberry Pi 3 B+.

Descrição: O programa beacon-reader compõe o sistema inteligente do protótipo e está escrito na linguagem Python. Suas principais bibliotecas são a ScanUtility e a BluePy. 
A primeira fica responsável por identificar dispositivos que utilizem protocolos Beacon, como \mbox{iBeacon} e \mbox{Eddystone}, já a segunda biblioteca 
escaneia o ambiente para identificar dispositivos BLE. Essa dupla verificação no ambiente é necessária pois a ScanUtility não é capaz de identificar SSID 
dos dispositivos, enquanto a Bluepy não consegue pegar o UUID. Assim, para que o receptor possa exportar em um arquivo as informações de SSID, MacAddrs e 
UUID deve ocorrer o uso de ambas as bibliotecas. 