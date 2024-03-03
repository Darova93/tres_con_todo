import "@testing-library/jest-dom";
import { fireEvent, render, screen } from "@testing-library/react";
import { BrowserRouter } from "react-router-dom";
import { expect, test } from "vitest";
import Wordle from "../games/wordle/wordle";

test("loads wordle", () => {
    const keys = [
        "Q",
        "W",
        "E",
        "R",
        "T",
        "Y",
        "O",
        "U",
        "P",
        "A",
        "S",
        "D",
        "F",
        "G",
        "H",
        "J",
        "K",
        "L",
        "Ñ",
        "ENTER",
        "Z",
        "X",
        "C",
        "V",
        "B",
        "N",
        "M",
        "DELETE",
    ];
    render(
        <BrowserRouter>
            <Wordle />
        </BrowserRouter>
    );
    keys.forEach((key) => {
        const button = screen.getByText(key);
        expect(button).toBeInTheDocument();
    });
});

test("loads wordle and can insert letters", () => {
    const word = ["P", "A", "T", "O", "S"];
    render(
        <BrowserRouter>
            <Wordle />
        </BrowserRouter>
    );
    word.forEach((letter) => {
        fireEvent.click(screen.getByText(letter));
        expect(screen.getAllByText(letter).length).toBeGreaterThanOrEqual(2);
    });
});
