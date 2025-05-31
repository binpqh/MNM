FROM mcr.microsoft.com/dotnet/aspnet:9.0 AS base
USER $APP_UID
WORKDIR /app
EXPOSE 8080
EXPOSE 8081

FROM mcr.microsoft.com/dotnet/sdk:9.0 AS build
ARG BUILD_CONFIGURATION=Release
WORKDIR /src
COPY ["MNM.Product.gRPC/MNM.Product.gRPC.csproj", "MNM.Product.gRPC/"]
RUN dotnet restore "MNM.Product.gRPC/MNM.Product.gRPC.csproj"
COPY . .
WORKDIR "/src/MNM.Product.gRPC"
RUN dotnet build "MNM.Product.gRPC.csproj" -c $BUILD_CONFIGURATION -o /app/build

FROM build AS publish
ARG BUILD_CONFIGURATION=Release
RUN dotnet publish "MNM.Product.gRPC.csproj" -c $BUILD_CONFIGURATION -o /app/publish /p:UseAppHost=false

FROM base AS final
WORKDIR /app
COPY --from=publish /app/publish .
ENTRYPOINT ["dotnet", "MNM.Product.gRPC.dll"]
