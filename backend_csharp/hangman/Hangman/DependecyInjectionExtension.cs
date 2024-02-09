using Hangman.Services;
using Microsoft.EntityFrameworkCore;
using MongoDB.Driver;

namespace Hangman
{
    public static class DependecyInjectionExtension
    {
        public static IServiceCollection AddDependencyInjection(this IServiceCollection services)
        {
            services.AddHttpContextAccessor();

            //DB context
            var connectionString = "mongodb+srv://games-dev:exK0juZnNZJzaJQK@west-cluster.p2tfglm.mongodb.net/?retryWrites=true&w=majority";
            var client = new MongoClient(connectionString);
            services.AddDbContext<GamesDbContext>((DbContextOptionsBuilder builder) => builder.UseMongoDB(client, "games"));

            services.AddScoped<IWordService>((IServiceProvider sp) => new WordService(sp.GetService<GamesDbContext>()));

            return services;
        }
    }
}
