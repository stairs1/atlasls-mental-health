import React, { Component } from "react";
import { render } from "react-dom";
import JournalRecommendations from "./JournalRecommendations";
import Survey from "./Survey";
import { BrowserRouter as Router, Switch, Route } from "react-router-dom";
import SignIn from "./SignIn";

class App extends Component {
  constructor(props) {
    super(props);
  }

  render() {
    return (
      <Router>
        <div>
          <Switch>
            <Route path="/journal_recommendations">
              <JournalRecommendations />
            </Route>
            <Route path="/survey">
                <Survey />
            </Route>
            <Route path="/">
                <SignIn />
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
