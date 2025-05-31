namespace MDM.Product.gRPC.Data;

public sealed class Product(int id, string name, decimal price)
{
    public int Id { get; init; } = id;

    public string Name { get; set; } = name.Length <= 100
        ? name
        : throw new ArgumentException("Name is too long (max 100 characters)");

    public decimal Price { get; set; } = price;
}