const { src, dest, watch, series } = require('gulp');
const sass = require('gulp-sass')(require('sass'));

// This function will automatically build all scss files
// Scss files starting with _ will be ignored.
// To build scss files execute 'npm run gulp' in the terminal.
// You must be in react-app/src
const buildSass = () => {
    return src('*.scss')
        .pipe(sass())
        .pipe(dest('../css'));
};

// This is used to watch all scss files so the compiler knows
// when to update the file. You will still need to run
// 'npm run gulp' in the terminal.
const watchSass = () => {
    watch(['*.scss'], buildSass);
}

exports.default = series(buildSass, watchSass);
