import 'dart:async';

abstract class IMqttClient {
  void connect();
  void disconnect();
  void sendData(String message);
  void readData(StreamController controller);

  late bool willSave;
  late bool error;
}