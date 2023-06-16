require(["esri/Map", "esri/views/MapView", "esri/Graphic"], (Map, MapView, Graphic) => {
    const map = new Map({
      basemap: "hybrid"
    });
    console.log(p)
    const view = new MapView({
      center: [3.026, 36.741],
      container: "viewDiv",
      map: map,
      zoom: 5
    });
    //[[-111.3, 52.68], [-98, 49.5], [-93.94, 29.89]]
    // First create a line geometry (this is the Keystone pipeline)
    const polyline = {
      type: "polyline", // autocasts as new Polyline()
      paths:p
    };

    // Create a symbol for drawing the line
    const lineSymbol = {
      type: "simple-marker", // autocasts as SimpleLineSymbol()
      color: [255, 0, 0],
      width: 4
    };

    // Create an object for storing attributes related to the line
    const lineAtt = {
      Name: "Keystone Pipeline",
      Owner: "TransCanada",
      Length: "3,456 km"
    };

    /*******************************************
     * Create a new graphic and add the geometry,
     * symbol, and attributes to it. You may also
     * add a simple PopupTemplate to the graphic.
     * This allows users to view the graphic's
     * attributes when it is clicked.
     ******************************************/
    const polylineGraphic = new Graphic({
      geometry: polyline,
      symbol: lineSymbol,
      attributes: lineAtt,
      popupTemplate: {
        // autocasts as new PopupTemplate()
        title: "{Name}",
        content: [
          {
            type: "fields",
            fieldInfos: [
              {
                fieldName: "Name"
              },
              {
                fieldName: "Owner"
              },
              {
                fieldName: "Length"
              }
            ]
          }
        ]
      }
    });

    // Add the line graphic to the view's GraphicsLayer
    view.graphics.add(polylineGraphic);
  });