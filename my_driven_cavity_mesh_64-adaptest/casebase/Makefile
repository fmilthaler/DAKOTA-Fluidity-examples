include envcheck.mk

preprocess:
	@echo **********Creating mesh for each refinement N = 1/64.
	@$(foreach NN, 64, \
		echo **********Installing directory for N = $(NN) simulation.;\
		install -d driven_cavity-$(NN); \
		cd driven_cavity-$(NN); \
		ln -s ../driven_cavity.flml .;\
		ln -s ../driven_cavity.py .;\
		ln -s ../generate_mesh .;\
		echo **********Generating mesh for N = $(NN) simulation.;\
		./generate_mesh $(NN); \
		cd ..; \
	)

run: envcheck
	@echo **********Running simulation for each refinement.
	@$(foreach NN,64, \
		cd driven_cavity-$(NN); \
		echo **********Running simulation for N = $(NN) mesh.;\
		echo ${BINPREFIX}fluidity -v0 driven_cavity.flml; \
		${BINPREFIX}fluidity -v0 driven_cavity.flml; \
		cd ..;\
	) 

postprocess: envcheck
	@echo **********Plotting convergence data.
	PYTHONPATH=${PWD}/../../python:$$PYTHONPATH ./plot_data 64

input: clean preprocess

clean:
	$(foreach NN,64, rm -rf driven_cavity-$(NN);)
	rm -f *.stat
	rm -f *.d.* *.vtu
	rm -f *.msh *.geo
