function loadCustomScript() {
    var draggableMarker = L.marker([51.505, -0.09], {draggable: true}).addTo(mymap);

    draggableMarker.on('dragend', function(e) {
        var position = draggableMarker.getLatLng();
        alert("Nouvelle position : " + position.lat + ", " + position.lng);
    });
}
