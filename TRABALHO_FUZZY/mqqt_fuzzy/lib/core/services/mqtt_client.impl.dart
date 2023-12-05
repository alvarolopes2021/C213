import 'dart:async';
import 'package:mqqt_fuzzy/graph/data/models/data_model.dart';
import 'package:mqtt_client/mqtt_browser_client.dart';

import 'package:mqqt_fuzzy/core/services/imqtt_client.dart';
import 'package:mqtt_client/mqtt_client.dart';

class MqttClientImpl implements IMqttClient {
  final client = MqttBrowserClient('ws://test.mosquitto.org', 'projetinho');

  int _id = 0;
  int _idError = 0;

  @override
  late StreamController controller;

  @override
  late StreamController errorController;

  @override
  late bool error;

  @override
  late bool isConnected;

  @override
  late bool willSave;

  @override
  void connect() async {
    try {
      // the next 2 lines are necessary to connect with tls, which is used by HiveMQ Cloud
      client.websocketProtocols = ['mqtt'];
      client.keepAlivePeriod = 20;
      client.port = 8080;
      await client.connect();

      print('con status: ');
      print(client.connectionStatus);

      client.subscribe('resfriador/temperatura', MqttQos.atLeastOnce);
      client.subscribe('resfriador/erro', MqttQos.atLeastOnce);

      isConnected = client.connectionStatus == MqttConnectionState.connected;

      readData();
    } catch (e) {
      print('client exception - $e');
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
  void readData() {
    // TODO: implement readData
    print('will read data');

    try {
      client.updates!.listen((event) async {
        final recMess = event[0].payload as MqttPublishMessage;

        final tag =
            MqttPublishPayload.bytesToStringAsString(recMess.payload.message);

        _id++;
        _idError++;

        if (event[0].topic == "resfriador/erro") {
          DataModel model = DataModel(_idError, double.parse(tag));
          errorController.add(model);
        } else {
          DataModel model = DataModel(_id, double.parse(tag));
          controller.add(model);
        }
      });
    } catch (e) {
      print(e);
    }
  }

  @override
  void sendData(String message) {
    final MqttClientPayloadBuilder builder = MqttClientPayloadBuilder();
    builder.addString(message);

    print('Publishing message "$message" to topic PET_CONTROLLER_ETE_ACTION');
    client.publishMessage(
        "PET_CONTROLLER_ETE_ACTION", MqttQos.exactlyOnce, builder.payload!);
  }
}
