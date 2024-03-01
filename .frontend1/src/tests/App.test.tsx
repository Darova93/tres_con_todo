import { render, screen } from "@testing-library/react";
import React from "react";
import { BrowserRouter } from "react-router-dom";
import Home from "../components/Home";

test("renders learn react link", () => {
    render(
        <BrowserRouter>
            <Home />
        </BrowserRouter>
    );
    const linkElement = screen.getByText(/Juega Wordle/i);
    expect(linkElement).toBeInTheDocument();
});
