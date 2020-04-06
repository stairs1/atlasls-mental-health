import React, { Component } from "react";
import { Link } from "react-router-dom";

class Survey extends Component {
  constructor(props) {
    super(props);
    this.state = {};
  }

  render() {
    return (
      <div>
        <h3>Take the Questionnaire</h3>
        <p>Q1</p>
        <Link to="/journal_recommendations">
            <button>Submit</button> 
        </Link>
      </div>
    );
  }
}

export default Survey;