const WordleLetter = ({letter, index, className} : {letter:string, index:number, className:string}) => {
    return(
            <div className={`letter ${className}`}>
                {letter}
            </div>
    )
}

export default WordleLetter
