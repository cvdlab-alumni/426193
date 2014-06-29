		
function createLuci(){	
		var luci = new THREE.Object3D();
		// add spotlights
		var spotSala = createSpotLight(35,60,-55);
		luci.add(spotSala);
		var spotSala1 = createSpotLight(100,60,-55);
		luci.add(spotSala1);
		var spotCamera1 = createSpotLight(100,60,70);
		luci.add(spotCamera1);
		var spotCamera = createSpotLight(-100,60,70);
		luci.add(spotCamera);
		var spotCucina = createSpotLight(-90,60,-70);
		luci.add(spotCucina);
		var spotCameretta = createSpotLight(-40,60,70);
		luci.add(spotCameretta);
		var spotBagno = createSpotLight(20,60,70);
		luci.add(spotBagno);
		//add directional light
		var directionalAngolo1 = createSpotDirectional(140,50,90);
		luci.add(directionalAngolo1);
		var directionalAngolo2 = createSpotDirectional(-140,50,-90);
		luci.add(directionalAngolo2);
		
		return luci;
}

