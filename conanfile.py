from conan import ConanFile
from conan.tools.cmake import CMake, CMakeToolchain, CMakeDeps, cmake_layout
from conan.tools.microsoft import is_msvc


class LuaConan(ConanFile):
    name = "lua"
    version = "5.1"
    license = "MIT"
    author = "Marius Elvert marius.elvert@googlemail.com"
    url = "https://github.com/ltjax/lua"
    description = "https://github.com/ltjax/lua"
    topics = ("lua")
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = {"shared": False}
    exports_sources = "src/*", "test/*", "etc/*", "cmake/*", "doc/*", "CMakeLists.txt", "dist.info", "README.md", "COPYRIGHT", "HISTORY"

    def source(self):
        pass

    def configure(self):
        if not is_msvc(self):
            del self.settings.compiler.libcxx

    def generate(self):
        deps = CMakeDeps(self)
        deps.generate()

        toolchain = CMakeToolchain(self)
        toolchain.variables['BUILD_SHARED_LIBS'] = self.options.shared;
        toolchain.variables['BUILD_TESTING'] = False;
        
        if self.settings.os == "Windows":
            toolchain.variables['LUA_BUILD_AS_DLL'] = self.options.shared
            toolchain.variables['LUA_BUILD_WLUA'] = False
        
        toolchain.generate()

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def package(self):
        cmake = CMake(self)
        cmake.install()

    def package_info(self):
        if self.settings.os != "Windows" or self.options.shared:
            self.cpp_info.libs = ["lua"]
        else:
            self.cpp_info.libs = ["liblua"]
