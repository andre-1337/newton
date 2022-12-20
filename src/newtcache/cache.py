# = object to keep track of imports from certain files
# = in charge of managing imports (validating paths, extracting data)

class Cache:
    def __init__(self, imports, modulename):
        self.imports = imports
        self.modulename = modulename
    
    def validate(self):
        for i in self.imports:
            # check if import is extern (if it is then approve)
            # check if system type in cache otherwise check system type
            # check if the name of the import is in project, starting from root directory
            # check if the name of the import is in the package manager directory
            # otherwise give an error "unknown import path"
            ...


class CacheImport:
    def __init__(self, name, path, objs):
        self.name = name
        self.path = path
        self.objs = objs
