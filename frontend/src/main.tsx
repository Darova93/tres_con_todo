import React from "react";
import ReactDOM from "react-dom/client";
import App from "./App";
import { initializeDocumentHead } from "./utils/utilities";

const root = ReactDOM.createRoot(document.getElementById("root") as HTMLElement);
initializeDocumentHead();

root.render(
    <React.StrictMode>
        <App />
    </React.StrictMode>
);
