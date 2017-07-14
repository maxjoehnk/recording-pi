import React from 'react';
import Button from 'material-ui/Button';
import { connect } from 'react-redux';
import { startRecording, stopRecording } from '../../store/actions/recording';

const RecordButton = ({ recording, onStartRecording, onStopRecording }) => (
    <Button raised onClick={() => recording ? onStopRecording() : onStartRecording()}>{recording ? 'Stop' : 'Start'} Recording</Button>
);

const mapStateToProps = state => ({
    recording: state.recording
});

const mapDispatchToProps = dispatch => ({
    onStartRecording: () => dispatch(startRecording()),
    onStopRecording: () => dispatch(stopRecording())
});

export default connect(mapStateToProps, mapDispatchToProps)(RecordButton);
