using Dapper;
using MDM.Product.gRPC.Primitives;
using MDM.Product.gRPC.Services;
using Microsoft.Data.SqlClient;

namespace MDM.Product.gRPC.Repositories;

using Data;

public interface IProductRepository
{
    Task<IEnumerable<Product>> GetAllAsync();

    Task<IEnumerable<Product>> GetProductsAsync(PaginationRequest paginationRequest);

    Task<Product?> GetByIdAsync(Guid id);
    Task<Product> CreateAsync(string name, decimal price);
    Task UpdateAsync(Guid id, string name, decimal price);
    Task<bool> DeleteAsync(Guid id);
}

public sealed class ProductRepository : IProductRepository, IDisposable
{
    private readonly SqlConnection _sqlConnection;

    public ProductRepository(IConfiguration config)
    {
        var connectionString = config.GetConnectionString("DefaultConnection");
        if (string.IsNullOrWhiteSpace(connectionString))
        {
            throw new NullReferenceException("Default connection string not found");
        }

        _sqlConnection = new SqlConnection(connectionString);

    }

    public async Task<IEnumerable<Product>> GetAllAsync()
    {
        return await _sqlConnection.QueryAsync<Product>("SELECT * FROM Products");
    }
    public async Task<IEnumerable<Product>> GetProductsAsync(PaginationRequest paginationRequest)
    {
        var offset = (paginationRequest.PageNumber - 1) * paginationRequest.PageSize;
        var sql = "SELECT * FROM Products ORDER BY CreatedAt DESC OFFSET @Offset ROWS FETCH NEXT @PageSize ROWS ONLY";
        return await _sqlConnection.QueryAsync<Product>(sql, new { Offset = offset, PageSize = paginationRequest.PageSize });
    }

    public async Task<Product?> GetByIdAsync(Guid id)
    {
        return await _sqlConnection.QuerySingleOrDefaultAsync<Product>(
            "SELECT * FROM Products WHERE Id = @Id", new { Id = id });
    }

    public async Task<Product> CreateAsync(string name, decimal price)
    {
        var product = new Product
        {
            Id = Guid.NewGuid(),
            Name = Guard.AgainstNullOrEmpty(name, nameof(name), 100),
            Price = price,
            CreatedAt = DateTimeOffset.UtcNow,
            CreatedBy = Guid.Empty
        };

        await _sqlConnection.ExecuteAsync(
            """
                INSERT INTO Products (Id, Name, Price, CreatedAt, CreatedBy, IsDeleted)
                VALUES (@Id, @Name, @Price, @CreatedAt, @CreatedBy, @IsDeleted)
            """, product);

        return product;
    }

    public async Task UpdateAsync(Guid id, string name, decimal price)
    {
        var affectedRows  = await _sqlConnection.ExecuteAsync(
            """
                UPDATE Products
                SET Name = @Name, Price = @Price
                WHERE Id = @Id
            """, new { Id = id, Name = name, Price = price });
        
        if (affectedRows == 0)
        {
            throw new KeyNotFoundException($"Product with ID {id} not found.");
        }

    }

    public async Task<bool> DeleteAsync(Guid id)
    {
        var affected = await _sqlConnection.ExecuteAsync("DELETE FROM Products WHERE Id = @Id", new { Id = id });
        return affected > 0;
    }
    public void Dispose()
    {
        _sqlConnection.Dispose();
    }

    public async Task DisposeAsync()
    {
        await _sqlConnection.DisposeAsync();
    }
}