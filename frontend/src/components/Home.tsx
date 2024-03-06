import { Link } from "react-router-dom";
import pastorTaco from "../assets/icons/pastor-taco512.png";
import "./HomeStyles.scss";

const Home = () => {
    return (
        <div className="home-container">
            <img src={pastorTaco} />
            <Link to={"/wordle"}>Juega Wordle</Link>
            <h3>tres con todo</h3>
        </div>
    );
};
export default Home;
