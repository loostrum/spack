##############################################################################
# Copyright (c) 2013-2017, Lawrence Livermore National Security, LLC.
# Produced at the Lawrence Livermore National Laboratory.
#
# This file is part of Spack.
# Created by Todd Gamblin, tgamblin@llnl.gov, All rights reserved.
# LLNL-CODE-647188
#
# For details, see https://github.com/spack/spack
# Please also see the NOTICE and LICENSE files for our notice and the LGPL.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License (as
# published by the Free Software Foundation) version 2.1, February 1999.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the IMPLIED WARRANTY OF
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the terms and
# conditions of the GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA
##############################################################################

from spack import *


class Dedispersion(CMakePackage):
    """Radio astronomy dedispersion algorithm implemented for many-core accelerators."""

    homepage = "https://github.com/AA-ALERT/Dedispersion"
    url      = "https://github.com/AA-ALERT/Dedispersion/archive/4.1.tar.gz"

    version("master", git="https://github.com/AA-ALERT/Dedispersion.git", branch="master")
    version("development", git="https://github.com/AA-ALERT/Dedispersion.git", branch="development")
    version("4.1", "7467486ec6682da7f62d82a1f0f8581e", url="https://github.com/AA-ALERT/Dedispersion/archive/4.1.tar.gz")

    variant("lofar", default=False, description="Enable LOFAR HDF5 file format support.")
    variant("psrdada", default=False, description="Enable PSRDADA ringbuffer support.")

    depends_on("cmake@3.10:")
    depends_on("googletest")
    depends_on("cuda%gcc@4.8.5")
    depends_on("libisautils")
    depends_on("libisaopencl")
    depends_on("astrodata")
    depends_on("astrodata +lofar", when="+lofar")
    depends_on("astrodata +psrdada", when="+psrdada")
    depends_on("astrodata +lofar +psrdada", when="+lofar +psrdada")

    def setup_environment(self, spack_env, run_env):
        if "+lofar" in self.spec:
            spack_env.set("LOFAR", True)
        if "+psrdada" in self.spec:
            spack_env.set("PSRDADA", True)
