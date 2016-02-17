var Backbone = require('backbone');

var Group = Backbone.Model.extend({
	// urlRoot: '/api/people/',
	defaults: {
		id: '',
		name: '',
	},
});

module.exports = Group;
