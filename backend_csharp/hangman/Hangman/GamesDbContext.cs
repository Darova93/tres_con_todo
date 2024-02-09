using Hangman.Entities;
using Microsoft.EntityFrameworkCore;
using MongoDB.EntityFrameworkCore.Extensions;

namespace Hangman
{
    public class GamesDbContext : DbContext
    {
        public DbSet<Word> Words { get; init; }
        public DbSet<Session> Sessions { get; init; }

        public GamesDbContext(DbContextOptions options)
            : base(options)
        {
        }
        protected override void OnModelCreating(ModelBuilder modelBuilder)
        {
            base.OnModelCreating(modelBuilder);
            modelBuilder.Entity<Word>().ToCollection("words");
            modelBuilder.Entity<Session>().ToCollection("session");
        }
    }
}
