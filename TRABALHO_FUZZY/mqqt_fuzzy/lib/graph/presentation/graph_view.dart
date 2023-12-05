import 'dart:async';
import 'dart:io';

import 'package:flutter/material.dart';
import 'package:charts_flutter/flutter.dart' as charts;
import 'package:mqqt_fuzzy/core/services/imqtt_client.dart';
import 'package:mqqt_fuzzy/graph/data/models/data_model.dart';
import 'package:mqqt_fuzzy/main.dart';

class GraphView extends StatefulWidget {
  @override
  State<StatefulWidget> createState() {
    return _GraphView();
  }
}

class _GraphView extends State<GraphView> {
  late final List<charts.Series<DataModel, int>> seriesList = [];
  StreamController controller = StreamController<DataModel>.broadcast();
  List<DataModel> chartData = [];
  late IMqttClient _client;
  int time = 0;

  @override
  void initState() {
    _client = getIt.get<IMqttClient>();
    _client.controller = controller;
    _client.connect();
    _client.readData();
    super.initState();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text("Fuzzy"),
      ),
      body: StreamBuilder(
        builder: (context, snapshot) {
          if (snapshot.data == null) {
            return const Center(
              child: CircularProgressIndicator(color: Colors.blue),
            );
          }

          if (snapshot.connectionState == ConnectionState.waiting) {
            return const Center(
              child: CircularProgressIndicator(color: Colors.blue),
            );
          }

          chartData.add(snapshot.data);

          print(chartData.length);

          seriesList.add(
            charts.Series<DataModel, int>(
                data: chartData,
                domainFn: (DataModel data, _) => data.id,
                id: "Fuzzy",
                measureFn: (DataModel data, _) => data.data),
          );

          return Column(
            children: [
              Expanded(
                child: Container(
                  width: MediaQuery.of(context).size.width,
                  child: charts.LineChart(
                    seriesList,
                    animate: true,
                  ),
                ),
              )
            ],
          );
        },
        stream: controller.stream,
      ),
    );
  }
}
