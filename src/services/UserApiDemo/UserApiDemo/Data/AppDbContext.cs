using Microsoft.EntityFrameworkCore;
using UserApiDemo.Models;
namespace UserApiDemo.Data
{
    public class AppDbContext : DbContext
    {
        public AppDbContext(DbContextOptions<AppDbContext> options) : base(options) {}

        public DbSet<User> Users => Set<User>();
    }
}
