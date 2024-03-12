function loadCustomScript(mymap) {
    var draggableMarker = L.marker([50.67183453379191, 4.609907269477845], {draggable: true}).addTo(mymap);
    var circle = L.circle([50.67183453379191, 4.609907269477845], {
        color: 'green', // Couleur du bord du cercle
    fillColor: '#90EE90',
        fillOpacity: 0.5,
        radius: 500000
    }).addTo(mymap);
    
    var draggableMarker2 = L.marker([40.508, -1.11], {draggable: true}).addTo(mymap);
    var circle2 = L.circle([40.508, -1.11], {
        color: 'green', // Couleur du bord du cercle
    fillColor: '#90EE90',
        fillOpacity: 0.5,
        radius: 500000
    }).addTo(mymap);

    var draggableMarker3 = L.marker([31.505, -0.09], {draggable: true}).addTo(mymap);
    var circle3 = L.circle([31.505, -0.09], {
        color: 'green', // Couleur du bord du cercle
    fillColor: '#90EE90',
        fillOpacity: 0.5,
        radius: 500000
    }).addTo(mymap);


    var draggableMarker3 = L.marker([70, -0.09], {draggable: true}).addTo(mymap);
    var circle3 = L.circle([70, -0.09], {
        color: 'green', // Couleur du bord du cercle
    fillColor: '#90EE90',
        fillOpacity: 0.5,
        radius: 500000
    }).addTo(mymap)
    






    
    draggableMarker.on('dragend', function(e) {
        var position = draggableMarker.getLatLng();
        circle.setLatLng(position);
        //alert("Nouvelle position : " + position.lat + ", " + position.lng);
        fetch('/calculer_pourcentage', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({lat: position.lat, lng: position.lng})
        })
        .then(response => response.json())
        .then(data => {
            // Mettre à jour l'information sur la carte avec le pourcentage reçu
            var infoDiv = document.querySelector('.infoSurPopu');
            if (infoDiv) {
                infoDiv.innerHTML = 'Pourcentage de la population couverte : ' + data.pourcentage + '%';
            }
        })
        .catch(error => {
            console.error('Erreur lors de la requête AJAX :', error);
        });
    });
    draggableMarker2.on('dragend', function(e) {
        var position2 = draggableMarker2.getLatLng();
        circle2.setLatLng(position2);
        //alert("Nouvelle position 2 : " + position2.lat + ", " + position2.lng);
        fetch('/calculer_pourcentage', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({lat: position2.lat, lng: position2.lng})
        })
        .then(response => response.json())
        .then(data => {
            var infoDiv = document.querySelector('.infoSurPopu');
            if (infoDiv) {
                infoDiv.innerHTML = 'Pourcentage de la population couverte : ' + data.pourcentage + '%';
            }
        })
        .catch(error => {
            console.error('Erreur lors de la requête AJAX :', error);
        });
    });
    draggableMarker3.on('dragend', function(e) {
        var position3 = draggableMarker3.getLatLng();
        circle3.setLatLng(position3);
        //alert("Nouvelle position 3 : " + position3.lat + ", " + position3.lng);
        fetch('/calculer_pourcentage', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({lat: position3.lat, lng: position3.lng})
        })
        .then(response => response.json())
        .then(data => {
            var infoDiv = document.querySelector('.infoSurPopu');
            if (infoDiv) {
                infoDiv.innerHTML = 'Pourcentage de la population couverte : ' + data.pourcentage + '%';
            }
        })
        .catch(error => {
            console.error('Erreur lors de la requête AJAX :', error);
        });
    });

    draggableMarker4.on('dragend', function(e) {
        var position4 = draggableMarker4.getLatLng();
        circle3.setLatLng(position4);
        //alert("Nouvelle position 4 : " + position4.lat + ", " + position4.lng);
        fetch('/calculer_pourcentage', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({lat: position4.lat, lng: position4.lng})
        })
        .then(response => response.json())
        .then(data => {
            var infoDiv = document.querySelector('.infoSurPopu');
            if (infoDiv) {
                infoDiv.innerHTML = 'Pourcentage de la population couverte : ' + data.pourcentage + '%';
            }
        })
        .catch(error => {
            console.error('Erreur lors de la requête AJAX :', error);
        });
    });





    var infoSurPopu = L.control({position: 'topright'});
    infoSurPopu.onAdd = function (mymap) {
        var div = L.DomUtil.create('div', 'infoSurPopu');
        div.innerHTML = 'Pourcentage de la population couverte :</h4>' + '80%';
        return div;
    };
    infoSurPopu.addTo(mymap);
}
