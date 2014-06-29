/*
* Functions Muri
*/
function createWalls(){
	var walls = new THREE.Object3D();
	
	//cucina sala
	var wallCreateMuroCucinaSala = createMuroCucinaSala("brick-wall.jpg");
		wallCreateMuroCucinaSala.position.set(-0.2,0,-0.2);
	var wallCreateMuroCucinaSalaInterno = createMuroCucinaSala("paisley-and-flowers.jpg");
		wallCreateMuroCucinaSalaInterno.position.set(-0.2,0,5.2);
	//cunina
	var wallCreateMuroCucinaCamera = createMuroCucinaCamera("brick-wall.jpg");
		wallCreateMuroCucinaCamera.position.set(-0.2,0,95.2);
	var wallCreateMuroCucinaCameraInterno = createMuroCucinaCamera("paisley-and-flowers.jpg");
		wallCreateMuroCucinaCameraInterno.position.set(5.2,0,95.2);		
	//sala	
	var wallCreateMuroSalaCamera = createMuroCucinaCamera("brick-wall.jpg");
		wallCreateMuroSalaCamera.position.set(150.2,0,95.2);
	var wallCreateMuroSalaCameraInterno = createMuroCucinaCamera("paisley-and-flowers.jpg");
		wallCreateMuroSalaCameraInterno.position.set(144.8,0,95.2);	
	//camere	
	var wallCreateMuroCamere = createMuroCamere("brick-wall.jpg");
		wallCreateMuroCamere.position.set(-0.2,0,95.2);
	var wallCreateMuroCamereInterno = createMuroCamere("paisley-and-flowers.jpg");
		wallCreateMuroCamereInterno.position.set(-0.2,0,89.8);
	//corridoio
	var wallCreateMuroCorridoio1 = createMuroCorridoio("paisley-and-flowers.jpg");
		wallCreateMuroCorridoio1.position.set(-0.2,0,50.2);	
	var wallCreateMuroCorridoio2 = createMuroCorridoio("paisley-and-flowers.jpg");
		wallCreateMuroCorridoio2.position.set(-0.2,0,44.8);			
	//corridoio cucina
	var wallMuroCorridoioCucina1 = createMuroCorridoioCucina("paisley-and-flowers.jpg");
		wallMuroCorridoioCucina1.position.set(39.8,0,95);	
	var wallMuroCorridoioCucina2 = createMuroCorridoioCucina("paisley-and-flowers.jpg");
		wallMuroCorridoioCucina2.position.set(45.2,0,95);		
	//corridoio sala	
	var wallMuroCorridoioSala1 = createMuroCorridoioSala("paisley-and-flowers.jpg");
		wallMuroCorridoioSala1.position.set(59.8,0,50.2);
	var wallMuroCorridoioSala2 = createMuroCorridoioSala("paisley-and-flowers.jpg");
		wallMuroCorridoioSala2.position.set(65.2,0,50.2);	
	//corridoio camera
	var wallMuroCorridoioCamera1 = createMuroCorridoioCamera("paisley-and-flowers.jpg");
		wallMuroCorridoioCamera1.position.set(99.8,0,95);
	var wallMuroCorridoioCamera2 = createMuroCorridoioCamera("paisley-and-flowers.jpg");
		wallMuroCorridoioCamera2.position.set(105.2,0,95);
	//bagno corridoio
	var wallMuroBagnoCorridoio1 = createMuroBagnoCorridoio("paisley-and-flowers.jpg");
		wallMuroBagnoCorridoio1.position.set(40,0,59.8);
	var wallMuroBagnoCorridoio2 = createMuroBagnoCorridoio("paisley-and-flowers.jpg");
		wallMuroBagnoCorridoio2.position.set(40,0,65.2);
	//intermezzo camere
	var wallMuroIntermezzoCamere1 = createMuroIntermezzoCamere("paisley-and-flowers.jpg");
		wallMuroIntermezzoCamere1.position.set(74.8,0,95);
	var wallMuroIntermezzoCamere2 = createMuroIntermezzoCamere("paisley-and-flowers.jpg");
		wallMuroIntermezzoCamere2.position.set(80.2,0,95);
		
	walls.add(wallCreateMuroCucinaSala);
	walls.add(wallCreateMuroCucinaCamera);
	walls.add(wallCreateMuroSalaCamera);
	walls.add(wallCreateMuroCamere);
	walls.add(wallCreateMuroCamereInterno);
	walls.add(wallCreateMuroCucinaCameraInterno);
	walls.add(wallCreateMuroCucinaSalaInterno);
	walls.add(wallCreateMuroSalaCameraInterno);
	walls.add(wallCreateMuroCorridoio1);
	walls.add(wallCreateMuroCorridoio2);
	walls.add(wallMuroCorridoioCucina1);
	walls.add(wallMuroCorridoioCucina2);
	walls.add(wallMuroCorridoioSala1);
	walls.add(wallMuroCorridoioSala2);
	walls.add(wallMuroCorridoioCamera1);
	walls.add(wallMuroCorridoioCamera2);
	walls.add(wallMuroBagnoCorridoio1);
	walls.add(wallMuroBagnoCorridoio2);
	walls.add(wallMuroIntermezzoCamere1);
	walls.add(wallMuroIntermezzoCamere2);
	return walls
}

function createMesh(geom, texture) {
	var texture = THREE.ImageUtils.loadTexture("assets/textures/general/" + texture)
	texture.wrapS = THREE.RepeatWrapping;
	texture.wrapT = THREE.RepeatWrapping;
	geom.computeVertexNormals();
		
	var mat = new THREE.MeshPhongMaterial({side: THREE.DoubleSide});
		mat.map = texture;
		mat.map.repeat.set(0.1, 0.1);
	var mesh = new THREE.Mesh(geom, mat);
		
	return mesh;
}

function createMuroCucinaSala(cartaParati) {
		function drawShape() {
			var shape = new THREE.Shape();
				shape.moveTo(0,25);
				shape.lineTo(150.4,25);
				shape.lineTo(150.4,-3);
				shape.lineTo(0,-3);
				shape.lineTo(0,25);
			var hole1 = new THREE.Path();
				hole1.moveTo(57.7,0);
				hole1.lineTo(57.7,20);
				hole1.lineTo(47.7,20);
				hole1.lineTo(47.7,0);
				shape.holes.push(hole1);
			var hole2 = new THREE.Path();
				hole2.moveTo(140.2,9.5);
				hole2.lineTo(140.2,18);
				hole2.lineTo(110.2,18);
				hole2.lineTo(110.2,9.5);
				shape.holes.push(hole2);
		return shape;
		}
		var shape1 = createMesh(new THREE.ShapeGeometry(drawShape()),cartaParati);
		
	return shape1;		
}

function createMuroCucinaCamera(cartaParati) {
	function drawShape() {
			var shape = new THREE.Shape();
				shape.moveTo(0,25);
				shape.lineTo(95.4,25);
				shape.lineTo(95.4,-3);
				shape.lineTo(0,-3);
				shape.lineTo(0,25);
			var hole2 = new THREE.Path();
				hole2.moveTo(80,9.5);
				hole2.lineTo(80,18.5);
				hole2.lineTo(60.2,18.5);
				hole2.lineTo(60.2,9.5);
				shape.holes.push(hole2);
		return shape;
		}
	
	var shape1 = createMesh(new THREE.ShapeGeometry(drawShape()), cartaParati);
	shape1.rotation.y = Math.PI/2;
	
	return shape1;
}

function createMuroCamere(cartaParati) {
		function drawShape() {
			var shape = new THREE.Shape();
				shape.moveTo(0,25);
				shape.lineTo(150.4,25);
				shape.lineTo(150.4,-3);
				shape.lineTo(0,-3);
				shape.lineTo(0,25);
			var hole1 = new THREE.Path();
				hole1.moveTo(27.2,9.5);
				hole1.lineTo(27.2,15.5);
				hole1.lineTo(5.2,15.5);
				hole1.lineTo(5.2,9.5);
				shape.holes.push(hole1);
			var hole2 = new THREE.Path();
				hole2.moveTo(60.2,9.5);
				hole2.lineTo(60.2,15.5);
				hole2.lineTo(45.2,15.5);
				hole2.lineTo(45.2,9.5);
				shape.holes.push(hole2);
			var hole3 = new THREE.Path();
				hole3.moveTo(92.8,9.5);
				hole3.lineTo(92.8,15.5);
				hole3.lineTo(80.2,15.5);
				hole3.lineTo(80.2,9.5);
				shape.holes.push(hole3);
			var hole4 = new THREE.Path();
				hole4.moveTo(120.2,9.5);
				hole4.lineTo(120.2,15.5);
				hole4.lineTo(105.2,15.5);
				hole4.lineTo(105.2,9.5);
				shape.holes.push(hole4);
			var hole5 = new THREE.Path();
				hole5.moveTo(145.2,9.5);
				hole5.lineTo(145.2,15.5);
				hole5.lineTo(130.2,15.5);
				hole5.lineTo(130.2,9.5);
				shape.holes.push(hole5);
		return shape;
		}
		var shape1 = createMesh(new THREE.ShapeGeometry(drawShape()), cartaParati);
		
	return shape1;		
}

function createMuroCorridoio(cartaParati) {
		function drawShape() {
			var shape = new THREE.Shape();
				shape.moveTo(0,25);
				shape.lineTo(150,25);
				shape.lineTo(150,-3);
				shape.lineTo(0,-3);
				shape.lineTo(0,25);
			var hole1 = new THREE.Path();
				hole1.moveTo(60,-1.5);
				hole1.lineTo(60,25);
				hole1.lineTo(45,25);
				hole1.lineTo(45,-1.5);
				shape.holes.push(hole1);
		return shape;
		}
		var shape1 = createMesh(new THREE.ShapeGeometry(drawShape()),cartaParati);
		
	return shape1;		
}

function createMuroCorridoioCucina(cartaParati) {
	function drawShape() {
			var shape = new THREE.Shape();
				shape.moveTo(0,25);
				shape.lineTo(95,25);
				shape.lineTo(95,-3);
				shape.lineTo(0,-3);
				shape.lineTo(0,25);
			var hole1 = new THREE.Path();
				hole1.moveTo(75,-3);
				hole1.lineTo(75,20);
				hole1.lineTo(65,20);
				hole1.lineTo(65,-3);
				shape.holes.push(hole1);	
			var hole2 = new THREE.Path();
				hole2.moveTo(45,-3);
				hole2.lineTo(45,20);
				hole2.lineTo(37,20);
				hole2.lineTo(37,-3);
				shape.holes.push(hole2);
		return shape;
		}
	
	var shape1 = createMesh(new THREE.ShapeGeometry(drawShape()), cartaParati);
	shape1.rotation.y = Math.PI/2;
	
	return shape1;
}

function createMuroCorridoioSala(cartaParati) {
	function drawShape() {
			var shape = new THREE.Shape();
				shape.moveTo(0,25);
				shape.lineTo(45,25);
				shape.lineTo(45,-3);
				shape.lineTo(0,-3);
				shape.lineTo(0,25);
				
			var hole1 = new THREE.Path();
				hole1.moveTo(30,-3);
				hole1.lineTo(30,20);
				hole1.lineTo(15,20);
				hole1.lineTo(15,-3);
				shape.holes.push(hole1);
				
		return shape;
		}
	
	var shape1 = createMesh(new THREE.ShapeGeometry(drawShape()), cartaParati);
	shape1.rotation.y = Math.PI/2;
	
	return shape1;
}

function createMuroCorridoioCamera(cartaParati) {
	function drawShape() {
			var shape = new THREE.Shape();
				shape.moveTo(0,25);
				shape.lineTo(45,25);
				shape.lineTo(45,-3);
				shape.lineTo(0,-3);
				shape.lineTo(0,25);
			var hole1 = new THREE.Path();
				hole1.moveTo(45,-3);
				hole1.lineTo(45,20);
				hole1.lineTo(37,20);
				hole1.lineTo(37,-3);
				shape.holes.push(hole1);		
		return shape;
		}
	
	var shape1 = createMesh(new THREE.ShapeGeometry(drawShape()), cartaParati);
	shape1.rotation.y = Math.PI/2;
	
	return shape1;
}

function createMuroBagnoCorridoio(cartaParati) {
		function drawShape() {
			var shape = new THREE.Shape();
				shape.moveTo(0,25);
				shape.lineTo(60,25);
				shape.lineTo(60,-3);
				shape.lineTo(0,-3);
				shape.lineTo(0,25);
			var hole1 = new THREE.Path();
				hole1.moveTo(35,-3);
				hole1.lineTo(35,20);
				hole1.lineTo(25,20);
				hole1.lineTo(25,-3);
				shape.holes.push(hole1);
			var hole2 = new THREE.Path();
				hole2.moveTo(55,-3);
				hole2.lineTo(55,20);
				hole2.lineTo(45,20);
				hole2.lineTo(45,-3);
				shape.holes.push(hole2);
		return shape;
		}
		var shape1 = createMesh(new THREE.ShapeGeometry(drawShape()),cartaParati);
		
	return shape1;		
}

function createMuroIntermezzoCamere(cartaParati) {
		function drawShape() {
			var shape = new THREE.Shape();
				shape.moveTo(0,25);
				shape.lineTo(30,25);
				shape.lineTo(30,-3);
				shape.lineTo(0,-3);
				shape.lineTo(0,25);
		return shape;
		}
		var shape1 = createMesh(new THREE.ShapeGeometry(drawShape()),cartaParati);
		shape1.rotation.y = Math.PI/2;
	return shape1;		
}
