import React, { Component, PropTypes } from 'react';
import { connect } from 'react-redux';
import { get } from 'lodash';
import FileInput from 'react-file-input';

class App extends Component {
  constructor(props) {
    super(props);
    this.handleChange = this.handleChange.bind(this);
  }

  componentDidMount() {
  }

  componentWillReceiveProps(nextProps) {
  }

  handleChange(event) {
    console.log(event);
  }

  render() {
    return (
      <div>
        <FileInput
          placeholder="audio file (.wav)"
          accept=".wav"
          name = "swig"
          className="arr"
          onChange={this.handleChange}
        />
      </div>
    )
  }
}

App.propTypes = {};

function mapStateToProps(state, ownProps) {
  return {};
}

function mapDispatchToProps(dispatch, ownProps){
  return {};
}

export default connect(mapStateToProps, mapDispatchToProps)(App)
