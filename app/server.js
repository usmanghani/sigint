var app = new (require('express'))()
var port = 3000

// holding place root api should point to a frontend
app.get('/', function (req, res) {
  res.status(200).send('OK');
});

app.use('/api', require('./backend/api'));

app.listen(port, function(error) {
  if (error) {
    console.error(error)
  } else {
    console.info('==> 🌎  Listening on port %s. Open up http://localhost:%s/ in your browser.', port, port)
  }
})
