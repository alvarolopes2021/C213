import 'dart:async';

import 'package:mqqt_fuzzy/core/services/imqtt_client.dart';
import 'package:mqqt_fuzzy/graph/data/datasources/igraph_datasource.dart';
import 'package:mqqt_fuzzy/main.dart';

class GraphDataSource implements IGraphDataSource {
  late IMqttClient client;

  GraphDataSource() {
    client = getIt.get<IMqttClient>();
  }

  @override
  Future<void> getError(StreamController controller) async {
    client.readData();
  }

  @override
  Future<void> getTemp(StreamController controller) async{
    client.readData();
  }
}
