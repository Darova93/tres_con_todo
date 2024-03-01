import React from "react";
import { Navigate, Route, Routes } from "react-router";
import { BrowserRouter } from "react-router-dom";
import GoogleLogin from "./components/GoogleLogin";
import Home from "./components/Home";
import Wordle from "./games/wordle/wordle";
import "./styles/global.scss";

function App() {
    return (
        <div className="App">
            <div className="App-header">
                <BrowserRouter>
                    <Routes>
                        <Route path="/" element={<Home />} />
                        <Route path="/wordle" element={<Wordle />} />
                        <Route path="*" element={<Navigate replace to="/" />} />
                    </Routes>
                </BrowserRouter>
            </div>
        </div>
    );
}

export default App;
