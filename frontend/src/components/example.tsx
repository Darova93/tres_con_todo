import {useState, useEffect} from "react";

function Example() {
  const [response, setResponse] = useState({});

  useEffect(() => {
    fetch('http://127.0.0.1:5000')
      .then(res => {
        return res.json();
      })
      .then((res) => {
        setResponse(res)
      })
      .catch(_ => {
        setResponse({message: "There was an error fetching the request"});
      });
  }, []);

  return (
    <div>
        {JSON.stringify(response)}
    </div>
  );
}

export default Example;
