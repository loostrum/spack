from glob import glob
from spack import *

class Presto(MakefilePackage):
    """Open source pulsar search and analysis toolkit """

    homepage = "http://www.cv.nrao.edu/~sransom/presto/"
    url      = "https://github.com/scottransom/presto/archive/v2.1.tar.gz"

    version('2.1', '36b8007b0e8513371a1e886bf79f309c')

    depends_on('python')
    depends_on('fftw')
    depends_on('cfitsio')
    depends_on('libpng')
    depends_on('glib')
    depends_on('pgplot')

    build_directory = "src"

    def setup_environment(self, spack_env, run_env):
        self.source_path = "{}/{}-{}/".format(self.stage.path, self.name, self.version)
        spack_env.set('PRESTO',  self.source_path)
        spack_env.append_path('LD_LIBRARY_PATH', self.source_path + "/lib")

    def install(self, spec, prefix):
        mkdir(prefix.bin)
        mkdir(prefix.lib)

        for i in glob('bin/*'):
            install(i, prefix.bin)

        for i in glob('lib/*.so'):
            install(i, prefix.lib)
