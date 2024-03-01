import { fireEvent, render, screen } from "@testing-library/react";
import React from "react";
import { BrowserRouter } from "react-router-dom";
import Wordle from "../games/wordle/wordle";

test("loads wordle and can insert letters", () => {
    render(
        <BrowserRouter>
            <Wordle />
        </BrowserRouter>
    );
    fireEvent.click(screen.getByText("Q"));
    expect(screen.getAllByText("Q").length).toBeGreaterThan(2);
});
