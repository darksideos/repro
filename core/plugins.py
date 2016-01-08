from core import arch
from core import execfmt

arch_plugins = []
execfmt_plugins = []

def register_plugin(plugin):
	"""Register an instruction set plugin"""
	if issubclass(plugin,arch.InstructionSet):
		arch_plugins.append(plugin)
	elif issubclass(plugin,execfmt.ExecutableFormat):
		execfmt_plugins.append(plugin)
