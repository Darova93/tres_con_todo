namespace Hangman.Entities
{
    public class Session
    {
        public int Id { get; set; }
        public int WordId { get; set; }
        public int? NumberOfLetters { get; set; }
        public int? Attempts { get; set; } = 0;
        public bool? Success { get; set; } = false;
        public char[]? Letters { get; set; } = Array.Empty<char>();
    }
}
