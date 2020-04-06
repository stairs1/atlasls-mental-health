import React, { Component } from "react";
import { Link } from "react-router-dom";

class SignIn extends Component {
  constructor(props) {
    super(props);
  }

  render() {
    return (
      <div>
        <h3>Welcome to the sign in page</h3>
        <form>
          <label>
            Username:
            <input type="text" name="username" />
          </label>
          <div />
          <label>
            Password:
            <input type="password" name="password" />
          </label>
          <Link to="/survey">
            <input type="submit" value="Sign In" />
          </Link>
        </form>
      </div>
    );
  }
}

export default SignIn;
