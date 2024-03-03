import "@testing-library/jest-dom";
import { render, screen } from "@testing-library/react";
import { BrowserRouter } from "react-router-dom";
import { expect, test } from "vitest";
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
