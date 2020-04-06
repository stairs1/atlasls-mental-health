import React, { Component } from "react";
import { Link } from "react-router-dom";

class JournalRecommendations extends Component {
  constructor(props) {
    super(props);
    this.state = {
      data: [],
      loaded: false,
      placeholder: "Loading",
    };
  }

  componentDidMount() {
    fetch("api/journals")
      .then((response) => {
        if (response.status > 400) {
          return this.setState(() => {
            return { placeholder: "Bad stuff went down" };
          });
        }
        return response.json();
      })
      .then((data) => {
        this.setState(() => {
          return {
            data,
            loaded: true,
          };
        });
      });
  }
  render() {
    return (
      <div>
        <h3>Recommended research papers</h3>
        <ul>
          {this.state.data.map((journalStub) => {
            return <li>{journalStub.title}</li>;
          })}
        </ul>
        <Link to="/survey">
          <button>Take Survey</button>
        </Link>
      </div>
    );
  }
}

export default JournalRecommendations;