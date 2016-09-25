import React, { Component, PropTypes } from 'react';
import { bindActionCreators } from 'redux'
import { connect } from 'react-redux';
import { get } from 'lodash';
import FileInput from 'react-file-input';

import { loadFile } from '../actions';
import ReactAudioPlayer from './Player.js';

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
    // no files
    if (!event.target.files.length){
      return
    }
    let file = event.target.files[0];

    this.props.loadFile(file);
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
        {(() => {
          if (this.props.dataUrl){
            return <ReactAudioPlayer
              src={this.props.dataUrl}
            />
          }
        })()}
      </div>
    )
  }
}

App.propTypes = {};

function mapStateToProps(state, ownProps) {
  return {
    file: state.file,
    dataUrl: state.dataUrl,
  };
}

function mapDispatchToProps(dispatch, ownProps){
  return bindActionCreators({
    loadFile
  },
    dispatch
  )
}

export default connect(mapStateToProps, mapDispatchToProps)(App)
