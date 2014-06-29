function createObj(){
	
		var allObj = new THREE.Object3D();
	
		//mobile TV
		var loader = new THREE.OBJMTLLoader();
		loader.load('assets/models/Modern_Table/Modern_Table_obj.obj','assets/models/Modern_Table/Modern_Table_obj.mtl',function ( object ) { 
			object.rotation.y = Math.PI/2;
			object.scale.x = 2;
			object.scale.y = 2;
			object.scale.z = 2;
			object.position.set(25,0,-8);
			allObj.add( object ); 
		} );
		//TV
		var loader = new THREE.OBJMTLLoader();
		loader.load('assets/models/Old TV.obj','assets/models/Old TV.mtl',function ( tv ) { 
			tv.rotation.y = -Math.PI/2;
			tv.scale.x = 0.3;
			tv.scale.y = 0.3;
			tv.scale.z = 0.3;
			tv.position.set(25,4.5,-8);
			allObj.add( tv ); 
		} );
		//Tavolo cucina
		var loader = new THREE.OBJMTLLoader();
		loader.load('assets/models/tavolo/table ERNEST 160_200 & chair SYLWEK 1.obj','assets/models/tavolo/table ERNEST 160_200 & chair SYLWEK 1.mtl',function ( obj ) { 
			obj.rotation.y = Math.PI/2;
			obj.scale.x = 0.15;
			obj.scale.y = 0.15;
			obj.scale.z = 0.15;
			obj.position.set(-60,0,-30);
			allObj.add( obj ); 
		} );
		//divano
		var loader = new THREE.OBJMTLLoader();
		loader.load('assets/models/divano/modernn1.obj','assets/models/divano/modernn1.mtl',function ( divano ) { 
			divano.rotation.y = Math.PI;
			divano.scale.x = 4;
			divano.scale.y = 4;
			divano.scale.z = 4;
			divano.position.set(25,0,-34);
			allObj.add( divano ); 
		} ); 
		//porca Calcio
		var loader = new THREE.OBJMTLLoader();
		loader.load('assets/models/porta/WoodenCrate02.obj','assets/models/porta/WoodenCrate02.mtl',function ( object ) { 
			object.position.set(85,0.8,-70);
			object.rotation.y = Math.PI/2;
			object.scale.x = 2;
			object.scale.y = 2;
			object.scale.z = 2;
			allObj.add( object ); 
		} );	
		
		return allObj;
}