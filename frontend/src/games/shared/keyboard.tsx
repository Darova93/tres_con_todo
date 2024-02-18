import './keyboard.scss';

type KeyboardLetterProps = {
    letter: string,
    isUsed: boolean,
    onKeyClickHandler: (letter: string) => void
}
const KeyboardLetter = ({letter, isUsed, onKeyClickHandler}: KeyboardLetterProps) => {
    return (
        <span
            className={
                'keyboard__letter ' +
                (letter.length > 1 ? 'keyboard__long' : '') +
                (isUsed ? 'keyboard__used-letter' : '')
            }
            onClick={() => onKeyClickHandler(letter)}
        >
            {letter}
        </span>
    );
};

type KeyboardProps = {
    usedLetters: Set<string>,
    keyClickHandler: (letter: string) => void
}

const Keyboard = ({usedLetters, keyClickHandler}: KeyboardProps) => {
    const qwerty: string[][] = [
        'qwertyuiop'.toUpperCase().split(''),
        'asdfghjklñ'.toUpperCase().split(''),
        'zxcvbnm'.toUpperCase().split('')
    ];
    qwerty[2].push('DELETE');
    qwerty[2].unshift('ENTER');
    return (
        <div className='keyboard'>
            {qwerty.map((letters, index) => {
                return (
                    <div key={index} className='keyboard__line'>
                        {letters.map((letter, index) =>
                            <KeyboardLetter
                                key={index}
                                letter={letter}
                                onKeyClickHandler={keyClickHandler}
                                isUsed={usedLetters.has(letter)}
                            />)}
                    </div>
                );
            })}
        </div>
    )
};

export default Keyboard;
