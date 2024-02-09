import { WordData } from "../../types/wordleTypes"
import WordleLetter from "./wordleLettter"

const WordleWord = ({value, index, className=""} : {value: WordData, index:number, className:string}) => {
    const classes = {
        correct: "correct",
        missing: "missing",
        fails: "fails"
    }

    const getLetterClass = (value:WordData, index:number):string => {
        if(value.correct.includes(index)) return classes.correct
        if(value.missplaced.includes(index)) return classes.missing
        if(value.fails.includes(index)) return classes.fails

        return ""
    }

    return (
        <div className={`word ${className}`}>
            {value.word.split("").map((letter, index) => 
                <WordleLetter key={`letter-${letter}-${index}`} letter={letter} index={index} className={getLetterClass(value, index)}/>
            )}
        </div>
    )
}

export default WordleWord
