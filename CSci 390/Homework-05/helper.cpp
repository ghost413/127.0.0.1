//Helper.cpp:
#include "helper.h"

#if defined(__GNUC__)
#include <cxxabi.h>
#endif

std::string DemangleName(const char *Name)
{
	std::string DemangledName = Name;

#if defined(__GNUC__)
	int Status = -1;

	char *demangledName = abi::__cxa_demangle(Name, nullptr, nullptr, &Status);
	if (Status == 0)
	{
		DemangledName = demangledName;
	}

	free(demangledName);
#endif

	return DemangledName;
}
