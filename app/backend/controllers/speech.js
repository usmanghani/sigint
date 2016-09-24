const express = require('express');
const fs = require('fs');
const watson = require('watson-developer-cloud');
const ibmCredentials = require('../secrets.json').ibm_speech.credentials



let transcibe = function(audio_file_path, callback){
  let speech_to_text = watson.speech_to_text(ibmCredentials);
  let params = {
    audio: fs.createReadStream(audio_file_path),
    content_type: 'audio/wav',
    timestamps: true,
    word_alternatives_threshold: 0.9,
    continuous: true
  };

  speech_to_text.recognize(params, callback);
};

let router = express.Router();

router.post('/transcibe', function(req, res) {
  req.pipe(req.busboy);
  req.busboy.on('file', function(fieldname, file, filename) {
    var fstream = fs.createWriteStream(`tmp/${fieldname}`);
    fstream.on('close', function () {
      transcibe(`tmp/${fieldname}`, function(error, transcript){
        if (error) {
          res.status(500).send({'error': error});
        } else {
          res.send(JSON.stringify(transcript, null, 2));
        }
      });
    });
    file.pipe(fstream);
  });
});

module.exports = router;
