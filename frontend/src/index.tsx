import React from "react";
import ReactDOM from "react-dom/client";
import { BrowserRouter } from "react-router-dom";
import { initializeDocumentHead } from "../src/utils/utilities";
import App from "./App";
import "./index.css";

const root = ReactDOM.createRoot(document.getElementById("root") as HTMLElement);
initializeDocumentHead();

root.render(
    <React.StrictMode>
        <App />
    </React.StrictMode>
);
