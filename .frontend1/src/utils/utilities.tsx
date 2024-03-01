export const initializeDocumentHead = () => {
    const scriptTag = document.createElement('script');
    const metaTag = document.createElement('meta');
    const noReferrer = document.createElement('meta');
    scriptTag.src = "https://apis.google.com/js/platform.js";
    scriptTag.async = true;
    scriptTag.defer = true;
    metaTag.name = "google-signin-client_id";
    metaTag.content = "349040231335-se4eve4roq1tmkvoi3k2b0ddkp87mhfg.apps.googleusercontent.com";
    noReferrer.name = "Referrer-Policy";
    noReferrer.content = "no-referrer-when-downgrade";

    document.getElementsByTagName("head")[0].appendChild(scriptTag);
    document.getElementsByTagName("head")[0].appendChild(metaTag);
    document.getElementsByTagName("head")[0].appendChild(noReferrer);
}
