using Hangman.Entities;

namespace Hangman.Services
{
    public interface IWordService
    {
        public Session GetSession(int id = 0);

        public Session AddLetter(int sessionId, char letter);
    }
}
