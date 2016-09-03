const express = require('express');
const SpeechToTextV1 = require('watson-developer-cloud/speech-to-text/v1');
const ibmCredentials = require('../secrets.json').ibm.credentials

var speechToText = new SpeechToTextV1(ibmCredentials);

var params = {
  content_type: 'audio/wav'
};


// create the stream
var recognizeStream = speech_to_text.createRecognizeStream(params);

// pipe in some audio
fs.createReadStream(__dirname + '/resources/speech.wav').pipe(recognizeStream);

// and pipe out the transcription
recognizeStream.pipe(fs.createWriteStream('transcription.txt'));


// listen for 'data' events for just the final text
// listen for 'results' events to get the raw JSON with interim results, timings, etc.

recognizeStream.setEncoding('utf8'); // to get strings instead of Buffers from `data` events

['data', 'results', 'error', 'connection-close'].forEach(function(eventName) {
  recognizeStream.on(eventName, console.log.bind(console, eventName + ' event: '));
});


let router = express.Router();

router.get('/transcibe', function (req, res) {
  res.status(200).send('OK');
});


module.exports = router;
