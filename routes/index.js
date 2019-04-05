var express = require('express');
var router = express.Router();

var exec = require('child_process').exec;
function execute(command, callback) {
  exec(command, function(error, stdout, stderr) {
    callback(stdout);
  });
}

var FILE_NAME = 'GenderPredictor.py';
var PATH = 'python/';

/* GET home page. */
router.get('/', function(req, res, next) {
  res.render('index', {
    name: req.body.name
  });
});

router.post('/', function(req, res, next) {
  execute("python " + PATH + FILE_NAME + ' "' + req.body.name + '"', function(result) {
    res.render('index', {
      name: req.body.name,
      gender: parseInt(result) === 0 ? "Female" : "Male"
    });
  });
});

module.exports = router;