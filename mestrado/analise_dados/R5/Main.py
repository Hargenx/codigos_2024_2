'''
Random walk (R4)
Copyright (c) 2017 N.P. Rougier and F.C.Y. Benureau
Adapted by Serra
Release under the Windows 10
Pyhton 3.8 - Jupyter notebook
Tested with 64 bit (AMD64) 
'''
import comput_walk_module, comput_results_module, provenance
if __name__ == "__main__":
    # Unit test checking reproducibility
    # (will fail with Python<=3.2)
    assert (comput_walk_module.compute_walk(10, 0, 1, 42) ==
	        [1,0,-1,-2,-1,0,1,0,-1,-2])

    # Simulation parameters
    count, x0, seed = 10, 0, 1
    results = comput_results_module.comput_results(count, x0=x0, seed=seed)

    # Save & display results
    with open("./results-R4.txt", "w") as fd:
        fd.write(str(results))
    print(results["data"])
    provenance.desenha()