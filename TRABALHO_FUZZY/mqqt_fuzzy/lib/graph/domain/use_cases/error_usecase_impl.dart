import 'dart:async';

import 'package:mqqt_fuzzy/core/use_cases/error/error_usecase.dart';
import 'package:mqqt_fuzzy/graph/domain/repositories/igraph_repository.dart';

class ErrorUseCaseImpl implements ErrorUseCase {
  late IGraphRepository graphRepository;

  ErrorUseCaseImpl({required this.graphRepository});

  @override
  Future<int> getError(StreamController controller) {
    return graphRepository.getError(controller);
  }
}
