'use strict';
var app = angular.module('app', ['ngRoute','ngMaterial','ngMessages'])
app.config(function($routeProvider) {
    $routeProvider
    .when("/login", {
        templateUrl : "/static/view/login.html"
    })
    .when("/registration", {
        templateUrl : "/static/view/registration.html"
    })
    .otherwise({ redirectTo: '/login' });
});