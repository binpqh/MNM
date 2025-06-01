using MDM.Product.gRPC.Services;

namespace MDM.Product.gRPC.Data;

public sealed class Product
{
    public Guid Id { get; init; }

    public string Name { get; set; } = string.Empty;

    public decimal Price { get; set; }
    
    public Guid ShopId { get; set; } = Guid.Empty;
    
    public List<Image> Images { get; set; } = new List<Image>();
    
    public DateTimeOffset CreatedAt { get; set; } = DateTimeOffset.UtcNow;
    
    public DateTimeOffset? UpdatedAt { get; set; }
    
    public DateTimeOffset? DeletedAt { get; set; }
    
    public Guid CreatedBy { get; set; } = Guid.Empty;
    
    public Guid? LastModifier { get; set; }
    
    public Guid? DeletedBy { get; set; }
    
    public bool IsDeleted { get; set; } = false;
    
    public ProductResponse ToResponse()
    {
        return new ProductResponse
        {
            Id = Id,
            Name = Name,
            Price = Price,
            CreatedAt = CreatedAt,
            UpdatedAt = UpdatedAt,
            DeletedAt = DeletedAt,
            CreatedBy = CreatedBy,
            LastModifier = LastModifier,
            DeletedBy = DeletedBy,
            IsDeleted = IsDeleted
        };
    }
}