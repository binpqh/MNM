namespace MDM.Product.gRPC.Data;

public sealed class Image
{
    public Guid Id { get; set; }
    
    public string Url { get; set; } = string.Empty;
}