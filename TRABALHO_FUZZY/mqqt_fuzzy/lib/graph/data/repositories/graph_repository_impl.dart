import 'dart:async';

import 'package:mqqt_fuzzy/graph/data/datasources/igraph_datasource.dart';
import 'package:mqqt_fuzzy/graph/domain/repositories/igraph_repository.dart';

class GraphRepositoryImpl implements IGraphRepository {
  late IGraphDataSource dataSource;

  GraphRepositoryImpl({required this.dataSource});

  @override
  Future<int> getError(StreamController controller) async{
    dataSource.getError(controller);
    return 0;
  }

  @override
  Future<double> getTemp(StreamController controller) async{
    dataSource.getTemp(controller);
    return 0;
  }
}
