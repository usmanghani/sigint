import React, { Component, PropTypes } from 'react';

const DEFAULT_LISTEN_INTERVAL = 100;


// note to self look into howler to make a nicer player
class ReactAudioPlayer extends Component {
  componentDidMount() {
    const audio = this.audioEl;

    audio.addEventListener('error', (e) => {
      this.props.onError && this.props.onError(e);
    });

    // When enough of the file has downloaded to start playing
    audio.addEventListener('canplay', (e) => {
      this.props.onCanPlay && this.props.onCanPlay(e);
    });

    // When enough of the file has downloaded to play the entire file
    audio.addEventListener('canplaythrough', (e) => {
      this.props.onCanPlayThrough && this.props.onCanPlayThrough(e);
    });

    // When audio play starts
    audio.addEventListener('playing', (e) => {
      this.setListenTrack();
      this.props.onPlay && this.props.onPlay(e);
    });

    // When unloading the audio player (switching to another src)
    audio.addEventListener('abort', (e) => {
      this.clearListenTrack();
      this.props.onAbort && this.props.onAbort(e);
    });

    // When the file has finished playing to the end
    audio.addEventListener('ended', (e) => {
      this.clearListenTrack();
      this.props.onEnded && this.props.onEnded(e);
    });

    // When the user pauses playback
    audio.addEventListener('pause', (e) => {
      this.clearListenTrack();
      this.props.onPause && this.props.onPause(e);
    });

    // When the user drags the time indicator to a new time
    audio.addEventListener('seeked', (e) => {
      this.clearListenTrack();
      this.props.onSeeked && this.props.onSeeked(e);
    });

    if (this.props.startTime){
      audio.currentTime = this.props.startTime;
    }
  }

  componentWillReceiveProps(nextProps) {
    const audio = this.audioEl;
    if (nextProps.selectedPlayerEvent) {
      audio.currentTime = nextProps.selectedPlayerEvent.playTime;
      audio.play();
    }

    // time reset programaticly not from seek
    if (nextProps.startTime !== this.props.startTime){
      audio.currentTime = nextProps.startTime;
      audio.play();
    }
  }

  /**
   * Set an interval to call props.onListen every props.listenInterval time period
   */
  setListenTrack() {
    if (!this.listenTracker) {
      const listenInterval = this.props.listenInterval || DEFAULT_LISTEN_INTERVAL;
      this.listenTracker = setInterval(() => {
        this.props.onListen && this.props.onListen(this.audioEl.currentTime);
      }, listenInterval);
    }
  }

  /**
   * Clear the onListen interval
   */
  clearListenTrack() {
    if (this.listenTracker) {
      clearInterval(this.listenTracker);
      this.listenTracker = null;
    }
  }

  render() {
    const incompatibilityMessage = this.props.children || (
      <p>Your browser does not support the <code>audio</code> element.</p>
    );

    return (
      <audio
        className="react-audio-player"
        src={this.props.src}
        autoPlay={this.props.autoPlay}
        preload={this.props.preload}
        controls
        ref={(ref) => this.audioEl = ref}
        onPlay={this.onPlay}
      >
        {incompatibilityMessage}
      </audio>
    );
  }
}

ReactAudioPlayer.propTypes = {
  autoPlay: PropTypes.string,
  children: PropTypes.array,
  listenInterval: PropTypes.number,
  onAbort: PropTypes.func,
  onCanPlay: PropTypes.func,
  onCanPlayThrough: PropTypes.func,
  onEnded: PropTypes.func,
  onError: PropTypes.func,
  onListen: PropTypes.func,
  onPause: PropTypes.func,
  onPlay: PropTypes.func,
  onSeeked: PropTypes.func,
  preload: PropTypes.string,
  src: PropTypes.string,
  startTime: PropTypes.number,
};

export default ReactAudioPlayer;
