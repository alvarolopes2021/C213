import 'dart:async';

abstract class ErrorUseCase{
  Future<int> getError(StreamController controller);
}