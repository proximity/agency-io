var $ = require('jquery');
var _ = require('underscore');
var Backbone = require('backbone');
var Hammer = require('hammer');

var PersonView = Backbone.View.extend({
	tagName: 'li',
	template: _.template($('#person-template').html()),
	events: {}, // Events are handled by Hammer
	initialize: function() {
		this.initializeTouchEvents();

		this.listenTo(this.model, 'change', this.render);
		this.listenTo(this.model, 'destroy', this.remove);
		this.listenTo(this.model, 'visible', this.toggleVisible);
		this.listenTo(this.model, 'show', this.show);
		this.listenTo(this.model, 'hide', this.hide);
	},
	toggleVisible : function () {
		this.$el.toggleClass('hidden');
	},
	show: function() {
		this.$el.removeClass('hidden');
	},
	hide: function() {
		this.$el.addClass('hidden');
	},
	initializeTouchEvents: function() {
		this.hammer = new Hammer.Manager(this.el);
		this.hammer.add(new Hammer.Tap());
		this.hammer.on('tap', this.toggleCheckedIn.bind(this));

		var threshold = 2000;

		this.hammer.add(new Hammer.Press({threshold: threshold}));
		this.hammer.add(new Hammer.Press({event: 'longpress', time: 3000, threshold: threshold}));
		this.hammer.on('press pressup longpress', function(evt) {
			if (evt.type == 'press' && this.model.get('isGuest')) {
				this.$el.addClass('removed');
			}

			if (evt.type == 'pressup' && this.$el.hasClass('removed')) {
				this.$el.removeClass('removed');
			}

			if (evt.type == 'longpress' && this.model.get('isGuest')) {
				this.model.destroy();
			}
		}.bind(this));
	},
	render: function() {
		this.$el.html(this.template(this.model.toJSON()));
		this.$el.toggleClass('checked-in', this.model.get('checkedIn'));

		return this;
	},
	toggleCheckedIn: function() {
		this.model.toggleCheckedIn();
	},
});

module.exports = PersonView;
