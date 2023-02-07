from syt import CfgNode


def test_templating_1():
    cfg = CfgNode()
    cfg.root = CfgNode()
    cfg.root.ident = None
    cfg.root.node = CfgNode()
    cfg.root.node.key1 = ''
    cfg.root.node.subnode = CfgNode()
    cfg.root.node.subnode.key2 = ''
    cfg.root.node.subnode.key3 = 0.1
    cfg.root.node.subnode.key4 = 4.5
    cfg.root.node.subnode.key5 = ['0']
    cfgs = cfg.apply_template('data/input1.syt')
    assert len(cfgs) == 81


def test_templating_2():
    cfg = CfgNode()
    cfg.data = CfgNode()
    cfg.data.spec = None
    cfg.data.eval_spec = None
    cfgs = cfg.apply_template('data/input2.syt')
    assert len(cfgs) == 16
