const WordleLetter = ({ letter, className }: { letter: string; className: string }) => {
    return <div className={`letter ${className}`}>{letter}</div>;
};

export default WordleLetter;
