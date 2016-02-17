var Backbone = require('backbone');

var Person = Backbone.Model.extend({
	// urlRoot: '/api/people/',
	defaults: {
		email: '',
		firstName: '',
		lastName: '',
		isGuest: false,
		checkedIn: false,
		group: null
	},
	toggleGuest: function() {
		this.save({
			isGuest: !this.get('isGuest')
		});
	},
	toggleCheckedIn: function() {
		this.save({
			checkedIn: !this.get('checkedIn')
		});
	},
	checkIn: function() {
		this.save({
			checkedIn: true
		});
	},
	checkOut: function() {
		this.save({
			checkedIn: false
		});
	}
});

module.exports = Person;
