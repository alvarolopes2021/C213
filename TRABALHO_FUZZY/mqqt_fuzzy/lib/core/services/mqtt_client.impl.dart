import 'dart:io';
import 'dart:async';
import 'package:mqtt_client/mqtt_client.dart';
import 'package:mqtt_client/mqtt_server_client.dart';

import 'package:mqqt_fuzzy/core/services/imqtt_client.dart';

class MqttClientImpl implements IMqttClient {
  final client =
      MqttServerClient.withPort('', '9e56a0f11e464cb594616faf0ed42dfe', 8883);

  @override
  late bool error;

  @override
  late bool willSave;

  @override
  void connect() async {
    try {
      // the next 2 lines are necessary to connect with tls, which is used by HiveMQ Cloud
      client.secure = true;
      client.securityContext = SecurityContext.defaultContext;
      client.keepAlivePeriod = 20;
      await client.connect("projetinho", "Projetinh0");

      print('con status: ');
      print(client.connectionStatus);

      client.subscribe('PET_CONTROLLER_ETE', MqttQos.atLeastOnce);
    } catch (e) {
      print('client exception - $e');
      client.disconnect();
    }
  }

  @override
  void disconnect() {
    try {
      client.disconnect();
      print('con status: ');
      print(client.connectionStatus);
    } catch (e) {
      print('con refused: ');
    }
  }

  @override
  void readData(StreamController controller) {
    // TODO: implement readData
    client.updates!.listen((event) async {
      final recMess = event[0].payload as MqttPublishMessage;

      final tag =
          MqttPublishPayload.bytesToStringAsString(recMess.payload.message);

      sendData("OPEN");
      
      controller.add(tag);
    });
  }

  @override
  void sendData(String message) {
    final MqttClientPayloadBuilder builder = MqttClientPayloadBuilder();
    builder.addString(message);

    print(
        'Publishing message "$message" to topic PET_CONTROLLER_ETE_ACTION');
    client.publishMessage("PET_CONTROLLER_ETE_ACTION", MqttQos.exactlyOnce, builder.payload!);
  }
}
