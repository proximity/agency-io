var browserify   = require('browserify');
var gulp         = require('gulp');
var autoprefixer = require('gulp-autoprefixer');
var minifyCss    = require('gulp-minify-css');
var sass         = require('gulp-sass');
var size         = require('gulp-size');
var uglify       = require('gulp-uglify');
var gutil        = require('gulp-util');
var source       = require('vinyl-source-stream');
var buffer       = require('vinyl-buffer');
var watchify     = require('watchify');
var assign       = require('lodash').assign;

var config = {
	autoprefixer: {
		cascade: false,
	},
	browserify: {
		dest: './src/static/js',
		options: {
			debug: false,
			entries: './src/static/js/main.js',
			fullPaths: false,
		},
		error: function(err) {
			gutil.log(gutil.colors.red('Browserify Error:') + ' ' + err.message);

			this.emit('end');
		},
	},
	compress: false,
	minifyCss: {
		keepBreaks: true,
		keepSpecialComments: false,
	},
	sass: {
		src: './src/static/scss/**/*.scss',
		dest: './src/static/css',
		options: {
			includePaths: [
				'./src/static/bower_components/bootstrap-sass/assets/stylesheets/'
			],
		},
		error: function(err) {
			gutil.log(gutil.colors.red('Sass Error:') + ' ' + err.message);

			this.emit('end');
		},
	},
	size: {
		showFiles: true,
	},
};

gulp.task('css', function() {
	return gulp.src(config.sass.src)
		.pipe(sass(config.sass.options).on('error', config.sass.error))
		.pipe(autoprefixer(config.autoprefixer))
		.pipe(config.compress ? minifyCss(config.minifyCss) : gutil.noop())
		.pipe(size(config.size))
		.pipe(gulp.dest(config.sass.dest));
});

gulp.task('js', function() {
	var bundler  = browserify(config.browserify.options);

	return bundler.bundle()
		.on('error', config.browserify.error)
		.pipe(source('bundle.js'))
		.pipe(buffer())
		.pipe(config.compress ? uglify() : gutil.noop())
		.pipe(size(config.size))
		.pipe(gulp.dest(config.browserify.dest));
});

gulp.task('watch', ['css'], function() {
	var options = assign({}, watchify.args, config.browserify.options);
	var bundler = watchify(browserify(options));

	bundler.on('update', build);

	function build() {
		return bundler.bundle()
			.on('error', config.browserify.error)
			.pipe(source('bundle.js'))
			.pipe(buffer())
			.pipe(config.compress ? uglify() : gutil.noop())
			.pipe(size(config.size))
			.pipe(gulp.dest(config.browserify.dest));
	}

	gulp.watch(config.sass.src, ['css']);

	return build();
});

gulp.task('default', ['css', 'js']);
