// add api for https://www.ibm.com/watson/developercloud/alchemy-language/api/v1/#combined-call
// get ngrams api call
// basic ui for upload documents and show responces
// twillio streaming
// javascript show waveform
// sales force integration
// timelines

const express = require('express');

let router = express.Router();

router.use('/speech', require('./speech'))
router.use('/text', require('./text'))

router.get('/', function (req, res) {
  res.status(200).send('OK');
});


module.exports = router;
