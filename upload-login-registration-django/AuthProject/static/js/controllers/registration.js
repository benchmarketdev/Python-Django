app.controller('registraioncontroller',function($scope,$http,$location) {

	$scope.registration = function()
	{

		$scope.user = {firstname:$scope.firstname,lastname:$scope.lastname,
			email:$scope.mail,mobile:$scope.phone,password:$scope.psswd};
			var log =  $http({
				method: 'POST',
				url: 'http://192.168.0.84:8080/authenticate/registration/',
				headers: {'Content-Type': 'application/json'},
				data: $scope.user,
			});
			log.success(function(data,status){
				if(status == 200)
				{
					if(data == 'exists')
					{
						alert("Username already exists");
					}
					if(data == 'OKAY')
					{
						$location.path('/');
					}
				}
			});
			log.error(function(data,status){
				if(data == 'PASSWORD_INVALID')
				{
					alert("Username password missmatch");
				}
				if(data == 'pattern')
				{
					alert("Please Fill Fields Correct");
				}
			});
		};
	});