import React, {Component} from 'react';
import logo from './logo.svg';
import './App.css';
import io from "socket.io-client";

class App extends Component {

  componentDidMount() {
    const socket = io('http://localhost:5001' + `/socket/test`);
    socket.on('data', data => {
      console.log("recieving");
    });
  }

  render() {
    return (
      <div className="App">
        <header className="App-header">
          <img
            src={logo}
            className="App-logo"
            alt="logo"
          />
          <h1 className="App-title">Welcome to React</h1>
        </header>
        <p className="App-intro">
          To get started, edit <code>src/App.js</code> and save to reload.
        </p>
      </div>
    );
  }
}

export default App;
