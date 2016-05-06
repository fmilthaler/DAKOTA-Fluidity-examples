include envcheck.mk

mesh: envcheck
	gmsh -2 box_with_void_cylinder.geo

run: envcheck
	@echo **********Running simulation

clean:
	rm -rf *.vtu *.stat *.detectors *.msh fluidity.* *.pyc
