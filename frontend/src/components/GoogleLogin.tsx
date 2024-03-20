import GLogo from "../assets/Google_G_logo.svg";
const loginURL = import.meta.env.VITE_LOGIN_PATH;

export function GoogleLogin() {
    const loginRequest = async () => {
        try {
            const response = await fetch(loginURL, {
                method: "POST",
                redirect: "follow",
            });
            const result = await response.json();
            window.location.assign(result.auth_url);
        } catch (error) {
            console.error("Error:", error);
        }
    };
    return (
        <>
            <button onClick={loginRequest}>
                <img src={GLogo} />
                <label>Login with Google</label>
            </button>
        </>
    );
}
