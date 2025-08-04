#include <ESP8266WiFi.h>
#include <WebSocketsServer.h>

// Wi-Fi Credentials
const char* ssid = "IoT_Car";  // Change to your Wi-Fi SSID
const char* password = "12345678";  // Change to your Wi-Fi Password

// Motor Pins
#define IN1 D1
#define IN2 D2
#define IN3 D3
#define IN4 D4

WebSocketsServer webSocket(81); // WebSocket server on port 81

void controlCar(String command) {
    if (command == "F") { // Forward
        digitalWrite(IN1, HIGH);
        digitalWrite(IN2, LOW);
        digitalWrite(IN3, HIGH);
        digitalWrite(IN4, LOW);
    } else if (command == "B") { // Backward
        digitalWrite(IN1, LOW);
        digitalWrite(IN2, HIGH);
        digitalWrite(IN3, LOW);
        digitalWrite(IN4, HIGH);
    } else if (command == "L") { // Left
        digitalWrite(IN1, LOW);
        digitalWrite(IN2, HIGH);
        digitalWrite(IN3, HIGH);
        digitalWrite(IN4, LOW);
    } else if (command == "R") { // Right
        digitalWrite(IN1, HIGH);
        digitalWrite(IN2, LOW);
        digitalWrite(IN3, LOW);
        digitalWrite(IN4, HIGH);
    } else { // Stop
        digitalWrite(IN1, LOW);
        digitalWrite(IN2, LOW);
        digitalWrite(IN3, LOW);
        digitalWrite(IN4, LOW);
    }
}

// WebSocket Event Handler
void webSocketEvent(uint8_t num, WStype_t type, uint8_t *payload, size_t length) {
    if (type == WStype_TEXT) {
        String command = String((char *)payload);
        Serial.println("Command Received: " + command);
        controlCar(command);
    }
}

void setup() {
    Serial.begin(115200);

    pinMode(IN1, OUTPUT);
    pinMode(IN2, OUTPUT);
    pinMode(IN3, OUTPUT);
    pinMode(IN4, OUTPUT);

    // Connect to Wi-Fi
    WiFi.softAP(ssid, password);
    Serial.println("WiFi Started!");
    Serial.print("IP Address: ");
    Serial.println(WiFi.softAPIP());

    // Start WebSocket Server
    webSocket.begin();
    webSocket.onEvent(webSocketEvent);
}

void loop() {
    webSocket.loop(); // Keep WebSocket running
}
