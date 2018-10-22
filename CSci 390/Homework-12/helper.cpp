#include "helper.h"
#include <cxxabi.h>
// Fake unwritten code yet by commenting out code.
std::string 
DemangleName
(const char *Name)
{
int Status = -1;
std::string DemangledName = Name;
char *demangledName = abi::__cxa_demangle (Name, nullptr, nullptr, &Status);
if (Status == 0)
{
DemangledName = demangledName;
}
free (demangledName);
return DemangledName;
}