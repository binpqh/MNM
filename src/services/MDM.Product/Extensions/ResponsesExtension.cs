namespace MDM.Product.gRPC.Extensions;

public static class ResponsesExtension
{
    public static IEnumerable<Services.ProductResponse> ToResponses(this IEnumerable<Data.Product> products)
    {
        return products.Select(p => p.ToResponse());
    }
}