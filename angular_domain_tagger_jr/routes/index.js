var express = require('express');
var router = express.Router();

var mongoose = require('mongoose');
var Domain = mongoose.model('Domain');

router.get('/domains', function(req, res, next) {
  Domain.find(function(err, domains){
    if(err){ return next(err); }

    res.json(domains);
  });
});

router.post('/domains', function(req, res, next) {
  var domain = new Domain(req.body);

  domain.save(function(err, domain){
    if(err){ return next(err); }

    res.json(domain);
  });
});

/* GET home page. */
router.get('/', function(req, res, next) {
  res.render('index', { title: 'Express' });
});

module.exports = router;
