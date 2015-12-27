var osmLink = '<a href="http://openstreetmap.org">OpenStreetMap</a>',
	thunLink = '<a href="http://thunderforest.com/">Thunderforest</a>';

var osmUrl = 'http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png',
	osmAttrib = '&copy; ' + osmLink + ' Contributors',
	landUrl = 'http://{s}.tile.thunderforest.com/landscape/{z}/{x}/{y}.png',
	thunAttrib = '&copy; '+osmLink+' Contributors & '+thunLink;

var mapUrl = 'http://otile4.mqcdn.com/tiles/1.0.0/sat/{z}/{x}/{y}.png',
	mapAttrib = '&copy; ' + osmLink + ' Contributors';

var osmMap = L.tileLayer(osmUrl, {attribution: osmAttrib}),
	landMap = L.tileLayer(landUrl, {attribution: thunAttrib});

var aerial= L.tileLayer(mapUrl, {attribution: mapAttrib});

var dataurl = '/parcel_data/'


var parcel= L.geoJson();


function parcelStyle(feature) {
	return {
		weight: 2,
		//opacity: 1,
		color: 'brown',
		dashArray: '3',
		fillOpacity: 0.3,
		fillColor: 'brown'
	};
}


var map = L.map('map',{
	layers: [osmMap],
	keyboard: true,
	boxZoom: true,
	zoomControl: false,
	//measureControl: true,
	doubleClickZoom: true,
	scrollWheelZoom: true,
	fullscreenControl: true,
	fullscreenControlOptions: {
		position: 'topleft'
	} 
	}).setView([-0.421897, 36.951358], 15);
	mapLink ='<a href="http://openstreetmap.org">OpenStreetMap</a>';
	L.tileLayer('http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
				attribution: 'Map data &copy; ' + mapLink,
			    maxZoom:32,
			    }).addTo(map);
				

// add the new control to the map

map.addControl(new L.Control.ZoomMin())

var measureControl = L.control.measure({
	position: 'topleft',
	completedColor: '#C8F2BE'
});
measureControl.addTo(map);

L.tileLayer('http://{s}.tile.osm.org/{z}/{x}/{y}.png', {
    attribution: '© OpenStreetMap contributors'
}).addTo(map);


// control that shows state info on hover
$.getJSON(dataurl, function (data) {
    parcel.addData(data).setStyle(parcelStyle);
    parcel.eachLayer(function (layer) { 
    layer.on('click', function (e) {
		var popup = "<strong>" + "Id : " + e.target.feature.properties.objectid + "<br>" + "Area: " + e.target.feature.properties.shape_area + "<br>" + " Length : " + e.target.feature.properties.shape_leng +  "<br>" + "LR Number: " + e.target.feature.properties.lr_number + "<br>" +  "</strong>";
		layer.bindPopup(popup).openPopup(e.latlng);
		//map.fitBounds(e.target.getBounds());
	});	
	//locations.bindLabel(feature.properties['location_b'], { 'noHide': true });

	});	
});

var legend = L.control({position:'bottomleft'});
legend.onAdd = function (map) {
	var div = L.DomUtil.create('div','info legend');
	div.innerHTML = "<h3>Legend</h3><table></table>";
	return div;
}
legend.addTo(map);

map.addLayer(parcel)


var baseLayers = {
	"OSM Mapnik": osmMap,
	"Landscape": landMap,
	"Aerial":aerial
};

var overlays = {
	"Parcels": parcel,
	
};

L.control.layers(baseLayers,overlays,{collapsed:true}).addTo(map);
L.control.scale({position:"bottomleft"}).addTo(map);
var routing = L.Routing.control({
	    waypoints: [
	        L.latLng(-0.421897, 36.951358),
	        L.latLng(-0.426890, 36.951758)
	    ],
	    routeWhileDragging: true,
	    geocoder: L.Control.Geocoder.nominatim()
	});
L.easyButton('fa-compass',
  function (){
    $('.leaflet-routing-container').is(':visible') ? routing.removeFrom(map) : routing.addTo(map)
  },
  'Routing'
).addTo(map);


function createButton(label, container) {
    var btn = L.DomUtil.create('button', '', container);
    btn.setAttribute('type', 'button');
    btn.innerHTML = label;
    return btn;
}
