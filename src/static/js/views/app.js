var $ = require('jquery');
var Backbone = require('backbone');

var People = require('../collections/people');
var Groups = require('../collections/groups');
var PersonView = require('./person');

var AppView = Backbone.View.extend({
	el: 'body',
	events: {
		'click #name-input .btn': 'toggleNameInput',
		'keypress #name': 'createOnEnter',
	},
	filtersTemplate: _.template($('#filters-template').html()),
	initialize: function() {
		this.people = new People();
		this.$people = $('#people');
		this.$input = $('#name');
		this.$inputWrap = $('#name-input');
		this.$filters = $('#filters');

		$.ajaxSetup({cache: false});

		this.groups = new Groups();
		this.groups.fetch();

		this.syncPeople(this.initializeRoutes.bind(this));
		this.preventSleep();

		this.listenTo(this.people, 'add', this.addPerson);
		this.listenTo(this.people, 'filter', this.filterGroup);
		this.listenTo(this.people, 'all', this.render);
	},
	render: function() {
		this.$filters.html(this.filtersTemplate({
			groups: this.groups
		}));

		this.$('#filters li a')
			.removeClass('selected')
			.filter('[href="#toggle/' + (this.activeGroup || '') + '"]')
			.addClass('selected');
	},
	initializeRoutes: function() {
		this.router = new Backbone.Router();
		this.router.route('toggle/(:group)', 'toggleGroup', this.toggleGroup.bind(this));

		Backbone.history.start();
	},
	filterOne: function() {

	},
	activeGroup: null,
	filterGroup: function(group) {

		this.activeGroup = parseFloat(group);

		this.people.each(function(person) {
			if (this.activeGroup && this.activeGroup !== person.get('group')) {
				return person.trigger('hide');
			}

			person.trigger('show');
		}.bind(this));
	},
	toggleGroup: function(group) {
		this.people.trigger('filter', group);
	},
	addPerson: function(person) {
		var view = new PersonView({model: person});

		this.$people.append(view.render().el);
	},
	createOnEnter: function(e) {
		if (e.which === 13) {
			var fullName = this.$input.val().trim();

			if (!fullName) {
				this.$input.blur();
				this.$inputWrap.removeClass('input-visible');
				return;
			}

			fullName = this.splitFullName(fullName);

			this.people.create({
				firstName: fullName.firstName,
				lastName: fullName.lastName,
				isGuest: true,
				checkedIn: true
			});

			this.$input.val('').blur();
			this.$inputWrap.removeClass('input-visible');
		}
	},
	splitFullName: function(fullName) {
		var parts = fullName.split(/\s+/),
			firstName = parts.shift().trim(),
			lastName = (parts.shift() || '').trim();

		return { firstName: firstName, lastName: lastName };
	},
	toggleNameInput: function(e) {
		this.$inputWrap.toggleClass('input-visible');
		this.$inputWrap.hasClass('input-visible') ? this.$input.focus() : this.$input.blur();
	},
	allowSleep: function() {
		clearInterval(this.sleepInterval);
	},
	preventSleep: function() {
		this.sleepInterval = setInterval(function () {
			location.href = location.href; // try refreshing
			window.setTimeout(window.stop, 0); // stop it soon after
		}, 29017);
	},
	syncPeople: function(callback) {
		function sync(callback) {
			this.people.fetch({success: callback || $.noop});
		}

		this.syncInterval = setInterval(sync.bind(this), 13099);

		sync.call(this, callback);
	}
});

module.exports = AppView;
