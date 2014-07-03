function createBump(){

	var bump = new THREE.Object3D();

	var cornice = createMeshBump(new THREE.BoxGeometry(15, 15, 2), "prova1.jpg", "prova1_inv.jpg");
	cornice.position.set(40,15,-5);
	bump.add(cornice);

	




	function createMeshBump(geom, imageFile, bump) {
		var texture = THREE.ImageUtils.loadTexture("assets/textures/general/" + imageFile);
		geom.computeVertexNormals();
		var mat = new THREE.MeshPhongMaterial();
		mat.map = texture;

		if (bump) {
			var bump = THREE.ImageUtils.loadTexture("assets/textures/general/"+ imageFile);
			mat.bumpMap = bump;
			mat.bumpScale = 0.2;
		}

		var mesh = new THREE.Mesh(geom, mat);

		return mesh;
	}

	
	return bump;
}

