
var mongoose = require('mongoose');

var DomainSchema = new mongoose.Schema({
    name: String,
    description: String,
    valid: Boolean,
    created: { type: Date, default: Date.now }
});

mongoose.model('Domain', DomainSchema);