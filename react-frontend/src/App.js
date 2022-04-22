import React, { useState } from "react";
import './App.css';
import axios from 'axios'
import * as ReactBootstrap from 'react-bootstrap';

import logo from './assets/yt_logo.svg';     
      

const App = () => {
  const [url, setUrl] = useState(null);
  const [output, setOutput] = useState(null);
  const [error, setError] = useState(null);
  const [loading, setLoading] = useState(false);

  const onUrlChange = e => setUrl(e.target.value);

  const urlFunction = async () => {
    setLoading(true) //starts spinner
    try {
      const data = await axios.post("/getResult", { url: url, })
        .then(res => {
          console.log(res)
          setOutput(res.data.response)
          setError(res.data.error)
        }).finally(function () {
          setLoading(false) //stop spinner
        });
    } catch (e) {
      console.log(e)
    }
  };


  return (
    <div className='homepage'>
      <label>
      <img src={logo} className='logo'/>
        YouTube Video URL:
      </label>
      <input className='input' placeholder="URL" type="text" value={url} onChange={onUrlChange} />
      <br />
      <button className='submitbtn submitbtn-lg' type="submit" onClick={urlFunction}>
        Submit
      </button>
      {loading ? (<ReactBootstrap.Spinner animation="grow" />) : ({error} ? (<p className='error'>{error}</p>) : (<p>"Success"</p>))}
    </div>
  );
}

export default App;