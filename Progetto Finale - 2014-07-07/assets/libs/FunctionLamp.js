function createLamps(){
	var lamps = new THREE.Object3D();
	var lampSala = createLamp();
		lampSala.position.set(50,0,-22.5);
		lamps.add(lampSala);
	var lampSala2 = createLamp();
		lampSala2.position.set(15,0,-22.5);
		lamps.add(lampSala2);
	var lampCucina = createLamp();
		lampCucina.position.set(-52.5,0,-22.5);
		lamps.add(lampCucina);		
	var lampCamera = createLamp();
		lampCamera.position.set(-52.5,0,22.5);
		lamps.add(lampCamera);
	var lampCamera2 = createLamp();
		lampCamera2.position.set(50,0,22.5);
		lamps.add(lampCamera2);
	var lampCameretta = createLamp();
		lampCameretta.position.set(-15,0,30);
		lamps.add(lampCameretta);	
	var lampBagno = createLamp();
		lampBagno.position.set(16,0,30);
		lamps.add(lampBagno);			
	return lamps;
}

function createLamp(){
	//base
	var lamp = new THREE.Object3D();
	var baseGeometry = new THREE.CylinderGeometry(4, 4, 0.5, 20, 20, false);
	var baseMaterial = new THREE.MeshBasicMaterial({ color: 0xcccccc, shading: THREE.FlatShading });
	var base = new THREE.Mesh(baseGeometry, baseMaterial);
	base.position.set(0, 25, 0);
	lamp.add(base);
	//half_sphere
	var half_sphereGeometry = new THREE.SphereGeometry(4, 20, 20, 0, Math.PI*2, -Math.PI/2, Math.PI/2);
	var half_sphereMaterial = new THREE.MeshBasicMaterial({ color: 0xeb5555, side: THREE.DoubleSide });
	var half_sphere = new THREE.Mesh(half_sphereGeometry, half_sphereMaterial);
	half_sphere.position.set(0, 21, 0);
	lamp.add(half_sphere);
	//bulb
	var bulb = createSphere(1.5, 10, 10, 0xffffff,true, 1);
	bulb.material.side = THREE.BackSide
    bulb.position.set(0,23,0);
    lamp.add(bulb);
	
	return lamp;
}

function createSphere(radius, pol1, pol2, colore,trasparente, opacita){
	var sphereGeometry = new THREE.SphereGeometry(radius, pol1, pol2);
	var sphereMaterial = new THREE.MeshBasicMaterial({ color: colore,transparent: trasparente, opacity: opacita});
	var sphere = new THREE.Mesh(sphereGeometry, sphereMaterial);
	return sphere;
}