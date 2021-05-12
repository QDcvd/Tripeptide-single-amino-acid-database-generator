import sys
from modeller import *
object0name, template0name = sys.argv[1:]
# mod9.23 single_model.py qseq1 tseq1

env = environ()
aln = alignment(env)
mdl = model(env, file=template0name, model_segment=('FIRST:A','LAST:A'))
aln.append_model(mdl, align_codes=template0name, atom_files=template0name+'.pdb')
aln.append(file=object0name+'.ali', align_codes=object0name)
aln.align2d()
aln.write(file=object0name+template0name+'.ali', alignment_format='PIR')
aln.write(file=object0name+template0name+'.pap', alignment_format='PAP')

from modeller import *
from modeller.automodel import *
from modeller import soap_protein_od

# Example of changing the default optmization schedule
# you can see the ref script in  https://salilab.org/modeller/9.23/manual/node19.html
from modeller.automodel import *

log.verbose()
env = environ()

# Give less weight to all soft-sphere restraints:
env.schedule_scale = physical.values(default=1.0, soft_sphere=0.7)
env.io.atom_files_directory = ['.', '../atom_files']

a = automodel(env, alnfile=object0name+template0name+'.ali',
              knowns=template0name, sequence=object0name,
              assess_methods=(assess.DOPE,
                              #soap_protein_od.Scorer(),
                              assess.GA341))
a.starting_model = a.ending_model = 1

# Very thorough VTFM optimization:
a.library_schedule = autosched.slow
a.max_var_iterations = 300

# Thorough MD optimization:
a.md_level = refine.slow

# Repeat the whole cycle 2 times and do not stop unless obj.func. > 1E6
a.repeat_optimization = 2
a.max_molpdf = 1e6


a.make()


