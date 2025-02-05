
import os


import angr


test_location = os.path.join(os.path.dirname(os.path.realpath(__file__)), '..', '..', 'binaries', 'tests')


def test_cfgfast_clflush():
    bin_path = os.path.join(test_location, "x86_64", 'igt_stats')
    p = angr.Project(bin_path, auto_load_libs=False)
    # build a CFG of function 0x12190
    cfg = p.analyses.CFG(function_starts=(0x412190,),
                         # Do not scan the entire binary
                         force_complete_scan=False,
                         symbols=False,
                         function_prologues=False,
                         )
    node = cfg.get_any_node(0x4121aa)
    assert node is not None
    assert len(node.successors) == 1


def test_cfgemulated_clflush():
    bin_path = os.path.join(test_location, "x86_64", 'igt_stats')
    p = angr.Project(bin_path, auto_load_libs=False)
    # build a CFG of function 0x12190
    cfg = p.analyses.CFGEmulated(starts=(0x412190,))
    node = cfg.get_any_node(0x4121aa)
    assert node is not None
    assert len(node.successors) == 1


if __name__ == "__main__":
    test_cfgfast_clflush()
    test_cfgemulated_clflush()
