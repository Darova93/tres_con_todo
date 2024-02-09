using Hangman.Entities;
using MongoDB.Driver;
using MongoDB.Driver.Linq;

namespace Hangman.Services
{
    public class WordService : IWordService
    {
        private readonly GamesDbContext dbContext;

        public WordService(GamesDbContext _dbContext)
        {
            dbContext = _dbContext;
        }

        public Session AddLetter(int sessionId, char letter)
        {
            Session? session = dbContext.Sessions.Where(x => x.Id == sessionId).FirstOrDefault();
            Word? word = dbContext.Words.Where(x => x.Id == session.WordId).FirstOrDefault();
            if (word != null && session != null)
            {
                if (!word.Name.Contains(letter))
                {
                    session.Attempts++;
                    if (session.Attempts == 6)
                    {
                        session.Success = false;
                        dbContext.SaveChanges();
                    }
                }

                session.Letters = (char[]?)session.Letters.Append(letter).ToArray();
                var lettersInWord = word.Name.Distinct();
                session.Success = lettersInWord.All(s => session.Letters.Contains(s));
                dbContext.SaveChanges();

            }
            return session ?? throw new Exception("cant find any session");
        }

        public Session GetSession(int id = 0)
        {
            if (id == 0)
            {
                Session? lastSession = dbContext.Sessions.OrderBy(x => x.Id).ToList().LastOrDefault() ?? throw new Exception("cant find any session");
                id = lastSession?.Id + 1 ?? 0;

                Word newWord = GetWord();

                dbContext.Sessions.Add(new Session { Id = id, WordId = newWord.Id, NumberOfLetters = newWord.Name?.Length ?? 0 });
                dbContext.SaveChanges();
            }

            Session? session = dbContext.Sessions.Where(x => x.Id == id).FirstOrDefault();
            return session ?? throw new Exception("cant find any session");
        }

        private Word GetWord()
        {
            Random rnd = new();
            int wordsCount = dbContext.Words.Count();
            int wordId = rnd.Next(wordsCount + 1);

            Word? word = dbContext.Words.Where(x => x.Id == wordId).FirstOrDefault();

            return word ?? throw new Exception("cant find any word");
        }
    }
}
