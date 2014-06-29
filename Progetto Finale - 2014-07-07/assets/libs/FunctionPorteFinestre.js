function createPorteFinestre(camera,pulsante){

		var oggetto = new THREE.Object3D();
		//PORTE
		var portaCameretta = createPorta(10, 20, 2,0,10,15,false,false);
		oggetto.add(portaCameretta);
		var portaBagno = createPorta(10, 20, 2,20,10,15,false,false);
		oggetto.add(portaBagno);
		var portaCamera2 = createPorta(8, 20, 2,31.5,10,6.5,false,true);
		portaCamera2.children[0].rotation.y = Math.PI/2;
		oggetto.add(portaCamera2);
		var portaCamera = createPorta(8, 20, 2,-32.5,10,3,true,false);
		oggetto.add(portaCamera);
		var portaCucina = createPorta(10, 20, 2,-32.5,10,-27,true,false);
		oggetto.add(portaCucina);
		var portaSala1 = createPorta(7.5, 20, 2,-9,10,-23.8,false,true);
		portaSala1.children[0].rotation.y = Math.PI/2;
		oggetto.add(portaSala1);
		var portaSala2 = createPorta(7.5, 20, 2,-9,10,-16.2,false,false);
		portaSala2.children[0].rotation.y = Math.PI/2;
		oggetto.add(portaSala2);
		var portaIngresso = createPorta(10, 20, 2,-17.5,10,-46,false,false);
		oggetto.add(portaIngresso);
		//Finestre
		var finestraCamera = createFinestra(22,7,1,-59,12,45,false,false);
		oggetto.add(finestraCamera);
		var finestraCameretta = createFinestra(15,7,1,-22.5,12,45,false,false);
		oggetto.add(finestraCameretta);
		var finestraBagno = createFinestra(13,7,1,11,12,45,false,false);
		oggetto.add(finestraBagno);
		var finestraCamera21 = createFinestra(16,7,1,38,12,45,false,false);
		oggetto.add(finestraCamera21);
		var finestraCamera22 = createFinestra(16,7,1,63,12,45,false,false);
		oggetto.add(finestraCamera22);
		var finestraSala1 = createFinestra(30,10,1,50,14,-45,false,true);
		oggetto.add(finestraSala1);
		var finestraSala2 = createFinestra(21,10,1,72,14,-23,true,true);
		oggetto.add(finestraSala2);
		var finestraCucina = createFinestra(21,10,1,-72,14,-23,true,true);
		oggetto.add(finestraCucina);

//########################################################################
		function reset() {
			pallone.position.set(-85,-1.5,-70);
		}
		var pallone = createMeshFunction(new THREE.SphereGeometry(2,10,10), "pallone.jpg");
		pallone.position.set(-85,-1.5,-70);
		var value = true;
		pallone.azione = function(){
			if(value){
				initAnimator();
				animator.start();
				value = false;					
			}
			else{
				reset();
				value = true;
			}
		}
		oggetto.add(pallone);

		var animator = null;
		var duration = 7; // sec
		var loopAnimation = true;

		function initAnimator() {
			animator = new KF.KeyFrameAnimator();
			animator.init({ interps:[{ keys:[0,0.09,0.16,0.23,0.3,0.37,0.44,0.51,0.58,0.65,0.72,0.79,0.86,0.93,1],
			values:[
				  {	x:-85,y:-1.5,z:-70},
				  {	x:-69,y:8,z:-70},
				  {	x:-53,y:20,z:-70},
				  {	x:-37,y:8,z:-70},
				  {	x:-21,y:-1.5,z:-70},
				  {	x:-10.5,y:8,z:-70},
				  {	x:0,y:20,z:-70},
				  {	x:10.5,y:8,z:-70},
				  {	x:21,y:-1.5,z:-70},
				  {	x:37,y:8,z:-70},
				  {	x:53,y:20,z:-70},
				  {	x:69,y:12,z:-70},
				  {	x:85,y:5,z:-70},
				  {	x:85,y:3,z:-70},
				  {	x:85,y:-1.5,z:-70},
                ], target:pallone.position }, ], duration: duration * 1000, easing: TWEEN.Easing.Quadratic.In });
		}
//########################################################################
		
		
		
		var projector = new THREE.Projector();
		document.addEventListener('mousedown', onDocumentMouseDown, false);
		function onDocumentMouseDown (event) {
			event.preventDefault();
			var vector = new THREE.Vector3(( event.clientX / window.innerWidth ) * 2 - 1, -( event.clientY / window.innerHeight ) * 2 + 1, 0.5);
			projector.unprojectVector(vector, camera);
			var raycaster = new THREE.Raycaster(camera.position, vector.sub(camera.position).normalize());
			var intersects = raycaster.intersectObjects([pulsante, pallone, finestraCucina,finestraSala2,finestraSala1,finestraCamera22,
			finestraCamera21,finestraBagno,finestraCameretta,finestraCamera,
			portaIngresso.children[0],portaSala1.children[0],portaSala2.children[0],portaCucina.children[0],
			portaCamera.children[0],portaCamera2.children[0],portaCameretta.children[0],portaBagno.children[0]]);
			if (intersects.length > 0) {
			  intersects[ 0 ].object.azione();
			}
		}
		
		return oggetto;
}