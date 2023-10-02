# ->> Import Libs: pip install qrcode 
import qrcode

# ->> Functions:
def create_qrcode(ssid: str, passwd: str):
    wifi_config = f'WIFI:T:WPA;S:{ssid};P:{passwd};;'
    return qrcode.make(wifi_config)

def main():
    # Solicite ao usuário o SSID e a senha da rede Wi-Fi
    ssid = input("Digite o nome da rede Wi-Fi (SSID): ")
    passwd = input("Digite a senha da rede Wi-Fi: ")
    
    # Geração de código QR com base nas informações fornecidas
    qrcode_ = create_qrcode(ssid, passwd)
    
    # Salvando código QR em um arquivo com base no SSID
    qrcode_.save(f'{ssid}_wifi_qrcode.png')
    
    print(f'Código QR criado com exito.')

if __name__ == '__main__':
    main()