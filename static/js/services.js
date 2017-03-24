(function (){
	angular.module('platform.services', [])
		.factory('commService', ['$http', '$q', '$window', function ($http, $q, $window){
			
			var localStorage = $window.localStorage;

				function getAll(){
					var dfd = $q.defer();

			        $http.post('http://0.0.0.0:8000/main/')
			        	.then(function(response){
						res = JSON.parse(response.data);//success
						dfd.resolve(res);
					},function(data){
						dfd.reject();
				});

		        return dfd.promise;
				}

		      function getOne(id) {
		      	var dfd = $q.defer();

		      	postData = {'id':id};

		        $http.post('http://0.0.0.0:8000/main/',postData)
		        	.then(function(response){
					res = JSON.parse(response.data);//success
					dfd.resolve(res);
				},function(data){
					dfd.reject();
				});

		        return dfd.promise;

		      }

			return {
				getOne:getOne,
				getAll:getAll
			}
		}])
})();