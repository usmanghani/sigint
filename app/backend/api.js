const express = require('express');

let app = express();


app.use(require('./controllers'))



app.listen(3030, function () {
  console.log('Example app listening on port 3000!');
});

module.exports = app;
