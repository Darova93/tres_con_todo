import { WordData } from "../../types/wordleTypes"

export const getMockResponse = (): WordData[] => {
    return [
        // {word: "HOTEL", missplaced: [4], fails: [0, 1, 2], correct: [3]},
        // {word: "MOTEL", missplaced: [4], fails: [0, 1, 2], correct: [3]},
        {word: "LUNAS", missplaced: [], fails: [3], correct: [0, 1, 2, 4]}
    ]
}
