import 'dart:async';

abstract class TempUseCase{
  Future<double> getTemp(StreamController controller);
}