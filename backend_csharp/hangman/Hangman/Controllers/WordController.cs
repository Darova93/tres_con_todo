using Hangman.Entities;
using Hangman.Services;
using Microsoft.AspNetCore.Mvc;

namespace Hangman.Controllers
{
    [ApiController]
    [Route("[controller]")]
    public class WordController : ControllerBase
    {

        private readonly IWordService wordService;

        public WordController(IWordService _wordService)
        {
            wordService = _wordService;
        }

        [HttpGet(Name = "GetSession")]
        public Session GetSession(int id = 0)
        {
            return wordService.GetSession(id);
        }


        [HttpPost(Name = "AddLetter")]
        public Session AddLetter(int sessionId, char letter)
        {
            return wordService.AddLetter(sessionId, letter);
        }
    }
}
