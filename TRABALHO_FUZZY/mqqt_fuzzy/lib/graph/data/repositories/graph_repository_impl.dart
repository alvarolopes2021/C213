import 'package:mqqt_fuzzy/graph/data/datasources/igraph_datasource.dart';
import 'package:mqqt_fuzzy/graph/domain/repositories/igraph_repository.dart';

class GraphRepositoryImpl implements IGraphRepository {
  late IGraphDataSource dataSource;

  GraphRepositoryImpl({required this.dataSource});

  @override
  Future<int> getError() {
    return dataSource.getError();
  }

  @override
  Future<double> getTemp() {
    return dataSource.getTemp();
  }
}
