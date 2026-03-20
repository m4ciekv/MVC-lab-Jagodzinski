using Microsoft.EntityFrameworkCore;

namespace MvcMovie.Models;

public class MvcMovieContext : DbContext
{
    public MvcMovieContext(DbContextOptions<MvcMovieContext> options)
        : base(options)
    {
    }

    public DbSet<Movie> Movies { get; set; }
}