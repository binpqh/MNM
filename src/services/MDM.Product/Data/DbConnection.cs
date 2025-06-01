using System.Data;
using System.Data.Common;
using System.Diagnostics.CodeAnalysis;

namespace MDM.Product.gRPC.Data;

public class AppDbConnection : DbConnection
{
    protected override DbTransaction BeginDbTransaction(IsolationLevel isolationLevel) => throw new NotImplementedException();
    public override void ChangeDatabase(string databaseName)
    {
        throw new NotImplementedException();
    }
    public override void Close()
    {
        throw new NotImplementedException();
    }
    public override void Open()
    {
        throw new NotImplementedException();
    }
    [AllowNull] public override string ConnectionString { get; set; }
    public override string Database { get; }
    public override ConnectionState State { get; }
    public override string DataSource { get; }
    public override string ServerVersion { get; }
    protected override DbCommand CreateDbCommand() => throw new NotImplementedException();
}