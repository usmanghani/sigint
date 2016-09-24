const express = require('express');
const webpack = require('webpack');
const webpackDevMiddleware = require('webpack-dev-middleware');
const webpackHotMiddleware = require('webpack-hot-middleware');
const config = require('./webpack.config');

let app = express();
let busboy = require('connect-busboy');

let port = 3000;

// middleware
const compiler = webpack(config);
app.use(webpackDevMiddleware(compiler, {
  noInfo: true,
  publicPath: config.output.publicPath,
  stats: { colors: true},
  hot: true,
  lazy: false
}));
app.use(webpackHotMiddleware(compiler));

app.use(busboy());

// holding place root api should point to a frontend
app.get('/', function (req, res) {
   res.sendFile(__dirname + '/frontend/index.html');
});

app.use('/api', require('./backend/api'));

app.listen(port, function(error) {
  if (error) {
    console.error(error);
  } else {
    console.info('==> 🌎  Listening on port %s. Open up http://localhost:%s/ in your browser.', port, port);
  }
})
