import React, { Component } from "react";
import { render } from "react-dom";
import JournalRecommendations from "./JournalRecommendations";
import { BrowserRouter as Router, Switch, Route, Link } from "react-router-dom";

class App extends Component {
  constructor(props) {
    super(props);
  }

  render() {
    return (
      <Router>
        <div>
          <Switch>
            <Route path="/">
              <JournalRecommendations />
            </Route>
          </Switch>
        </div>
      </Router>
    );
  }
}

export default App;

const container = document.getElementById("app");
render(<App />, container);
