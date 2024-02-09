import { useEffect, useState } from "react";
import { GameState, Status, WordData } from "../../types/wordleTypes";
import Keyboard from "../shared/keyboard";
import "./styles.scss";
import WordleWord from "./wordleWord";
const apiURL: string = process.env.REACT_APP_LOCALHOST as string;

const Wordle = () => {
    const [currentWord, setCurrentWord] = useState<string>(" ");
    const [gameState, setGameState] = useState<GameState>();
    const [wordList, setWordList] = useState<WordData[]>();
    const [playing, setPlaying] = useState<boolean>(true);

    useEffect(() => {
        const lastGuess = document.getElementsByClassName("last-guess")[0];
        guessAnimation(lastGuess);
    }, [wordList]);

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
        let word = currentWord;
        if (word.includes(" ")) word = word.slice(0, -1);
        if (char === "ENTER") {
            handleEnter();
            return;
        }
        if (!isLetter(char) && !(char === "BACKSPACE")) {
            shakeWord();
            return;
        }
        if (isLetter(char) && word.length < 5) word += char;
        if (char === "BACKSPACE") {
            word = word.slice(0, -1);
        }
        if (word.length === 0) word = " ";
        setCurrentWord(word);
    };

    const createPayload = (): GameState => {
        let wordsPlaying: WordData[] = wordList ? wordList : [];

        wordsPlaying.push({
            word: currentWord,
            correct: [],
            missplaced: [],
            fails: [],
        });

        let payload = {
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

    const endGame = () => {
        setCurrentWord("");
        setPlaying(false);
    };

    const processResponse = (serverResponse: GameState) => {
        if (serverResponse.status === Status.WIN) endGame();
        if (serverResponse.status === Status.LOSS) endGame();
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
            <div
                tabIndex={0}
                className="wordle"
                onKeyDown={(event) => handleKeyDown(event.key.toString().toUpperCase())}
            >
                <div className="words-wrapper">
                    {wordList?.map((value, index) => (
                        <WordleWord
                            key={`word-${value.word}-${index}`}
                            value={value}
                            index={index}
                            className={index === wordList.length - 1 ? "last-guess" : "past-guess"}
                        />
                    ))}
                    {playing && (
                        <WordleWord
                            key={`current-word`}
                            value={{ word: currentWord, correct: [], missplaced: [], fails: [] }}
                            index={currentWord.length - 1}
                            className="current-word"
                        />
                    )}
                </div>
                <Keyboard
                    usedLetters={getCurrentLetters() || new Set()}
                    keyClickHandler={(key) => handleKeyDown(key)}
                ></Keyboard>
            </div>
        </>
    );
};

export default Wordle;
