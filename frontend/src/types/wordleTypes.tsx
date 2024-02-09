export type WordleRequest = {
    word:string
}

export type WordData = {
    word: string,
    missplaced: number[],
    fails: number[],
    correct: number[]
}

export type GameState = {
    status: Status,
    words: WordData[]
}

export enum Status {
    CONTINUE = "CONTINUE",
    NEW = "NEW",
    WIN = "WIN",
    LOSS = "LOSS"
}
