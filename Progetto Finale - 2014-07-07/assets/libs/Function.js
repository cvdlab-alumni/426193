/*
* Functions
*/      

function createMeshFunction(geom, texture) {
	var texture = THREE.ImageUtils.loadTexture("assets/textures/general/" + texture)
	texture.wrapS = THREE.RepeatWrapping;
	texture.wrapT = THREE.RepeatWrapping;
	geom.computeVertexNormals();
		
	var mat = new THREE.MeshPhongMaterial({side: THREE.DoubleSide});
		mat.map = texture;
	var mesh = new THREE.Mesh(geom, mat);
		
	return mesh;
}
	  
function createSpotLight(x,y,z){
	var spotLight = new THREE.SpotLight(0xffffff, 3.5);
	spotLight.position.set(x,y,z);
	spotLight.distance = 100
	return spotLight;
}

function createSpotDirectional(x,y,z){
	var directionalLight = new THREE.DirectionalLight( 0xffffff, 1 );
	directionalLight.position.set(x, y, z );
	return directionalLight;
}

function createPorta(x,y,z,x1,y1,z1,ruotaPerno,ruotaPernoNegativo){
	var perno = new THREE.Object3D();
	var portaGeometry = new THREE.BoxGeometry(x,y,z);
	var porta = createMeshFunction(portaGeometry,"porta.jpg");
	
	porta.azione = function (){
		if (porta.parent.rotation.y == 0){
			porta.parent.rotation.y = Math.PI/2;
		}
		else
			porta.parent.rotation.y = 0;
	};
	
	perno.add(porta);
	perno.position.set(x1,y1,z1);
	porta.position.x = -x/2;
	
	if(ruotaPerno){
		perno.rotation.y = Math.PI/2;
	}
	
	if(ruotaPernoNegativo){
		porta.azione = function (){
		if (porta.parent.rotation.y == 0){
			porta.parent.rotation.y = -(Math.PI/2);
		}
		else
			porta.parent.rotation.y = 0;
	};
	}
	
	return perno;
}

function createFinestra(x,y,z,x1,y1,z1,rotate, inverso){

	var finestraGeometry = new THREE.BoxGeometry(x,y,z);
	var finestraMaterial = new THREE.MeshLambertMaterial({ color: 0xFFFFFF, transparent: true, opacity: 0.5});
	var finestra = new THREE.Mesh(finestraGeometry, finestraMaterial);
	
	finestra.position.set(x1,y1,z1);
	
	finestra.azione = function (){
		if (finestra.position.y == 12){
			finestra.position.y = 17;
		}
		else
			finestra.position.y = 12;
	};
	
	if(rotate){
		finestra.rotation.y = Math.PI/2;
	}
	
	if(inverso){
		finestra.azione = function (){
		if (finestra.position.y == 14){
			finestra.position.y = 7;
		}
		else
			finestra.position.y = 14;
	};
	}
	

	return finestra;
}


