(function (){
	var app = angular.module('platform', [
		'ui.router',
		'ngResource',
		'platform.controllers',
		'platform.services'
		]);

	app.config(['$httpProvider', '$resourceProvider', '$stateProvider', '$urlRouterProvider',
	 function ($httpProvider, $resourceProvider, $stateProvider, $urlRouterProvider) {

		//$resourceProvider.defaults.stripTrailingSlashes = false;
		$httpProvider.defaults.xsrfCookieName = 'csrftoken';
    	$httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
		$httpProvider.defaults.headers.common['X-Requested-With'] = 'XMLHttpRequest';
        //$httpProvider.defaults.headers.post['Content-Type'] = 'application/x-www-form-urlencoded';

        $stateProvider
        .state('app',{
        	url: '/',
            templateUrl: 'templates/devices.html',
            controller: 'mainController',
            resolve: {
            		items: function(commService){
                        return commService.getAll()
                        }
            		}
        })

        ;

        $urlRouterProvider.otherwise('/');
    }])

})();