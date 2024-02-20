const int pinBuzzer = 7;
boolean somTocando = false;

void setup() {
  // Inicia a comunicação serial
  Serial.begin(9600);
  pinMode(pinBuzzer, OUTPUT);
}

void loop() {
  // Verifica se há dados disponíveis na comunicação serial
  if (Serial.available() > 0) {
    // Lê o caractere recebido
    char caractere = Serial.read();

    // Se o caractere for 'A', toca o som continuamente
    if (caractere == 'A') {
      somTocando = true;
      while (somTocando) { // Loop enquanto o som estiver tocando
        digitalWrite(pinBuzzer, HIGH); // Liga o buzzer
        delay(1000); // Mantém o som ligado por 1 segundo
        digitalWrite(pinBuzzer, LOW); // Desliga o buzzer
        delay(1000); // Espera 1 segundo antes de ligar o som novamente
        
        // Verifica se um caractere de parada foi recebido
        if (Serial.available() > 0) {
          char stopChar = Serial.read();
          if (stopChar == 'P') {
            somTocando = false; // Para o som
          }
        }
      }
    }
  }
}
