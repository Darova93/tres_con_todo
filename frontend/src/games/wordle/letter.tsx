export enum LetterState {
  Blank = "blank",
  Incorrect = "incorrect",
  Correct = "correct",
  Empty = "empty",
}

export const Letter = ({
    letter, letterState
} : {letter: string, letterState: LetterState}) => {

    return(
        <div className={`letter ${letterState}`}>
            {letterState === LetterState.Empty ? " " : letter.trim().charAt(0)}
        </div>
    );
};
