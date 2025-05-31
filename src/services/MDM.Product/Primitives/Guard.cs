namespace MDM.Product.gRPC.Primitives;

public static class Guard
{
    public static string AgainstNullOrEmpty(string value, string paramName, int? maxLength = null)
    {
        if (string.IsNullOrWhiteSpace(value))
            throw new ArgumentException($"{paramName} must not be null or empty.", paramName);

        if (maxLength.HasValue && value.Length > maxLength.Value)
            throw new ArgumentException($"{paramName} must not exceed {maxLength} characters.", paramName);

        return value;
    }
}
