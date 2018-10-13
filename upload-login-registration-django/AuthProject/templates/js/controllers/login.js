
app.controller('logincontroller', function($scope,$http,$window) {

  $scope.login = function()
  {
    
    $scope.user = {username:$scope.mail,password:$scope.psswd};
    var log =  $http({
    method: 'POST',
    url: 'http://192.168.0.84:8080/login/',
    headers: {'Content-Type': 'application/json'},
    data: $scope.user,
  });
   log.success(function(data,status){
    if(status == 200)
    {
      $window.location.href = 'static/view/home.html';
      /*$window.location.href = 'Login.html';*/
    }
  });
   log.error(function(data,status){
      if(data == 'PASSWORD_INVALID')
      {
        alert("Username password missmatch");
      }
  });
 };
});