import 'dart:async';

abstract class IGraphRepository {
  Future<int> getError(StreamController controller);
  Future<double> getTemp(StreamController controller);
}
