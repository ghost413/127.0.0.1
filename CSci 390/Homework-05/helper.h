//Helper.h:
#include <string>
#include <typeinfo>

std::string DemangleName(const char *Name);

#define DUMPTYPE(Symbol) "Type: " << DemangleName(typeid(Symbol).name()) << ", Length: " << sizeof(Symbol)

#define DUMPVAR(Symbol) "Variable: " << #Symbol <<  ", " DUMPTYPE(Symbol) << ", Address: " << ((void *) &(Symbol)) << ", Value: " << (Symbol)

#define DUMPVAL(Symbol) "Expression: " << #Symbol <<  ", " DUMPTYPE(Symbol) << ", Value: " << (Symbol)
