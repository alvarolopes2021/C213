import 'dart:async';

import 'package:mqqt_fuzzy/core/use_cases/temp/temp_usecase.dart';
import 'package:mqqt_fuzzy/graph/domain/repositories/Igraph_repository.dart';

class TempUseCaseImpl implements TempUseCase {
  late IGraphRepository graphRepository;

  TempUseCaseImpl({required this.graphRepository});

  @override
  Future<double> getTemp(StreamController controller) {
    return graphRepository.getTemp(controller);
  }
}
