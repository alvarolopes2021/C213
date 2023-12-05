import 'dart:async';

abstract class IMqttClient {
  void connect();
  void disconnect();
  void sendData(String message);
  void readData();

  late StreamController controller;
  late bool willSave;
  late bool error;
  late bool isConnected;
}