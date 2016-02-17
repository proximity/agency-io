var Backbone = require('backbone');
var Group = require('../models/group');

var Group = Backbone.Collection.extend({
	url: '/api/groups',
	model: Group
});

module.exports = Group;
