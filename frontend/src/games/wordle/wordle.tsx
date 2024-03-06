import { useEffect, useRef, useState } from "react";
import { GameState, Status, WordData } from "../../types/wordleTypes";
import Keyboard from "../shared/keyboard";
import "./styles.scss";
import WordleWord from "./wordleWord";
const apiURL = import.meta.env.VITE_API_PATH;

const Wordle = () => {
    const [currentWord, setCurrentWord] = useState<string>(" ");
    const [gameState, setGameState] = useState<GameState>();
    const [wordList, setWordList] = useState<WordData[]>();
    const [playing, setPlaying] = useState<boolean>(true);
    const [gameWon, setGameWon] = useState(false);
    const [animateGuess, setAnimateGuess] = useState<boolean>(true);
    const wordleRef = useRef<HTMLDivElement | null>(null);

    useEffect(() => {
        wordleRef.current?.focus();
    }, []);

    useEffect(() => {
        const lastGuess = document.getElementsByClassName("last-guess")[0];
        if (animateGuess) guessAnimation(lastGuess);
    }, [wordList, animateGuess]);

    const guessAnimation = (guess: Element) => {
        if (guess) {
            Array.from(guess.getElementsByClassName("letter"))?.forEach((element, index) => {
                setTimeout(() => {
                    element
                        .animate(
                            { transform: ["rotateX(0)", "rotateX(90deg)"] },
                            { duration: 250, iterations: 1, easing: "ease-in" }
                        )
                        .addEventListener("finish", () => {
                            if (element.classList.contains("correct")) element.classList.add("correctGuessed");
                            if (element.classList.contains("missing")) element.classList.add("missingGuessed");
                            if (element.classList.contains("fails")) element.classList.add("failGuessed");
                            element.animate(
                                { transform: ["rotateX(90deg)", "rotateX(0)"] },
                                { duration: 250, iterations: 1, easing: "ease-out" }
                            );
                        });
                }, (index * 500) / 2);
            });
        }
    };

    const handleKeyDown = (char: string) => {
        if (!playing) return;
        const word = currentWord;
        if (char === "ENTER") {
            handleEnter();
            return;
        }
        if (char === "BACKSPACE" || char === "DELETE") {
            setCurrentWord(word.slice(0, -1) || " ");
            return;
        }
        if (isLetter(char) && word.length < 5) {
            setCurrentWord(word.trim() + char);
            return;
        }
        shakeWord();
    };

    const createPayload = (): GameState => {
        const wordsPlaying: WordData[] = wordList ? wordList : [];

        wordsPlaying.push({
            word: currentWord,
            correct: [],
            missplaced: [],
            fails: [],
        });

        const payload = {
            status: gameState?.status || Status.NEW,
            words: wordsPlaying,
        };
        return payload;
    };

    const isLetter = (char: string) => {
        return char.length === 1 && char.match(/[a-zñ]/i) != null;
    };

    const handleEnter = async () => {
        if (currentWord.length < 5) {
            shakeWord();
            return;
        }
        try {
            const serverResponse = await wordRequest(apiURL, createPayload());
            processResponse(serverResponse);
        } catch (e) {
            console.log(e);
        }
    };

    const shakeWord = () => {
        document.getElementsByClassName("current-word")[0].animate(
            {
                transform: [
                    "translate(-5%)",
                    "translateX(5%)",
                    "translateX(-10%)",
                    "translateX(10%)",
                    "translateX(-5%)",
                    "translateX(0)",
                ],
                offset: [0.1, 0.3, 0.5, 0.7, 0.9, 1],
            },
            {
                duration: 150,
                iterations: 1,
                easing: "ease-in-out",
            }
        );
    };

    const endGame = (won: boolean) => {
        setCurrentWord("");
        setPlaying(false);
        setGameWon(won);
    };

    const processResponse = (serverResponse: GameState) => {
        if (serverResponse.status === Status.WIN) endGame(true);
        if (serverResponse.status === Status.LOSS) endGame(false);
        if (serverResponse.words[serverResponse.words.length - 1]?.word !== currentWord) {
            shakeWord();
            setAnimateGuess(false);
        } else {
            setAnimateGuess(true);
        }
        setGameState(serverResponse);
        setWordList((prevList) => serverResponse.words ?? prevList?.push(serverResponse.words));
        setCurrentWord(" ");
    };

    const wordRequest = async (url: string, data: GameState) => {
        try {
            const response = await fetch(url, {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify(data),
            });

            if (!response.ok) {
                throw new Error("Fail");
            }
            return await response.json();
        } catch (error) {
            console.error("Error:", error);
        }
    };

    const getCurrentLetters = () => {
        return wordList?.reduce((usedLetters: Set<string>, value: WordData): Set<string> => {
            [...value.word].forEach((char) => {
                usedLetters.add(char);
            });
            return usedLetters;
        }, new Set<string>());
    };

    return (
        <>
            {!gameWon && !playing && (
                <div className="you-lose">
                    <div className="you-lose-text"></div>YOU LOSE
                </div>
            )}
            {gameWon && !playing && (
                <div className="you-win">
                    <div className="you-win-text"></div>
                </div>
            )}
            <div
                tabIndex={-1}
                ref={wordleRef}
                className="wordle"
                onKeyDown={(event) => handleKeyDown(event.key.toString().toUpperCase())}
            >
                <div className="words-wrapper">
                    {wordList?.map((value, index) => (
                        <WordleWord
                            key={`word-${value.word}-${index}`}
                            value={value}
                            className={index === wordList.length - 1 ? "last-guess" : "past-guess"}
                        />
                    ))}
                    {playing && (
                        <WordleWord
                            key={`current-word`}
                            value={{ word: currentWord, correct: [], missplaced: [], fails: [] }}
                            className="current-word"
                        />
                    )}
                </div>
                <div className="keyboard-wrapper">
                    <Keyboard
                        usedLetters={getCurrentLetters() || new Set()}
                        keyClickHandler={(key) => handleKeyDown(key)}
                    ></Keyboard>
                </div>
            </div>
        </>
    );
};

export default Wordle;
