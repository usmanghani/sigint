const express = require('express');
const watson = require('watson-developer-cloud');
const ibmCredentials = require('../secrets.json').ibm_alchemy.credentials



let text_analysis = function(text, callback){
  let alchemy_language = watson.alchemy_language(ibmCredentials)
  let parameters = {
    extract: 'authors,concepts,dates,doc-emotion,entities,feeds,keywords,pub-date,relations,typed-rels,doc-sentiment,taxonomy,title',
    sentiment: 1,
    maxRetrieve: 1,
    text: text
  };

  alchemy_language.combined(parameters, callback);

}

let router = express.Router();

// might change this to a post and use the body instead of a query string
router.get('/analysis', function(req, res) {
  let text = req.query.text || "";
  text_analysis(text, function(error, response) {
    if (error) {
      res.status(500).send({'error': error});
    } else {
      res.send(JSON.stringify(response, null, 2));
    }
  });

});

module.exports = router;
