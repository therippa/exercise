var app = angular.module('domain-tagging-jr', [
    'ui.router'
]);

app.config([
    '$stateProvider',
    '$urlRouterProvider',
    function($stateProvider, $urlRouterProvider) {

        $stateProvider
            .state('home', {
                url: '/home',
                templateUrl: '/home.html',
                controller: 'MainCtrl',
                resolve: {
                    postPromise: ['domains', function(domains){
                        return domains.getAll();
                    }]}
            });

        $urlRouterProvider.otherwise('home');
    }]);

// interface to model
app.factory('domains', ['$http', function($http) {
    var ret = {
        data: []
    };

    ret.getAll = function() {
        return $http.get('/domains').success(function(data){
            angular.copy(data, ret.data);
        });
    };

    ret.create = function(domain) {
        return $http.post('/domains', domain).success(function(data){
            ret.data.push(data);
        });
    };

    return ret;
}]);

app.controller('MainCtrl', [
    '$scope',
    'domains',
    '$http',
    function($scope, domains, $http){
        $scope.domains = domains.data;
        $scope.error = false;

        $scope.addDomain = function(){
            // this will control css styling for bad entries
            $scope.error = false;

            if (typeof $scope.name == 'undefined' || $scope.name == '') { return }

            var name = $scope.name;

            // uri library expects a uri, not just domain, so let's try to detect and fix that
            if (!/^(http:\/\/|https:\/\/)/g.test(name)) {
                name = 'http://' + name;
            }

            // parse uri
            var uri = new URI(name);
            name = uri.domain();

            // build ajax request
            var req = {
                method: 'GET',
                url: 'https://ancient-crag-3153.herokuapp.com/ip_check/',
                params: {
                    domain: name
                }
            };

            // ajax call to WHOIS service
            $http(req).success(function(data) {
                console.log(data);
                if (!data.valid) {
                    console.error('bad domain');
                }

                // create model entry
                domains.create({
                    name: name,
                    description: $scope.description,
                    valid: data.valid
                });

                // reset fields
                $scope.name = '';
                $scope.description = '';

            }).error(function() {
                // error handling
                console.error('Something went wrong');
                $scope.error = true;
            });

        };
    }]);

app.controller('DomainsCtrl', [
    '$scope',
    '$stateParams',
    'domains',
    function($scope, domains, domain){
        $scope.domain = domain;
    }]);



