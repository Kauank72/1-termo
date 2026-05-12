# Notas de Aula: Arquitetura de IoT
**Disciplina:** Arquitetura IOT  
**Tópicos:** Arduino, C++ e Python

---

## 1. Introdução ao Arduino
O Arduino é a camada de **Hardware (Percepção)** na arquitetura IoT, responsável por interagir com o mundo físico através de sensores e atuadores.

### Componentes Principais:
*   **Microcontrolador:** Atmel AVR (Ex: ATmega328P no Uno).
*   **Pinos Digitais:** Entradas/Saídas (0 e 1).
*   **Pinos Analógicos:** Leitura de sensores (0 a 1023).
*   **Comunicação:** USB, UART, I2C e SPI.

---

## 2. Programação em C++ (Firmware)
O Arduino utiliza uma variante de C++. O código é dividido em duas funções principais:

```cpp
// Definição de pinos
const int ledPin = 13;

void setup() {
  // Executa uma vez ao iniciar
  pinMode(ledPin, OUTPUT);
  Serial.begin(9600); // Inicia comunicação serial
}

void loop() {
  // Executa em loop infinito
  digitalWrite(ledPin, HIGH);
  delay(1000);
  digitalWrite(ledPin, LOW);
  delay(1000);
  
  Serial.println("LED Piscando...");
}
```

---

## 3. Programação em Python (Integração e Dados)
Na arquitetura IoT, o Python geralmente atua na **Camada de Aplicação ou Gateway**, processando dados vindos do Arduino ou enviando comandos via Serial.

### Exemplo: Lendo dados do Arduino via PySerial
```python
import serial
import time

# Configuração da porta (ajuste o 'COM3' ou '/dev/ttyUSB0')
arduino = serial.Serial(port='COM3', baudrate=9600, timeout=.1)

def read_arduino():
    time.sleep(2) # Aguarda conexão
    while True:
        data = arduino.readline().decode('utf-8').strip()
        if data:
            print(f"Dados recebidos: {data}")

if __name__ == "__main__":
    read_arduino()
```

---

## 4. Fluxo de Dados na Arquitetura
1.  **Sensores (Hardware):** Captam sinais analógicos.
2.  **Arduino (C++):** Processa o sinal e converte em dados digitais.
3.  **Comunicação (Serial/MQTT/HTTP):** Envia os dados para um computador ou nuvem.
4.  **Python (Software):** Recebe, armazena em bancos de dados e gera dashboards.

---

## Recursos Úteis
*   [Documentação Oficial Arduino](https://arduino.cc)
*   [Biblioteca PySerial](https://pythonhosted.org)
*   [Simulador Wokwi](https://wokwi.com)
