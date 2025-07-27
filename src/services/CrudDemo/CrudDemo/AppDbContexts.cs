using Microsoft.EntityFrameworkCore;

namespace CrudDemo;

public class AppDbContexts : DbContext
{
    public DbSet<Student> Students { get; set; }

    protected override void OnConfiguring(DbContextOptionsBuilder optionsBuilder)
    {
        optionsBuilder.UseSqlServer("Server=localhost,1433;Database=CrudDemoDb;User Id=sa;Password=ga123!@#;");
    }
}