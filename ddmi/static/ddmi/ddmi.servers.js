var servers = ddmi.controller('DDMIServersCtrl', function ($scope, $http, $interval) {
    $scope.action = {};

    /**
     * Uptime Format
     */
    $scope.fmtUptime = function (t) {
        if (typeof t !== 'number') {
            return t;
        }
        var days = Math.floor(t / 86400);
        t -= days * 86400;
        var hours = Math.floor(t / 3600);
        t -= hours * 3600;
        var minutes = Math.floor(t / 60);
        t -= minutes * 60;
        var seconds = t;

        return (days ? ''+days+'d ' : '') +
               (hours ? ''+hours+'h ' : '') +
               (minutes ? ''+minutes+'m ' : '') +
               seconds + 's';
    };

    /**
     * Get Server Data
     */
    var uptimeTimeout;
    var uptimeTimeoutIter;
    var loadServers = function () {
        $http.get('/api/servers').success(function (data) {
            $scope.servers = data.servers;
            uptimeTimeoutIter = 0;
            $interval.cancel(uptimeTimeout);
            uptimeTimeout = $interval(function () {
                uptimeTimeoutIter ++;
                if (uptimeTimeoutIter > 20) {
                    $scope.servers.forEach(function (server) {
                        server.uptime = 'disconnected';
                    });
                    return;
                }
                $scope.servers.forEach(function (server) {
                    server.uptime += 1;
                });
            }, 1000);
        });
    };
    loadServers();
    $interval(loadServers, 5000);

    /**
     * Suspend Server
     */
    $scope.suspend = function (server) {
        $scope.action.processing = true;
        $http.post('/api/server/' + server.ddmi_id + '/suspend').success(function () {
            $scope.act();
            loadServers();
        });
    };

    /**
     * Resume Server
     */
    $scope.resume = function (server) {
        $scope.action.processing = true;
        $http.post('/api/server/' + server.ddmi_id + '/resume').success(function () {
            $scope.act();
            loadServers();
        });
    };

    /**
     * Set Action
     */
    $scope.act = function (type, server) {
        $scope.action.processing = false;
        $scope.action.type = type;
        $scope.action.server = server;
    }
});

