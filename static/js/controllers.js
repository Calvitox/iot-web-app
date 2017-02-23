(function (){
	angular.module('platform.controllers', [])
		.controller('mainController', ['$scope', '$state','commService', 'items', function($scope, $state, commService, items){
			//console.log($state.current);
			$scope.items = items;

			$scope.pick = function(id){
				console.log(id);

				commService.getOne(id).then(function(response){
					console.log(response);
				});
				//alert($scope.device);					
			}

			$scope.h = function(){
				
				console.log($scope);
					
			}
		}])
})();