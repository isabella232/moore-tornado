$(document).ready(function(){
    
    var map = L.mapbox.map('map','npr.map-g7ewv5af',{
        minZoom:12,
        maxZoom:19
    });
    
    L.control.scale().addTo(map);
    
    var width = $(window).width();
    if(width > 768){
        map.setView([35.338, -97.486], 14);
    } else {
        map.setView([35.338, -97.486], 13);
    }

    var zoommap = L.mapbox.map('zoommap', 'npr.ok-moore-tornado-satellite', {    
    //var zoommap = L.mapbox.map('zoommap', 'http://localdev.npr.org:20009/api/Project/ok-moore-tornado/', {
        fadeAnimation: false,
        zoomControl: false,
        attributionControl: false
    });
    
    var $zl = $('#zoomlens');
    var $tooltip = $('#tooltip');
    var zl_radius = $zl.width() / 2;
    
    map.on('mousemove', function(e) {
        $zl.css('top', ~~e.containerPoint.y - zl_radius + 'px');
        $zl.css('left', ~~e.containerPoint.x - zl_radius + 'px');
        zoommap.setView(e.latlng, map.getZoom(), true);
        zoommap.gridLayer.getData(e.latlng,function(data){
            if(data){
                
                var html = '';
                if(data.locationad) {
                    html += '<p class="locationad">' + data.locationad + '</p>';                    
                }
                html += '<p class="owner">';
                if(data.ownername1) {
                    html += ' ' + data.ownername1;
                }
                if(data.ownername2) {
                    html += ' ' + data.ownername2;
                }
                html += '</p>'
                $tooltip.html(html);
            }
        });
    });
    map.on('zoomend', function(e) {
        if (zoommap._loaded) zoommap.setZoom(map.getZoom());
    });
    
    map.gridLayer.on('mousemove', function(e){
       console.log(e.data); 
    });
    


    $('#about').click(function(){
        if($('.modal-body').children().length < 1 ) {
            $('.legend-contents').clone().appendTo('.modal-body');
        }
    });
    
});
