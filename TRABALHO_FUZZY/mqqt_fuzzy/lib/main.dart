import 'package:flutter/material.dart';
import 'package:get_it/get_it.dart';
import 'package:mqqt_fuzzy/core/services/imqtt_client.dart';
import 'package:mqqt_fuzzy/core/services/mqtt_client.impl.dart';
import 'package:mqqt_fuzzy/graph/presentation/graph_view.dart';

// This is our global ServiceLocator
GetIt getIt = GetIt.instance;

void main() {
  getIt.registerSingleton<IMqttClient>(MqttClientImpl(),
      signalsReady: true);

  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  // This widget is the root of your application.
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Fuzzy - Mqtt Client',
      theme: ThemeData(
        primarySwatch: Colors.blue,
      ),
      home:  GraphView(),
    );
  }
}
