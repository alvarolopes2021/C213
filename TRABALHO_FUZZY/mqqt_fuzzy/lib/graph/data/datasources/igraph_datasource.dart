import 'dart:async';

abstract class IGraphDataSource {
  Future<void> getError(StreamController controller);
  Future<void> getTemp(StreamController controller);
}
