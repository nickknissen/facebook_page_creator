module.exports = function( grunt ) {
    'use strict';
    //
    // Grunt configuration:
    //
    // https://github.com/cowboy/grunt/blob/master/docs/getting_started.md
    //
    grunt.initConfig({

        watch: {
            scripts: {
                files: [
                    'app/templates/page/*.html',
                    'app/templates/*.html'

                ],
                options: {
                    livereload: true
                }
            }
        }
    });

    grunt.loadNpmTasks('grunt-contrib-watch');
    grunt.registerTask('default', ['watch']);

};
