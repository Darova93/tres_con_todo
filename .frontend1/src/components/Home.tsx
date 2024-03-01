import React from "react";
import { Link } from "react-router-dom";
const Home = () => {
    return (
        <>
            <ul>
                <li>
                    <Link to={"/wordle"}>Juega Wordle</Link>
                </li>
            </ul>
        </>
    );
};
export default Home;
