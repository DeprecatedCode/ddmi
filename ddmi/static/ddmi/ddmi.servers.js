var servers = ddmi.controller('DDMIServersCtrl', function ($scope) {
    $scope.action = {};

    /**
     * Mock Server Data
     */
    $scope.servers = [
        1, 2, 3, 4
    ];

    /**
     * Set Action
     */
    $scope.act = function (type, server) {
        $scope.action.type = type;
        $scope.action.server = server;
    } 
});

