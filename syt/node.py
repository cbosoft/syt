from yacs.config import CfgNode as _CfgNode, load_cfg

from .templating import read_template


class CfgNode(_CfgNode):

    def apply_template(self, file_path: str):
        variant_sources = read_template(file_path)
        variants = []
        for variant_source in variant_sources:
            variant = self.clone()
            variant.merge_from_other_cfg(load_cfg(variant_source))
            variants.append(variant)
        return variants
