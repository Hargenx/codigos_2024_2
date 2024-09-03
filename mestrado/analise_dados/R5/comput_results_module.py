import sys, subprocess, datetime, entradas, comput_walk_module

def comput_results(count: int, x0=0, step=1, seed=0) -> dict:
    """Compute a walk and return it with context"""
    # If repository is dirty, don't do anything
    if subprocess.call(("notepad", "diff-index",
                        "--quiet", "HEAD")):
        print("data/Repository is dirty, please commit")
        sys.exit(1)

    # Get git hash if any
    hash_cmd = ("notepad", "rev-parse", "HEAD")
    revision = subprocess.check_output(hash_cmd)

    # Compute results and Full Retrospective Provenance
    walk = comput_walk_module.compute_walk(count=count, x0=x0,
                        step=step, seed=seed)
    return {
        "data"      : walk,
        "parameters": {"count": count, "x0": x0,
                       "step": step, "seed": seed},
        "timestamp" : str(datetime.datetime.now(datetime.UTC)),
        "revision"  : revision,
        "system"    : sys.version,
        "Provenance": { 
                        "PROV-agent "     : entradas.agent,  "wasAttributedTo "
                        "PROV-entity "    : entradas.entity, "wasGeneratedBy "
                        "PROV-activity "  : entradas.activity}
           }