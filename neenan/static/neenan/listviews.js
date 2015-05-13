neenan.controller('listview', ['$scope', function ($scope) {
    $scope.tracks = []
}])

neenan.controller('queue', ['$scope', '$controller', function ($scope, $contoller)
    $controller('listview', {$scope: $scope});
}])

neenan.controller('browserlist', ['$scope', '$controller', function ($scope, $contoller)
    $controller('listview', {$scope: $scope});
}])
