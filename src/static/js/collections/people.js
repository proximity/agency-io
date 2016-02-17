var Backbone = require('backbone');
var Person = require('../models/person');

var People = Backbone.Collection.extend({
	url: '/api/people',
	model: Person,
	employees: function() {
		return this.where({isGuest: false});
	},
	guests: function() {
		return this.where({isGuest: true});
	},
	checkedIn: function() {
		return this.where({checkedIn: true});
	},
	checkedOut: function() {
		return this.where({checkedIn: true});
	},
	group: function(group) {
		return this.where({group: group});
	}
});

module.exports = People;
