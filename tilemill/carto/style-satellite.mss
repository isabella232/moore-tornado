Map {
//  background-color: #666;
}

#damage {
  line-width: 3;
  line-color: #EFC637;
  line-opacity: .5;
}

#roads {
  line-color: #bababa;
  [zoom <= 12 ] {
    line-width: 0;
    [CLASS = 'A15'] { line-width: 2; }
  }
  [zoom > 12 ][zoom < 15 ] {
    line-width: 1;
    [CLASS = 'A15'] { line-width: 2; }
  }
  [zoom >= 15 ] {
    line-width: 1;
    [CLASS = 'A15'] { line-width: 3; }
  }
  
  ::labels {
    text-name: [COMBINEDST];
    text-face-name: "Helvetica Neue Medium";
    text-fill: #333;
    text-placement: line;
    text-min-distance: 500;
    text-halo-fill: #fff;
    text-halo-radius: 2;
    text-avoid-edges: true;
    text-size: 13px;
    text-opacity: 0;

    [CLASS = 'A15'] {
      text-face-name: "Helvetica Neue Bold";
      text-opacity: 1;
      [zoom < 15]  { text-size: 10px; }
      [zoom >= 15] { text-size: 13px; }
    }
    [CLASS = 'A31'] {
      [zoom >= 15] {
        text-size: 12px;
        text-opacity: 1;
      }
    }
    [CLASS = 'A40'],
    [CLASS = 'A41'],
    [CLASS = 'A61'] {
      [zoom >= 16] { 
        text-size: 11px;
        text-fill: #666;
        text-opacity: 1;
      }
    }
    [CLASS = 'A63'] {
      [zoom >= 17] { 
        text-size: 10px;
        text-fill: #666;
        text-opacity: 1;
      }
    }
  }
}

#buildings {
  [is_in_path = true] {
    line-width: .5;
    line-color: #ccc;
  	polygon-fill: #F7E39B;
  	polygon-opacity: .3;
  }
}

#parcels {
  [is_in_path = true] {
    line-width: 1;
    line-color: #fff;
    line-opacity: .2;
  	polygon-fill: #FBF1CD;
  	polygon-opacity: .1;
  }
}

/*
#damage-bg {
  polygon-fill: #ECA395;
  polygon-opacity: .5;
}
*/