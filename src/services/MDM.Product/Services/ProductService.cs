using MDM.Product.gRPC.Extensions;
using MDM.Product.gRPC.Primitives;
using MDM.Product.gRPC.Repositories;

namespace MDM.Product.gRPC.Services;

public sealed record ProductResponse
{
    public Guid Id { get; set; }
    public string Name { get; set; } = string.Empty;
    public decimal Price { get; set; }
    public DateTimeOffset CreatedAt { get; set; } = DateTimeOffset.UtcNow;
    public DateTimeOffset? UpdatedAt { get; set; }
    public DateTimeOffset? DeletedAt { get; set; }
    public Guid CreatedBy { get; set; } = Guid.Empty;
    public Guid? LastModifier { get; set; }
    public Guid? DeletedBy { get; set; }
    public bool IsDeleted { get; set; } = false;
}

public sealed record ProductRequest
{
    public string Name { get; set; } = string.Empty;
    public decimal Price { get; set; }

    public Data.Product ToProduct()
    {
        return new Data.Product
        {
            Name = Guard.AgainstNullOrEmpty(Name, nameof(Name), 100),
            Price = Price,
            CreatedAt = DateTimeOffset.UtcNow,
            CreatedBy = Guid.Empty
        };
    }
    
    public Data.Product ToProduct(Guid id)
    {
        return new Data.Product
        {
            Id = id,
            Name = Guard.AgainstNullOrEmpty(Name, nameof(Name), 100),
            Price = Price,
            CreatedAt = DateTimeOffset.UtcNow,
            CreatedBy = Guid.Empty
        };
    }
}

public sealed record PaginationRequest
{
    public int PageNumber { get; set; } = 1;
    public int PageSize { get; set; } = 10;
}

public interface IProductService
{
    // Define methods for product operations, e.g., CreateProduct, GetProduct, UpdateProduct, DeleteProduct
    Task<ProductResponse> AddProductAsync(ProductRequest request);

    Task<ProductResponse?> GetProductAsync(Guid id);

    Task<IEnumerable<ProductResponse>> GetProductsAsync(PaginationRequest paginationRequest);

    Task<ProductResponse> UpdateProductAsync(Guid id, ProductRequest request);

    Task<bool> DeleteProductAsync(Guid id);
}

public class ProductService(IProductRepository productRepository) : IProductService
{
    public async Task<ProductResponse> AddProductAsync(ProductRequest request)
    {
        var product = await productRepository.CreateAsync(request.Name, request.Price);
        return product.ToResponse();
    }

    public async Task<ProductResponse?> GetProductAsync(Guid id) => (await productRepository.GetByIdAsync(id))?.ToResponse();
    public async Task<IEnumerable<ProductResponse>> GetProductsAsync(PaginationRequest paginationRequest)
        => (await productRepository.GetProductsAsync(paginationRequest)).ToResponses();

    public Task<ProductResponse> UpdateProductAsync(Guid id, ProductRequest request)
    {
        var updatingProduct = request.ToProduct(id);
        
        productRepository.UpdateAsync(id, updatingProduct.Name, updatingProduct.Price);
        return updatingProduct
    }
    public Task<bool> DeleteProductAsync(Guid id) => throw new NotImplementedException();
}