import 'package:flutter/widgets.dart';
import 'package:charts_flutter/flutter.dart' as charts;
import 'package:mqqt_fuzzy/core/services/imqtt_client.dart';
import 'package:mqqt_fuzzy/main.dart';

class GraphView extends StatefulWidget {
  @override
  State<StatefulWidget> createState() {
    return _GraphView();
  }
}

class _GraphView extends State<GraphView> {
  late final List<charts.Series<dynamic, DateTime>> seriesList;
  late final bool animate;

  @override
  void initState() {
    getIt.isReady<IMqttClient>().then((_) => getIt<IMqttClient>().connect());    

    super.initState();
  }

  @override
  Widget build(BuildContext context) {
    return charts.TimeSeriesChart(
      seriesList,
      animate: animate,
      // Optionally pass in a [DateTimeFactory] used by the chart. The factory
      // should create the same type of [DateTime] as the data provided. If none
      // specified, the default creates local date time.
      dateTimeFactory: const charts.LocalDateTimeFactory(),
    );
  }
}
