var mark;
var polygon;
var layers_oi = [];
var current_layers = [];		
var polygon_array = {};
var current_marker;
var greenIcon = new L.Icon({
  iconUrl: 'data:image/png;base64,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',
  shadowUrl: 'data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACkAAAApCAQAAAACach9AAACJ0lEQVR4Ae3ShY6bQRADYIeZ3v+9yszMDZPlkSWtslPuiS6+C+8n/zNp4p/froi8Jq/Jxk+TkwmHX//Wz8lG3jNjTeaguabD6HAVbphMwIIzqtd+rzKYhsgUNNcqo3fEBlyyOWmwhbbS4b8SaLBu7SGlpL9gklw3YpYR6J5Bm0zAguspZjvqSVQxqvxsPSJJKYIFKh5A2VIDyMgYfYB9hvcmI0VPTxVZS81ER7qiBoFqBAa9MKOKLzzv2BE3EOnlmDTrNRXryToGOGR65nhvSphjMP6b6WJ6xMYYxSW7l1Pp6CSzbLFPgAN3NGLKPRn3c59qxzapCTPUFNVKh0vUe24azMkW+uRm/B8UU3O3Eiw4nOrrafOSF5gS7PqHUotBQQ6f11p22HDOi+66i2LIHcWJOZrTP+rkhOl7n8YcTzCQIuIvyZPQrvs5Br0OdTsyB+YYrwKokXvsgOIXZzbeQ0DMnhHIqGOdBMEl9qKYAo3pBbbDNkijUSgjv/PrMFhwRwS2YbbMzqg+SzdukoxbeiSEVlgyK6yFmjSYtDxhTXRv1OsgsCb2jflu8hLMyC0P7Qg54NE1qc/MF5PqeAHWSfDL3zxN9dsQ+YD3zEeRS4GeYgFm5I7HNiJPfP4V7/CKeUvwsxpqhkwFzMgjj33Vwe+EnuIxngn8FvNTSCkwmJG+rQm8J/MId/EQL3nZwe2EmSNm9ufkFq9xHzcJPscnLGMRomBKqdzOY2EH+IPOLMEAAAAASUVORK5CYII=',
  iconSize: [25, 41],
  iconAnchor: [12, 41],
  popupAnchor: [1, -34],
  shadowSize: [41, 41]
});

var redIcon = new L.Icon({
  iconUrl: 'data:image/png;base64,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',
  shadowUrl: 'data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACkAAAApCAQAAAACach9AAACJ0lEQVR4Ae3ShY6bQRADYIeZ3v+9yszMDZPlkSWtslPuiS6+C+8n/zNp4p/froi8Jq/Jxk+TkwmHX//Wz8lG3jNjTeaguabD6HAVbphMwIIzqtd+rzKYhsgUNNcqo3fEBlyyOWmwhbbS4b8SaLBu7SGlpL9gklw3YpYR6J5Bm0zAguspZjvqSVQxqvxsPSJJKYIFKh5A2VIDyMgYfYB9hvcmI0VPTxVZS81ER7qiBoFqBAa9MKOKLzzv2BE3EOnlmDTrNRXryToGOGR65nhvSphjMP6b6WJ6xMYYxSW7l1Pp6CSzbLFPgAN3NGLKPRn3c59qxzapCTPUFNVKh0vUe24azMkW+uRm/B8UU3O3Eiw4nOrrafOSF5gS7PqHUotBQQ6f11p22HDOi+66i2LIHcWJOZrTP+rkhOl7n8YcTzCQIuIvyZPQrvs5Br0OdTsyB+YYrwKokXvsgOIXZzbeQ0DMnhHIqGOdBMEl9qKYAo3pBbbDNkijUSgjv/PrMFhwRwS2YbbMzqg+SzdukoxbeiSEVlgyK6yFmjSYtDxhTXRv1OsgsCb2jflu8hLMyC0P7Qg54NE1qc/MF5PqeAHWSfDL3zxN9dsQ+YD3zEeRS4GeYgFm5I7HNiJPfP4V7/CKeUvwsxpqhkwFzMgjj33Vwe+EnuIxngn8FvNTSCkwmJG+rQm8J/MId/EQL3nZwe2EmSNm9ufkFq9xHzcJPscnLGMRomBKqdzOY2EH+IPOLMEAAAAASUVORK5CYII=',
  iconSize: [25, 41],
  iconAnchor: [12, 41],
  popupAnchor: [1, -34],
        shadowSize: [41, 41],
});

    var osmUrl = 'http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png',
        osmAttrib = '&copy; <a href="http://openstreetmap.org/copyright">OpenStreetMap</a> contributors',
        osm = L.tileLayer(osmUrl, { maxZoom: 18, attribution: osmAttrib }),
        google = L.tileLayer('http://www.google.cn/maps/vt?lyrs=s@189&gl=cn&x={x}&y={y}&z={z}', {attribution: 'google'}),
        googleHybrid = L.tileLayer('http://{s}.google.com/vt/lyrs=s,h&x={x}&y={y}&z={z}',{
      maxZoom: 20,
      subdomains:['mt0','mt1','mt2','mt3']
  }),
  Kosmosnimki = L.tileLayer(
    'http://{s}.tile.osm.kosmosnimki.ru/kosmo/{z}/{x}/{y}.png',
      {
          maxZoom: 18,
          attribution: 'Map data: © <a href="http://www.openstreetmap.org/copyright" target="_blank">OpenStreetMap</a> contributors, under ODbL | Tiles: © <a href="http://osm.kosmosnimki.ru/" target="_blank">ScanEx</a>',
          subdomains: 'abcd'
      }
  ),
        map = new L.Map('map', { center: new L.LatLng(55.7522, 37.6156), zoom: 10 }),
        rosreestrLayer = L.tileLayer.Rosreestr('https://pkk.rosreestr.ru/arcgis/rest/services/PKK6/Cadastre/MapServer/export?layers%3Dshow%3A21&dpi=96&format=PNG32&bboxSR=102100&imageSR=102100&size=1024%2C1024&transparent=true&f=image&bbox={bbox}', { tileSize: 1024, attribution: 'Rosreestr' }),
        drawnItems = L.featureGroup();

var baseLayers = {
  "osm": osm.addTo(map),
  "google": google,
  'Космоснимки': Kosmosnimki,
  'Гибридная google': googleHybrid
}

var overlays = {
  'Кадастровый слой': rosreestrLayer
};

// Добавляем в оверлеи слои 1с
if (typeof layers_1c !== "undefined") {
    Object.assign(overlays, layers_1c);
  };

// Полноэкранный режим
map.addControl(new L.Control.Fullscreen({
  title: {
    'false': 'Полноэкранный режим',
    'true': 'Выйти из полноэкранного режима'
  }
}));

// Пробрасываем событие в 1с о том. что юзер нажал fullscreen
map.on('fullscreenchange', function () {
  if (map.isFullscreen()) {
    send_to_1C('FullScreen', true);
  }
});

L.control.layers(baseLayers, overlays, { position: 'topleft', collapsed: true }).addTo(map);

// Линейка масштаба
L.control.scale({imperial: false}).addTo(map);

// измеритель расстояния
var options = {
  lengthUnit: {
    decimal: 2,
    label: 'Расстояние',
    display: 'км'
  },
  angleUnit: {
    display: '&deg;',           // This is the display value will be shown on the screen. Example: 'Gradian'
    decimal: 2,                 // Bearing result will be fixed to this value.
    factor: null,               // This option is required to customize angle unit. Specify solid angle value for angle unit. Example: 400 (for gradian).
    label: 'Угол:'
  }
};

// L.control.ruler(options).addTo(map);

// вывод координат на карту
L.control.coordinates({
  position: "bottomright",
  decimals: 6,
  decimalSeperator: ",",
  useLatLngOrder: true,
  labelTemplateLng: "Долгота: {x}",
  labelTemplateLat: "Широта: {y}"
}).addTo(map);

// add leaflet-geoman controls with some options to the map
map.pm.addControls({
  position: 'topleft',
  // drawCircle: false,
  drawCircleMarker: false,
});

// Установка русского языка для панели рисования
map.pm.setLang('ru');
// Стиль для многоугольника
var polygonStyle = {
  color: '#FFF',
  fillColor: '#000'
};

// Инициализация кластера маркеров организаций
var markers_org = L.markerClusterGroup();

    // Добавление маркеров организаций в кластер
    function marker_org(latv,lngv,org_name,adress){
  mark = L.marker([latv, lngv], {
  title: org_name,
  icon: redIcon
  });
  mark.bindPopup('<table><tr><td><b>Наименование</b></td><td>'+org_name+'</td></tr><tr><td><b>Адрес</b></td><td>'+adress+'</td></tr></table>');
  markers_org.addLayer(mark);
  };

  // Добавление слоя маркеров организаций на карту
  function add_layer_marker_org(quantity){
    map.addLayer(markers_org);
    map.fitBounds(markers_org.getBounds());
    if (quantity == 1) {
      mark.openPopup();
    };
    };
    
  // Удаление слоя маркеров организаций с карты
  function remove_layer_marker_org(){
    if (typeof markers_org !== "undefined") {
      markers_org.remove();
    };
  };

  // Удаление маркеров со слоя объектов имущества
function clear_marker_org(){
  markers_org.clearLayers();
  };

  // Инициализация кластера маркеров объектов имущества
var markers_oi = L.markerClusterGroup();

  // Добавление маркеров объектов имущества в кластер
    function marker_oi(latv,lngv,oi_name,id, org_name, cad_number, cad_value, adress){
  var mark = L.marker([latv, lngv], {
  title: oi_name,
  customId: id
  }).on('click', set_current_marker);
  mark.bindPopup('<table><tr><td><b>Наименование</b></td><td>'+oi_name+'</td></tr><tr><td><b>Организация</b></td><td>'+org_name+'</td></tr><tr><td><b>Кадастровый №</b></td><td>'+cad_number+'</td></tr><tr><td><b>Кадастровая стоимость</b></td><td>'+cad_value+'</td></tr><tr><td><b>Адрес</b></td><td>'+adress+'</td></tr></table><br><button type="button" onclick="view_oi()"><svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#000000" stroke-width="1" stroke-linecap="square" stroke-linejoin="arcs"><circle cx="11" cy="11" r="8"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line></svg></button><button type="button" onclick="edit_oi()"><svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#000000" stroke-width="1" stroke-linecap="square" stroke-linejoin="arcs"><path d="M20 14.66V20a2 2 0 0 1-2 2H4a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h5.34"></path><polygon points="18 2 22 6 12 16 8 16 8 12 18 2"></polygon></svg></button><br><a href="javascript:open_oi();">Подробнее</a>');
  markers_oi.addLayer(mark);
  };

  // Показать объект имущества в отдельном окне
function open_oi(){
  send_to_1C("open_oi", current_marker);
  };

  // Добавление слоя маркеров объектов имущества на карту
  function add_layer_marker_oi(){
    map.addLayer(markers_oi);
    map.fitBounds(markers_oi.getBounds());
  };

// Удаление маркеров со слоя объектов имущества
function clear_marker_oi(){
  markers_oi.clearLayers();
  };

  // Удаление слоя маркеров организаций с карты
  function remove_layer_marker_oi(){
    markers_oi.remove();
  };

  // Удаление маркеров поиска
function clear_search_marker(){
  markers_search.clearLayers();
  };

  // Просмотр границ объекта имущества
  function view_oi(){
  clear_marker_oi();
  send_to_1C('view_oi', current_marker);
  };

  // Редактировать объект имущества
  function edit_oi(){
  clear_marker_oi();
  send_to_1C('edit_oi', current_marker);
  };

  // Установить текущий редактируемый маркер
  function set_current_marker(e){
  current_marker = e.target.options.customId;
  };

  // Рисует многоугольник по заданным координатам
  function polygon_org(polygon_array, color_hex = 'blue', fill_color_hex = 'blue', layer_opacity = 100, layer_fillOpacity = 20, stroke_weight = 3, id_layerGroup){
  var obj = JSON.parse(polygon_array);
  polygon = new L.polygon(obj, {color: color_hex, fillColor: fill_color_hex, opacity: (layer_opacity / 100), fillOpacity: (layer_fillOpacity / 100), weight: stroke_weight}).addTo(overlays[id_layerGroup]);
  overlays[id_layerGroup].addTo(map);
  // zoom the map to the polygon
  map.fitBounds(polygon.getBounds());
  //polygon.remove();
  current_layers.push(polygon);

  polygon.on('pm:cut', e => {
    // check item
    const index = current_layers.indexOf(e.originalLayer);
    if (index > -1) {
      current_layers.splice(index, 1);
      current_layers.push(e.layer);
    }
  });
  };

  // Рисует многоугольник по заданным координатам и открывает режим редактирования
  function polygon_edit(polygon_array, color_hex = 'blue', fill_color_hex = 'blue', layer_opacity = 100, layer_fillOpacity = 20, stroke_weight = 3, id_layerGroup){
  var obj = JSON.parse(polygon_array);
  polygon = new L.polygon(obj, {color: color_hex, fillColor: fill_color_hex, opacity: (layer_opacity / 100), fillOpacity: (layer_fillOpacity / 100), weight: stroke_weight}).addTo(overlays[id_layerGroup]);
  overlays[id_layerGroup].addTo(map);
  map.addLayer(overlays[id_layerGroup]);
  // enable edit mode
  polygon.pm.enable({
    allowSelfIntersection: false,
  });
  // zoom the map to the polygon			
  map.fitBounds(polygon.getBounds());

  current_layers.push(polygon);

  polygon.on('pm:cut', e => {
    // check item
    const index = current_layers.indexOf(e.originalLayer);
    if (index > -1) {
      current_layers.splice(index, 1);
      current_layers.push(e.layer);
    }
  });
  };

// Рисует контур объекта имущества и его зон    	
    	function polygon_oi(polygon_array, color_hex = 'blue', fill_color_hex = 'blue', layer_opacity = 100, layer_fillOpacity = 20, stroke_weight = 3, id_layerGroup){			
			var id_group = L.layerGroup();			
			//var obj = JSON.parse(polygon_array);
			polygon = new L.polygon(obj, {color: color_hex, fillColor: fill_color_hex, opacity: (layer_opacity / 100), fillOpacity: (layer_fillOpacity / 100), weight: stroke_weight}).addTo(id_group);
			current_layers.push(polygon);			
			
			layers_oi.push({
				[id_layerGroup]: id_group
			});			
			
			polygon.on('pm:cut', e => {
				// check item
				const index = current_layers.indexOf(e.originalLayer);
				if (index > -1) {
					current_layers.splice(index, 1);
					current_layers.push(e.layer);
				}
			});
			id_group.addTo(map);
    	};
		
		// Убираем многоугольник
    	function remove_layers_oi(id_layerGroup){    		
			console.log(typeof id_layerGroup);
			console.log(layers_oi);			
			layers_oi.forEach(item => {				
				//if (item[id_layerGroup] !== "undefined") {
				//	console.log(item[id_layerGroup]);
				//	map.removeLayer(item[id_layerGroup]);					
				//}
				console.log(typeof item);
				//map.removeLayer(item);				
			})
    	};

// Убираем многоугольник
  function remove_layers_oi(id_layerGroup){    		
  console.log(layers_oi);			
  layers_oi.forEach(item => { 
    if (item.id_layerGroup === id_layerGroup) {
      map.removeLayer(item[id_layerGroup]);					
    }				
  })
  };

  // Очистим текущие слои
  function remove_current_layers(){
    current_layers.forEach(function(layer) {
       console.log(layer);
       layer.remove();
  });
  };

  function prepare_current_layers_to_save(){
  current_layers.forEach(function(layer, i, current_layers) {
    send_to_1C('save_layer', JSON.stringify(layer.toGeoJSON()));
  });
};

  // Кнопка сохранения
  const saveButton = L.easyButton({
  states:[
    {
      icon: '<svg xmlns="http://www.w3.org/2000/svg" width="18" height="22" viewBox="0 -3 24 20" fill="none" stroke="#000000" stroke-width="1.5" stroke-linecap="square" stroke-linejoin="arcs"><path d="M19 21H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h11l5 5v11a2 2 0 0 1-2 2z"></path><polyline points="17 21 17 13 7 13 7 21"></polyline><polyline points="7 3 7 8 15 8"></polyline></svg>',
      onClick: function(){prepare_current_layers_to_save(); }
    }
  ]
});
saveButton.button.style.padding = '0px';
saveButton.button.style.width = "30px";
saveButton.button.style.height = "30px";
saveButton.button.style.minWidth = "30px";
saveButton.button.style.minHeight = "30px";
saveButton.addTo(map);

// Вызывается если создан новый объект рисования
map.on('pm:create', e => {
  current_layers.push(e.layer);
  // добавить в current layers
  //console.log(e);
  //var data = JSON.stringify(e.layer.toGeoJSON());
  //send_to_1C("pm:create", data);
});

map.on('pm:remove', e => {
  // check items
  const index = current_layers.indexOf(e.layer);
  if (index > -1) {
    current_layers.splice(index, 1);
  }
});

function send_to_1C(name,data){
  console.log(name, data);
  document.getElementById('message_name').innerHTML  = name;
  document.getElementById('message_data').innerHTML  = data;
  // Необходимо для срабатывания события при нажатии 			
  button1c.click();
};

  var markers_search = L.markerClusterGroup();

// Добавление маркеров поиска
    function search_marker(latv,lngv){
  markers_search.addLayer(L.marker([latv, lngv]));
  map.addLayer(markers_search);
  map.fitBounds(markers_search.getBounds());
  };

  function ClearMap(){
    drawnItems.remove();
  };

  // Произвольные действия try catch
  function DoEvalAction(strCode) {eval(strCode);}

  // Срабатывает на все добавленные слои
map.on('layeradd', e => {
  //console.log(e);
  e.layer.on('pm:cut', e => {
    // check item
    const index = current_layers.indexOf(e.originalLayer);
    if (index > -1) {
      current_layers.splice(index, 1);
      current_layers.push(e.layer);
    }
  });
    });
    
    map.on('pm:drawend', e => {
  map.eachLayer(function(layer){
    if(
      layer instanceof L.Polygon || 
      layer instanceof L.Rectangle || 
      layer instanceof L.Polyline ||
      layer instanceof L.Circle
    ){
      layer.showMeasurements();

    }
  });
});

function exportScreenBase64() {
  html2canvas(document.querySelector("#map"),
  {
    allowTaint: true,
    useCORS: true
  })
  .then(canvas => {
    document.body.appendChild(canvas)
    canvas.setAttribute('crossorigin', 'anonymous');
    send_to_1C('base64ImgData', canvas.toDataURL(("image/png")));
  });
}

function exportGeoJson() {
  const data = [];
  map.eachLayer(function (layer) {
    if (
      layer instanceof L.Polygon || 
      layer instanceof L.Rectangle || 
      layer instanceof L.Polyline ||
      layer instanceof L.Circle ||
      layer instanceof L.Marker
    ) {
      data.push(layer.toGeoJSON());
    }
  });

  send_to_1C('geoJsonData', JSON.stringify(data));
}

  // #placeholder#