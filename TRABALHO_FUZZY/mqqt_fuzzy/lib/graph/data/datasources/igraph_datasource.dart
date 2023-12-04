abstract class IGraphDataSource {
  Future<int> getError();
  Future<double> getTemp();
}
