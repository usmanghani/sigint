let app = new (require('express'))()
let busboy = require('connect-busboy')


let port = 3000

// middleware
app.use(busboy());


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
