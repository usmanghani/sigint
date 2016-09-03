const express = require('express');

let router = express.Router();

router.use('/speech',require('./speech'))

router.get('/', function (req, res) {
  res.status(200).send('OK');
});


module.exports = router;
